"""Provisional C3: prepare bounded, read-only investigator context.
Input is an in-process Stage B analyze() report, NOT arbitrary imported report JSON.
No inference, collection, tool calls or authorization. No semantic adjudication.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from typing import Any

from .ssh_incident import SCHEMA as REPORT_SCHEMA

CONTEXT_SCHEMA = "aegislab.ssh-investigator-context.v0.1"
MAX_CONTEXT_EVENTS = 32
MAX_CONTEXT_BYTES = 16_384
RELATED_SECONDS = 120
EVENT_FIELDS = ("event_id", "record_id", "source_line", "observed_at",
                "outcome", "username", "source_ip", "source_port", "sshd_pid")
FINDING_FIELDS = ("finding_id", "rule_id", "subject", "window_start", "window_end",
                  "distinct_failed_observations", "evidence_event_ids", "assessment")


def _encode(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("utf-8")


def _time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def prepare_context(report: dict[str, Any], *, finding_id: str | None = None) -> dict[str, Any]:
    """Select one finding and related observations; refuse rather than silently truncate.
    If no finding, permit a small source review, not an incident conclusion.
    Limits bound serialized context bytes, not model tokens.
    """
    result: dict[str, Any] = {"context_schema": CONTEXT_SCHEMA, "eligible": False,
                              "reason": None, "context": None}
    def stop(reason: str) -> dict[str, Any]:
        result["reason"] = reason
        return result

    try:
        if report["schema"] != REPORT_SCHEMA:
            return stop("unsupported_report_schema")
        events, findings, source = report["events"], report["findings"], report["source"]
        if not isinstance(events, list) or not isinstance(findings, list):
            return stop("invalid_report")
        by_id = {e["event_id"]: e for e in events}
        if len(by_id) != len(events) or source["accepted_event_count"] != len(events):
            return stop("inconsistent_report")
        if not events:
            return stop("no_accepted_observations")
        if finding_id is None and len(findings) > 1:
            return stop("finding_selection_required")
        if finding_id is not None:
            matches = [f for f in findings if f["finding_id"] == finding_id]
            if len(matches) != 1:
                return stop("unknown_or_ambiguous_finding")
            finding = matches[0]
        else:
            finding = findings[0] if findings else None
        supporting: set[str] = set()
        if finding is not None:
            refs = finding["evidence_event_ids"]
            supporting = set(refs)
            if not refs or len(supporting) != len(refs) or not supporting <= by_id.keys():
                return stop("inconsistent_finding_references")
            subject = finding["subject"]
            start, end = _time(finding["window_start"]), _time(finding["window_end"])
            if start > end:
                return stop("inconsistent_finding_window")
            def related(e: dict[str, Any]) -> bool:
                return (e["username"] == subject["username"]
                        and e["source_ip"] == subject["source_ip"]
                        and start - timedelta(seconds=RELATED_SECONDS) <= _time(e["observed_at"])
                        <= end + timedelta(seconds=RELATED_SECONDS))
            if any(not related(by_id[x]) for x in supporting):
                return stop("inconsistent_finding_scope")
            selected = [e for e in events if related(e)]
        else:
            selected = events
        if len(selected) > MAX_CONTEXT_EVENTS:
            return stop("event_budget_exceeded")
        selected = sorted(selected, key=lambda e: (e["observed_at"], e["event_id"]))
        # Whitelist fields. Never pass the entire report or evaluator truth.
        context = {
            "schema": CONTEXT_SCHEMA,
            "task": {"kind": "finding_review" if finding else "source_review",
                     "question": ("What additional authorized observation would reduce uncertainty "
                                  "about the selected SSH finding?" if finding else
                                  "Is any additional evidence-linked observation justified for these records?")},
            "source": {k: source[k] for k in ("id", "declared_kind", "sha256")},
            "status": report["status"],
            "selection": {"accepted_total": len(events), "included": len(selected),
                          "omitted": len(events) - len(selected),
                          "other_findings_omitted": len(findings) - int(finding is not None),
                          "supporting_event_ids": sorted(supporting),
                          "policy": "same_subject_window_plus_120s" if finding else "all_accepted",
                          "complete_source_coverage": "not_established"},
            "events": [{k: e[k] for k in EVENT_FIELDS} for e in selected],
            "finding": ({**{k: finding[k] for k in FINDING_FIELDS if k != "subject"},
                         "subject": {k: finding["subject"][k] for k in ("username", "source_ip")}}
                        if finding else None),
            "evidence_quality": {
                "quarantined_record_count": source["quarantined_record_count"],
                "duplicate_failure_observations_ignored": source["duplicate_failure_observations_ignored"],
                "network_correlation": "not_supplied",
                "source_authenticity": "not_established",
                "clock_accuracy": "not_established",
                "target_hostname": None,
            },
            "limitations": list(report["limitations"]),
        }
        # JSON roundtrip also detaches nested values from the baseline.
        encoded = _encode(context)
        if len(encoded) > MAX_CONTEXT_BYTES:
            return stop("byte_budget_exceeded")
        result.update(eligible=True, reason="context_prepared", context=json.loads(encoded),
                      context_bytes=len(encoded))
        return result
    except (KeyError, TypeError, ValueError, AttributeError, OverflowError):
        return stop("invalid_report")
