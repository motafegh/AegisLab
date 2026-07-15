# AegisLab — Core Execution Map

**Status:** Active supporting execution map  
**Last meaningful update:** 2026-07-15  
**Authority:** Non-normative; the [Project Definition](<../AegisLab — Project Definition v1.0.md>), [Core Charter](<AegisLab — Core Charter v1.0.md>), and [Initial Journey Plan](<AegisLab — Initial Journey Plan.md>) remain controlling

## 1. Purpose

This document translates the accepted Core direction into visible milestone gates, required evidence, transition rules, and durable artifacts.

It does not replace the Charter, become a day-by-day schedule, or authorize later-scope technologies early.

The operating model is:

```text
understand one bounded mechanism
        ↓
observe and test it
        ↓
explain what the evidence proves
        ↓
modify or break it safely
        ↓
record the result
        ↓
advance only when the transition gate is satisfied
```

## 2. Core journey at a glance

```text
M0  Definition and bounded Core accepted
        ↓
M1  Networking and namespace substrate
        ↓
M2  Namespace SSH control path
        ↓
M3  Namespace SSH observability              ← current
        ↓
M4  Canonical namespace scenario
        ↓
M5  Docker adapter reproduction
        ↓
M6  VM adapter reproduction
        ↓
M7  Three-environment comparison and Slice 1 closure
        ↓
M8  Versioned scenario and evidence bundle
        ↓
M9  Shared host-evidence and truth path
        ↓
M10 Raw preservation and provenance
        ↓
M11 Normalization, validation, and quarantine
        ↓
M12 Repeated-failure detection
        ↓
M13 Finding, alert, incident, and deterministic report
        ↓
M14 Evaluation against experimental truth
        ↓
M15 Network-evidence correlation
        ↓
M16 Producer–collector runtime boundary
        ↓
M17 Replay, resilience, and Core graduation
```

The milestone numbers are navigation aids, not architecture or release versions.

## 3. Global transition rules

Every milestone follows these rules:

1. **Manual mechanism first.** Do not automate an important mechanism before the learner can explain and operate its manual form at the required depth.
2. **Prediction before changed behavior.** Record a concise expected result before a meaningful run, modification, or deliberate failure.
3. **Evidence before claims.** A successful exit status does not prove the intended behavior without inspecting the resulting state or artifact.
4. **Negative and failure evidence.** Include a non-match or negative case and one relevant bounded failure where the milestone requires them.
5. **Learner ownership.** Distinguish guided execution from stable recall, independent reconstruction, diagnosis, and transfer.
6. **No silent semantic drift.** Docker and VM adapters must preserve canonical scenario meaning rather than changing the case to simplify setup.
7. **One new principal difficulty.** Do not combine multiple major unfamiliar mechanisms in one learning unit without a blocking reason.
8. **Stop at the gate.** When a milestone passes, record the result and move on rather than adding unrelated polish.
9. **Volatile state is rechecked.** Namespaces, containers, VMs, PIDs, addresses, ports, services, files under `/tmp`, and tool integration are inspected before reuse.
10. **Deferred ideas require triggers.** Interesting technologies and enhancements remain in the [Deferred Ideas and Review Triggers](<AegisLab — Deferred Ideas and Review Triggers.md>) file until their entry condition exists.

## 4. Standard milestone evidence

An important milestone should preserve enough evidence to answer:

| Question | Required record |
|---|---|
| What did we intend to happen? | Scenario expectation or prediction |
| What action was requested? | Commanded or attempted action |
| What did the executor report? | Exit status and bounded output |
| What did the target observe? | Target log, process, socket, or application evidence |
| What crossed the network? | Selected packet or connection evidence where applicable |
| What actually occurred? | Separately maintained experimental truth using multiple observation classes |
| What failed or remained missing? | Explicit missing evidence and failure-layer statement |
| What changed the system? | Configuration, code, environment, or identity record |
| Can it be repeated? | Reconstruction or run instructions and cleanup state |
| Who currently owns the knowledge? | Assistance level and learner evidence |

Do not force every milestone to create every artifact. Preserve only what is materially required by the active mechanism.

## 5. M0 — Definition and bounded Core

**Status:** Complete enough to build.

### Exit evidence

- Project Definition v1.0 accepted.
- Core Charter v1.0 accepted.
- Initial Journey Plan active.
- Safety boundaries, deferred technologies, and first scenario family defined.

### Stop line

Do not repeatedly reopen project identity unless current evidence reveals a real contradiction or a major goal changes.

## 6. M1 — Networking and namespace substrate

**Status:** Practically built with guidance; durable independent ownership still developing.

### Mechanism

Two named Linux network namespaces connected by a veth pair with directly connected IPv4 addressing and routing.

### Evidence obtained

- interfaces and addresses;
- connected routes;
- ICMP connectivity;
- neighbor behavior;
- rebuild after restart;
- explanation that network namespaces do not provide full-machine isolation.

### Remaining ownership evidence

- changed-case reconstruction with reduced prompting;
- one bounded network-path diagnosis;
- concise explanation of interface, address, route, neighbor, namespace, and veth responsibilities.

M1 practical output is sufficient to continue learning inside M2–M4; it is not claimed as independent mastery.

## 7. M2 — Namespace SSH control path

**Status:** Working and understood with substantial guidance.

### Mechanism

A lab-specific OpenSSH client and server path using temporary identities, explicit authorization, isolated client trust state, and a listener bound only inside `aegis-peer`.

### Evidence obtained

- separate server host and client authentication key pairs;
- fingerprints and permission inspection;
- `authorized_keys` and `known_hosts` roles;
- validated lab-specific `sshd_config`;
- `/run/sshd` prerequisite diagnosed;
- `10.10.0.2:22` listener owned by `sshd`;
- successful public-key authentication;
- automatic repeat host verification;
- valid but unauthorized key rejection;
- bounded `ForceCommand /usr/bin/id` execution.

### Important limitation

`ForceCommand /usr/bin/id` is instructional scaffolding. M4 must define the canonical normal-authentication behavior without silently treating this scaffold as the final case.

## 8. M3 — Namespace SSH observability

**Status:** Active current milestone.

### Principal difficulty

Correlating one event across multiple observation positions without assuming that each source proves the same fact.

### Required observations

- client SSH debug trace;
- foreground or preserved server authentication log;
- listener and `ESTABLISHED` socket states;
- client, listener, pre-authentication, and authenticated process relationships;
- one narrow packet capture;
- deliberate connection closure and teardown;
- explicit visibility limitations caused by encryption and namespace-only isolation.

### Exit gate

The learner can draw and explain one connection using:

```text
10.10.0.1:<ephemeral-port>
        ↕
10.10.0.2:22
```

and accurately state what each of these proves or does not prove:

```text
client debug line
server log line
socket-table line
process-table line
packet observation
```

The learner also predicts and interprets a changed observation with materially less step-by-step assistance.

## 9. M4 — Canonical namespace scenario

**Status:** Pending after M3.

### Required scenario cases

1. normal authorized authentication;
2. benign or non-malicious negative case;
3. repeated unauthorized authentication failures;
4. threshold or boundary case when the later detector contract is prepared;
5. one deliberately broken infrastructure or evidence path.

### Required scenario contract

- actor and target identities;
- authorized addresses and environment;
- normal and repeated-failure semantics;
- explicit attempt count and time bounds;
- start and end markers;
- commanded actions versus expected observable effects;
- host and network evidence checklist;
- abort conditions;
- cleanup;
- separately maintained expected truth.

### Exit gate

- The complete scenario runs manually and safely.
- The learner explains normal and failed authentication behavior.
- A bounded failure is predicted, introduced, diagnosed, repaired, and revalidated.
- Cleanup succeeds.
- The scenario contract is stable enough to reproduce without changing its meaning.

## 10. M5 — Docker adapter reproduction

**Status:** Pending.

### Entry gate

- M4 scenario semantics and evidence checklist are stable.
- Docker Desktop is running and Ubuntu WSL integration is verified.
- The learner understands at the required depth which responsibilities Docker automates or isolates.

### Required comparison points

- container network attachment;
- filesystem and user views;
- shared-kernel boundary;
- service lifecycle;
- process visibility;
- logs;
- packet-capture position;
- persistence and cleanup;
- exposure to host or external networks.

### Exit gate

The same normal and repeated-failure cases run with comparable evidence, and environment-specific limitations are documented rather than hidden.

## 11. M6 — VM adapter reproduction

**Status:** Pending.

### Entry gate

- M4 scenario semantics are stable.
- A usable local Linux VM path is selected from evidence.
- Hyper-V remains the default candidate when suitable; another local manager requires a documented reason.

### Required comparison points

- separate guest kernel;
- virtual switch and adapter topology;
- guest filesystem and user database;
- service lifecycle and boot persistence;
- host/guest observation boundaries;
- packet-capture positions;
- snapshots or recovery where justified;
- operational cost and cleanup.

### Exit gate

The same scenario and evidence checklist run across separate machine boundaries, and the learner explains the added isolation and hidden automation.

## 12. M7 — Three-environment comparison and first-slice closure

**Status:** Pending.

### Required comparison artifact

| Dimension | Namespaces | Docker | VMs |
|---|---|---|---|
| Network topology |  |  |  |
| Kernel isolation |  |  |  |
| Process boundary |  |  |  |
| Filesystem/user boundary |  |  |  |
| Service lifecycle |  |  |  |
| Host logs |  |  |  |
| Network evidence |  |  |  |
| Persistence |  |  |  |
| Cleanup |  |  |  |
| Security limitations |  |  |  |
| Operational cost |  |  |  |

### Exit gate

- All three adapters work or a bounded blocker is documented with an explicit follow-up gate.
- The learner can explain what each environment exposes, hides, automates, and isolates.
- The same scenario meaning is preserved.
- The first slice worklog, learning state, and project handoff are updated.

No event-pipeline code is required before this point.

## 13. M8 — Versioned scenario and evidence bundle

**Status:** Pending after manual cross-environment understanding.

### Principal difficulty

Turning a understood manual experiment into a reproducible, inspectable contract without automating away the mechanism.

### Initial artifacts

- scenario identifier and version;
- run identifier;
- environment adapter identity;
- actor, target, address, account, and key-fingerprint metadata using public identifiers only;
- expected actions and outcomes;
- start/end timestamps and markers;
- command-attempt record;
- evidence inventory;
- expected truth record;
- cleanup result;
- checksums for preserved evidence where justified.

### Exit gate

A fresh run can be understood and audited without relying on chat history, while the learner can still execute and explain the underlying manual mechanism.

## 14. Shared Core milestones M9–M17

These milestones follow the sequence already defined by the Core Charter and Journey Plan.

| Milestone | Principal new difficulty | Minimum exit condition |
|---|---|---|
| M9 Host evidence and truth | Distinguishing action, observation, and truth | One host source is collected and linked to a scenario run |
| M10 Raw preservation and provenance | Preserving origin before transformation | Raw records are addressable, attributable, and unchanged |
| M11 Normalization and validation | Transforming without losing meaning | Valid records normalize; invalid records are quarantined explicitly |
| M12 Detection | Stateful counting in a time window | Below/at/above and duplicate cases behave correctly |
| M13 Incident and report | Evidence-backed claims and uncertainty | Finding, alert, incident, and deterministic report link to evidence |
| M14 Evaluation | Comparing output with independent truth | Expected-versus-observed results identify supported failure layers |
| M15 Network correlation | Relating connection and authentication evidence | Network and host evidence correlate without overclaiming equivalence |
| M16 Producer–collector boundary | Partial failure across runtimes | Delivery, interruption, retry, and duplicate behavior are observable |
| M17 Replay and resilience | Honest behavior under imperfect telemetry | Fixed inputs replay deterministically; one delayed/missing case is diagnosed |

Detailed specifications should be created only when each milestone becomes active.

## 15. Artifact ladder

The project should produce durable artifacts in this order:

```text
observed command and output
        ↓
worklog checkpoint
        ↓
learner-facing study guide when a complete concept unit exists
        ↓
scenario contract and evidence checklist
        ↓
versioned run evidence
        ↓
normalized event and provenance records
        ↓
detection and incident evidence
        ↓
evaluation and report
        ↓
portfolio-facing demonstration after the mechanism is defensible
```

Documentation consolidates demonstrated work. It must not become a substitute for implementation or explanation.

## 16. Portfolio checkpoints

A portfolio artifact is justified only after a meaningful gate, not after every command.

Recommended checkpoints:

- first-slice three-environment comparison;
- first end-to-end evidence-linked detection;
- first controlled failure postmortem;
- Core graduation demonstration.

Each portfolio artifact should disclose:

- learner-owned work;
- AI-assisted work;
- observed evidence;
- known limitations;
- what can be independently explained and modified.

## 17. Current handoff

Current active location:

```text
M3 — Namespace SSH observability
```

Immediate next evidence:

1. inspect both sides of the live `ESTABLISHED` socket;
2. inspect the SSH process tree and namespace PIDs;
3. correlate the endpoint and process identifiers with server logs;
4. close the connection and observe teardown;
5. capture one new connection using a narrow packet filter.

See [PROJECT_STATE.md](../../PROJECT_STATE.md), the [Current Learning State](../learning/CURRENT_LEARNING_STATE.md), and the [active namespace SSH worklog](../worklogs/2026-07-14-1505-namespace-ssh-foundations.md).

## 18. Maintenance contract

- Update when milestone gates, evidence requirements, or the current transition materially change.
- Do not turn this file into a session diary or duplicate the active worklog.
- Preserve canonical scope; proposed expansions belong in the deferred-ideas register.
- Add detailed specifications only when the associated milestone becomes active.
- Keep completion language evidence-based and distinguish guided work from independence.
