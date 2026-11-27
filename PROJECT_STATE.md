# AegisLab Project State

**Updated:** 2026-11-27 | **Authority:** non-normative handoff; current Git/runtime and active normative documents control.
**Active authority:** [Project Definition](<docs/AegisLab — Project Definition v1.0.md>), [Core Charter v2](<docs/plans/AegisLab — Core Charter v2.0.md>), [Capability Execution Map v2](<docs/plans/AegisLab — Capability Execution Map v2.md>).
**Prior route:** [Charter v1](<docs/plans/AegisLab — Core Charter v1.0.md>), [M0–M17 Map](<docs/plans/AegisLab — Core Execution Map.md>) and [M5 Docker planning](<docs/plans/AegisLab — M5 Docker Learning and Execution Plan.md>) are preserved history, **not active next steps**.

## Decision

Owner authorized the [2026-11-22 AI-first evolution](docs/proposals/2026-11-22-ai-first-aegislab-evolution-plan.md): retain AegisLab's evidence-centered network-defense mission; build a working SSH incident workflow before mandatory Docker/VM parity; introduce useful, evaluated local AI and later safe agent authorization; preserve human control and independent truth.

## Owner-approved learning reset and roadmap refinement (2026-11-26)

Treat every skill or concept learned/practiced before the November 22 return as unavailable for prerequisites until personally re-established. Preserve historical engineering evidence and software; retain post-return learner demonstrations at their actual depth only. The [foundations rebuild](docs/learning/FOUNDATION-REBUILD.md) schedules connected security/systems, AI/software and industry-tool tracks: native Sigma first, then first-principles SSH/Linux/networking/cryptography, focused C2–C5, C6–C8 evaluation, and D operational lab. Elasticsearch/Kibana in F, Elastic Security/OpenSearch and bounded Splunk/SPL exposure in G, deeper Elasticsearch post-Core. No prior guided lab completion counts as current competence; no change to A–G capability acceptance or authorization boundaries.

## Historical evidence and actual runtime

- July: namespace networking, authorized-key SSH success, unauthorized-key rejection, process/socket/log/packet observation and teardown **demonstrated with guidance historically**, not current learner competence (reset). See [SSH closure worklog](docs/worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md) and [reconstruction runbook](docs/runbooks/namespace-ssh-lab-reconstruction.md).
- Formal old M4 repeated-failure scenario contract: **deferred**, not passed.
- Old M5: planning and Docker object inventory only. No Docker SSH adapter, Compose implementation, VM parity or pipeline proof.
- Initial 2026-11-22 local WSL worktree was clean at `b5f0234`; remote `main` had one proposal commit `939225a`. Local was safely fast-forwarded to that commit.
- At inspection, `/tmp/aegislab-namespace-ssh` was **absent**. July worklog preserves summarized observations, **not importable raw sshd log lines**. There is no attested retained source suitable for claiming a live raw-log detection. Begin Stage B with labeled public-safe **synthetic** fixtures; fresh authorized sensor evidence belongs to Stage D.
- No privileged SSH or Docker operations were authorized or performed in this evolution work.
- **Stage C transport readiness (read-only):** local model catalog responded at `http://127.0.0.1:18080/v1/models` from Windows and WSL. WSL's existing `http_proxy=http://127.0.0.1:8080` intercepted the default request and produced an empty reply; a direct WSL `curl --noproxy 127.0.0.1` request succeeded. This confirms only model-list endpoint connectivity, **not** a loaded model, successful inference or AI evaluation. Future local client must bypass ambient HTTP proxy explicitly without broadening listener/network exposure.

## Recent verified experiments (November 23–24; reconstructed session record)

See the [learning and experiment reconciliation worklog](docs/worklogs/2026-11-24-1953-learning-reconciliation-and-stage-c2.md). WSL reruns of the CLI and 15 tests passed. Additional synthetic variations verified inclusive 120/121-second boundaries, sliding windows, separate source/account grouping, duplicate retention versus counting, invalid port quarantine and incomplete/empty inputs. The learner correctly predicted several changed cases after guidance; the AI executed the later tests remotely. No fresh SSH sensor collection.

Local Gemma E2B inference succeeded in bounded experiments at the loopback API. A 256-token completion truncated; 512 permitted a complete answer. A first investigation returned Markdown-fenced JSON and failed strict parsing. A later schema-constrained trial passed mechanical checks but human adjudication found weak hypotheses and an insufficiently scoped next check. These are exploratory results, not integrated Stage C functionality or proof of usefulness. C1's experimental foundation is established; availability must be rechecked when used. Exact model/prompt/budgets and known limitations are recorded to the extent retained.

## Current capability and next execution

1. **A — adopted:** v2 Charter and stage map govern the new route; old plans marked historical. Verify consistent links and worktree.
2. **B — executable software verified, learner gate open:** lightweight stdlib Python CLI, bounded imported authentication envelopes, explicit source/record/event identities, raw line SHA-256, quarantine, one repeated-failure rule and positive/negative/boundary/missing tests. The final 15-test suite and synthetic positive/normal CLI demos ran successfully in WSL. Evidence is **synthetic**, not real retained sensor data; learner demonstrated changed-case reasoning with corrections, but personal modification/run/diagnosis and delayed recall remain pending.
3. **C — active, C1 exploratory foundation demonstrated; C2 candidate design under evaluation:** use the [Stage C execution plan](docs/plans/STAGE-C-EXECUTION.md) (C1–C8). An opt-in experimental local AI CLI probe now exists; no accepted product-level AI workflow yet. C2 defines advisory hypotheses and proposed evidence needs with explicit abstention and deterministic scope. The [two-case design probe](docs/worklogs/evidence/2026-11-24-stage-c2-probe.json) admitted 1/2 mechanically (empty case correct; positive case contradictory abstention rejected); useful investigation not established; C3–C8 implement, verify and evaluate these boundaries. Do not assume current endpoint/model readiness or semantic acceptance.
4. **D–G:** fresh safe operation, read-only agent-policy tests, recovery, second scenario and credible comparative usefulness evidence.

## C2 paired comparison (2026-11-25)

The [comparison worklog](docs/worklogs/2026-11-25-1511-c2-contract-context-comparison.md) and [12-trial artifact](docs/worklogs/evidence/2026-11-25-stage-c2-comparison.jsonl) compare the original disposition contract, simplified contract and structured quality context on the same four synthetic cases. All requests completed; mechanical admission 2/4, 3/4 and 4/4 respectively. None of the six missing/discrepancy outputs adequately handled the network quality condition; usefulness not established. Structured output and quality fields alone are insufficient. No live sensor evidence, new integrated client or finalized contract.

## C2 prompt/context ablation (2026-11-25, later session)

The [prompt ablation worklog](docs/worklogs/2026-11-25-1724-c2-prompt-ablation.md) records nine synthetic trials: fresh control, improved prompt, and improved prompt without the existing recommendation in model context; normal/empty and partial coverage checks. All nine mechanically admitted but none of seven burst responses adequately handled its network quality condition; one partially acknowledged missing correlation. Explicit contradiction and unsupported interpretations observed; correct empty abstention. No useful integrated investigator established. Preserve the full baseline and keep C2 open for learner review and a bounded task-specific refinement/decision, rather than indefinite generic prompt tuning.

## Provisional C3 implementation (2026-11-25)

[Context builder increment](docs/worklogs/2026-11-25-1824-provisional-context-builder.md): reusable deterministic context selection, eligibility, omissions/limitations, explicit bounds, baseline preservation and CLI --prepare-context now implemented. All 27 tests pass (12 new); burst, empty, unknown-finding and flag behavior verified. At that increment no inference was integrated. C2 decision remains open; C3 is partially implemented, not accepted. Learner requested batched teaching/quiz and more building progress.

## Provisional C4/C5 integration (2026-11-25)

[Local inference and validation increment](docs/worklogs/2026-11-25-2013-local-inference-and-validation.md): direct loopback HTTP client, optional jsonschema validator, dynamic context reference checks, deterministic eligibility and unchanged baseline integrated under --probe-investigator. 49/49 tests pass (22 new); actual local inference completed and admitted as unadjudicated; model confused source IP with target, so semantic usefulness not established. Empty input did not invoke model. C2/C3/C4/C5 remain open; At that increment whole-request deadline, final contract, token budgeting and evaluation remained pending; caller supervision was added subsequently.

## Sigma semantics and inference supervision (2026-11-26)

[Increment and evidence](docs/worklogs/2026-11-26-1539-sigma-and-inference-deadline.md): candidate Sigma YAML and seven-case offline handwritten SQL semantics comparison (not native conversion); three fixed-bucket/raw-count mismatches, seven sliding/distinct subject matches. pySigma unavailable; native exercise remains open. Integrated inference supervisor with caller deadline, controlled slow loopback and fallback tests; 55/55 tests passed, real local probe admitted unadjudicated, baseline unchanged, prior source/target error remains. Caller worker termination does not guarantee server cancellation; token budgeting and C2–C5 acceptance remain open.

## R1 native Sigma exercise (2026-11-26)

[Native worklog](docs/worklogs/2026-11-26-2023-native-sigma-practice.md): isolated temporary venv, strict native rule validation 0 issues after UUID additions, CLI/API query equality, 10 synthetic SQLite cases. Raw subject agreement 8/10, reference-style dedup 9/10; case normalization and multiple alert windows differ. 55/55 regression tests passed. No permanent application dependency; R1 learner practical gate remains open; R2 foundational sequence next.

## R2.1 Linux process foundations (2026-11-27)

[Worklog](docs/worklogs/2026-11-27-1627-linux-process-foundations.md): AI executed a disposable nonprivileged loopback client/server and permissions experiment; process/FD ownership, two established endpoints, application exchange, permission denial, cleanup and scoped journal query observed; 55/55 existing tests passed. No product source changes. F1 learner assessment and personal operation open; R1 personal Sigma operation deferred due to reported PC access limit. R2 continues to networking, then cryptography and SSH.

## Industry tooling and product direction

The [industry tooling and product strategy](docs/plans/INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md) records stage-linked practical exercises, build/integrate/exercise decisions and ecosystem/usefulness comparisons. Near-term: complete learner native Sigma practice after AI-operated comparison; validator and evaluation-runner review in C3/C5/C6; Wazuh comparison before or during D/F. Product positioning remains a hypothesis; no new tool installed or integration implemented. C2 remains open while reversible C3 context work progresses.

## Learning and safety handoff

Software completion and personal mastery are separate. Learner has predicted changed cases and evaluated model output; still needs to personally change/run a case, trace the event/evidence chain and diagnose one failure with reduced prompting. See [learning ledger](docs/learning/LEARNING_LEDGER.md). AI may author the code, but this does not prove transfer. No unapproved sudo, ordinary SSH configuration change, exposure of lab ports, unrelated Docker modification, or external targeting.

**Next action:** R2.1 combined learner assessment, then R2.2 networking foundations; R1 native personal practice and delayed responsibility/window recall remain open; R3 focused C2–C5 and R4 C6–C8 evaluation. Follow the [foundations rebuild](docs/learning/FOUNDATION-REBUILD.md); if native tooling is blocked, record reason and revisit, then proceed R2. Close Stage B personal practical ownership when PC access permits; do not rely on pre-return competence. Consult the [current learning state](docs/learning/CURRENT_LEARNING_STATE.md), [learning ledger](docs/learning/LEARNING_LEDGER.md), and [Stage C plan](docs/plans/STAGE-C-EXECUTION.md).
