# AegisLab Project State

**Updated:** 2026-11-22 | **Authority:** non-normative handoff; current Git/runtime and active normative documents control.
**Active authority:** [Project Definition](<docs/AegisLab — Project Definition v1.0.md>), [Core Charter v2](<docs/plans/AegisLab — Core Charter v2.0.md>), [Capability Execution Map v2](<docs/plans/AegisLab — Capability Execution Map v2.md>).
**Prior route:** [Charter v1](<docs/plans/AegisLab — Core Charter v1.0.md>), [M0–M17 Map](<docs/plans/AegisLab — Core Execution Map.md>) and [M5 Docker planning](<docs/plans/AegisLab — M5 Docker Learning and Execution Plan.md>) are preserved history, **not active next steps**.

## Decision

Owner authorized the [2026-11-22 AI-first evolution](docs/proposals/2026-11-22-ai-first-aegislab-evolution-plan.md): retain AegisLab's evidence-centered network-defense mission; build a working SSH incident workflow before mandatory Docker/VM parity; introduce useful, evaluated local AI and later safe agent authorization; preserve human control and independent truth.

## Historical evidence and actual runtime

- July: namespace networking, authorized-key SSH success, unauthorized-key rejection, process/socket/log/packet observation and teardown **demonstrated with guidance**, not independently mastered. See [SSH closure worklog](docs/worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md) and [reconstruction runbook](docs/runbooks/namespace-ssh-lab-reconstruction.md).
- Formal old M4 repeated-failure scenario contract: **deferred**, not passed.
- Old M5: planning and Docker object inventory only. No Docker SSH adapter, Compose implementation, VM parity or pipeline proof.
- Initial 2026-11-22 local WSL worktree was clean at `b5f0234`; remote `main` had one proposal commit `939225a`. Local was safely fast-forwarded to that commit.
- At inspection, `/tmp/aegislab-namespace-ssh` was **absent**. July worklog preserves summarized observations, **not importable raw sshd log lines**. There is no attested retained source suitable for claiming a live raw-log detection. Begin Stage B with labeled public-safe **synthetic** fixtures; fresh authorized sensor evidence belongs to Stage D.
- No privileged SSH or Docker operations were authorized or performed in this evolution work.
- **Stage C transport readiness (read-only):** local model catalog responded at `http://127.0.0.1:18080/v1/models` from Windows and WSL. WSL's existing `http_proxy=http://127.0.0.1:8080` intercepted the default request and produced an empty reply; a direct WSL `curl --noproxy 127.0.0.1` request succeeded. This confirms only model-list endpoint connectivity, **not** a loaded model, successful inference or AI evaluation. Future local client must bypass ambient HTTP proxy explicitly without broadening listener/network exposure.

## Current capability and next execution

1. **A — adopted:** v2 Charter and stage map govern the new route; old plans marked historical. Verify consistent links and worktree.
2. **B — executable software verified, learner gate open:** lightweight stdlib Python CLI, bounded imported authentication envelopes, explicit source/record/event identities, raw line SHA-256, quarantine, one repeated-failure rule and positive/negative/boundary/missing tests. The final 15-test suite and synthetic positive/normal CLI demos ran successfully in WSL. Evidence is **synthetic**, not real retained sensor data; personally demonstrated changed-case diagnosis is still pending.
3. **C — next after verified B:** optional local-model investigation against the identical evidence and a no-AI baseline; validate structured and semantic claims, reject unsupported IDs and measure fallback. Do not assume the local endpoint currently runs.
4. **D–G:** fresh safe operation, read-only agent-policy tests, recovery, second scenario and credible comparative usefulness evidence.

## Learning and safety handoff

Software completion and personal mastery are separate. Learner still needs to predict and change a case, inspect the resulting event/evidence chain, and diagnose one failure with reduced prompting. AI may author the code, but this does not prove transfer. No unapproved sudo, ordinary SSH configuration change, exposure of lab ports, unrelated Docker modification, or external targeting.

**Next action:** verify and run the Stage B CLI/tests; then perform a learner-owned changed-case prediction and result interpretation. Consult the [current learning state](docs/learning/CURRENT_LEARNING_STATE.md) and active [stage map](<docs/plans/AegisLab — Capability Execution Map v2.md>).
