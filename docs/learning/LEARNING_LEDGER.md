# AegisLab — Learning ledger

**Updated:** 2026-11-27. **Status:** living, non-normative learning coverage and recall tracker; not a second roadmap. Governed by [Learning Preferences](../../LEARNING-PREFERENCES.md), [Learning and Technology Strategy](../definition/learning-and-technology-strategy.md), [current learning handoff](CURRENT_LEARNING_STATE.md) and [Stage C execution](../plans/STAGE-C-EXECUTION.md).
**Evidence:** July guided records are historical only; active learning evidence begins at the November 22 return, including [November learning/experiment reconciliation](../worklogs/2026-11-24-1953-learning-reconciliation-and-stage-c2.md). Conversation-derived assessments are explicitly distinguished from retained runtime output and AI-executed work.

## How to use

Depth labels follow the normative strategy: not encountered, introduced, explained with guidance, practiced with guidance, applied independently, diagnosed independently, transferred, technical depth. Record the strongest *specific* demonstrated behavior, help level and remaining gap; a correct prediction is not independent execution. Recall state is separate (recent, needs revisit, or not assessed); recent does not mean stable recall. When access is unavailable, AI may run tests while learner predicts/interprets; practical independence remains open. Review at meaningful milestones, not every message.

**Owner reset (2026-11-26):** all pre-2026-11-22 learning and practice unavailable as prerequisites until re-established. Keep historical facts, not historical depth credit. Current rows reflect only post-return demonstrations; reset-only topics are marked unavailable, not never encountered. Follow the [foundations rebuild](FOUNDATION-REBUILD.md).

## Current demonstrated learning

| Topic | Current depth / evidence | Target for Core / next revisit |
|---|---|---|
| TCP/IP, sockets, ports, loopback | Practiced with guidance: learner ran ss -ltn, ss -tn; correctly distinguished ESTAB and authentication | D/F: personally trace a connection and diagnose missing listener; refresh routing/DNS |
| Linux processes, PID, FD, services | Practiced with guidance: learner ran ss -ltnp and ps; correctly identified absent socket owner evidence | D/F: directly establish ownership, diagnose service failure |
| SSH authentication, host/user keys, logging | Post-return: introductory SSH/authentication distinction and journalctl/synthetic message inspection; learner explicitly reports insufficient SSH knowledge; deeper prerequisites unavailable | R2/D: learn cryptography, SSH phases and trust from first principles, reconstruct safe isolated case and diagnose |
| Namespaces, veth, IPv4 routes, ICMP, packet capture | Unavailable after reset; no post-return practical reconstruction | R2/D: rebuild network/isolation mechanics from first principles, inspect capture limits and personally configure |
| Linux file ownership/permissions | R2.1 AI-operated mode 0600/0000 controlled denial demonstrated; learner explanation and personal operation not yet assessed | R2/D/E: explain owner/group/other and diagnose permission failure without weakening controls |
| Docker/VM | Unavailable after reset; historical inventory only, no current practical competence | D/F: justified container operation and isolation, not mandatory prior to AI |
| JSONL and parsing/validation | Explained with guidance; learner recognized invalid port and correct finding, initially conflated decode and event acceptance | B/C3: independently change invalid record and trace quarantine; distinguish syntax, shape, values, truth |
| Event/record/source IDs, SHA-256, lineage | Introduced and examined in actual reports (AI ran CLI) | B/D: trace finding to source bytes; explain why a hash is not authentication |
| Sliding windows | Applied reasoning with corrections; latest delayed recall correctly calculated [130,250], C/D and fixed bucket 1/2/1; full-stream earlier trigger refined | B/D: personally modify/run case and distinguish specified endpoint from first qualifying finding; spaced transfer |
| Composite keys and detection coverage | Applied reasoning: three groups, no threshold; identified coverage limitation of grouping | G: evaluate complementary rule against benign/ambiguous cases and independent truth |
| Deduplication and set membership | Guided reasoning: A/B/D count, four accepted vs three corrected; no separate-action proof explained | B/F: reproduce duplicates, explain identity and idempotency limitations |
| Assessment states and missing evidence | Explained with guidance; correctly predicted valid finding plus invalid input not fully valid | B/D: diagnose empty/partial/quarantined cases and source loss |
| Software tests, Python modules, CLI | Introduced/refreshed; AI ran 15 tests and experiments, learner not yet personally modified or debugged new code | B/C4–C5: run tests, change fixture/code intentionally, diagnose and restore |
| HTTP client/server and API verification | Applied reasoning: catalog 200 establishes reachability/listing, not inference or reliability; AI ran GET/POST | C4/F: personally inspect request/response and diagnose timeout or API failure |
| Model inference, context vs generation budget | Explained with guidance; learner proposed increasing max_tokens and raised efficiency; AI ran comparison | C4/C7: predict and diagnose truncation; distinguish context capacity, actual tokens, latency confounds |
| Context engineering | Guided design: learner favored bounded relevant context and deterministic core; related non-trigger event importance taught | C2/C3: choose scope and explain omission trade-off in new case |
| Structured output and schema | Explained with guidance; actual JSON fence failure and schema request demonstrated by AI | C3/C5: independently validate type/shape and unknown values, test invalid reference |
| Semantic grounding and uncertainty | Post-return reasoning: rejected unsupported attacker/compromise claim and asked for precise references; no assumed prior-project competence | C5/C6: adjudicate valid-looking unsupported claim; separate factual statement from hypothesis |
| AI evaluation and usefulness | First guided human review: semantic partial, additional value fail, hypotheses partial, investigation fail; identified vague next check | C6/C7: apply fixed rubric to new case, compare same-evidence baseline and record disagreement |
| Agent authorization / tool security | Introduced conceptually; no agent or tool implementation | E: independently explain and test allow/deny, injection, least authority |
| Observability, deployment, distributed systems | Concepts introduced (duplicates, partial failure); operational competence not demonstrated | F/later: logs, recovery, queues, ordering, retries, backpressure, replay |
| Applied security ML | Prior external ML experience does not establish AegisLab security ML competence | Later dedicated expansion: data leakage, splits, metrics, drift, justified baseline |
| DFIR and threat hunting | Evidence preservation and hypotheses introduced; forensic/hunt practice not established | D/G/later: acquisition, timeline, scoping, competing hypotheses and negative evidence |

## Additional November 25 learning evidence

Missing/invalid/conflicting evidence: learner correctly distinguished incomplete from corrupted or wrong evidence and identified unassessed network correlation as a problem; guided correction to distinguish unavailability from a verified negative observation. Target D/G: independently assess coverage, provenance and cross-source discrepancy. Ownership/trust boundary: learner reasoned about critical deterministic decisions and acquisition facts; guided refinement for human adjudication and unverified source observations. Target E: demonstrate external policy. C2 comparison: AI executed 12 trials; learner review pending. See [comparison worklog](../worklogs/2026-11-25-1511-c2-contract-context-comparison.md). No practical independence or stable recall claimed.

Prompt/context engineering: learner proposed clearer investigation direction and evidence references and asked about actual prompt/configuration; AI demonstrated controlled prompt-only and recommendation-removal comparison, including semantic failures despite valid shape. See [prompt ablation](../worklogs/2026-11-25-1724-c2-prompt-ablation.md). Guided design reasoning only; learner-owned output adjudication and independent execution pending.

Context preparation and eligibility: AI implemented deterministic scope, omission metadata, versioned interface, refusal on bounds, baseline isolation and CLI preview; 12 tests and real CLI verified. Learner correctly predicted trigger records, explicit budget refusal and traceability; scope and omitted relevance required guidance. Personal execution pending; see [context increment](../worklogs/2026-11-25-1824-provisional-context-builder.md) and [later assessment](../worklogs/2026-11-25-2013-local-inference-and-validation.md).

Local inference and output validation: AI implemented reusable direct loopback HTTP client, optional jsonschema 4.10.3 validator and explicit orchestration/fallback; 22 new tests and actual local CLI verified. Learner correctly explained source/target and baseline fallback and answered seven recognition questions; personal request/failure diagnosis pending; see [implementation worklog](../worklogs/2026-11-25-2013-local-inference-and-validation.md). No independent mastery claimed.

November 26: Sigma detection intent, logsource/field mapping, correlation versus backend execution and fixed versus sliding window introduced by AI-operated offline comparison. Inference process supervision, caller deadline versus socket timeout and server cancellation boundaries demonstrated in controlled test. Changed-case explanation and independent execution pending. Learner requested more open-ended assessments; do not equate recognition with transfer. [Worklog](../worklogs/2026-11-26-1539-sigma-and-inference-deadline.md).

November 26 later assessment: correct composite key and sliding-window trigger; fixed-bucket misunderstanding persists and was corrected, so re-assess changed bucket alignment in R1. Initial platform delegation and explicit entity representation ideas needed refinement; correct preservation of conflicting evidence and general deadline reasoning. SSH depth explicitly insufficient. Pre-return learning reset applies globally; see [foundations rebuild](FOUNDATION-REBUILD.md).

New rebuild topics: cryptography/trust (hash vs encryption/signature/key exchange), SSH transport/authentication/channel lifecycle, Linux permissions, networking layers/isolation, search/indexing and security platform operations. Current credit only where post-return evidence above supports it; all other prerequisites unavailable. Target R2/D foundations, F/G search and platform competence.

R1 native Sigma: AI executed CLI/API conversion and native SQL, diagnosed missing UUID metadata, mapped timestamps/event IDs, compared ten cases. Learner later correctly reasoned about grouping, mapping and case policy; specification/conversion/execution and fixed/sliding windows required correction; tool operation deferred because PC unavailable; do not assume competence from AI execution. See [native worklog](../worklogs/2026-11-26-2023-native-sigma-practice.md).

R2.1 Linux foundations: AI demonstrated program/process lifecycle, PID/PPID, sleeping state, per-process FDs, stdin/stdout/stderr pipes, listening/connected sockets, temporary permission denial and scoped no-entry journal query; learner assessment subsequently recorded below. Earlier November guided socket/process inspection retained at actual depth, no July credit. [Worklog](../worklogs/2026-11-27-1627-linux-process-foundations.md).

## Industry-tool competence

The [industry competency matrix](../plans/INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md) tracks practical tool operation, configuration, integration and diagnosis separately from conceptual learning. Review applicable rows at each milestone; AI-only execution does not establish personal competence.

R2.1 learner assessment: correct program/process and kernel-level responsibility, per-process FD identity, mode 640 and ordinary access denial; PID/PPID correct, sleeping vs runnable needed clarification; bind/listen/accept broadly understood, listener vs connected socket refined. TCP ESTAB not authentication correctly identified but unavailable application response was conflated with nonexecution; revisit evidence absence in networking/SSH. Delayed recall correctly selected interval [30,150] and observations 90,130,150; included unnecessary [0,120] and conflated no finding with no observations. Fixed-bucket distinction still a revisit priority. No personal operation promoted. Learner explicitly values recurring recall/re-explanation and mixed older/new assessments; adapt repetition to weak topics and transfer.

R2.2 F2: AI demonstrated IP prefix membership, route lookup and next hop, loopback TCP refusal and success, UDP datagrams, and capture permission limitation. Actual packet capture and independent learner diagnosis remain open. Mixed assessment includes old PID/FD, evidence absence and Sigma responsibility/window recall. [Worklog](../worklogs/2026-11-27-1751-network-foundations.md).

R2.2 assessment: correct subnet and next-hop reasoning, listener diagnosis, UDP/TCP distinction, unavailable authentication evidence, FD ownership, Sigma conversion boundary, and delayed sliding/fixed-window membership. Endpoint identity needs refinement; distinguish earlier qualifying windows from specified endpoint. Continue spaced recall through cryptography and SSH; personal operation and capture remain open. Windows host access restored; readiness evidence is infrastructure observation, not learner competence.

## Active recall and ownership queue

- B practical closure when PC access permits: learner selects a copy of a fixture, predicts a changed case, modifies/runs it, traces output to source lines, deliberately diagnoses one invalid input or wrong rule assumption, and explains evidence limits. AI may review, not perform the learner's critical step.
- C2 next: represent unknown target identity without hallucination, derive scope from existing references and evaluate a proposal against evidence. Revisit distinction among valid JSON, valid types, reference existence, entailment, usefulness and permission.
- C4/C5: personally run one local request and reproduce a bounded failure/fallback when possible.
- R1/R2: learner native Sigma practice (AI-operated native exercise verified) and first-principles foundations rebuild; D: newly demonstrate namespace/routing/SSH mechanics before relying on them. No July competence credit.
- At next meaningful handoff, review two older concepts through delayed recall or transfer (e.g. socket ownership in inference and duplicate delivery in collection), not rote repetition.

Do not mark stable recall or independent practical mastery until supported by a later learner-owned demonstration. Keep the state summary short; update this ledger and link dated worklogs rather than recreating a competing curriculum.
