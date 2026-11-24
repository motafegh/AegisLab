# AegisLab — Learning ledger

**Updated:** 2026-11-24. **Status:** living, non-normative learning coverage and recall tracker; not a second roadmap. Governed by [Learning Preferences](../../LEARNING-PREFERENCES.md), [Learning and Technology Strategy](../definition/learning-and-technology-strategy.md), [current learning handoff](CURRENT_LEARNING_STATE.md) and [Stage C execution](../plans/STAGE-C-EXECUTION.md).
**Evidence:** July guided records and [November learning/experiment reconciliation](../worklogs/2026-11-24-1953-learning-reconciliation-and-stage-c2.md). Conversation-derived assessments are explicitly distinguished from retained runtime output and AI-executed work.

## How to use

Depth labels follow the normative strategy: not encountered, introduced, explained with guidance, practiced with guidance, applied independently, diagnosed independently, transferred, technical depth. Record the strongest *specific* demonstrated behavior, help level and remaining gap; a correct prediction is not independent execution. Recall state is separate (recent, needs revisit, or not assessed); recent does not mean stable recall. When access is unavailable, AI may run tests while learner predicts/interprets; practical independence remains open. Review at meaningful milestones, not every message.

## Current demonstrated learning

| Topic | Current depth / evidence | Target for Core / next revisit |
|---|---|---|
| TCP/IP, sockets, ports, loopback | Practiced with guidance: learner ran ss -ltn, ss -tn; correctly distinguished ESTAB and authentication | D/F: personally trace a connection and diagnose missing listener; refresh routing/DNS |
| Linux processes, PID, FD, services | Practiced with guidance: learner ran ss -ltnp and ps; correctly identified absent socket owner evidence | D/F: directly establish ownership, diagnose service failure |
| SSH authentication, host/user keys, logging | July guided practice; November refreshed with journalctl and synthetic message; learner initially reported weak recall | D: reconstruct safe isolated case, distinguish TCP, key authentication and session; recall check |
| Namespaces, veth, IPv4 routes, ICMP, packet capture | July practiced with guidance; independent reconstruction not established | D: revisit only needed network/isolation mechanics and capture limits |
| Linux file ownership/permissions | July guided key setup; recall not assessed | D/E: diagnose permissions without weakening controls |
| Docker/VM | Docker object inventory/planning only; VM parity not built | D/F: justified container operation and isolation, not mandatory prior to AI |
| JSONL and parsing/validation | Explained with guidance; learner recognized invalid port and correct finding, initially conflated decode and event acceptance | B/C3: independently change invalid record and trace quarantine; distinguish syntax, shape, values, truth |
| Event/record/source IDs, SHA-256, lineage | Introduced and examined in actual reports (AI ran CLI) | B/D: trace finding to source bytes; explain why a hash is not authentication |
| Sliding windows | Applied concept to changed case: initial fixed-window error corrected; predicted 0/50/140/171 no finding and 51s cutoff correctly | B: personally modify/run case, inspect events and explain exact boundary; delayed recall |
| Composite keys and detection coverage | Applied reasoning: three groups, no threshold; identified coverage limitation of grouping | G: evaluate complementary rule against benign/ambiguous cases and independent truth |
| Deduplication and set membership | Guided reasoning: A/B/D count, four accepted vs three corrected; no separate-action proof explained | B/F: reproduce duplicates, explain identity and idempotency limitations |
| Assessment states and missing evidence | Explained with guidance; correctly predicted valid finding plus invalid input not fully valid | B/D: diagnose empty/partial/quarantined cases and source loss |
| Software tests, Python modules, CLI | Introduced/refreshed; AI ran 15 tests and experiments, learner not yet personally modified or debugged new code | B/C4–C5: run tests, change fixture/code intentionally, diagnose and restore |
| HTTP client/server and API verification | Applied reasoning: catalog 200 establishes reachability/listing, not inference or reliability; AI ran GET/POST | C4/F: personally inspect request/response and diagnose timeout or API failure |
| Model inference, context vs generation budget | Explained with guidance; learner proposed increasing max_tokens and raised efficiency; AI ran comparison | C4/C7: predict and diagnose truncation; distinguish context capacity, actual tokens, latency confounds |
| Context engineering | Guided design: learner favored bounded relevant context and deterministic core; related non-trigger event importance taught | C2/C3: choose scope and explain omission trade-off in new case |
| Structured output and schema | Explained with guidance; actual JSON fence failure and schema request demonstrated by AI | C3/C5: independently validate type/shape and unknown values, test invalid reference |
| Semantic grounding and uncertainty | Transferred reasoning from prior dependency-review work: rejected unsupported attacker/compromise claim, asked for precise references | C5/C6: adjudicate valid-looking unsupported claim; separate factual statement from hypothesis |
| AI evaluation and usefulness | First guided human review: semantic partial, additional value fail, hypotheses partial, investigation fail; identified vague next check | C6/C7: apply fixed rubric to new case, compare same-evidence baseline and record disagreement |
| Agent authorization / tool security | Introduced conceptually; no agent or tool implementation | E: independently explain and test allow/deny, injection, least authority |
| Observability, deployment, distributed systems | Concepts introduced (duplicates, partial failure); operational competence not demonstrated | F/later: logs, recovery, queues, ordering, retries, backpressure, replay |
| Applied security ML | Prior external ML experience does not establish AegisLab security ML competence | Later dedicated expansion: data leakage, splits, metrics, drift, justified baseline |
| DFIR and threat hunting | Evidence preservation and hypotheses introduced; forensic/hunt practice not established | D/G/later: acquisition, timeline, scoping, competing hypotheses and negative evidence |

## Industry-tool competence

The [industry competency matrix](../plans/INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md) tracks practical tool operation, configuration, integration and diagnosis separately from conceptual learning. Review applicable rows at each milestone; AI-only execution does not establish personal competence.

## Active recall and ownership queue

- B practical closure when PC access permits: learner selects a copy of a fixture, predicts a changed case, modifies/runs it, traces output to source lines, deliberately diagnoses one invalid input or wrong rule assumption, and explains evidence limits. AI may review, not perform the learner's critical step.
- C2 next: represent unknown target identity without hallucination, derive scope from existing references and evaluate a proposal against evidence. Revisit distinction among valid JSON, valid types, reference existence, entailment, usefulness and permission.
- C4/C5: personally run one local request and reproduce a bounded failure/fallback when possible.
- D: refresh July namespace/routing/SSH mechanics immediately before the authorized reconstruction; do not equate historical guided work with current independent competence.
- At next meaningful handoff, review two older concepts through delayed recall or transfer (e.g. socket ownership in inference and duplicate delivery in collection), not rote repetition.

Do not mark stable recall or independent practical mastery until supported by a later learner-owned demonstration. Keep the state summary short; update this ledger and link dated worklogs rather than recreating a competing curriculum.
