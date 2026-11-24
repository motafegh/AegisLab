# 2026-11-24 — Learning reconciliation and Stage C2 design probe

## Session metadata

- **Started:** 2026-11-24 19:53 +03:30 (reconciliation; earlier sessions reconstructed below)
- **Status:** completed (planning and exploratory evaluation; C2 design gate open)
- **Objective:** synchronize actual learning/engineering evidence, adopt the Stage C execution plan and ledger, evaluate a bounded investigator contract.
- **Primary role:** Reviewer / Teacher / Evaluator; direct execution for records and probe, learner-owned reasoning retained.
- **Starting revision:** feed0b428f94e2e3cf936de89b455ac90537ff1e (local/remote main matched; clean).
- **Continues:** [Core v2 and Stage B](2026-11-22-2013-core-v2-stage-b.md).
- **Authority:** historical evidence; not a normative specification.

## Scope and success criteria

Record recent Stage B and Stage C work with exact observed results where retained, explicit attribution and gaps; create/link the plan and ledger; exercise one positive and one insufficient-evidence case against an advisory C2 candidate; verify links and tests. No integrated AI CLI, new detector rules, live SSH collection, privileges, external API, agent tools or persistent model configuration changes.

## Reconstructed Stage B learning and experiments (November 23–24)

The following is reconstructed from the actual teaching-session outputs, not a retroactively invented contemporaneous lab log. The learner personally ran WSL socket inspection (`ss -ltn`, `ss -tn`, `ss -ltnp`), process listing and `journalctl -t sshd --no-pager -n 10` (no matching entries), and inspected the first three synthetic input lines. The process listing supported conventional Redis/PostgreSQL/DNS service hypotheses, not direct socket ownership; no matching sshd process was observed. No live SSH telemetry was collected. Host/process/network details unrelated to the synthetic case are intentionally omitted.

AI reran from WSL repo root: `PYTHONPATH=src python3 -m aegislab analyze --input examples/fixtures/ssh-auth-burst.synthetic.jsonl --source-id fixture:ssh-burst-v1 --json` and the normal fixture with `fixture:ssh-normal-v1`; `PYTHONPATH=src python3 -m unittest discover -s tests -v` returned 15/15 pass. Burst: four accepted events, three distinct failed records over 80s, finding-bb327298c251bbf8b102; supporting events evt-92dd78ac94389f505d01, evt-9830f50593d9fc2c0306, evt-6b77aa30169c4e13c524. The fourth event records acceptance; no actual attack or compromise is established. Normal: two accepted events, no finding.

Temporary variations of the synthetic fixture (AI executed via remote WSL; no source changes):
| Case | Input change | Observed status / counts |
|---|---|---|
| Exact boundary | Three distinct failed records at 0/30/120s | finding_present; 3 accepted |
| Outside boundary | 0/30/121s | no_finding_observed; 3 accepted |
| Duplicate | Two distinct failure records plus exact duplicate | no_finding_observed; 3 accepted, 1 duplicate ignored |
| Malformed | Two valid failure records plus invalid JSON | incomplete_evidence; 2 accepted, 1 quarantined |
| Empty | Empty file | unassessable; 0 accepted |
| lesson:sliding-window-four | All four failures at 0/40/130/160s | finding_present; B,C,D support inclusive 120s; A preserved |
| lesson:sliding-window-171 | All four failures at 0/50/140/171s | no_finding_observed; all four preserved |
| lesson:composite-key | A,D same IP/account; B same IP/different account; C different IP/same account | no_finding_observed; 4 accepted; three groups |
| lesson:dedup-four | A,B,C=A,D different source port from A at same timestamp/PID | finding_present; 4 accepted, 1 duplicate ignored; A,B,D support |
| lesson:invalid-port | Four failure records; third source port 99999 | finding_present_with_gaps; 3 accepted, 1 quarantined (line 3, invalid_port); A,B,D support |

The learner first treated the window as fixed; after explanation correctly predicted 51s cutoff at 171s and asked why A remained outside the count. Correct composite grouping and limitation reasoning, distinct failure counting, invalid port and supported finding. Initially conflated parsed/accepted events with unique observations and JSON decoding with validation; both corrected. The AI ran the changed cases, not the learner. One shell-quoting error during the earlier probe was corrected and the intended case rerun. Personal fixture modification, execution, diagnosis and stable recall remain open. See [Learning Ledger](../learning/LEARNING_LEDGER.md).

## Reconstructed Stage C inference and human evaluation

Direct local endpoint `http://127.0.0.1:18080`; WSL proxy bypass explicit. GET /v1/models returned 200 and 14 listed models in the recent session; catalog is not loaded-model or inference proof. POST /v1/chat/completions used gemma-4-e2b-it, temperature 0, stream false; local Python HTTP client, no cloud or security tools. Earlier runs were temporary; exact full historical prompts/schema are not retained as files. Metrics below transcribed from returned tool results; latency not a controlled benchmark.

| Experiment | Input tokens | Max generation | Generated / reasoning | Duration | Result |
|---|---:|---:|---:|---:|---|
| TCP versus SSH auth (two short sentences) | 35 | 256 | 256 / 239 | 18.42s | HTTP 200, length; incomplete answer |
| Same task, increased budget | 35 | 512 | 280 / 237 | 2.52s | HTTP 200, stop; complete substantially correct answer |
| First investigation, five fields, prompt-only JSON | 781 | 1024 | 972 / 709 | 7.41s | HTTP 200, stop; Markdown fences caused strict JSON parsing failure |
| Revised investigation, two hypotheses and discriminating check, schema requested | 838 | 1536 | 1056 / 666 | 9.01s | HTTP 200, stop; JSON/required shape/two hypotheses/four references passed |

Earlier inference prompt: "What is the difference between an established TCP connection and successful SSH authentication? Answer in two short sentences." Increased budget fixed truncation in that trial, not proof of performance gains (loading/cache uncontrolled). First investigation mostly repeated baseline. Revised schema requested observation, evidence_event_ids, hypotheses, uncertainty, next_check and why_check_matters; model offered configuration/key error and provisioning routine, vaguely proposed correlating acceptance with prior failures, and referenced existing records. Human learner evaluation: semantic **partial**, additional value **fail**, hypotheses **partial**, investigation **fail**; requested precise next-check scope/fields/times and expressed uncertainty. AI review: semantic partial, other three partial but insufficient for acceptance. No invented hostname claimed in those runs; a later teaching example was hypothetical, not model output. The hypotheses overlap, "expired public key" is imprecise for ordinary SSH keys, wording does not sufficiently distinguish records from real actions, and check lacks a precise discriminating observation. Neither semantic accuracy nor usefulness has been established across cases.

Learner correctly distinguished catalog response from actual inference, proposed raising generation budget while balancing efficiency, reasoned about context selection and deterministic ownership, rejected unsupported compromise/attacker claims and identified three separate requirements (syntax, semantics, usefulness).

## Current session — C2 evaluation (actual new evidence)

Adopted [Stage C execution](../plans/STAGE-C-EXECUTION.md) and [Learning Ledger](../learning/LEARNING_LEDGER.md). Proposed C2 contract owns tentative hypotheses, evidence references, read-only proposed observations and uncertainty. Model cannot set factual target identity; application derives scope from references, unknown target remains null. Abstention is permitted and distinct from uncertainty about incident truth. No agent permission or execution. The [reproducible probe](../../examples/stage_c2_probe.py) uses only fixed synthetic inputs and a direct loopback API, proxy bypass, no redirects, bounded payload/body, generation cap 2048, socket timeout 60s (not a guaranteed hard wall-clock deadline), one request per case, temperature 0, exact prompt/schema in script. Run from root: `PYTHONPATH=src python3 examples/stage_c2_probe.py`. The [actual response record](evidence/2026-11-24-stage-c2-probe.json) includes both selected contexts, baseline source/status, outputs, metrics, mechanical decisions. No independent truth supplied; deterministic baseline stays intact.

| Case | Result | Adjudication |
|---|---|---|
| Burst + acceptance | HTTP 200, stop; 881 input, 980 output (689 reasoning); 8.48s; insufficient_evidence with nonempty hypotheses and null check | Rejected by cross-field validator. It offers one tentative explanation but no next observation; treats insufficient incident attribution as insufficient investigation. Does not explicitly label observations synthetic in answer; no added operator value established. |
| Empty | HTTP 200, stop; 270 input, 435 output (378 reasoning); 3.57s; insufficient_evidence, empty hypotheses, null check | Mechanically admitted; human review supports "No events were supplied for assessment." Correct abstention, repeats baseline; no added value expected or established. |

Mechanical pass: 1/2. Neither case establishes improved investigative usefulness. Structured generation can still violate cross-field semantics. The two trials are not a model ranking or a general failure-rate estimate.

Offline handwritten control checks (AI authored/ran, not model results): valid candidate admitted unadjudicated; deterministic scope derived account labuser, IP 10.10.0.1, observed range 10:00:00–10:01:30 UTC and hostname null. Unknown evidence ID rejected; extra invented hostname field rejected; contradictory abstention rejected; finish_reason length rejected; valid-shaped prose asserting definite compromise admitted **unadjudicated**, illustrating need for semantic review. All six expectations matched. This does not prove an automated semantic validator exists.

## Decisions, limitations and next action

- Keep C2 candidate as experimental. Clarify that insufficient evidence to establish compromise is not necessarily insufficient evidence to propose a helpful next check; an abstention must be internally consistent. Consider removing baseline recommendation text from model context while preserving equal human access to full baseline evidence to avoid parroting; compare fairly in C3/C6.
- C3–C8 are not shipped. Freeze no contract until learner reviews C2 findings and explicit scope/unknown representation. Probe is intentionally fixed and small, not a general client or test suite. No claims of repeatability, security detection effectiveness or operational AI reliability.
- Stage B software verified; learner reasoning progressed but personal execution/diagnosis remains open. Revisit when computer access permits. No privileged changes, real credentials, live telemetry, agent actions, persistent model settings or external APIs.
- Update [project state](../../PROJECT_STATE.md), [learning handoff](../learning/CURRENT_LEARNING_STATE.md), plan and ledger. Preserve accepted Charter and historical docs. Repository changes limited to documentation, synthetic probe and its result.
- Next: learner evaluates the positive response's abstention contradiction, the meaning of unknown hostname and a specific proposed observation; decide C2 disposition wording and contract refinement before C3.

## Verification

Final WSL verification: 15/15 Stage B tests passed; burst CLI reproduced the finding ID, three supporting events and four accepted records. Checked 85 relative file-link targets across nine affected Markdown files: none missing. Probe Python compilation and result JSON parsing passed. Unstaged diff whitespace check passed. See commit for final tracked change set. The probe and its handwritten controls were executed as described; no additional model trials or independent analyst/user test claimed.
