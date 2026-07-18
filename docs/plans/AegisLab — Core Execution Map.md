# AegisLab — Core Execution Map

**Status:** Active supporting execution map  
**Last meaningful update:** 2026-07-18  
**Authority:** Non-normative; the Project Definition, Core Charter, Initial Journey Plan, explicit user direction, and current evidence remain controlling

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
advance when the active transition decision is supported
```

## 2. Core journey at a glance

```text
M0  Definition and bounded Core accepted
        ↓
M1  Networking and namespace substrate
        ↓
M2  Namespace SSH control path
        ↓
M3  Namespace SSH observability                  guided baseline complete
        ↓
M4  Canonical namespace scenario                 formal remainder deferred
        ↓
M5  Docker adapter reproduction                  ← active
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

Milestone numbers are navigation aids, not architecture or release versions.

## 3. Current transition decision

The learner completed a guided namespace baseline covering:

- authorized SSH authentication;
- valid but unauthorized-key rejection;
- server trust and client authorization;
- process, socket, namespace, log, packet, and teardown observations;
- listener survival after connection teardown.

The learner explicitly directed progression to M5 because the remaining formal M4 work was judged redundant for current learning value.

Therefore:

```text
remaining M4 formal scenario-contract work
→ deferred
→ not claimed complete

M5 Docker learning and reproduction
→ active
```

Deferred M4 items include fixed-count repeated failures, formal time bounds, start/end markers, separately maintained expected truth, threshold cases, and the full formal scenario contract. They return when later detection/evaluation work creates a concrete requirement or the learner chooses to revisit them.

The active Docker scope and exception are owned by:

- [M5 Docker Learning and Execution Plan](<AegisLab — M5 Docker Learning and Execution Plan.md>);
- [M5 Docker Session Playbook](<AegisLab — M5 Docker Session Playbook.md>);
- `PROJECT_STATE.md` for current handoff.

## 4. Global transition rules

1. **Manual mechanism first.** Do not automate an important learning-critical mechanism before the learner can explain and operate its manual form at the required depth.
2. **Prediction before meaningful change.** Record an expected result before an important run, modification, or deliberate failure.
3. **Evidence before claims.** A successful exit status does not prove intended behavior without inspecting resulting state or artifacts.
4. **Negative and failure evidence.** Include a meaningful negative case and a bounded failure where the active milestone requires them.
5. **Learner ownership.** Distinguish guided execution from recall, independent reconstruction, diagnosis, and transfer.
6. **No silent semantic drift.** Docker and VM adapters preserve demonstrated SSH success/failure meaning unless a deliberate change is recorded.
7. **One principal difficulty.** Do not combine several major unfamiliar mechanisms in one learning unit without a blocking reason.
8. **Stop at the gate.** When a phase passes, record it and move on rather than adding unrelated polish.
9. **Volatile state is rechecked.** Namespaces, containers, VMs, PIDs, addresses, ports, services, temporary files, networks, and volumes are inspected before reuse.
10. **Explicit decisions may change the route.** When the learner deliberately skips or defers a gate, record the exception and missing evidence honestly rather than pretending the gate passed.
11. **Explanation is proportionate.** Use full depth for core boundaries, confusion, diagnosis, and transfer; keep simple familiar mechanics concise.
12. **Deferred ideas require triggers.** Interesting technologies remain deferred until their entry condition exists.

## 5. Standard milestone evidence

An important milestone should preserve enough evidence to answer:

| Question | Required record |
|---|---|
| What did we intend? | Expectation or prediction |
| What action was requested? | Commanded or attempted action |
| What did the executor report? | Exit status and bounded output |
| What did the target observe? | Logs, process, socket, or application evidence |
| What crossed the network? | Selected connection or packet evidence where material |
| What actually occurred? | Supported conclusion using multiple observation classes |
| What failed or remained missing? | Missing evidence and failure-layer statement |
| What changed the system? | Configuration, code, environment, identity, image, or runtime record |
| Can it be repeated? | Reconstruction/run instructions and cleanup state |
| Who owns the knowledge? | Assistance level and learner evidence |

Do not force every milestone to create every artifact. Preserve only materially required evidence.

## 6. M0 — Definition and bounded Core

**Status:** Complete enough to build.

Exit evidence:

- Project Definition v1.0 accepted;
- Core Charter v1.0 accepted;
- Initial Journey Plan active;
- safety boundaries, deferred technologies, and first scenario family defined.

Stop line: do not repeatedly reopen project identity without a real contradiction or goal change.

## 7. M1 — Networking and namespace substrate

**Status:** Practical guided baseline complete; independent ownership still developing.

Mechanism: two named Linux network namespaces connected by a veth pair with IPv4 addressing and routing.

Evidence obtained:

- interfaces, addresses, routes, and ICMP;
- rebuild after restart;
- network-isolation explanation;
- one guided network failure diagnosis.

Remaining ownership:

- changed-case reconstruction with reduced prompting;
- concise independent responsibility explanation.

## 8. M2 — Namespace SSH control path

**Status:** Working and understood with substantial guidance.

Mechanism: lab-specific OpenSSH client/server path using temporary identities, explicit authorization, isolated client trust, and a namespace-only listener.

Evidence obtained:

- distinct server and client identities;
- fingerprints and permissions;
- `authorized_keys` and `known_hosts` roles;
- validated lab `sshd_config`;
- namespace listener;
- successful public-key authentication;
- unauthorized-key rejection;
- bounded instructional execution.

Important limitation: temporary scaffolding is not a production recommendation.

## 9. M3 — Namespace SSH observability

**Status:** Guided baseline complete.

Principal difficulty: correlate one connection across observation positions without treating each source as equivalent.

Evidence obtained:

- client debug trace;
- foreground server success/failure/disconnect logs;
- listener and `ESTABLISHED` sockets;
- client, listener, privileged, and authenticated process relationships;
- namespace PID membership;
- selected packet establishment and teardown;
- explicit encryption and namespace-visibility limitations.

Remaining ownership:

- concise reduced-prompt explanation;
- independent changed-case diagnosis;
- delayed reconstruction.

These gaps transfer into later work rather than blocking M5 by explicit learner decision.

## 10. M4 — Canonical namespace scenario

**Status:** Formal remainder deferred by explicit learner decision.

Demonstrated semantic baseline preserved for M5:

1. authorized authentication succeeds;
2. valid unauthorized key reaches authentication and fails;
3. successful connection can be observed;
4. connection teardown removes connection-specific state while the listener survives.

Deferred formal requirements:

- repeated fixed-count failures;
- explicit time bounds;
- start/end markers;
- separate expected-truth record;
- threshold/boundary case;
- full scenario contract;
- independent bounded failure exercise.

This milestone is not marked complete.

## 11. M5 — Docker adapter reproduction

**Status:** Active.

### Active purpose

Reproduce the demonstrated SSH baseline while learning Docker-specific responsibilities rather than merely replaying namespace commands.

### Phase route

```text
Docker operating model
→ adapter design
→ server image
→ manual client/server topology
→ SSH success/failure
→ Docker observability
→ lifecycle/persistence/failure
→ Compose reproducibility
→ namespace comparison
```

### Required comparison points

- image, container, and process responsibilities;
- container network attachment and DNS;
- filesystem and user/UID/GID views;
- shared-kernel and namespace boundaries;
- service and PID 1 lifecycle;
- process and socket visibility;
- logs and target evidence;
- state persistence and cleanup;
- one Docker-specific predicted failure;
- manual operation before Compose.

### Entry evidence

- Docker Desktop engine reachable from WSL;
- Docker client/server 29.6.1, API 1.55, context `default`;
- no running containers at entry;
- unrelated Docker objects identified and excluded from project ownership;
- M5 plan and session playbook versioned.

### Exit gate

- core Docker object/lifecycle model demonstrated;
- two-container private-network adapter built without unnecessary host port publication;
- authorized success and unauthorized failure reproduced;
- private material excluded from Git and committed image layers;
- process, network, filesystem, log, and lifecycle evidence correlated;
- one Docker-specific failure diagnosed and repaired;
- Compose adapter verified from a fresh state;
- namespace-versus-Docker comparison recorded;
- learner depth and remaining gaps stated honestly.

## 12. M6 — VM adapter reproduction

**Status:** Pending after M5.

Purpose: reproduce the same semantic baseline across separate Linux VM endpoints and compare full-kernel, boot, service, storage, networking, and observation boundaries.

Entry requires a stable Docker comparison and a verified local VM path.

## 13. M7 — Three-environment comparison

**Status:** Pending.

Compare namespaces, Docker, and VMs across:

- topology;
- kernel/process boundaries;
- service lifecycle;
- routing and packet observation;
- logging;
- filesystem and persistence;
- reconstruction and cleanup;
- isolation, trust, and failure classes.

Slice 1 closes only when the learner can explain what each environment automates, exposes, hides, shares, and isolates.

## 14. Later Core milestones

M8–M17 remain intentionally later:

- versioned scenario/evidence bundle;
- shared host evidence and truth;
- raw preservation and provenance;
- normalization, validation, and quarantine;
- repeated-failure detection;
- finding/alert/incident/report;
- evaluation against truth;
- network-evidence correlation;
- producer/collector boundary;
- replay, resilience, and Core graduation.

Do not pull these mechanisms into M5 without a demonstrated requirement.

## 15. Maintenance contract

- Update after a milestone transition, explicit route exception, changed gate, or materially new evidence.
- Keep current runtime state in `PROJECT_STATE.md` and the active session playbook.
- Keep detailed chronology in worklogs.
- Record skipped/deferred work honestly rather than changing its status to complete.
- Preserve canonical documents as stronger authorities.
