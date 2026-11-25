# 2026-11-25 — C2 paired contract and context comparison

- Started: 2026-11-25 15:11 +03:30 (local WSL clock).
- Status: completed (exploratory comparison; C2 gate and learner review remain open).
- Starting revision: 47381caaeac96546524581f4f763cff942d85ffb; local/remote matched at inspection.
- Continues: [learning reconciliation and C2](2026-11-24-1953-learning-reconciliation-and-stage-c2.md).
- Role: teacher/evaluator; AI operates the lab, learner owns reasoning. No independent practical mastery claimed.

## Learner-owned reasoning

In intervening teaching checkpoints, learner assigned critical authority to deterministic/external components and observed that source facts belong to acquisition; refined by distinguishing observations from authenticated truth and human judgment from deterministic checks. Learner distinguished incomplete from corrupted/wrong evidence, proposed preserving uncertainty and explaining its impact, and identified the missing network correlation state as a problem in a fabricated negative-evidence inference. Guided correction: unavailable/not_assessed does not establish no matching connection; a tentative hypothesis cannot repair an unsupported premise. This is conceptual reasoning, not a demonstrated live multi-sensor or independent diagnosis.

## Experimental protocol

[Comparison script](../../examples/stage_c2_compare.py) uses fixed synthetic cases and the previously recorded [probe](../../examples/stage_c2_probe.py). Local catalog reachable and listed gemma-4-e2b-it before trial. Same model, temperature 0, max_tokens 2048, nonstreaming, strict schema requested, local loopback only, proxy bypass/no redirects, bounded bytes, socket timeout 45s (not a hard deadline). One trial per version per case, rotated order, no replicated runs. V0.1 retains disposition and original instructions, V0.2 removes disposition and permits independently empty hypotheses/null check, V0.3 uses identical V0.2 output schema/prompt and structured network quality rather than equivalent textual limitations. Prompt and schema change together in V0.2; cannot isolate their effects. The probe reuses legacy field validation through temporary placeholders only for mechanical checking; those placeholders never enter admitted output. No tool requests or actions, no new dependencies.

Four cases: burst with unavailable network sensor and unassessed correlation, burst with stipulated no-match within synthetic scoped coverage but unverified clock/correlation correctness, normal fixture (accepted then failed; no threshold finding, not proof of benign activity), empty input. Synthetic metadata is stipulated test input, not a sensor acquisition result. All versions receive the same underlying information, and baseline reviewers receive the same quality metadata. No independent action/target truth provided to the model; its recommendation text appears in the baseline finding context and may anchor replies. Expected properties: no invented negative evidence, preserve discrepancies and uncertainty, avoid treating no finding as benign certainty, empty case should not invent hypotheses/IDs. Evaluate mechanical admission separately from semantic quality and added usefulness; latency/token counts descriptive only.

Full requests, outputs, metadata and validator decisions are retained in [comparison JSONL](evidence/2026-11-25-stage-c2-comparison.jsonl). Human adjudication is pending; AI review is preliminary.

## Actual results and preliminary AI-assisted review

All 12 requests completed (HTTP 200, finish reason stop); 9 admitted mechanically, none adjudicated automatically. In each version the four rows are missing, discrepancy, normal and empty. Counts are exploratory, not estimates of general reliability.

| Version | Missing | Discrepancy | Normal | Empty | Mechanical pass |
|---|---|---|---|---|---|
| 0.1 | reject (contradictory abstention) | reject (contradictory abstention) | admit | admit | 2/4 |
| 0.2 | admit | admit | admit | reject (N/A invented reference, no events) | 3/4 |
| 0.3 | admit | admit | admit | admit | 4/4 |

| Case | Version | Prompt / completion / reasoning tokens | Seconds |
|---|---|---|---|
| Missing | 0.1 | 932 / 977 / 706 | 22.47 |
| Missing | 0.2 | 952 / 987 / 534 | 8.42 |
| Missing | 0.3 | 958 / 1077 / 569 | 9.04 |
| Discrepancy | 0.1 | 947 / 872 / 601 | 7.37 |
| Discrepancy | 0.2 | 967 / 1171 / 582 | 10.01 |
| Discrepancy | 0.3 | 975 / 1125 / 520 | 9.65 |
| Normal | 0.1 | 490 / 658 / 568 | 5.57 |
| Normal | 0.2 | 510 / 900 / 492 | 7.80 |
| Normal | 0.3 | 516 / 875 / 470 | 7.50 |
| Empty | 0.1 | 318 / 434 / 376 | 3.65 |
| Empty | 0.2 | 338 / 530 / 412 | 4.67 |
| Empty | 0.3 | 344 / 463 / 417 | 3.89 |

Preliminary review (AI reviewer; learner/independent human review remains pending):

- Missing: V0.1 repeats the original disposition failure. V0.2 and V0.3 propose existing baseline recommendation to inspect target authentication successes and independent truth; they omit the supplied unavailable/not_assessed network condition. V0.3's required evidence interval ends 10:01:20 although the sole cited acceptance is at 10:01:30; its unavailable branch conflates lack of corroborating success with unavailable evidence. V0.2/V0.3 repeat a prompt sentence as uncertainty.
- Discrepancy: none of the three adequately addresses the stipulated network no-match; V0.2/V0.3 repeat the baseline objective with some additional log/authorization detail but do not propose a discriminating check for the discrepancy. V0.2 calls a session established from a PID and cites only acceptance for a broader narrative; V0.3 describes a successful connection as a possible explanation without accounting for the discrepancy. No compromise is established.
- Normal: V0.1 abstains without declaring benign certainty. V0.2/V0.3 suggest additional observations (session context/hostname), but describe actual activity rather than supplied records; their usefulness depends on operator task. V0.2 literal string "null" in if_unavailable passes nonempty-string mechanical validation but fails to describe a meaningful fallback. No matching rule is not proof of benign activity.
- Empty: V0.1/V0.3 correctly abstain; V0.2 produces a hypothesis object restating absence with a nonexistent N/A reference; rejected. Deterministic input eligibility could avoid inference entirely when no accepted observations exist, provided incomplete/unassessable baseline remains explicit.

No version establishes sufficient investigative usefulness in this set. V0.3 is promising mechanically, but structured context alone did not solve evidence-quality use. No general model ranking or causal proof; V0.1/V0.2 prompt and schema both change; model loading/cache not controlled. No fresh telemetry or new security action. The old validator reuse through temporary placeholders is experimental, not the intended C3/C5 implementation.

## Decisions to review before C3

Keep C2 open. Discuss one actual output with learner; choose whether to remove redundant baseline recommendation from model context (not from operator baseline), supply an explicit investigative question focused on known evidence gaps, and let deterministic eligibility and scope handling own facts rather than repeat generated values. Do not force more schema fields just to correct reasoning. Test changes on the same fixed cases and reserve a changed case for transfer; avoid indefinite tuning on four cases. C2 candidate is not finalized; Sigma exercise remains next alongside C after C2. Stage B learner practical closure remains pending.

## Verification and handoff

All 12 response decisions replayed offline; HTTP status and finish reasons checked; Python compilation and all 15 existing Stage B tests passed. Relative file link targets checked across affected Markdown files, no missing targets. No code changed under src/ or tests/. Record C2 as open for learner review; no live telemetry, installations or persistent model settings changed.
