"""Stage B: observable, deliberately bounded rule and provenance tests."""

from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from aegislab.ssh_incident import InputError, MAX_INPUT_BYTES, analyze


def envelope(second: int, *, outcome: str = "Failed", port: int = 51001,
             username: str = "labuser", ip: str = "10.10.0.1") -> dict[str, str]:
    timestamp = (datetime(2026, 11, 22, 10, 0, tzinfo=timezone.utc)
                 + timedelta(seconds=second)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "observed_at": timestamp,
        "message": f"sshd[201]: {outcome} publickey for {username} from {ip} port {port} ssh2",
    }


class StageBTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "events.jsonl"

    def run_case(self, items: list[dict[str, str] | str]) -> dict:
        self.path.write_text(
            "\n".join(json.dumps(item) if isinstance(item, dict) else item
                      for item in items) + "\n",
            encoding="utf-8",
        )
        return analyze(self.path, source_id="fixture:ssh-v1", source_kind="synthetic")

    def test_three_distinct_failures_produce_evidence_linked_finding(self) -> None:
        report = self.run_case([
            envelope(0, port=51001),
            envelope(35, port=51002),
            envelope(80, port=51003),
        ])
        self.assertEqual(report["status"], "finding_present")
        self.assertEqual(len(report["findings"]), 1)
        finding = report["findings"][0]
        self.assertEqual(finding["distinct_failed_observations"], 3)
        self.assertEqual(
            set(finding["evidence_event_ids"]),
            {e["event_id"] for e in report["events"]},
        )
        self.assertTrue(all(e["record_id"].startswith("rec-") for e in report["events"]))
        self.assertEqual([e["source_line"] for e in report["events"]], [1, 2, 3])
        self.assertTrue(all(len(e["raw_record_sha256"]) == 64 for e in report["events"]))
        self.assertIn("not establish", finding["assessment"])
        self.assertEqual(report["rule"]["window_seconds_inclusive"], 120)

    def test_success_only_is_negative_not_proof_of_safety(self) -> None:
        report = self.run_case([envelope(0, outcome="Accepted")])
        self.assertEqual(report["status"], "no_finding_observed")
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["events"][0]["outcome"], "accepted_publickey")

    def test_two_failures_are_below_threshold(self) -> None:
        report = self.run_case([envelope(0), envelope(50, port=51002)])
        self.assertEqual(report["status"], "no_finding_observed")

    def test_window_is_inclusive_at_120_seconds(self) -> None:
        report = self.run_case([
            envelope(0, port=51001),
            envelope(60, port=51002),
            envelope(120, port=51003),
        ])
        self.assertEqual(report["status"], "finding_present")

    def test_window_outside_boundary_does_not_trigger(self) -> None:
        report = self.run_case([
            envelope(0, port=51001),
            envelope(60, port=51002),
            envelope(121, port=51003),
        ])
        self.assertEqual(report["status"], "no_finding_observed")

    def test_duplicate_log_line_does_not_inflate_count(self) -> None:
        a = envelope(0, port=51001)
        report = self.run_case([a, a, envelope(50, port=51002)])
        self.assertEqual(report["status"], "no_finding_observed")
        self.assertEqual(report["source"]["duplicate_failure_observations_ignored"], 1)
        self.assertEqual(len(report["events"]), 3)  # raw observations remain traceable

    def test_distinct_subjects_are_not_mixed(self) -> None:
        report = self.run_case([
            envelope(0, port=51001, username="one"),
            envelope(10, port=51002, username="two"),
            envelope(20, port=51003, username="one"),
        ])
        self.assertEqual(report["status"], "no_finding_observed")

    def test_malformed_json_is_quarantined_and_finding_retained_with_gaps(self) -> None:
        report = self.run_case([
            envelope(0, port=51001), "not-json",
            envelope(40, port=51002), envelope(70, port=51003),
        ])
        self.assertEqual(report["status"], "finding_present_with_gaps")
        self.assertEqual(report["quarantine"][0]["line"], 2)
        self.assertEqual(report["quarantine"][0]["reason"], "invalid_json")
        self.assertEqual(len(report["findings"][0]["evidence_event_ids"]), 3)

    def test_only_invalid_data_is_unassessable(self) -> None:
        report = self.run_case(["not-json", {"observed_at": "nope", "message": "foo"}])
        self.assertEqual(report["status"], "unassessable")
        self.assertEqual(report["source"]["quarantined_record_count"], 2)
        self.assertEqual(len(report["events"]), 0)

    def test_unsupported_message_does_not_become_a_failure(self) -> None:
        report = self.run_case([{
            "observed_at": "2026-11-22T10:00:00Z",
            "message": "sshd[201]: Invalid user example from 10.10.0.1",
        }])
        self.assertEqual(report["status"], "unassessable")
        self.assertEqual(report["quarantine"][0]["reason"], "unsupported_message")

    def test_duplicate_json_keys_are_quarantined(self) -> None:
        raw = ('{"observed_at":"2026-11-22T10:00:00Z",'
               '"observed_at":"2026-11-22T10:00:10Z","message":"x"}')
        report = self.run_case([raw])
        self.assertEqual(report["status"], "unassessable")
        self.assertEqual(report["quarantine"][0]["reason"], "invalid_json")

    def test_record_ids_stable_for_same_source_and_content(self) -> None:
        entries = [envelope(0), envelope(1, port=51002)]
        first = self.run_case(entries)
        second = self.run_case(entries)
        self.assertEqual(first["events"], second["events"])
        self.assertEqual(first["source"]["sha256"], second["source"]["sha256"])
        other = analyze(self.path, source_id="fixture:other", source_kind="synthetic")
        self.assertNotEqual(first["events"][0]["event_id"], other["events"][0]["event_id"])

    def test_empty_file_is_unassessable(self) -> None:
        self.path.write_bytes(b"")
        report = analyze(self.path, source_id="fixture:empty", source_kind="synthetic")
        self.assertEqual(report["status"], "unassessable")

    def test_missing_file_is_an_explicit_error(self) -> None:
        with self.assertRaises(InputError):
            analyze(self.path, source_id="fixture:missing", source_kind="synthetic")

    def test_size_bound_prevents_unsafe_read(self) -> None:
        self.path.write_bytes(b"x" * (MAX_INPUT_BYTES + 1))
        with self.assertRaisesRegex(InputError, "byte limit"):
            analyze(self.path, source_id="fixture:too-big", source_kind="synthetic")


if __name__ == "__main__":
    unittest.main()
