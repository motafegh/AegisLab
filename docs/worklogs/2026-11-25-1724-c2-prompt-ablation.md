# 2026-11-25 — C2 investigative prompt and context ablation

- Started: 2026-11-25 17:24 +03:30 (WSL clock).
- Status: completed exploratory experiment; C2 design and human review remain open.
- Starting revision: 7f85ece412e496fc00e30daae194ea5d6ac48a70; local/remote main matched.
- Continues: [C2 contract/context comparison](2026-11-25-1511-c2-contract-context-comparison.md).
- Role: teacher/evaluator; AI operates WSL and local API, learner owns reasoning.

## Learner contribution and objective

Learner proposed clearer investigative direction in the system prompt and evidence references for hypotheses and conclusions, and asked about actual prompt/configuration. Reviewed that V0.2/V0.3 only changed abstention wording, not the investigative objective; distinguish reference existence, relevance and support. The learner has not independently adjudicated the prior V0.3 timestamp/missing-evidence example; keep practical and semantic-review ownership open. This experiment implements the agreed prompt-first direction without adding schema fields.

## Protocol

[Experiment script](../../examples/stage_c2_prompt_ablation.py) reuses exact stored V0.3 request envelopes from [previous results](evidence/2026-11-25-stage-c2-comparison.jsonl). Local model catalog listed gemma-4-e2b-it. Same model, temperature 0, max_tokens 2048, nonstreaming, strict schema requested, socket timeout 45s (not a hard deadline), direct loopback, explicit proxy bypass and no redirects. No model tools, real telemetry, installations or persistent runtime changes.

Control = fresh replay of old V0.3. P1 = revised system prompt only (unresolved question, relevant evidence references, distinguish absent vs unavailable, preserve discrepancies, conditional evidence needs, no regenerated scope, no invented metadata, no forced hypothesis). P2 = same P1 prompt, removing only next_permitted_observation from model-visible findings. The operator's full context is retained separately in every result. All three maintain the same output schema and mechanical validator; quality field names may be used in prose because they do not have individual event IDs. Verified exact request equality for control, only system-message difference for P1, only recommendation removal for P2, operator context identical for each shared case.

Plan: 3 variants on each of the missing-sensor and discrepancy cases (6 trials); P1 on normal and empty (2 trials); P2 on a pre-specified changed case (partial coverage with scoped no-match, same SSH records; 1 trial). Nine requests total, one per condition. Reordered the second case to reduce simple order effects, not randomized/replicated. Changed case is a limited transfer check, not a blinded independent holdout. Normal/empty use prior V0.3 outputs as descriptive historical comparators, not fresh paired controls.

Review criteria: mechanical admission; faithful interpretation of synthetic evidence and network state; specific useful next observation and conditional meaning; meaningful references/scope; no invented conclusion or certainty; token/latency metrics descriptive only. Preserve no-AI baseline. Judge prompt package effect separately from removal of recommendation; do not attribute any effect to an individual sentence. Full requests/results: [prompt ablation JSONL](evidence/2026-11-25-stage-c2-prompt-ablation.jsonl).

## Actual results

All nine HTTP requests returned 200 and stop; all nine mechanically admitted as unadjudicated. No truncated completions or transport failures.

| Case | Variant | Input / completion / reasoning tokens | Seconds |
|---|---|---|---:|
| burst_missing | control | 958 / 1054 / 629 | 11.76 |
| burst_missing | P1 | 1062 / 1686 / 834 | 13.71 |
| burst_missing | P2 | 1039 / 1268 / 781 | 10.20 |
| burst_discrepancy | P2 | 1056 / 1812 / 981 | 14.75 |
| burst_discrepancy | control | 975 / 1199 / 616 | 10.17 |
| burst_discrepancy | P1 | 1079 / 1637 / 785 | 13.48 |
| normal | P1 | 620 / 1425 / 789 | 11.74 |
| empty | P1 | 448 / 724 / 590 | 6.06 |
| burst_partial_coverage | P2 | 1050 / 1450 / 979 | 12.07 |

## Preliminary AI adjudication (not independent human review)

- Missing: control again omits the network condition, repeats baseline and asserts low uncertainty without justification. P1 acknowledges lack of network correlation but not the exact unavailable/not_assessed state, links four different process IDs/source ports to a speculative single session, and still proposes broad authentication/session corroboration. P2 omits the network gap, returns null next_check and explicitly reverses the supplied limitation by saying no finding means activity was absent. This is a semantic contradiction despite valid references.
- Discrepancy: control ignores the stipulated no-match and repeats baseline. P1 ignores the no-match, misidentifies sshd server-side records as client-side negotiation events, and claims one success favors legitimacy whereas multiple/no successes favor adversarial intent; the counts alone do not justify that interpretation. P2 offers a more specific client-side evidence need but neglects the discrepancy and improperly labels the existing finding bounded negative evidence regarding intrusion. Valid IDs do not establish relevance or support.
- Normal: P1 suggests possible session hijacking without a distinguishing observation, conflates key exchange, authentication and session status, and says the failure type is not detailed despite failed_publickey. No rule match is not proof of benign activity, but neither is ordinary variation sufficient to suggest hijacking. Do not claim an incident.
- Empty: P1 correctly returns no hypotheses and null next_check, preserves unknown activity and mentions unknown network quality. Correct abstention, not additional operator value beyond baseline.
- Changed partial coverage: P2 omits partial coverage and no-match, supplies null next_check and mislabels the failure observations negative evidence regarding malicious intent. Transfer of the intended distinction not established.

The prompt package improved acknowledgment of correlation limits in one missing-sensor response, not reliable grounding. Removing the recommendation reduced direct parroting, but did not yield a consistently useful next observation and caused null checks in two of three P2 trials. None of the seven burst outputs adequately handled the specific quality condition; one partially acknowledged it. The normal and empty cases are descriptive historical comparisons, not controlled pairs. All nonempty trials remain unsuitable for unqualified operator use; the empty response correctly abstained. Not a formal usefulness score or general reliability estimate. One run per condition, runtime settings/cache not fully controlled, evaluator is AI and learner adjudication pending. P1 and P2 generated more tokens than control on both shared cases except no exception in these observed pairs; this is not a general cost conclusion. Exact prompts and data are retained.

## Decisions and next action

Do not keep tuning the generic prompt indefinitely or add compulsory fields solely to force wording. Provisional simplified V0.3 schema remains a useful mechanical interface, not a proven investigator. Next consider a task-specific operator question (e.g., determine what evidence would clarify a specific cross-source gap), deterministic evidence-quality presentation and eligibility, and a small general evidence-reference design in C3. A bounded explicit-task check or alternate local model comparison can test capability; formal selection and repeated comparative evaluation belong to C6/C7. Keep C2 design gate open for learner review and explicit decision, but distinguish design completion from eventual usefulness acceptance at C8. Sigma remains scheduled after C2 alongside C; Stage B practical ownership open. No claims of live network corroboration, authorized execution or production readiness.

## Verification

All nine requests and operator contexts verified against the script and retained V0.3 controls, all nine mechanical decisions replayed offline. Probe compiled; all 15 existing Stage B tests passed. No changes under src/ or tests/. No new dependencies, live sensors, tools or persistent runtime configuration changes. Historical control and results preserved.

Relative Markdown file links checked: 65, none missing.
