# AegisLab Current Learning State

**Last meaningful update:** 2026-07-18  
**Status:** Namespace SSH guided baseline completed; Docker transfer beginning  
**Authority:** Non-normative; current observed performance and canonical project documents override this file  
**Historical baseline:** [Learner Profile](LEARNER_PROFILE.md)

## Purpose

This file gives a concise current view of demonstrated learning, assistance level, active gaps, and the next ownership gate.

Do not treat successful commands, polished documentation, or guided reconstruction as evidence of independent mastery.

## Current project-learning phase

```text
AegisLab Core first learning slice
        ↓
namespace SSH guided baseline completed
        ↓
Docker scenario transfer and comparison
```

The learner rebuilt the namespace SSH lab after restart using the supplied reconstruction runbook and completed a guided end-to-end authentication lifecycle: successful long-lived authentication, socket/process/namespace correlation, controlled unauthorized-key failure, client/server log correlation, and clean teardown with listener survival.

The namespace implementation is now a valid guided baseline for Docker transfer. Reduced-prompt explanation, independent changed-case diagnosis, formal repeated-failure bounds, and independent reconstruction remain open.

## Primary study material

Use the [Study Guide Index](study-guides/README.md) and its layered study editions as the primary study path:

1. networking and namespace foundations;
2. SSH identities and Linux permissions;
3. namespace SSH configuration and authentication.

The original dated guides remain unchanged as full references and historical evidence. They are not the default linear reading path.

## Current demonstrated evidence

### Networking and namespaces

The learner has personally:

- created and rebuilt `aegis-test` and `aegis-peer` after restart;
- created and moved a veth pair;
- assigned `10.10.0.1/24` and `10.10.0.2/24`;
- brought loopback and veth interfaces up;
- inspected connected routes;
- diagnosed a missing-address case from `Network is unreachable`;
- verified ICMP connectivity;
- explained that network namespaces isolate networking rather than complete machines.

Current evidence level:

```text
reconstructed repeatedly using supplied documentation
one real changed case diagnosed with guidance
independent reconstruction from requirements not yet demonstrated
```

### Linux ownership and permissions

The learner has personally created and inspected:

- root-controlled server storage;
- learner-controlled client and authorization storage;
- modes `711`, `700`, `600`, `644`, and `755`;
- parent-directory traversal behavior;
- process identity versus file ownership;
- an unset `LAB_ROOT` path failure and its repair.

Current evidence level:

```text
concept explained and practiced
real permission/path issues interpreted
terminology and design transfer still need reinforcement
```

### SSH identities and trust directions

The learner has generated and inspected:

- a server Ed25519 host key pair;
- an authorized client Ed25519 key pair;
- a separate unauthorized test key pair;
- current public-key fingerprints;
- `authorized_keys`;
- a lab-specific `known_hosts`.

Taught distinction:

```text
server host key
→ client verifies server identity

client authentication key
→ server verifies possession of an authorized credential
```

Current evidence level:

```text
practiced with guidance
correct distinctions observed in real output
stable unaided explanation not yet assessed
```

### SSH server configuration and lifecycle

The learner has personally:

- created a lab-specific `sshd_config`;
- bound `sshd` to `10.10.0.2:22`;
- selected lab host-key and authorization paths;
- disabled password, keyboard-interactive, root-login, forwarding, and tunneling paths;
- used `ForceCommand /usr/bin/id` as bounded instructional scaffolding;
- validated configuration with `sshd -t`;
- diagnosed and repaired the missing `/run/sshd` prerequisite;
- started foreground `sshd` inside `aegis-peer`;
- observed the listener with `ss -ltnp`;
- verified that the listener survives individual connection teardown.

Current evidence level:

```text
built and rebuilt with substantial guidance
safe reconstruction runbook exists
independent configuration from requirements remains unproven
```

### Successful and failed authentication

The learner has observed and interpreted:

- first-use server fingerprint confirmation;
- automatic repeat verification from `known_hosts`;
- successful public-key authentication;
- execution of `/usr/bin/id` as `motafeq`;
- normal exit status `0`;
- a long-lived authenticated `ssh -N -T` transport;
- server-side authorized-key lookup, postponed public-key stage, accepted proof, and user-child creation;
- a valid but unauthorized key reaching the same server and failing with `Permission denied (publickey)`;
- matching server-side `Failed publickey` evidence and `[preauth]` closure;
- the distinction between an `authenticating user` and an authenticated user;
- isolation of the failure to authentication after network, TCP, SSH negotiation, and host trust succeeded.

Current evidence level:

```text
strong guided practical evidence
successful and negative paths correlated across client and server output
independent modified-case design remains pending
```

### Process, socket, and namespace correlation

The learner has observed and interpreted:

- both perspectives of one `ESTABLISHED` TCP endpoint pair;
- client ephemeral port versus stable server port;
- the listener `sshd` process;
- privileged per-connection `sshd`;
- authenticated user-side `sshd` child;
- the actual client `ssh` process and its privilege/namespace wrappers;
- network-namespace PID membership using `ip netns pids`;
- the fact that host `ps` sees all PIDs because no PID namespace was created;
- listener lifetime versus per-connection process lifetime;
- disappearance of both `ESTABLISHED` sockets and connection-specific processes after client teardown.

Current evidence level:

```text
completed with guided interpretation
cross-source model demonstrated
reduced-prompt explanation still required
```

### Packet, log, and teardown evidence

The learner has observed and interpreted:

- SYN, SYN-ACK, and ACK establishment;
- cleartext SSH identification strings;
- encrypted bidirectional traffic with visible metadata;
- client FIN followed by server FIN;
- foreground `sshd` success, failure, and disconnect logs;
- disappearance of both `ESTABLISHED` sockets;
- exit of per-connection server processes;
- survival of the listener after connection closure;
- the boundary between packet metadata and encrypted SSH content.

Current evidence level:

```text
packet, host-state, and server-log lifecycle correlated with guidance
complete guided namespace baseline available
independent concise correlation still unproven
```

## Honest current depth summary

| Area | Current evidence | Important limitation |
|---|---|---|
| Interface, address, route, namespace model | Rebuilt repeatedly with documentation | Needs independent changed-case reconstruction |
| Linux permission model | Practiced through real failures | Needs terminology and design transfer |
| SSH host and client identities | Correctly generated and distinguished | Needs stable unaided explanation |
| SSH authorization and trust files | Successful and negative cases correlated | Needs independent modified-case design |
| `sshd` configuration | Rebuilt and validated with runbook | Cannot yet derive safely from requirements alone |
| Process/socket/namespace correlation | Completed with guidance | Needs reduced-prompt teach-back |
| Packet/log lifecycle and visibility | Completed with guidance | Needs concise independent correlation |
| Namespace scenario baseline | Completed as a guided single-success/single-failure lifecycle | Formal repeated-count and time-bounded scenario remains pending |
| Docker transfer | Not yet begun | Must preserve scenario semantics while learning changed isolation/runtime mechanisms |
| Technical reporting | Strong assisted artifacts | Independent concise reporting still developing |

No area above is claimed as full practical independence.

## Learning-process controls

The teaching process must continue to enforce:

```text
main project objective
        ↓
why this step is needed
        ↓
question the action answers
        ↓
minimum complete concept
        ↓
command/code decomposition
        ↓
learner execution
        ↓
output meaning
        ↓
what it proves and does not prove
        ↓
next justified decision
        ↓
required depth: understand / recognize / defer
```

Avoid:

- long sequences whose relationship to the main objective is not visible;
- continuing evidence collection after its learning value becomes marginal;
- large unexplained command sequences during live teaching;
- treating the full historical guides as mandatory linear reading;
- using a security term without concrete actors and access decisions;
- treating a successful command as stable understanding;
- allowing documentation to replace the learner's own explanation;
- memorizing runtime-specific fingerprints, PIDs, ports, or indexes.

The governing contract is [Learning Preferences](../../LEARNING-PREFERENCES.md).

## Active learning gaps

1. Explain the namespace SSH endpoint, identity, process, socket, log, and teardown model with materially reduced prompting.
2. Reconstruct or modify the namespace scenario from requirements rather than only following the runbook.
3. Predict, introduce, diagnose, repair, and revalidate one bounded failure independently.
4. State the security and isolation limitations of network namespaces clearly.
5. Inspect the project’s Docker plan and identify invariants versus environment-specific mechanisms.
6. Reproduce the same authorized-success and unauthorized-failure semantics in Docker.
7. Compare process, network, filesystem, identity, logging, and teardown visibility between namespace and Docker implementations.
8. Define fixed counts, time bounds, start/end markers, separately maintained expected truth, abort conditions, and cleanup for the canonical repeated-failure experiment.
9. Transfer the stable scenario to VMs after Docker comparison.

## Next ownership gate

During the Docker transfer, the learner should be able to:

- describe the namespace baseline before translating it;
- distinguish scenario invariants from namespace-specific commands;
- explain what a container adds or changes compared with a network namespace;
- predict which processes, files, sockets, addresses, and logs should exist;
- identify what selected client, server-log, socket, process, and packet evidence proves and does not prove;
- diagnose at least one deliberately broken Docker layer from evidence;
- avoid copying private keys into the repository or image;
- state the security and isolation limitations of both variants.

Passing does not require memorizing every option. It requires a correct mental model, safe operation, evidence-based reasoning, and responsible recovery of details.

## Latest worklog

- [2026-07-18 — Namespace SSH authentication lifecycle closure](../worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md)

## Maintenance contract

- Update after meaningful demonstrated learning, a corrected misconception, a changed assistance level, or a new gap.
- Keep chronology in worklogs; keep this file concise and current.
- Preserve the detailed imported baseline in `LEARNER_PROFILE.md`.
- Preserve full historical study guides; use layered editions for primary study.
- Separate taught, guided practice, stable recall, independent application, diagnosis, and transfer.
- Never store credentials, private keys, passwords, sensitive personal data, malicious samples, or unbounded raw logs.
