# AegisLab Project State

**Last meaningful update:** 2026-07-18  
**Current stage:** Core first learning slice — M5 Docker operating model and adapter preparation  
**Authority:** Non-normative handoff; explicit user direction, current inspected evidence, and canonical documents override this file

## Current objective

Build the Docker adapter deliberately rather than translating namespace commands mechanically.

The active route is:

```text
Phase 0  Docker object, process, network, and lifecycle model
        ↓
Phase 1  client/server adapter design and security boundaries
        ↓
Phase 2  safe server image
        ↓
Phase 3  manual Docker network and two-container topology
        ↓
Phase 4  authorized SSH success and unauthorized-key failure
        ↓
Phase 5  Docker-specific observability
        ↓
Phase 6  lifecycle, persistence, and one controlled fault
        ↓
Phase 7  Compose reproducibility
        ↓
Phase 8  namespace-versus-Docker comparison
```

Use the [M5 Docker Learning and Execution Plan](<docs/plans/AegisLab — M5 Docker Learning and Execution Plan.md>) for complete scope, learning depth, phases, and gates. Use the [M5 Docker Session Playbook](<docs/plans/AegisLab — M5 Docker Session Playbook.md>) for the exact current step and next action.

## Transition decision

The namespace SSH guided baseline was completed across successful authentication, controlled unauthorized-key failure, client/server log correlation, process/socket/namespace evidence, and teardown.

The learner explicitly chose to defer remaining formal M4 work because it was judged redundant for current learning value and directed progression to M5.

Record the decision accurately:

```text
remaining formal M4 scenario-contract work
→ deferred
→ not claimed complete

M5 Docker learning and reproduction
→ active
```

M5 preserves the demonstrated baseline:

- authorized public-key authentication succeeds;
- a valid but unauthorized key reaches SSH authentication and fails;
- server trust and client authorization remain distinct;
- a live connection can be observed;
- connection-specific state disappears after client teardown;
- the reusable server remains until deliberately stopped.

Formal fixed-count repeated failures, time bounds, start/end markers, separately maintained truth, and threshold cases remain deferred until a later detector/evaluation requirement makes them material.

## Current position

```text
Project definition and Core Charter                         accepted
Namespace networking and SSH control path                   guided baseline completed
Success/failure/log/process/socket/teardown correlation      guided baseline completed
Remaining formal M4 experiment-contract work                explicitly deferred
M5 Docker plan and session playbook                         versioned
Docker Phase 0 baseline inspection                          active
Docker adapter design                                       pending
Docker implementation                                       pending
Docker SSH reproduction                                     pending
Docker observability and controlled failure                  pending
Compose reproducibility                                     pending
Namespace-versus-Docker comparison                          pending
VM reproduction                                             later
Shared evidence/detection pipeline                          intentionally later
```

## Current environment evidence

### WSL

- Ubuntu runs under WSL2.
- A WSL network/resolver failure temporarily left only loopback and no usable route.
- `wsl --shutdown` followed by reopening WSL restored interfaces, routing, DNS, ICMP, and GitHub access.
- The previous namespace runtime disappeared after WSL shutdown, as expected for volatile lab state.

### Repository

- The learner pulled `main` through commit `27833bc` before the new M5 planning commits were created remotely.
- Before implementation, pull the latest `main` only after checking `git status --short`.
- No Docker adapter implementation, Dockerfile, or Compose file existed at M5 entry.

### Docker

Observed current control plane:

```text
Docker client:       29.6.1
Docker Desktop:      4.80.0
Docker Engine:       29.6.1
API:                 1.55
context:             default
OS/architecture:     linux/amd64
```

Object inventory at M5 entry:

- no running containers;
- unrelated stopped containers named `kali`, `juiceshop`, `webgoat`, and `dvwa`;
- unrelated local images, including `alpine:latest`;
- standard networks `bridge`, `host`, and `none`;
- unrelated custom networks:
  - `lab-net-nat` — `172.18.0.0/16`, non-internal;
  - `lab-net-internal` — `172.19.0.0/16`, internal;
- default bridge subnet `172.17.0.0/16`;
- no AegisLab Docker network created yet.

Unrelated Docker objects must remain untouched and must not become hidden project dependencies.

## Current learning objective

Phase 0 establishes a working Docker model before SSH implementation.

Required D2 concepts:

- image versus container versus running process;
- container writable state and lifecycle;
- container versus VM shared-kernel boundary;
- Docker-managed process and network namespace behavior;
- what stop, start, remove, and recreate change.

Required D1 concepts:

- Docker client versus daemon;
- Docker Desktop/WSL boundary;
- current object inventory and safe ownership.

Advanced cgroup, storage-driver, Docker Desktop VM, and bridge/firewall internals remain deferred unless a real blocker requires them.

## Exact next action

1. Pull the latest M5 planning commits after confirming a safe worktree.
2. Read the M5 playbook locally.
3. Continue at **Phase 0, Step 0.2**.
4. Predict image/container/process state for one named disposable AegisLab container.
5. Run and inspect only that disposable object.
6. Do not create the final SSH network, Dockerfile, keys, or Compose project before Phase 0 and Phase 1 gates.

## Teaching and collaboration controls

- Scale explanation depth to novelty, risk, confusion, and required concept depth.
- Do not apply full flag-by-flag explanations to every simple command.
- Keep the active problem and question visible before collecting evidence.
- Group read-only commands when they answer one coherent question.
- Use one action at a time for state changes, security boundaries, or diagnosis.
- Re-expose concepts progressively rather than repeating identical lectures.
- Assess through prediction, comparison, changed cases, diagnosis, and reduced-prompt reconstruction—not trivia.
- Stop collecting evidence when additional views no longer change the model or decision.
- Keep guided practice, stable recall, diagnosis, transfer, and independence distinct.

## Safety decisions

- Do not publish the Docker SSH port to the host during the initial adapter.
- Do not modify the ordinary WSL SSH service.
- Never commit or embed private keys in Git or image layers.
- Use only AegisLab-owned containers, networks, volumes, files, and names for implementation and cleanup.
- Reinspect state after WSL, Docker Desktop, container, image, or network lifecycle changes.
- Explain blast radius and cleanup before destructive Docker actions.

## Active references

- [Project Definition](<docs/AegisLab — Project Definition v1.0.md>)
- [Core Charter](<docs/plans/AegisLab — Core Charter v1.0.md>)
- [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>)
- [Core Execution Map](<docs/plans/AegisLab — Core Execution Map.md>)
- [M5 Docker Learning and Execution Plan](<docs/plans/AegisLab — M5 Docker Learning and Execution Plan.md>)
- [M5 Docker Session Playbook](<docs/plans/AegisLab — M5 Docker Session Playbook.md>)
- [Learning Preferences](LEARNING-PREFERENCES.md)
- [Current Learning State](docs/learning/CURRENT_LEARNING_STATE.md)
- [Namespace SSH lifecycle closure worklog](docs/worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md)

## Maintenance contract

- Update only after a meaningful decision, environment change, blocker change, phase transition, or completed learning checkpoint.
- Keep this file below 200 lines by moving detail to focused plans and worklogs.
- Do not store secrets, credentials, private keys, sensitive data, or unverified claims.
- Correct stale runtime facts rather than carrying them forward.
