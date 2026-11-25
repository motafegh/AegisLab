"""Provisional context preparation tests; no model or network dependencies."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

from aegislab.investigator_context import prepare_context, MAX_CONTEXT_EVENTS
from aegislab.ssh_incident import analyze
from test_ssh_incident import envelope


class ContextTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.path = Path(tmp.name) / "case.jsonl"

    def report(self, items):
        self.path.write_text("".join(json.dumps(i) + "\n" if isinstance(i, dict)
                                     else i + "\n" for i in items))
        return analyze(self.path, source_id="fixture:context", source_kind="synthetic")

    def burst(self):
        return [envelope(0, port=51001), envelope(30, port=51002),
                envelope(80, port=51003), envelope(90, outcome="Accepted", port=51004)]

    def test_supporting_and_related_acceptance(self):
        report = self.report(self.burst())
        r = prepare_context(report)
        self.assertTrue(r["eligible"])
        c = r["context"]
        self.assertEqual(c["selection"]["included"], 4)
        self.assertEqual(len(c["selection"]["supporting_event_ids"]), 3)
        self.assertEqual(c["events"][-1]["outcome"], "accepted_publickey")
        self.assertEqual(c["evidence_quality"]["network_correlation"], "not_supplied")

    def test_selection_omits_other_subject_and_distant_event(self):
        report = self.report(self.burst() + [envelope(40, username="other"),
                                             envelope(201, outcome="Accepted")])
        c = prepare_context(report)["context"]
        self.assertEqual(c["selection"]["included"], 4)
        self.assertEqual(c["selection"]["omitted"], 2)
        self.assertEqual(c["selection"]["complete_source_coverage"], "not_established")

    def test_baseline_unchanged_and_no_recommendation_or_truth(self):
        report = self.report(self.burst())
        report["independent_truth"] = "hidden evaluator-only field"
        report["findings"][0]["subject"]["independent_truth"] = "hidden nested field"
        before = copy.deepcopy(report)
        r = prepare_context(report)
        self.assertEqual(report, before)
        self.assertNotIn("next_permitted_observation", r["context"]["finding"])
        self.assertNotIn("independent_truth", r["context"])
        self.assertNotIn("independent_truth", r["context"]["finding"]["subject"])
        r["context"]["finding"]["subject"]["username"] = "changed"
        self.assertEqual(report, before)

    def test_empty_or_quarantine_only_ineligible(self):
        for items in ([], ["bad-json"]):
            r = prepare_context(self.report(items))
            self.assertFalse(r["eligible"])
            self.assertEqual(r["reason"], "no_accepted_observations")
            self.assertIsNone(r["context"])

    def test_normal_source_review(self):
        r = prepare_context(self.report([envelope(0, outcome="Accepted")]))
        self.assertTrue(r["eligible"])
        self.assertEqual(r["context"]["task"]["kind"], "source_review")
        self.assertIsNone(r["context"]["finding"])

    def test_quarantine_preserves_known_gap(self):
        r = prepare_context(self.report(self.burst() + ["bad-json"]))
        c = r["context"]
        self.assertEqual(c["status"], "finding_present_with_gaps")
        self.assertEqual(c["evidence_quality"]["quarantined_record_count"], 1)

    def test_multiple_findings_require_selection(self):
        report = self.report(self.burst() + [
            envelope(i, username="other", port=52000+i) for i in (0, 20, 50)])
        self.assertEqual(prepare_context(report)["reason"], "finding_selection_required")
        r = prepare_context(report, finding_id=report["findings"][1]["finding_id"])
        self.assertTrue(r["eligible"])
        self.assertEqual(r["context"]["selection"]["other_findings_omitted"], 1)
        self.assertEqual(r["context"]["selection"]["omitted"], 4)

    def test_unknown_finding(self):
        self.assertEqual(prepare_context(self.report(self.burst()), finding_id="bogus")["reason"],
                         "unknown_or_ambiguous_finding")

    def test_event_bound_no_silent_truncation(self):
        report = self.report([envelope(i, outcome="Accepted", port=51001+i)
                              for i in range(MAX_CONTEXT_EVENTS + 1)])
        self.assertEqual(prepare_context(report)["reason"], "event_budget_exceeded")

    def test_byte_bound(self):
        report = self.report(self.burst())
        report["limitations"].append("x" * 16384)
        self.assertEqual(prepare_context(report)["reason"], "byte_budget_exceeded")

    def test_inconsistent_references_and_schema(self):
        report = self.report(self.burst())
        report["findings"][0]["evidence_event_ids"].append("missing")
        self.assertEqual(prepare_context(report)["reason"], "inconsistent_finding_references")
        report["schema"] = "future"
        self.assertEqual(prepare_context(report)["reason"], "unsupported_report_schema")
        self.assertEqual(prepare_context({})["reason"], "invalid_report")

    def test_determinism(self):
        report = self.report(self.burst())
        self.assertEqual(prepare_context(report), prepare_context(report))


if __name__ == "__main__":
    unittest.main()
