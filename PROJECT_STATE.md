# AegisLab Project State

**Last meaningful update:** 2026-07-17  
**Current stage:** Core first learning slice — namespace SSH scenario definition  
**Authority:** Non-normative handoff; current inspected evidence and canonical documents override this file

## Current objective

Finish the namespace form of the canonical two-endpoint SSH experiment before moving to Docker or virtual machines.

The observability mechanism is now understood across:

```text
client debug output
        ↕
server sshd logs
        ↕
process relationships
        ↕
LISTEN and ESTABLISHED sockets
        ↕
selected packet evidence
```

The immediate next work is to correlate preserved foreground server logs, then define and run the bounded normal-authentication and repeated-failure cases with explicit truth and timing.

## Current position in the journey

```text
Project definition and Core Charter                         accepted
Namespace networking substrate                              rebuilt and verified
SSH identities, authorization, and bounded configuration    rebuilt and verified
Namespace-bound SSH listener                                verified
Successful public-key authentication                        verified
Valid but unauthorized key rejection                        verified previously
Both ESTABLISHED socket perspectives                        verified
SSH process-tree and network-namespace PID correlation      verified
Connection teardown across sockets and processes            verified
TCP establishment and FIN teardown packet evidence          verified
SSH network visibility boundary                             explained
Full namespace SSH reconstruction runbook                   versioned
Server-log lifecycle correlation                            active next step
Canonical normal-login and repeated-failure scenario        pending
Docker reproduction                                         pending
VM reproduction                                             pending
Cross-environment comparison                                pending
Shared evidence and detection pipeline                      intentionally later
```

See the [Core Execution Map](<docs/plans/AegisLab — Core Execution Map.md>) for milestone gates and the [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>) for the governing sequence.

## Latest runtime snapshot

The 2026-07-16 runtime was rebuilt after WSL had removed all prior temporary state.

- `aegis-test` owns `veth-test` at `10.10.0.1/24`.
- `aegis-peer` owns `veth-peer` at `10.10.0.2/24`.
- Both namespaces have directly connected `10.10.0.0/24` routes and successful ICMP exchange.
- Temporary lab state is under `/tmp/aegislab-namespace-ssh`.
- The lab-specific `sshd` binds only to `10.10.0.2:22` and uses foreground logging.
- The ordinary WSL SSH service was not started or modified.
- The latest listener PID was `157590`; it remained after the client connection closed.
- No established SSH connection remained at the pause point.
- No per-connection `sshd` processes remained at the pause point.

Current runtime fingerprints:

```text
server host key:
SHA256:W4wUFw9uwvVnz7NrDfCLgWt+Um+N5NeK5hAHdUTU7xs

authorized client key:
SHA256:cZ3muVbww315suKD8+fpNBMRQJZTp64YpNPBALN6osY

unauthorized test key:
SHA256:rA1BVogOYbSx7j5IJ312AyNgWtcxaQ69DOc5QuVGmxg
```

All namespace names, addresses, interface indexes, PIDs, ports, fingerprints, `/tmp` files, and processes are runtime-specific. Reinspect them after any pause or restart.

## Latest completed evidence

One authenticated `ssh -N -T` connection used:

```text
client: 10.10.0.1:50420, ssh PID 158898
server: 10.10.0.2:22, sshd PIDs 158899 and 159032
listener: sshd PID 157590
```

Process ancestry was verified:

```text
sshd listener 157590
└── sshd: motafeq [priv] 158899
    └── sshd: motafeq 159032
```

Namespace membership was verified:

- `aegis-peer`: PIDs `157590`, `158899`, and `159032`.
- `aegis-test`: client wrapper PIDs `158896`, `158897`, and actual `ssh` PID `158898`.

After stopping only the client:

- both ESTABLISHED socket tables became empty;
- per-connection server PIDs `158899` and `159032` exited;
- listener PID `157590` and `LISTEN 10.10.0.2:22` remained.

A later captured connection used `10.10.0.1:57880 ↔ 10.10.0.2:22` and showed:

- SYN, SYN-ACK, ACK TCP establishment;
- cleartext SSH identification strings before encryption;
- bidirectional encrypted SSH traffic whose endpoints, timing, flags, and lengths remained visible;
- client FIN followed by server FIN during orderly teardown;
- no kernel capture drops.

Packet evidence did not reveal the authenticated username, accepted key, authentication result, command, or encrypted payload contents.

## Important design decisions

- Do not start or modify the ordinary WSL SSH service.
- Bind the lab server only to `10.10.0.2`.
- Keep host keys, client credentials, authorization, configuration, and `known_hosts` lab-specific.
- Do not commit private keys or copy temporary `/tmp` identity material into the repository.
- Keep public-key authentication as the initial mechanism; passwords and root login remain disabled.
- Treat `ForceCommand /usr/bin/id` as instructional scaffolding, not final normal-login semantics.
- Treat `StrictModes no` as a temporary `/tmp` exception, never as a production recommendation.
- Network namespaces isolate networking, not the filesystem, users, PID namespace, hostname, or kernel.
- Manual evidence understanding precedes scenario automation.
- Use the versioned reconstruction runbook after a restart; inspect first and rebuild only missing layers.

## Remaining namespace checkpoint work

- Correlate the most recent successful connection and teardown with foreground `sshd` log lines.
- Correlate successful and failed client events with preserved server authentication evidence.
- Define the canonical normal-authentication case.
- Define a fixed-count, time-bounded repeated-failure case.
- Add explicit start/end markers and separately maintained expected truth.
- Define abort conditions and cleanup.
- Introduce, diagnose, repair, and revalidate one bounded failure.
- Demonstrate reconstruction and explanation with reduced prompting.
- Produce the concise evidence checklist to reproduce in Docker and VMs.

## Resume sequence

1. Inspect whether the namespaces, `/tmp` lab material, and foreground `sshd` survived.
2. Use the [Namespace SSH Lab Reconstruction Runbook](docs/runbooks/namespace-ssh-lab-reconstruction.md) to rebuild only missing runtime layers.
3. Start the foreground lab `sshd` if it is not running.
4. Review the server log lines for the captured `10.10.0.1:57880` connection through disconnect.
5. Map each server log statement to client, socket, process, and packet evidence.
6. Define the canonical normal and repeated-failure experiment contract before generating new attempts.
7. Run the bounded cases with truth records, timestamps, abort conditions, and cleanup.

## Learning and collaboration state

- The versioned teaching contract is [Learning Preferences](LEARNING-PREFERENCES.md).
- Current demonstrated evidence, assistance, and gaps are summarized in [Current Learning State](docs/learning/CURRENT_LEARNING_STATE.md).
- Guided discovery remains the default: orient, teach the minimum complete concept, predict, act, observe, interpret, correct, and record.
- Today’s reconstruction and correlation were completed with stepwise guidance; this is demonstrated guided practice, not yet stable independent reconstruction.

## Authoritative references

- [Project Definition v1.0](<docs/AegisLab — Project Definition v1.0.md>)
- [Core Charter v1.0](<docs/plans/AegisLab — Core Charter v1.0.md>)
- [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>)
- [Core Execution Map](<docs/plans/AegisLab — Core Execution Map.md>)
- [Learning Preferences](LEARNING-PREFERENCES.md)
- [Namespace SSH Lab Reconstruction Runbook](docs/runbooks/namespace-ssh-lab-reconstruction.md)
- [Namespace SSH Foundations Worklog](docs/worklogs/2026-07-14-1505-namespace-ssh-foundations.md)
- [Namespace SSH Observability Handoff](docs/worklogs/2026-07-16-namespace-ssh-observability-handoff.md)

## Maintenance contract

- Update this file only after a meaningful decision, environment change, blocker change, or completed learning checkpoint.
- Keep it below 200 lines by moving durable detail to focused documents.
- Do not store secrets, credentials, private keys, malicious samples, personal data, or unverified claims.
- If this file conflicts with current evidence or a canonical document, correct it as part of the active work.