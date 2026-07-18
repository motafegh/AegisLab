# AegisLab Current Learning State

**Last meaningful update:** 2026-07-18  
**Status:** Namespace SSH guided baseline complete; M5 Docker Phase 0 active  
**Authority:** Non-normative; current observed performance and canonical project documents override this file  
**Historical baseline:** [Learner Profile](LEARNER_PROFILE.md)

## Purpose

This file gives a concise current view of demonstrated learning, assistance level, active gaps, and the next ownership gate.

Do not treat successful commands, polished documents, guided reconstruction, or AI-authored plans as evidence of independent mastery.

## Current project-learning phase

```text
namespace SSH guided baseline
        ↓
M4 remaining formal contract work deferred by learner decision
        ↓
M5 Docker operating model and adapter transfer
```

The learner completed a guided end-to-end namespace SSH lifecycle and explicitly directed the project to proceed to Docker rather than complete remaining formal M4 repeated-count work.

Current M5 focus is not yet SSH implementation. It is building a working Docker model before adapter design:

- Docker client and daemon;
- image, container, and running process;
- lifecycle and writable state;
- container versus VM boundary;
- Docker-managed process and network isolation;
- safe ownership of Docker objects.

Use the [M5 Docker Learning and Execution Plan](<../plans/AegisLab — M5 Docker Learning and Execution Plan.md>) for depth and phase gates and the [M5 Docker Session Playbook](<../plans/AegisLab — M5 Docker Session Playbook.md>) for the current step.

## Demonstrated namespace baseline

### Networking and namespaces

The learner has personally:

- created and rebuilt `aegis-test` and `aegis-peer`;
- created and moved a veth pair;
- assigned addresses and brought interfaces up;
- inspected connected routes;
- verified ICMP connectivity;
- diagnosed a missing-address/network-unreachable case with guidance;
- explained that a network namespace isolates networking rather than a complete machine.

Evidence level:

```text
repeated guided reconstruction
real output interpretation
one guided changed case
independent reconstruction from requirements not demonstrated
```

### Linux ownership and permissions

The learner has created and interpreted:

- root-controlled server storage;
- learner-controlled client and authorization storage;
- modes `711`, `700`, `600`, `644`, and `755`;
- parent-directory traversal behavior;
- process identity versus file ownership;
- path/environment and permission failures.

Evidence level:

```text
taught and practiced
real failures interpreted with guidance
design transfer and stable terminology still developing
```

### SSH identity, trust, and authorization

The learner has generated and distinguished:

- server host identity;
- authorized client identity;
- unauthorized client identity;
- `known_hosts` server trust;
- `authorized_keys` client authorization;
- public fingerprints versus private key material.

Evidence level:

```text
correct distinctions observed in real success and failure
re-exposure should be concise during Docker
stable unaided explanation not fully assessed
```

### SSH server and authentication lifecycle

The learner has built and observed:

- lab-specific `sshd_config`;
- a listener bound only to the namespace target;
- successful public-key authentication;
- long-lived `ssh -N -T` transport;
- authorized-key lookup and accepted proof;
- valid but unauthorized-key rejection;
- matching client and server fingerprints/log evidence;
- `[preauth]` failure closure;
- authenticated user-child creation only after success;
- clean client teardown while the listener survived.

Evidence level:

```text
strong guided practical evidence
success and failure layers correctly interpreted
independent configuration and modified-case design unproven
```

### Process, socket, namespace, packet, and log correlation

The learner has interpreted:

- opposite views of one TCP endpoint pair;
- stable server port versus ephemeral client port;
- listener versus per-connection server processes;
- client process and privilege/namespace wrappers;
- host-wide process visibility without a PID namespace;
- namespace PID membership;
- SYN/SYN-ACK/ACK establishment;
- encrypted traffic metadata boundaries;
- FIN-based teardown;
- success, failure, and disconnect server logs.

Evidence level:

```text
completed with guided interpretation
cross-source model demonstrated
concise reduced-prompt explanation still required
```

## Deferred M4 evidence

The following are not claimed complete:

- fixed-count repeated unauthorized attempts;
- explicit time bounds;
- formal start/end markers;
- separately maintained expected truth;
- threshold/boundary cases;
- full formal scenario contract;
- independent bounded infrastructure-failure exercise.

They remain deferred until later detection/evaluation work creates a concrete need or the learner chooses to revisit them.

## Current Docker evidence

The learner has personally inspected:

- Docker client and Docker Desktop engine versions;
- active Docker context;
- running and stopped container inventory;
- local image inventory;
- standard and custom Docker networks;
- bridge subnets and `Internal` state;
- the absence of existing AegisLab Docker implementation files.

A temporary WSL network/resolver failure was repaired by shutting down and reopening WSL, restoring routing, DNS, ICMP, and Git access.

Current Docker evidence level:

```text
control-plane availability verified
object inventory interpreted
image/container/process/lifecycle model not yet demonstrated
Docker adapter implementation not started
```

## Honest depth summary

| Area | Current evidence | Required next depth |
|---|---|---|
| Namespace networking | Rebuilt and interpreted with guidance | Retain as comparison baseline; changed-case independence later |
| Linux permissions | Practiced through real failures | Apply to container users and mounts at D2/D3 |
| SSH identities/trust | Guided success/failure correlation | Concise re-exposure and Docker transfer at D2 |
| SSH process/socket lifecycle | Guided cross-source model | Compare Docker PID/network isolation at D2/D3 |
| Docker CLI versus daemon | Verified operationally | D1 explanation |
| Image/container/process | Not yet demonstrated | D2 working model in Phase 0 |
| Container lifecycle/state | Not yet demonstrated | D2 prediction and observation |
| Container versus VM | Not yet demonstrated in current slice | D2 before adapter design closes |
| Docker networking | Existing networks inspected | D2 user-defined bridge/DNS/attachment model |
| Docker filesystem/users | Not begun | D2 mounts, writable layer, UID/GID |
| Docker observability | Not begun | D2/D3 logs, inspect, top, PIDs, sockets |
| Docker failure diagnosis | Not begun | D3 one predicted fault and repair |
| Compose | Not begun | D2 after manual mechanisms |

No area is claimed as full practical independence.

## Teaching controls for M5

Use the depth system defined in the M5 plan:

```text
D0 orientation
D1 recognition and safe operation
D2 working mental model
D3 diagnosis and transfer
D4 advanced internals deferred
```

Explanation must be proportionate:

- brief for familiar low-risk mechanics;
- standard for new project-relevant mechanisms;
- deep for D2/D3 concepts, security boundaries, confusion, conflicting evidence, diagnosis, or transfer.

Do not:

- give maximum-depth explanations for every command;
- repeat complete flag explanations when a short reminder is sufficient;
- collect multiple evidence views after they stop changing the model;
- hide the main question behind command sequences;
- assess untaught material;
- equate guided execution with stable recall;
- force repetitive worksheets or trivia.

Use progressive re-exposure:

```text
guided first exposure
→ shorter prediction on repeat
→ changed context
→ diagnosis or transfer
```

## Active learning gaps

1. Explain image, container, and running process responsibilities using real output.
2. Predict and observe stop/start/remove/recreate state lifetime.
3. Explain container shared-kernel and isolation boundaries versus a VM.
4. Correlate Docker, inside-container, and host-side process/network views.
5. Design the two-container SSH adapter without unnecessary host exposure.
6. Decide safe image-versus-runtime ownership for keys, authorization, trust, and configuration.
7. Build and inspect a server image without committing private material.
8. Reproduce authorized success and unauthorized failure in Docker.
9. Diagnose and repair one Docker-specific fault.
10. Encode the understood mechanism in Compose.
11. Compare namespace and Docker behavior from evidence.

## Next ownership gate

Phase 0 closes when the learner can explain from one disposable container:

- what comes from the image;
- what belongs to the container writable state;
- which process makes the container run;
- what stop changes;
- what remove/recreate changes;
- which kernel is shared;
- what Docker creates automatically for process and network isolation.

Passing does not require memorizing every Docker command or implementation detail.

## Current exact next action

After pulling the latest planning changes and confirming a safe worktree, continue at M5 Playbook **Phase 0, Step 0.2**: predict and run one named disposable AegisLab container, then inspect the minimum evidence needed to distinguish image, container, and process.

## Latest worklogs

- [2026-07-18 — M5 Docker planning and learning controls](../worklogs/2026-07-18-1640-m5-docker-planning.md)
- [2026-07-18 — Namespace SSH authentication lifecycle closure](../worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md)

## Maintenance contract

- Update after meaningful demonstrated learning, corrected misconception, changed assistance level, phase transition, or new gap.
- Keep chronology in worklogs and current position in the M5 playbook.
- Preserve the detailed historical Learner Profile and full study guides.
- Separate taught, guided practice, stable recall, diagnosis, transfer, and independent reproduction.
- Never store credentials, private keys, passwords, sensitive personal data, malicious samples, or unbounded raw logs.
