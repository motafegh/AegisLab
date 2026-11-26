# AegisLab — Capability Execution Map v2

**Status:** Active from 2026-11-22 | **Authority:** execution plan under [Core Charter v2](<AegisLab — Core Charter v2.0.md>) and the canonical Project Definition.
**Supersedes for execution:** [Initial Journey Plan](<AegisLab — Initial Journey Plan.md>), [Core Execution Map M0–M17](<AegisLab — Core Execution Map.md>) and the [M5 Docker playbook](<AegisLab — M5 Docker Session Playbook.md>). Their historical facts and technical exercises are preserved.

## Historical disposition

| Previous work | Actual supported state | Treatment |
| --- | --- | --- |
| M0–M3 namespace networking, SSH authentication and process/socket/log/packet observation | Completed **with guidance** in July; no independent reconstruction claim | Retain historical reference scenario and learning artifacts; present learner competence reset |
| M4 repeated-failure/formal independent scenario contract | Explicitly deferred; not passed | Reintroduce only parts required by B/D evaluation |
| M5 Docker Phase 0 and plan | Previous active route; initial object inventory and planning only; no Docker adapter/Compose proof | Historical only; container learning starts from first principles at D/F as justified |
| M6–M17 | Unbuilt | Replace obsolete order with capabilities A–G; later parity remains optional deliberate depth |

## Active route

```text
A  Adopt v2 + verify source limitations
       ↓
B  CLI: bounded source-declared log envelopes → normalized observations → deterministic finding
       ↓
C  local optional AI investigation vs identical-evidence baseline
       ↓
D  fresh authorized SSH run → sensor → collector → finding (controlled failure)
       ↓
E  read-only inquiry tools → policy mediation → adversarial testing
       ↓
F  deploy/observe/restart/recover reliably in bounded local environment
       ↓
G  transfer to different authorized context → compare → portfolio
```

Stages may be deliberately reordered if a verified prerequisite or flaw requires it. In particular, move a small D exercise before C when needed to validate live evidence assumptions. Never make Docker or VM parity a blocking prerequisite for B/C. Do not declare a stage finished solely because AI wrote it.

## Learning reset and three-track execution (owner-approved 2026-11-26)

Assume all pre-return (before 2026-11-22) learning/practice unavailable until re-established. Historical engineering evidence and current software survive; post-return learner evidence is retained only at its demonstrated depth. Follow the [foundations rebuild](../learning/FOUNDATION-REBUILD.md) for the ordered R1–R5 sessions and F1–F6 learning units. The three tracks are security/systems, AI/software engineering and industry tooling, connected through the same evidence and engineering problems.

Immediate sequence: native Sigma exercise (with prerequisite repair) → first-principles Linux/networking/cryptography/SSH rebuild → focused C2–C5 contract and reliability increment → C6–C8 evaluation → fresh authorized Stage D lab. B personal ownership stays open and may proceed in parallel. If native tooling is blocked, explicitly retain its checkpoint and advance foundations; do not skip it silently. Stage D requires newly demonstrated foundations, not July recall. The existing A–G product acceptance and safety gates are unchanged.

F/G adds practical search/indexing and security-platform exercises: Elasticsearch/Kibana foundation in F, Elastic Security/OpenSearch comparison and bounded Splunk/SPL exercise in G, with explicit blocker/deferral rules and deeper distributed search after Core. See the [industry register](INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md) for detailed outcomes. No simultaneous platform deployments or blanket package/service authorization.

## Executable gates and exact stop lines

| Stage | Demonstrable exit gate | Stop / do not imply |
| --- | --- | --- |
| A | v2 authority and handoff consistent; source and privacy limits recorded | historical logs are not retained raw input; do not reconstruct them as observations |
| B | single documented CLI; positive, normal, time-bound, duplicate, bad/missing data checks; exact source/event IDs, quarantine and report | no observed records ≠ no activity; a synthetic fixture ≠ a live run; no incident ≠ compromise ruled out |
| C | AI ON/OFF on identical evidence; bounded schema, ID validation, semantic-adjudication record, error fallback | ID validity ≠ factual entailment; no usefulness without measured baseline |
| D | fresh isolated controlled execution; target observation, source custody, expected-vs-actual, missing sensor and cleanup | no unapproved sudo, host SSH change or published port |
| E | approved scoped read-only inquiry, policy allow/deny, audited tool calls, injection and budget tests | no arbitrary command/network/credential/write/response tool |
| F | repeatable local run, one diagnosed failure and restart/replay proof, operating notes | no production SLO inference from homelab |
| G | new authorized event family with contrasted scenarios, error analysis and comparative operator task | no claim of independently demonstrated demand or mastery without evidence |

## Active stage detail

See [Stage C execution plan](STAGE-C-EXECUTION.md) for C1-C8 milestones and the current candidate contract. The [learning ledger](../learning/LEARNING_LEDGER.md) tracks depth and recall across stages; it does not replace these gates.

## Industry competence and product relevance

The [Industry Tools and Product Strategy](INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md) is the stage-linked tool competency and adoption register. At stage planning and closure review its applicable Core checkpoints; record practical learner evidence, integration/exercise decision, or explicit justified deferral with a revisit trigger. Industry exposure is not permanent dependency adoption. Keep the Core gates and safety boundaries unchanged. Compare with existing tools and measure operator usefulness before broadening custom implementations.

## Per-stage checkpoint record

1. **System works now:** exact command and source artifact / observable result.
2. **Evidence:** input provenance, tests actually run, failure cases and truth limitations.
3. **Human learning:** prediction, inspected output and personally diagnosed/changed case; help level.
4. **AI work:** implementation and test generation attribution.
5. **Unresolved / next:** one justified user-visible action, not a calendar promise.

Only add new tools/containers/services when a stage exercises a real responsibility. Preserve the [AI Collaboration Protocol](<../AegisLab — AI Collaboration Protocol.md>), [Learning Preferences](../../LEARNING-PREFERENCES.md) and [Current Learning State](../learning/CURRENT_LEARNING_STATE.md). Details for the adoption decision remain in the [2026-11-22 evolution proposal](../proposals/2026-11-22-ai-first-aegislab-evolution-plan.md).
