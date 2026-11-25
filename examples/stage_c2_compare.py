"""C2 exploratory paired contract/context comparison; synthetic only.
Run from repo root: PYTHONPATH=src python3 examples/stage_c2_compare.py
Emits one JSON record per trial, with exact prompt/schema/context.
No tools, writes by model, remote providers or live sensor queries.
"""
import copy
import json
import time
import urllib.request
from pathlib import Path
import stage_c2_probe as base
from aegislab.ssh_incident import analyze

OLD_SENTENCE = (
    "If evidence is insufficient, abstain with "
    "disposition insufficient_evidence, empty hypotheses and null next_check. "
)
PROMPT = base.PROMPT.replace(
    OLD_SENTENCE,
    "If no evidence supports a hypothesis, use an empty hypotheses array. "
    "If no useful evidence-linked check is possible, use null next_check. "
    "Uncertain incident attribution alone does not prevent a useful check. "
)
assert PROMPT != base.PROMPT
SCHEMA = base.obj({k: v for k, v in base.SCHEMA["properties"].items()
                   if k != "disposition"})

# Hypothetical coverage metadata, not collected telemetry. All variants
# receive the same information; only its representation changes in v0.3.
CASES = [
    ("burst_missing", "ssh-auth-burst.synthetic.jsonl", "fixture:ssh-burst-v1",
     {"network_sensor_status": "unavailable", "network_correlation": "not_assessed",
      "coverage": "unavailable", "scope": "corresponding TCP connection during supplied SSH observation interval"}),
    ("burst_discrepancy", "ssh-auth-burst.synthetic.jsonl", "fixture:ssh-burst-v1",
     {"network_sensor_status": "available", "network_correlation": "no_match_observed",
      "coverage": "stipulated adequate for the scoped synthetic interval; clocks and correlation correctness not independently established",
      "scope": "corresponding TCP connection during supplied SSH observation interval"}),
    ("normal", "ssh-auth-normal.synthetic.jsonl", "fixture:ssh-normal-v1",
     {"network_sensor_status": "unknown", "network_correlation": "not_assessed",
      "coverage": "unknown", "scope": "network corroboration"}),
    ("empty", None, "lesson:c2-empty",
     {"network_sensor_status": "unknown", "network_correlation": "not_assessed",
      "coverage": "unknown", "scope": "no SSH observations to correlate"}),
]

def validate(content, finish, events, version):
    if version == "0.1":
        return base.validate(content, finish, events)
    if finish != "stop":
        raise ValueError("incomplete generation")
    if not isinstance(content, str) or len(content.encode()) > 8192:
        raise ValueError("response size/type")
    data = json.loads(content, object_pairs_hook=base.unique_object)
    if not isinstance(data, dict) or set(data) != set(SCHEMA["required"]):
        raise ValueError("unexpected object keys")
    hypotheses, check = data["hypotheses"], data["next_check"]
    # Reuse the old field checks without inheriting its requirement
    # that hypotheses and next_check must always occur together.
    if not isinstance(hypotheses, list) or len(hypotheses) > 2:
        raise ValueError("invalid hypotheses")
    # Validate each independently using a minimal valid counterpart
    # constructed from existing references, never published as model output.
    if hypotheses or check is not None:
        if not events:
            raise ValueError("no supplied references")
        test = copy.deepcopy(data)
        test["disposition"] = "investigate"
        first = [events[0]["event_id"]]
        if not hypotheses:
            test["hypotheses"] = [{"explanation": "placeholder", "limitation": "placeholder",
                                    "basis_event_ids": first}]
        if check is None:
            test["next_check"] = {"basis_event_ids": first, "objective": "placeholder",
                                  "required_evidence": "placeholder", "if_present": "placeholder",
                                  "if_unavailable": "placeholder"}
        _, scope = base.validate(json.dumps(test), finish, events)
        return data, scope if check is not None else None
    test = dict(data, disposition="insufficient_evidence")
    base.validate(json.dumps(test), finish, events)
    return data, None

def run(case, version):
    name, filename, source_id, quality = case
    path = Path("examples/fixtures") / filename if filename else Path("/dev/null")
    report = analyze(path, source_id=source_id, source_kind="synthetic")
    fields = ("event_id", "observed_at", "outcome", "source_ip", "username", "source_port", "sshd_pid")
    events = [{k: e[k] for k in fields} for e in report["events"]]
    context = {"source_kind": "synthetic", "status": report["status"], "events": events,
               "findings": report["findings"], "limitations": list(report["limitations"]),
               "target_hostname": None}
    # Explicitly distinguish simulated metadata from a real sensor result.
    context["limitations"].append("Network coverage/correlation metadata in this case is hypothetical synthetic test input, not live telemetry.")
    if version == "0.3":
        context["network_evidence_quality"] = quality
    else:
        context["limitations"].append("; ".join(k + ": " + v for k, v in quality.items()))
    schema = base.SCHEMA if version == "0.1" else SCHEMA
    prompt = base.PROMPT if version == "0.1" else PROMPT
    payload = {"model": base.MODEL, "messages": [
        {"role": "system", "content": prompt},
        {"role": "user", "content": json.dumps(context, separators=(",", ":"))}],
        "temperature": 0, "max_tokens": 2048, "stream": False,
        "response_format": {"type": "json_schema", "json_schema": {
            "name": "c2_probe", "strict": True, "schema": schema}}}
    raw = json.dumps(payload).encode()
    assert len(raw) <= 16384 and len(events) <= 4
    result = {"case": name, "version": version, "baseline_source": report["source"],
              "baseline_status": report["status"], "request": payload,
              "mechanical_status": "not_admitted"}
    start = time.monotonic()
    try:
        req = urllib.request.Request(base.ENDPOINT, data=raw, method="POST",
                                     headers={"Content-Type": "application/json"})
        with urllib.request.build_opener(urllib.request.ProxyHandler({}), base.NoRedirect()).open(req, timeout=45) as response:
            result["http_status"] = response.status
            body = response.read(131073)
            if len(body) > 131072:
                raise ValueError("oversized response")
        body = json.loads(body, object_pairs_hook=base.unique_object)
        choice = body["choices"][0]
        result.update(model_reported=body.get("model"), usage=body.get("usage"),
                      finish_reason=choice["finish_reason"], content=choice["message"].get("content"))
        if body.get("model") != base.MODEL or choice["message"].get("tool_calls"):
            raise ValueError("unexpected model or tool call")
        data, scope = validate(result["content"], result["finish_reason"], events, version)
        result.update(mechanical_status="admitted_unadjudicated", parsed=data, derived_scope=scope)
    except (OSError, ValueError, TypeError, KeyError, IndexError) as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    result["elapsed_seconds"] = round(time.monotonic() - start, 2)
    return result

def main():
    versions = ["0.1", "0.2", "0.3"]
    for i, case in enumerate(CASES):
        # Rotate order to partially reduce position effects; not randomized replication.
        for version in versions[i % 3:] + versions[:i % 3]:
            result = run(case, version)
            print(json.dumps(result, ensure_ascii=False), flush=True)
            if "http_status" not in result:
                return  # transport failure: stop, retain partial results
if __name__ == "__main__":
    main()
