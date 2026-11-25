"""C4/C5 provisional transport and contract checks; mocked network by default."""
import copy
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from aegislab.investigator_context import prepare_context
from aegislab.investigator_contract import ContractError, validate_output, OUTPUT_SCHEMA
from aegislab.local_inference import LocalConfig, infer, MAX_RESPONSE_BYTES
from aegislab.investigator import investigate
from aegislab.ssh_incident import analyze

FIXTURE = Path("examples/fixtures/ssh-auth-burst.synthetic.jsonl")
MODEL = "gemma-4-e2b-it"


def report():
    return analyze(FIXTURE, source_id="fixture:ssh-burst-v1", source_kind="synthetic")


def candidate(context):
    ids = [e["event_id"] for e in context["events"]]
    return {"hypotheses": [], "next_check": {
        "objective": "Compare key identities", "basis_event_ids": ids,
        "required_evidence": "Server-side key fingerprints if available",
        "if_present": "Compare fingerprints without attributing intent",
        "if_unavailable": "Key identity remains unknown"},
        "uncertainty": "Source authenticity and actual intent remain unknown."}


def envelope(content, finish="stop", model=MODEL):
    return {"model": model, "choices": [{"finish_reason": finish,
                                         "message": {"content": content}}]}


class FakeResponse:
    def __init__(self, raw, status=200, encoding="identity"):
        self.raw, self.status, self.encoding = raw, status, encoding

    def getheader(self, name, default=None):
        return self.encoding if name == "Content-Encoding" else default

    def read(self, count):
        return self.raw[:count]


class FakeConnection:
    def __init__(self, response=None, error=None):
        self.response, self.error = response, error
        self.closed = False
        self.sent = None

    def request(self, method, path, **kwargs):
        self.sent = (method, path, kwargs)
        if self.error:
            raise self.error

    def getresponse(self):
        return self.response

    def close(self):
        self.closed = True


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.context = prepare_context(report())["context"]
        self.config = LocalConfig()

    def run_fake(self, payload=None, *, raw=None, status=200, encoding="identity", error=None):
        conn = FakeConnection(FakeResponse(raw if raw is not None else json.dumps(payload).encode(),
                                           status, encoding), error)
        def factory(host, port, timeout):
            self.assertEqual((host, port, timeout), ("127.0.0.1", 18080, 45.0))
            return conn
        r = infer(self.context, self.config, connection_factory=factory)
        self.assertTrue(conn.closed)
        self.assertEqual(conn.sent[:2], ("POST", "/v1/chat/completions"))
        self.assertNotIn("tools", json.loads(conn.sent[2]["body"]))
        return r

    def test_success_is_unvalidated(self):
        r = self.run_fake(envelope('{"anything":true}'))
        self.assertEqual(r["status"], "completed_unvalidated")

    def test_non_success_and_redirect_not_followed(self):
        for status in (302, 404, 429, 500):
            self.assertEqual(self.run_fake({}, status=status)["reason"], "http_non_success")

    def test_timeout_and_refusal(self):
        self.assertEqual(self.run_fake(error=TimeoutError())["reason"], "socket_timeout")
        self.assertEqual(self.run_fake(error=ConnectionRefusedError())["reason"], "transport_error")

    def test_response_limit(self):
        self.assertEqual(self.run_fake(raw=b"x" * (MAX_RESPONSE_BYTES+1))["reason"],
                         "response_byte_budget_exceeded")

    def test_invalid_envelope_and_duplicate_keys(self):
        for raw in (b"invalid", b'{"choices":[],"choices":[]}'):
            self.assertEqual(self.run_fake(raw=raw)["reason"], "invalid_response_envelope")

    def test_truncated_or_wrong_model(self):
        self.assertEqual(self.run_fake(envelope("{}", finish="length"))["reason"], "generation_incomplete")
        self.assertEqual(self.run_fake(envelope("{}", model="other"))["reason"], "unexpected_model")

    def test_no_tools(self):
        value = envelope("{}")
        value["choices"][0]["message"]["tool_calls"] = [{"id":"example"}]
        self.assertEqual(self.run_fake(value)["reason"], "unexpected_tool_request")

    def test_encoding(self):
        self.assertEqual(self.run_fake({}, encoding="gzip")["reason"], "unsupported_content_encoding")

    def test_request_bound_before_connection(self):
        ctx = copy.deepcopy(self.context)
        ctx["limitations"].append("x" * 32768)
        def forbidden(*a, **kw):
            self.fail("must not connect")
        self.assertEqual(infer(ctx, self.config, connection_factory=forbidden)["reason"],
                         "invalid_or_oversized_request")

    def test_config_bounds(self):
        for kwargs in ({"port":0}, {"model":"bad model"}, {"max_tokens":4097}, {"timeout":0}):
            with self.assertRaises(ValueError):
                LocalConfig(**kwargs)


try:
    import jsonschema
except ImportError:
    jsonschema = None


@unittest.skipIf(jsonschema is None, "optional jsonschema dependency unavailable")
class ContractAndWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.baseline = report()
        self.context = prepare_context(self.baseline)["context"]
        self.value = candidate(self.context)

    def test_schema_is_valid(self):
        jsonschema.Draft202012Validator.check_schema(OUTPUT_SCHEMA)

    def test_scope_from_refs(self):
        r = validate_output(json.dumps(self.value), self.context)
        self.assertEqual(r["status"], "admitted_unadjudicated")
        self.assertEqual(r["derived_scope"]["observed_at_max"], "2026-11-22T10:01:30Z")
        self.assertIsNone(r["derived_scope"]["target_hostname"])

    def test_unknown_id_shape_valid_but_rejected(self):
        self.value["next_check"]["basis_event_ids"] = ["evt-" + "0"*20]
        self.assertTrue(jsonschema.Draft202012Validator(OUTPUT_SCHEMA).is_valid(self.value))
        with self.assertRaisesRegex(ContractError, "out_of_context"):
            validate_output(json.dumps(self.value), self.context)

    def test_extra_fields_blank_text_and_duplicate_refs(self):
        for mutate in (
            lambda v: v.update(target_hostname="invented"),
            lambda v: v.update(uncertainty="   "),
            lambda v: v["next_check"]["basis_event_ids"].append(v["next_check"]["basis_event_ids"][0]),
        ):
            value = copy.deepcopy(self.value)
            mutate(value)
            with self.assertRaisesRegex(ContractError, "schema_mismatch"):
                validate_output(json.dumps(value), self.context)

    def test_invalid_json_and_duplicate_keys(self):
        for text in ("not json", '{"uncertainty":"a","uncertainty":"b"}', '{"uncertainty":NaN}'):
            with self.assertRaisesRegex(ContractError, "invalid_output_json"):
                validate_output(text, self.context)

    def test_semantic_falsehood_not_certified(self):
        self.value["hypotheses"] = [{"explanation":"The server was definitely compromised.",
                                      "basis_event_ids":[self.context["events"][0]["event_id"]],
                                      "limitation":"Unsupported assertion."}]
        self.assertEqual(validate_output(json.dumps(self.value), self.context)["status"],
                         "admitted_unadjudicated")

    def test_ineligible_empty_no_model_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.jsonl"
            path.write_bytes(b"")
            baseline = analyze(path, source_id="fixture:empty", source_kind="synthetic")
        def forbidden(*a):
            self.fail("must not invoke")
        r = investigate(baseline, LocalConfig(), inference=forbidden)
        self.assertEqual(r["investigation"]["status"], "not_invoked")
        self.assertEqual(r["baseline"], baseline)

    def test_unverified_import_does_not_invoke(self):
        baseline = analyze(FIXTURE, source_id="fixture:import", source_kind="unverified_import")
        def forbidden(*a):
            self.fail("must not invoke")
        r = investigate(baseline, LocalConfig(), inference=forbidden)
        self.assertEqual(r["investigation"]["reason"], "synthetic_only_experiment")
        self.assertEqual(r["baseline"], baseline)

    def test_optional_validator_missing_does_not_invoke(self):
        def forbidden(*a):
            self.fail("must not invoke")
        with patch.dict("sys.modules", {"jsonschema": None}):
            r = investigate(self.baseline, LocalConfig(), inference=forbidden)
        self.assertEqual(r["investigation"]["reason"], "validator_unavailable")
        self.assertEqual(r["baseline"], self.baseline)

    def test_transport_failure_preserves_baseline(self):
        before = copy.deepcopy(self.baseline)
        r = investigate(self.baseline, LocalConfig(), inference=lambda *a: {
            "status":"not_completed", "reason":"transport_error"})
        self.assertEqual(r["investigation"]["status"], "not_admitted")
        self.assertEqual(r["baseline"], before)

    def test_invalid_response_preserves_baseline(self):
        before = copy.deepcopy(self.baseline)
        r = investigate(self.baseline, LocalConfig(), inference=lambda *a: {
            "status":"completed_unvalidated", "content":"not JSON"})
        self.assertEqual(r["investigation"]["status"], "not_admitted")
        self.assertNotIn("content", r["transport"])
        self.assertEqual(r["baseline"], before)

    def test_valid_response_preserves_baseline(self):
        before = copy.deepcopy(self.baseline)
        r = investigate(self.baseline, LocalConfig(), inference=lambda *a: {
            "status":"completed_unvalidated", "content":json.dumps(self.value)})
        self.assertEqual(r["investigation"]["status"], "admitted_unadjudicated")
        self.assertEqual(r["baseline"], before)

if __name__ == "__main__":
    unittest.main()
