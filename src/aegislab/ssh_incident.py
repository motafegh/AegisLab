"""Bounded SSH public-key observation importer and deterministic incident rule.

Only source-declared JSONL envelopes are supported. No network or host access.
The envelope timestamp is NOT independently verified sensor or scenario truth.
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
import re
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

SCHEMA = "aegislab.ssh-incident-report.v1"
PARSER_VERSION = "ssh-publickey-envelope.v1"
RULE_ID = "ssh.failed-publickey-burst.v1"
THRESHOLD = 3
WINDOW_SECONDS = 120
MAX_INPUT_BYTES = 262_144
MAX_RECORDS = 1000
MAX_LINE_BYTES = 2048
MAX_MESSAGE_CHARS = 512

# Intentionally narrow: the laboratory's known public-key decision form.
# A real syslog/journald adapter will need its own clock/source handling.
AUTH_PATTERN = re.compile(
    r"^sshd\[(?P<pid>[1-9][0-9]{0,8})\]: "
    r"(?P<decision>Failed|Accepted) publickey for "
    r"(?P<username>[A-Za-z_][A-Za-z0-9._-]{0,31}) from "
    r"(?P<ip>[0-9A-Fa-f:.]+) port (?P<port>[0-9]{1,5}) ssh2"
    r"(?:\: (?:ED25519|RSA|ECDSA) SHA256:[A-Za-z0-9+/=]{10,100})?$"
)


class InputError(ValueError):
    """Source cannot be safely assessed, as opposed to a quarantinable record."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _id(prefix: str, key: str) -> str:
    return prefix + _sha256(key.encode("utf-8"))[:20]


def _object_without_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate_json_key")
        result[key] = value
    return result


def _utc_timestamp(value: Any) -> str:
    if not isinstance(value, str) or not re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", value
    ):
        raise ValueError("invalid_timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("invalid_timestamp") from exc
    if parsed.utcoffset() != timedelta(0):
        raise ValueError("invalid_timestamp")
    return value


def _parse_line(raw: bytes, record_id: str, source_id: str) -> dict[str, Any]:
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_object_without_duplicate_keys,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("invalid_json") from exc

    if not isinstance(payload, dict) or set(payload) != {"observed_at", "message"}:
        raise ValueError("invalid_envelope")
    timestamp = _utc_timestamp(payload["observed_at"])
    message = payload["message"]
    if (
        not isinstance(message, str)
        or len(message) > MAX_MESSAGE_CHARS
        or "\n" in message
        or "\r" in message
    ):
        raise ValueError("invalid_message")
    match = AUTH_PATTERN.fullmatch(message)
    if match is None:
        raise ValueError("unsupported_message")
    try:
        address = str(ipaddress.ip_address(match.group("ip")))
    except ValueError as exc:
        raise ValueError("invalid_ip") from exc
    port = int(match.group("port"))
    if not 1 <= port <= 65535:
        raise ValueError("invalid_port")
    return {
        "event_id": _id("evt-", record_id + ":" + PARSER_VERSION),
        "record_id": record_id,
        "source_id": source_id,
        "observed_at": timestamp,
        "outcome": match.group("decision").lower() + "_publickey",
        "username": match.group("username"),
        "source_ip": address,
        "source_port": port,
        "sshd_pid": int(match.group("pid")),
    }


def analyze(path: Path, *, source_id: str, source_kind: str) -> dict[str, Any]:
    """Analyze one bounded local JSONL file without contacting the target host.

    source_kind describes an operator DECLARATION, never an attestation.
    """
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}", source_id):
        raise InputError("source_id must be 1–80 safe identifier characters")
    if source_kind not in {"synthetic", "unverified_import"}:
        raise InputError("source_kind must be synthetic or unverified_import")

    try:
        with path.open("rb") as handle:
            content = handle.read(MAX_INPUT_BYTES + 1)
    except OSError as exc:
        raise InputError("input file cannot be opened") from exc
    if len(content) > MAX_INPUT_BYTES:
        raise InputError("input exceeds bounded byte limit")
    if b"\x00" in content:
        raise InputError("input contains NUL bytes")
    lines = content.splitlines()
    if len(lines) > MAX_RECORDS:
        raise InputError("input exceeds bounded record limit")

    file_digest = _sha256(content)
    events: list[dict[str, Any]] = []
    quarantine: list[dict[str, str | int]] = []
    for number, line in enumerate(lines, 1):
        record_id = _id("rec-", source_id + ":" + file_digest + ":" + str(number))
        if len(line) > MAX_LINE_BYTES:
            quarantine.append(
                {"line": number, "record_id": record_id, "reason": "oversized_record"}
            )
            continue
        try:
            event = _parse_line(line, record_id, source_id)
        except ValueError as exc:
            quarantine.append(
                {"line": number, "record_id": record_id, "reason": str(exc)}
            )
        else:
            event["source_line"] = number
            event["raw_record_sha256"] = _sha256(line)
            events.append(event)

    # Exact repeats of the same decision and transport identity at the same
    # declared time are one distinct observation for rule counting. This is
    # not proof of actual attempt identity or general replay resistance.
    failures: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    seen: set[tuple[str, str, str, int, str, str, int]] = set()
    duplicate_count = 0
    for event in events:
        if event["outcome"] != "failed_publickey":
            continue
        key = (
            event["username"],
            event["source_ip"],
            event["observed_at"],
            event["source_port"],
            event["outcome"],
            event["source_id"],
            event["sshd_pid"],
        )
        if key in seen:
            duplicate_count += 1
            continue
        seen.add(key)
        failures[(event["source_ip"], event["username"])].append(event)

    incidents: list[dict[str, Any]] = []
    for (ip, username), group in sorted(failures.items()):
        ordered = sorted(
            group, key=lambda e: (e["observed_at"], e["event_id"])
        )
        window: deque[dict[str, Any]] = deque()
        for event in ordered:
            t = datetime.fromisoformat(event["observed_at"].replace("Z", "+00:00"))
            while window:
                first = datetime.fromisoformat(
                    window[0]["observed_at"].replace("Z", "+00:00")
                )
                if (t - first).total_seconds() <= WINDOW_SECONDS:
                    break
                window.popleft()
            window.append(event)
            if len(window) >= THRESHOLD:
                supporting = list(window)
                event_ids = [e["event_id"] for e in supporting]
                incidents.append({
                    "finding_id": _id("finding-", RULE_ID + ":" + ":".join(event_ids)),
                    "rule_id": RULE_ID,
                    "subject": {"username": username, "source_ip": ip},
                    "window_start": supporting[0]["observed_at"],
                    "window_end": supporting[-1]["observed_at"],
                    "distinct_failed_observations": len(supporting),
                    "evidence_event_ids": event_ids,
                    "assessment": (
                        "Repeated failed public-key decision records observed; "
                        "this does not establish distinct client actions, "
                        "an intrusion, or a compromise."
                    ),
                    "next_permitted_observation": (
                        "Under authorization, inspect target authentication "
                        "successes and the independent action/target truth record."
                    ),
                })
                break  # one initial finding per subject, not overlapping alerts

    if incidents:
        status = "finding_present_with_gaps" if quarantine else "finding_present"
    elif not events:
        status = "unassessable"
    else:
        status = "incomplete_evidence" if quarantine else "no_finding_observed"

    limitations = [
        "Source kind and source ID are operator declarations, not authenticated provenance.",
        "UTC timestamps are supplied by the input envelope; clock accuracy and ordering are unverified.",
        "A distinct log observation is not proof of a distinct client action or target effect.",
        "No independent action/target truth or separate sensor correlation was supplied.",
        "Only supported sshd public-key decision messages are parsed; other activity is not assessed.",
        "No finding means this rule did not match the accepted records, not that activity was absent.",
    ]
    if quarantine:
        limitations.append("Quarantined records may change an investigative conclusion.")
    if duplicate_count:
        limitations.append(
            "Exact repeated failure observations were excluded from threshold counting."
        )
    if not content:
        limitations.append("The input file was empty; no event assessment is possible.")
    return {
        "schema": SCHEMA,
        "parser_version": PARSER_VERSION,
        "rule": {"id": RULE_ID, "threshold": THRESHOLD,
                 "window_seconds_inclusive": WINDOW_SECONDS},
        "source": {
            "id": source_id,
            "declared_kind": source_kind,
            "sha256": file_digest,
            "line_count": len(lines),
            "accepted_event_count": len(events),
            "quarantined_record_count": len(quarantine),
            "duplicate_failure_observations_ignored": duplicate_count,
        },
        "status": status,
        "findings": incidents,
        "events": events,
        "quarantine": quarantine,
        "limitations": limitations,
    }


def human_summary(report: dict[str, Any]) -> str:
    src = report["source"]
    lines = [
        "AegisLab deterministic SSH finding (no AI)",
        f"Source: {src['id']} [declared {src['declared_kind']}]",
        f"SHA-256: {src['sha256']}",
        (f"Accepted events: {src['accepted_event_count']}; quarantined: "
         f"{src['quarantined_record_count']}; duplicate failures ignored: "
         f"{src['duplicate_failure_observations_ignored']}"),
        f"Assessment status: {report['status']}",
    ]
    if not report["findings"]:
        lines.append("No supported repeated-failure finding; activity is NOT ruled out.")
    for finding in report["findings"]:
        subject = finding["subject"]
        lines.extend([
            f"FINDING {finding['finding_id']} ({finding['rule_id']})",
            (f"  {subject['username']} from {subject['source_ip']}: "
             f"{finding['distinct_failed_observations']} distinct failed "
             f"records from {finding['window_start']} to {finding['window_end']}"),
            "  Supporting event IDs: " + ", ".join(finding["evidence_event_ids"]),
            "  " + finding["assessment"],
            "  Next: " + finding["next_permitted_observation"],
        ])
    if report["quarantine"]:
        lines.append(
            "Quarantined lines: " + ", ".join(
                f"{item['line']} ({item['reason']})" for item in report["quarantine"]
            )
        )
    lines.append("Key uncertainty: producer/source authenticity, clock accuracy and independent action truth are unverified.")
    lines.append("See --json for complete limitations and event-to-record mapping.")
    return "\n".join(lines)
