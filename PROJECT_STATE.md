# AegisLab Project State

**Last meaningful update:** 2026-07-15  
**Current stage:** Core first learning slice — namespace SSH observability  
**Authority:** Non-normative handoff; current inspected evidence and canonical documents override this file

## Current objective

Finish and explain the namespace variant of the canonical two-endpoint SSH experiment before moving to Docker and virtual machines.

The immediate mechanism is one authenticated SSH transport from `aegis-test` to `aegis-peer`, correlated across:

```text
client debug output
        ↕
server sshd logs
        ↕
process relationships
        ↕
LISTEN and ESTABLISHED sockets
        ↕
selected network observations
```

The namespace variant leads. Docker and VM variants must later reproduce the same scenario semantics and evidence checklist before the first learning slice closes.

## Current position in the journey

```text
Project definition and Core Charter                         accepted
Namespace networking substrate                              built with guidance
SSH identities, authorization, and bounded configuration    built and explained
Namespace-bound SSH listener                                verified
Successful public-key authentication                        verified
First-use and repeat server-host verification               verified
Valid but unauthorized key rejection                        verified
Long-lived authenticated SSH transport                      established
Live process/socket/log/network correlation                 active next step
Canonical normal-login and repeated-failure scenario        pending
Docker reproduction                                         pending
VM reproduction                                             pending
Cross-environment comparison                                pending
Shared evidence and detection pipeline                      intentionally later
```

See the [Core Execution Map](<docs/plans/AegisLab — Core Execution Map.md>) for milestone gates and the [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>) for the governing sequence.

## Current observed environment and experiment evidence

- WSL2 with Ubuntu 24.04; OpenSSH client/server, `ip`, `ss`, `tcpdump`, systemd, and journaling are available.
- The ordinary WSL SSH service remained inactive; the experiment uses a lab-specific `sshd` process and configuration.
- `aegis-test` owns `veth-test` at `10.10.0.1/24`.
- `aegis-peer` owns `veth-peer` at `10.10.0.2/24`.
- Both namespaces have directly connected `10.10.0.0/24` routes and successful ICMP exchange.
- The lab server uses a temporary Ed25519 host identity and binds only to `10.10.0.2:22`.
- `ss` showed `10.10.0.2:22` in `LISTEN`, owned by `sshd`.
- The intended client key authenticated successfully as `motafeq` using public-key authentication.
- A first connection manually verified the server fingerprint and stored it in a lab-specific `known_hosts`; a second connection matched it automatically.
- `ForceCommand /usr/bin/id` produced bounded successful-session evidence and showed that the namespaces share the WSL user database.
- A separate valid but unauthorized key reached and verified the same server but failed with `Permission denied (publickey)`.
- A long-lived `ssh -N -T` transport authenticated successfully. The server reported client endpoint `10.10.0.1:54606`, server endpoint `10.10.0.2:22`, and an authenticated user child PID.

All namespace names, addresses, PIDs, ports, `/tmp` files, keys, fingerprints, and running processes are runtime-specific and temporary. Reinspect them before relying on this snapshot.

## Important design decisions now established

- Do not start or modify the ordinary WSL SSH service for this experiment.
- Bind the lab server only to the address owned by `aegis-peer`.
- Keep lab identities, authorization, configuration, and client trust state separate from normal host SSH state.
- Treat the current `ForceCommand /usr/bin/id` configuration as instructional scaffolding, not the final canonical normal-login case.
- Keep public-key authentication as the first controlled authentication mechanism; passwords and root login remain disabled.
- Network namespaces provide network isolation, not separate filesystems, users, hostnames, or kernels.
- Manual understanding and evidence correlation precede scenario automation.
- The same canonical scenario meaning must be preserved in namespaces, Docker, and VMs.

## Next checkpoint

The namespace observability checkpoint is complete when the learner can correlate and explain:

- the client and server views of one `ESTABLISHED` TCP four-tuple;
- the listening `sshd`, connection-handling process, and authenticated child relationship;
- successful and failed client output against the corresponding server logs;
- what host evidence proves versus what socket or packet evidence proves;
- connection establishment and closure using a narrow packet capture;
- the limitations created by SSH encryption and namespace-only isolation.

The namespace scenario checkpoint then additionally requires:

- a controlled normal authentication case;
- a documented repeated-failure case with explicit attempt count and time bounds;
- start/end markers and separately maintained expected truth;
- one bounded failure predicted, introduced, diagnosed, and repaired;
- cleanup and reconstruction instructions;
- a concise evidence checklist ready for Docker and VM reproduction.

## Active blockers and gaps

- Live `ESTABLISHED` socket and process-tree evidence has not yet been captured and interpreted.
- Successful and failed attempts have not yet been fully correlated with preserved server-side authentication records.
- Selected SSH packets have not yet been captured for this namespace scenario.
- The final normal-login semantics and repeated-failure contract are not yet defined.
- The current configuration uses a documented `StrictModes no` exception because authorization state is under `/tmp`; this must not silently become a production recommendation.
- Stable independent reconstruction and diagnosis have not yet been demonstrated; current evidence is guided practice.
- Docker Desktop must be started and integrated with the Ubuntu WSL distribution.
- A usable local Linux VM workflow must be selected and verified; Hyper-V remains the default candidate when suitable.

## Immediate next actions

1. While the authenticated `ssh -N -T` connection remains open, inspect both namespace socket tables and the SSH process tree.
2. Relate the socket endpoints and PIDs to the client debug trace and foreground `sshd` log.
3. Close the connection deliberately and observe process/socket teardown.
4. Capture one narrow SSH connection at the network level and explain the visibility boundary.
5. Define the canonical normal-authentication and repeated-failure cases, truth record, markers, abort conditions, and cleanup.
6. Run the complete namespace evidence checklist and one deliberate bounded failure.
7. Close and index the namespace worklog, update the current learning state, and then begin Docker integration.

## Learning and collaboration state

- The versioned teaching contract is [Learning Preferences](LEARNING-PREFERENCES.md).
- Current demonstrated evidence, assistance, and gaps are summarized in [Current Learning State](docs/learning/CURRENT_LEARNING_STATE.md).
- The historical imported foundation profile remains in [Learner Profile](docs/learning/LEARNER_PROFILE.md).
- Guided discovery remains the default for foundational work: orient, teach the minimum complete concept, predict, act, observe, interpret, correct, and record.
- Successful execution is not treated as stable recall or practical independence.

## Planning and idea control

- [Core Charter](<docs/plans/AegisLab — Core Charter v1.0.md>) defines the bounded Core.
- [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>) defines the governing sequence.
- [Core Execution Map](<docs/plans/AegisLab — Core Execution Map.md>) translates the plan into current milestone gates and artifacts.
- [Deferred Ideas and Review Triggers](<docs/plans/AegisLab — Deferred Ideas and Review Triggers.md>) preserves useful ideas without allowing scope creep.

## Authoritative references

- [Project Definition v1.0](<docs/AegisLab — Project Definition v1.0.md>)
- [Core Charter v1.0](<docs/plans/AegisLab — Core Charter v1.0.md>)
- [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>)
- [Governance, Safety, and Boundaries](docs/definition/governance-safety-and-boundaries.md)
- [Active namespace SSH worklog](docs/worklogs/2026-07-14-1505-namespace-ssh-foundations.md)

## Maintenance contract

- Update this file only after a meaningful decision, environment change, blocker change, or completed learning checkpoint.
- Keep it below 200 lines by moving durable detail to focused documents.
- Do not use it as a session diary, backlog, Git-status snapshot, or substitute for direct inspection.
- Do not store secrets, credentials, private keys, malicious samples, personal data, or unverified claims.
- If this file conflicts with current evidence or a canonical document, correct it as part of the active work.
