# 2026-11-25 — Provisional context builder and accelerated sessions

- Recorded: 2026-11-25 18:24 +03:30 (WSL clock).
- Status: completed (bounded implementation increment; C2/C3 gates remain open).
- Starting revision: 789c37e4ddd17b7fbb85b34d519b8f3442d402fa, clean local main and matching remote.
- Continues: [prompt ablation](2026-11-25-1724-c2-prompt-ablation.md).

## Owner direction and decisions

Learner requested faster progress, multiple concepts and quizzes per session and tangible building progress. Batch connected explanations and changed-case/review questions at meaningful milestones, with a concrete implementation and actual verification where appropriate. Keep dependency-driven teaching, safety and learner ownership gates; no automatic mastery, no skipping unresolved requirements. This is an execution rhythm adjustment consistent with Learning Preferences, not a change in the Core destination.

Generic investigator usefulness remains unestablished. AI chose to implement a reversible deterministic C3 slice in parallel with open C2 design/learner review, since the context boundary is needed independently of model choice. This does not close C2 or freeze the model output contract. No new LLM requests in this session.

## Implementation and responsibility

- [Context module](../../src/aegislab/investigator_context.py): versioned provisional schema, in-process Stage B report only; explicit eligibility/refusal; bounded single-finding context or small source review; supporting IDs always retained; related records use same source report, account and IP, inclusive finding interval extended 120s before/after; selection and omission counts; no inferred completeness. Explicit finding selection required for multiple findings. Empty/only quarantined observations cannot support this task.
- Whitelist normalized event/source/finding fields; exclude baseline recommendation and evaluator-only top-level/nested subject data. Preserve deterministic limitations and quality metadata (quarantine and duplicates, network correlation not_supplied, source authenticity/clock not established, hostname null). JSON roundtrip detaches nested context from the baseline. This is not a general untrusted imported-report validator or a proof of absence of all information leakage.
- Chosen experimental limits: 32 selected events and 16,384 canonical UTF-8 JSON bytes, not an input-token budget or final HTTP envelope bound. Refuse rather than silently truncate when over budget; no automatic ranking/pagination. The 120s padding is a provisional investigation relevance policy, not the detection rule or an established coverage interval. May omit relevant multi-account, cross-source or distant activity; later evaluation required.
- CLI: analyze --prepare-context returns the unchanged baseline plus preparation envelope; --finding-id requires preview and selects an existing finding. No inference or authorization. Existing --json and default human summary remain available.
- [Tests](../../tests/test_investigator_context.py): 12 added; test selection, related acceptance, omissions, missing/invalid evidence, ambiguity, event/byte budget, baseline equality/isolation, whitelist, consistent references/schema, deterministic output. AI implementation and tests; learner has not independently run or explained them.

## Observed verification

Command: PYTHONPATH=src python3 -m unittest discover -s tests -v (27/27 passed; rerun -q after nested subject whitelist, 27/27 passed). CLI burst demo: finding_present, 4 accepted, 4 included, 3 supporting IDs, 0 omitted; accepted event at 10:01:30 retained beyond 10:01:20 finding window. Context 2918 canonical bytes, eligible true, reason context_prepared. Baseline recommendation retained outside model context; full --json baseline equality verified. Empty /dev/null: unassessable, eligible false, no_accepted_observations, context null. Unknown finding: explicit unknown_or_ambiguous_finding and unchanged baseline; conflicting flags and --finding-id without --prepare-context both exit 2. No source code changed in detector. No installations, live sensors, model requests or permissions.

## Handoff

Next: batched learner checkpoints on SSH observation/intent, context eligibility/selection, provenance, validation and budget; then bounded task-specific C2 comparison/decision, Sigma exercise and continue C3/C4. C3 typed schema/library exercise, generic evidence-quality references, adversarial/untrusted input boundary, real token and request budget, integrated inference and fallback remain pending. Prioritization is a provisional AI engineering choice, not new owner-approved final gate or design. Maintain exact separate software and learner statuses.

Relative Markdown links checked: 79; none missing.
