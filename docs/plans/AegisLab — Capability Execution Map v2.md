# AegisLab — Capability Execution Map v2

**Status:** Active from 2026-11-22 | **Authority:** execution plan under [Core Charter v2](<AegisLab — Core Charter v2.0.md>) and the canonical Project Definition.
**Supersedes for execution:** [Initial Journey Plan](<AegisLab — Initial Journey Plan.md>), [Core Execution Map M0–M17](<AegisLab — Core Execution Map.md>) and the [M5 Docker playbook](<AegisLab — M5 Docker Session Playbook.md>). Their historical facts and technical exercises are preserved.

## Historical disposition

| Previous work | Actual supported state | Treatment |
| --- | --- | --- |
| M0–M3 namespace networking, SSH authentication and process/socket/log/packet observation | Completed **with guidance** in July; no independent reconstruction claim | Retain reference scenario and learning artifacts |
| M4 repeated-failure/formal independent scenario contract | Explicitly deferred; not passed | Reintroduce only parts required by B/D evaluation |
| M5 Docker Phase 0 and plan | Previous active route; initial object inventory and planning only; no Docker adapter/Compose proof | Historical, optional later D/F infrastructure learning |
| M6–M17 | Unbuilt | Replace obsolete order with capabilities A–G; later parity remains optional deliberate depth |

## Active route

```text
A  Adopt v2 + verify source limitations
       ↓
B  CLI: authentic log envelopes → normalized observations → deterministic finding
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

## Per-stage checkpoint record

1. **System works now:** exact command and source artifact / observable result.
2. **Evidence:** input provenance, tests actually run, failure cases and truth limitations.
3. **Human learning:** prediction, inspected output and personally diagnosed/changed case; help level.
4. **AI work:** implementation and test generation attribution.
5. **Unresolved / next:** one justified user-visible action, not a calendar promise.

Only add new tools/containers/services when a stage exercises a real responsibility. Preserve the [AI Collaboration Protocol](<../AegisLab — AI Collaboration Protocol.md>), [Learning Preferences](../../LEARNING-PREFERENCES.md) and [Current Learning State](../learning/CURRENT_LEARNING_STATE.md). Details for the adoption decision remain in the [2026-11-22 evolution proposal](../proposals/2026-11-22-ai-first-aegislab-evolution-plan.md).
