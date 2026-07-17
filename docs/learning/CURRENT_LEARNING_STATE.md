# AegisLab Current Learning State

**Last meaningful update:** 2026-07-17  
**Status:** Active evidence-aware learning handoff  
**Authority:** Non-normative; current observed performance and canonical project documents override this file  
**Historical baseline:** [Learner Profile](LEARNER_PROFILE.md)

## Purpose

This file gives a concise current view of demonstrated learning, assistance level, active gaps, and the next ownership gate.

Do not treat successful commands, polished documentation, or one guided reconstruction as evidence of independent mastery.

## Current project-learning phase

```text
AegisLab Core first learning slice
        ↓
namespace SSH observability closure
        ↓
canonical namespace scenario definition
```

The learner has built, rebuilt, and observed the namespace SSH control path with substantial guided teaching. Process, socket, namespace-membership, packet-establishment, and teardown correlation have been completed. The immediate unfinished M3 work is preserved server-log lifecycle correlation; M4 scenario definition follows.

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
- observed the listener with `ss -ltnp`.

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
- a valid but unauthorized key failing with `Permission denied (publickey)` after TCP and host verification;
- a long-lived authenticated `ssh -N -T` transport.

Current evidence level:

```text
strong guided practical evidence
layer distinctions understood in observed cases
independent modified-case design remains pending
```

### Process, socket, and namespace correlation

The learner has observed and interpreted:

- both perspectives of one `ESTABLISHED` TCP four-tuple;
- the listener `sshd` process;
- privileged per-connection `sshd`;
- authenticated user-side `sshd` child;
- the actual client `ssh` process and its wrappers;
- network-namespace PID membership using `ip netns pids`;
- the fact that host `ps` sees all PIDs because no PID namespace was created;
- listener lifetime versus per-connection process lifetime.

Current evidence level:

```text
completed with guided interpretation
cross-source model demonstrated
reduced-prompt explanation still required
```

### Packet evidence and teardown

The learner has observed and interpreted:

- SYN, SYN-ACK, and ACK establishment;
- cleartext SSH identification strings;
- encrypted bidirectional traffic with visible metadata;
- client FIN followed by server FIN;
- disappearance of both ESTABLISHED sockets;
- exit of per-connection server processes;
- survival of the listener after connection closure;
- the boundary between packet metadata and encrypted SSH content.

Current evidence level:

```text
packet and host-state lifecycle correlated with guidance
server-log lifecycle correlation remains unfinished
```

## Honest current depth summary

| Area | Current evidence | Important limitation |
|---|---|---|
| Interface, address, route, namespace model | Rebuilt repeatedly with documentation | Needs independent changed-case reconstruction |
| Linux permission model | Practiced through real failures | Needs terminology and design transfer |
| SSH host and client identities | Correctly generated and distinguished | Needs stable unaided explanation |
| SSH authorization and trust files | Successful and negative cases observed | Needs independent modified-case design |
| `sshd` configuration | Rebuilt and validated with runbook | Cannot yet derive safely from requirements alone |
| Process/socket correlation | Completed with guidance | Needs reduced-prompt teach-back |
| Packet lifecycle and visibility | Completed with guidance | Needs correlation with preserved server logs |
| Canonical scenario design | Not yet completed | Must define truth, markers, counts, bounds, and cleanup |
| Technical reporting | Strong assisted artifacts | Independent concise reporting still developing |

No area above is claimed as full practical independence.

## Learning-process controls

The teaching process must continue to enforce:

```text
problem and responsibility
        ↓
minimum complete concept
        ↓
prediction
        ↓
one practical action
        ↓
output interpretation
        ↓
next justified action
```

Avoid:

- large unexplained command sequences during live teaching;
- treating the full historical guides as mandatory linear reading;
- using a security term without concrete actors and access decisions;
- treating a successful command as stable understanding;
- allowing documentation to replace the learner's own explanation;
- memorizing runtime-specific fingerprints, PIDs, ports, or indexes.

The governing contract is [Learning Preferences](../../LEARNING-PREFERENCES.md).

## Active learning gaps

1. Correlate successful connection and teardown with complete foreground `sshd` log lines.
2. Explain the completed process/socket/packet lifecycle with materially reduced prompting.
3. Define the canonical normal-authentication case.
4. Define a fixed-count, time-bounded repeated unauthorized-key case.
5. Add explicit start/end markers and separately maintained expected truth.
6. Define abort conditions and cleanup.
7. Predict, introduce, diagnose, repair, and revalidate one bounded failure.
8. Reconstruct the core namespace scenario with reduced guidance.
9. Create the layered M3 observability study edition after server-log correlation closes the unit.
10. Transfer the stable scenario to Docker and then VMs without changing its meaning.

## Next ownership gate

Before the namespace variant is understood enough to transfer, the learner should be able to:

- draw the two endpoints and one SSH TCP four-tuple;
- explain `ssh`, listener `sshd`, per-connection `sshd`, host key, client key, `known_hosts`, and `authorized_keys`;
- identify what selected client, server-log, socket, process, and packet evidence proves and does not prove;
- predict one changed case before execution;
- diagnose one deliberately broken layer from evidence;
- run or reconstruct the scenario with materially less step-by-step instruction;
- state the security and isolation limitations of the namespace variant.

Passing does not require memorizing every option. It requires a correct mental model, safe operation, evidence-based reasoning, and responsible recovery of details.

## Maintenance contract

- Update after meaningful demonstrated learning, a corrected misconception, a changed assistance level, or a new gap.
- Keep chronology in worklogs; keep this file concise and current.
- Preserve the detailed imported baseline in `LEARNER_PROFILE.md`.
- Preserve full historical study guides; use layered editions for primary study.
- Separate taught, guided practice, stable recall, independent application, diagnosis, and transfer.
- Never store credentials, private keys, passwords, sensitive personal data, malicious samples, or unbounded raw logs.