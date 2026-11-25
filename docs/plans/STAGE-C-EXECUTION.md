# Stage C — Local AI investigation execution plan

**Adopted:** 2026-11-24 (owner approved execution planning). **Authority:** subordinate to [Core Charter v2](<AegisLab — Core Charter v2.0.md>) and [Capability Execution Map v2](<AegisLab — Capability Execution Map v2.md>). Current state lives in [PROJECT_STATE](../../PROJECT_STATE.md); learning depth in [Learning Ledger](../learning/LEARNING_LEDGER.md).
**Scope:** optional local, advisory investigator for the first SSH evidence workflow. No live collection, agents, tools, shell, autonomous response, external services or advanced ML in C. D/E own live collection and authorized tool execution. C2 contract below is a candidate under evaluation, not a shipped interface.

## Milestones and gates

| ID | Work and deliverable | Acceptance evidence | Status |
|---|---|---|---|
| C1 | Local inference foundation | Direct loopback catalog and completion; model ID, request and token budget, latency, truncated response and recovery documented; learner explains HTTP versus generation success | Exploratory foundation demonstrated; runtime readiness must be rechecked |
| C2 | Investigator responsibility and output contract | Concrete operator task, responsibilities, non-responsibilities, missing-evidence behavior, candidate contract and critique on positive and insufficient evidence; baseline comparison, explicit open decisions | Active design/evaluation |
| C3 | Context builder and versioned contract | Deterministic scoped context, supporting and related evidence, omissions/counts/source limitations, budgets and no truth leakage; malformed, missing and oversized context tests; schema and nullable/abstention semantics | Pending |
| C4 | Reusable local inference client | Explicit opt-in, configured local endpoint/model, proxy bypass, no redirect to external endpoint, bounded bytes/tokens/time, observable error categories, no tools; mocked transport and real bounded request | Pending |
| C5 | Independent validation and fallback | Strict response parsing/schema, permitted IDs and scoped facts, reject incomplete generation, invalid references, unsupported request kinds; separate unadjudicated semantics; preserve unchanged baseline on errors, test failure paths | Pending |
| C6 | Versioned evaluation harness | Fixed cases, separate truth/expected properties, same evidence baseline, claim-level adjudication and recorded disagreements; metrics and exact run configuration; positive/normal/ambiguous/gap/failure cases | Pending (initial human review only) |
| C7 | Controlled model/config comparison | Compare selected local model/prompt/schema/budget configurations across fixed cases; repeated runs, resource and latency observations, regression/holdout cases, documented selection or rejection; no single-run speed conclusions | Pending |
| C8 | Optional AI ON/OFF CLI and acceptance | Reproducible CLI demos with identical evidence, evaluated value beyond baseline, reliable mechanical rejection and deterministic fallback, security boundaries and human review; learner can diagnose a changed case and explain trade-offs; record unresolved gates | Pending |

Each milestone closes only with engineering evidence, safety/reliability checks, learner evidence and durable handoff (separate statuses). No arbitrary deadline or overall percent. Stop when safety or evidence gate fails; record partial results. Do not skip the independent Stage B practical exercise; it may run in parallel with C learning and remains open until the learner personally modifies, runs and diagnoses a case.

## C2 — operator task and proposed boundary

Given a bounded Stage B report, help a human decide what additional authorized observation would reduce uncertainty about a specific finding (or explain why there is insufficient evidence). Do not detect new attacks, assign attacker identity, establish compromise, rewrite deterministic facts, infer actual client actions, invent source metadata, or execute checks. AI OFF remains useful. Related accepted observations are included when relevant, not merely threshold-supporting events. For small fixtures include all accepted events; larger selection and explicit omissions belong to C3. The model never receives independent experimental truth or answer keys. The baseline exposes the same underlying evidence, not a deliberately impoverished summary.

Ownership:
- Deterministic report owns counts, times, source declarations, IDs, finding status, quarantine and limitations.
- Context builder owns evidence selection, bounds and omitted counts; explicit insufficient context state if necessary.
- Model owns tentative explanations and proposed evidence needs; it may abstain without inventing a hypothesis.
- Validator owns syntax, reference existence in *supplied* context, scope consistency and boundedness. It cannot prove arbitrary prose entails evidence.
- Human evaluation owns semantic adjudication and usefulness; tool authorization/execution is not part of C.

## Candidate C2 output contract (version 0.1, exploratory probe only; not integrated)

A single JSON object, no surrounding prose. Required keys:
- `disposition`: `investigate` or `insufficient_evidence`.
- `hypotheses`: 0–2 objects, each with `explanation` (tentative nonempty text), `basis_event_ids` (nonempty subset of supplied IDs), `limitation` (nonempty text). Never force two hypotheses when only one or none is defensible.
- `next_check`: null or object with `objective`, `basis_event_ids`, `required_evidence`, `if_present`, `if_unavailable` (nonempty bounded strings except IDs array); a proposed read-only evidence need, not a command or a permission grant.
- `uncertainty`: nonempty text explaining what is not established, including synthetic/unverified source and missing evidence where relevant.

For `investigate`, require at least one hypothesis and a non-null next check. For `insufficient_evidence`, require empty hypotheses and null next check in this candidate. Insufficient evidence to attribute compromise is not necessarily insufficient evidence to propose a useful investigation. Reject unknown keys, wrong types, empty strings/IDs where required, oversized fields or duplicate IDs within each list, invalid disposition, out-of-context IDs and incomplete generations. C3 will define exact byte/token/string caps, typed schema and bounded selection; prototype caps are not final. Never accept an invented hostname: scope is derived deterministically from referenced normalized events (account/IP/time/IDs), not generated by the model; unavailable target identity remains null/unknown. A range derived from event times is an observation range, not proof of a complete collection interval. Do not silently substitute a hostname or pretend required evidence exists. Hypotheses/proposals remain labeled unadjudicated unless reviewed. A mechanically valid response is not equivalent to a semantically accepted report.

## Evaluation and acceptance approach

| Criterion | Test |
|---|---|
| Mechanical admission | Parse strict JSON, exact keys/types, disposition rules, bounded fields and supplied references. Fail closed for malformed/truncated/unknown-ID outputs. |
| Semantic correctness | Claim-level comparison with evidence; distinguish records from actions, observation from hypothesis, synthetic from live and unknown from disproven; no invented metadata. |
| Additional operator value | Compared with identical-evidence AI OFF, does the proposal provide a concrete question and plausible alternatives rather than rephrase the report? |
| Actionability | Is the additional evidence specified, scope derivable, missing data acknowledged, and possible results explained without pretending that a check has run? |
| Reliability | Log model ID, prompt/schema revision, input and generation budgets, usage, finish status, elapsed time and error; preserve baseline on failure. |

C6 must freeze cases and evaluation rubric before comparing configurations. Include repeated-failure plus acceptance, normal/no finding, ambiguous multi-subject or duplicates, quarantined data, empty/invalid input, unavailable model, malformed/truncated response, unknown evidence reference and a valid-looking unsupported claim. Keep expected properties separate from model context. Count mechanical pass, supported/unsupported claims and operator-task usefulness separately; record case denominators and reviewer disagreements. No arbitrary numerical performance target until the evaluation task and cost envelope are defined. Safety gate: no fabricated evidence promoted to fact; no unauthorized execution; baseline remains available. If no measurable added value, stop/revise or retain AI OFF rather than claim success.

## Industry-tool checkpoints

Follow the [industry tooling register](INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md). C3/C5 compare and practically exercise a mature validator (Pydantic or JSON Schema); C6 review/exercise Promptfoo against the same fixed local cases and a simple reproducible baseline, after verifying local-only behavior. C7 review an alternative local runtime only if useful and resource-appropriate. Record evidence, learner depth and explicit adoption/deferral decisions; do not alter C2 or relax semantic and safety gates to adopt a library. Schedule the bounded Sigma comparison after C2 alongside C; Wazuh before or during D/F.

## Learning checkpoints

C1: explain GET/POST, context versus generation budget, finish reason and warm/cold confounders. C2/C3: choose context scope, unknown-value representation, and assess evidence entailment. C4/C5: trace a request, deliberately fail a bounded case and explain fallback. C6/C7: evaluate a response blind to expected answer, compare fixed cases and interpret cost/quality trade-offs. C8: reproduce and diagnose an unfamiliar case personally when PC access permits. See ledger for depth and recall status.

## Immediate next work

Review the [C2 probe and reconciliation](../worklogs/2026-11-24-1953-learning-reconciliation-and-stage-c2.md): 1/2 mechanically admitted, positive case rejected for contradictory abstention; empty input correctly abstained. Handwritten controls confirmed structural rejection and exposed the semantic limit. The [paired comparison](../worklogs/2026-11-25-1511-c2-contract-context-comparison.md) tested original, simplified and structured-quality variants across four synthetic cases: 2/4, 3/4, 4/4 mechanical admissions; no adequate quality handling in six missing/discrepancy responses. Keep C2 open. Review actual output with learner, consider deterministic eligibility and operator-question-focused context without redundant baseline recommendation, and test bounded changes including a changed case before freezing C3. The approved plan does not authorize live SSH changes, model service exposure, arbitrary tools, or Stage D/E operations.
