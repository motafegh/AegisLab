# 2026-11-25 — Local inference, schema validation and experimental integration

- Started: 2026-11-25 20:13 +03:30 (WSL clock).
- Status: completed bounded implementation increment; C2–C5 and C8 acceptance remain open.
- Starting revision: c9715fd8242f15ff56bbd1e919ab356ec339b7cc; clean main, remote matched.
- Continues: [provisional context builder](2026-11-25-1824-provisional-context-builder.md).

## Learner evidence and direction

The learner requested larger connected engineering sessions and answered the previous seven questions. Correct reasoning: successful-authentication count alone cannot determine legitimacy; source IP and historical behavior can help; three failure records satisfy the rule; quarantined input is not evidence of absence; validator checks reference existence; explicit refusal on exceeded bounds; lineage supports traceability/reproduction; byte count does not establish token count. Q2 context selection and broader relevance needed guidance (same subject plus padded time range selects four of six, not all; omitted account or later event might matter). Quarantine does not prove actual activity; full reproducibility needs source/config/versions. Guided conceptual assessment, no independent execution or stable recall claimed. This session's implementation and tests are AI-operated.

## Implementation and decisions

- [Local client](../../src/aegislab/local_inference.py): direct stdlib HTTPConnection to numeric IPv4 loopback 127.0.0.1, configurable local port/model, POST /v1/chat/completions; no proxy or redirect following, no tool declarations. Immutable configuration; 32,768 request bytes, 131,072 response bytes, max generation 4096 (default 2048), socket timeout up to 60s (default 45), temperature 0, nonstreaming. Separately report HTTP, transport, generation, model ID and token usage. Reject non-200, unsupported encoding, oversized response, invalid JSON envelope/duplicate keys, unexpected model/tool request, non-stop finish, missing content. Socket idle timeout is not a hard end-to-end deadline. Full context token budgeting, provider runtime trust and total deadline are pending.
- [Provisional output contract](../../src/aegislab/investigator_contract.py): v0.2 simplified hypotheses and nullable next_check, no disposition; Draft 2020-12 JSON Schema bounds/types/required fields, unique ID shape and no extra properties. Strict JSON parser rejects duplicate keys and nonstandard constants. Separate dynamic membership check against context events; scope derived from cited observations; unknown hostname and coverage remain explicit. Schema-valid unsupported claim still mechanically admits as unadjudicated.
- Already installed jsonschema 4.10.3 exercised directly: schema self-check, valid candidate, unknown ID that satisfies schema but fails membership, extra keys, duplicate references and whitespace-only text. Optional lazy dependency only for probe; no install/pin/version audit or mandatory runtime adoption. Baseline remains stdlib. Pydantic not installed; comparison with another validator not necessary for this exercise.
- [Orchestrator](../../src/aegislab/investigator.py): deterministic eligibility; only declared synthetic sources permitted for this experiment (declaration is not attestation); optional validator availability checked before request; no inference on empty/invalid input; failure result preserves baseline; output remains unadjudicated. CLI --probe-investigator explicit opt-in, --model and --local-port only in probe mode. No live telemetry, tools, privileged actions or persistent runtime changes.
- Chosen prompt version ssh-investigation-task.v0.1 uses context task question, distinguishes log decisions/actual actions/auth/session, asks for tentative evidence-linked hypotheses and read-only evidence needs, preserves unknowns. General task remains broad; not a controlled C2 prompt comparison or final prompt. Output contract and bounds are provisional choices, not a final C2 decision.

## Observed verification

PYTHONPATH=src python3 -m unittest discover -s tests -v: initial 47/47 passed; added two no-invocation cases, reran -q: 49/49 passed (22 new). Tests cover mocked HTTP statuses/redirect, connection failure, timeout, byte bounds, invalid envelopes, unexpected model/tool calls, incomplete generation; schema, reference membership, baseline-preserving validation/failure, empty and non-synthetic inputs, missing optional dependency. No actual network fault was induced.

Actual local CLI command:
```bash
PYTHONPATH=src python3 -m aegislab analyze --input examples/fixtures/ssh-auth-burst.synthetic.jsonl --source-id fixture:ssh-burst-v1 --probe-investigator
```
[Retained CLI output](evidence/2026-11-25-stage-c4-cli-probe.json): baseline finding_present; context 2918 bytes; request 5628 bytes, response 4865 bytes; HTTP 200, model gemma-4-e2b-it, stop, 14.947s, prompt 1315/completion 1127/reasoning 585/total 2442 tokens. Transport completed_unvalidated, validator admitted_unadjudicated. Model reported no supported hypotheses as a hypothesis object, confused 10.10.0.1 (source IP) with target host, generated a time range including the acceptance but cited only failure IDs, described sshd evidence as client-side negotiation, and did not provide a sufficiently discriminating observation. It did acknowledge lack of correlation. Preliminary AI review: not suitable for unqualified operator use; actual semantic adjudication remains open. Derived scope correctly retains source IP, null target hostname, failure-event time range 10:00:00Z–10:01:20Z. No execution. Fresh analyze() baseline equals retained baseline exactly. [Reconstructed request](evidence/2026-11-25-stage-c4-reconstructed-request.json) generated from retained context/config and same code; byte length matches, not a captured network trace. The admitted parsed output and transport metadata are retained, not original raw response envelope/content formatting.
[Empty CLI output](evidence/2026-11-25-stage-c4-empty-probe.json): unassessable, context null, not_invoked/no_accepted_observations, no transport entry. Mock verifies zero calls. Correct refusal is not a no-activity claim.

## Next and limits

C2/C3/C4/C5 partial; C8 usefulness/safety/learner gate unchanged. Mature validator exercised by AI, learner practical exercise still open. Before accepting C4 implement/test whole-request deadline and token/request budget policy; before accepting C3/C5 define quality references/typed input trust boundary, finalize contract and meaningful semantic guard strategy. C2 bounded task-specific decision and Sigma practical comparison remain scheduled; do not repeat generic prompt tuning. C6/C7 formal evaluation/model selection pending. Learner should personally exercise schema/ref validation and local API failure, then integrate recall checks. No claim of mastery, production readiness, actual threat activity, source authenticity or authorized action.

Relative Markdown links checked: 95, none missing.
