# 2026-07-18 — Namespace SSH authentication lifecycle closure

## Session metadata

- **Date:** 2026-07-18
- **Status:** completed guided session
- **Objective:** Reconstruct the disposable namespace SSH lab, correlate one successful authenticated connection across runtime evidence, compare it with a controlled unauthorized-key failure, and verify clean connection teardown
- **Primary role:** Teacher with guided learner execution
- **Starting procedure:** `docs/runbooks/namespace-ssh-lab-reconstruction.md`
- **Next project direction:** begin Docker transfer without changing the SSH scenario’s meaning

## Session result

The namespace SSH runtime was rebuilt after laptop shutdown by following the reconstruction runbook through Part IX. The learner then completed the current observability and authentication-lifecycle checks with guided interpretation.

The session established the following evidence chain:

```text
namespace network restored
        ↓
sshd listener verified
        ↓
authorized long-lived SSH transport established
        ↓
client/server socket views correlated
        ↓
listener and per-connection process ancestry interpreted
        ↓
network-namespace PID membership inspected
        ↓
successful server authentication logs correlated
        ↓
unauthorized key attempted as a controlled negative case
        ↓
client and server failure evidence correlated
        ↓
authorized connection deliberately closed
        ↓
ESTABLISHED sockets and per-connection processes disappeared
        ↓
listener remained available
```

## Current runtime evidence

Runtime-specific values below are historical evidence for this session only and must not be reused after reconstruction.

### Successful connection

- **Client endpoint:** `10.10.0.1:39864`
- **Server endpoint:** `10.10.0.2:22`
- **Requested account:** `motafeq`
- **Server decision:** `Accepted publickey`
- **User child observed:** PID `5625`

The server log showed the authorized Ed25519 key was found in the lab-specific `authorized_keys`, public-key authentication completed, and a user child was created.

### Controlled failed connection

- **Client endpoint:** `10.10.0.1:42146`
- **Server endpoint:** `10.10.0.2:22`
- **Requested account:** `motafeq`
- **Client identity:** deliberately unauthorized Ed25519 key
- **Client result:** `Permission denied (publickey)`
- **Server decision:** `Failed publickey`
- **Final phase:** connection closed during `[preauth]`
- **Authenticated user child:** none created

Only the client identity was intentionally changed. Networking, TCP reachability, SSH negotiation, and server-host verification still succeeded. This localized the failure to the public-key authentication/authorization layer.

### Teardown

After the long-lived authorized client was stopped deliberately:

- both client and server `ESTABLISHED` socket views disappeared;
- the client `ssh` process exited;
- the privileged per-connection `sshd` process exited;
- the authenticated user-side `sshd` process exited;
- the listener remained on `10.10.0.2:22`.

The server log reported a user-initiated disconnect for the successful connection.

## Learning demonstrated

With substantial explanation and prompting, the learner interpreted:

- that the SSH command explicitly requested the connection while Linux performed the TCP handshake and state transition;
- opposite client/server views of one TCP connection;
- the difference between a reusable listener and per-connection runtime state;
- the relationship among `ss`, `ps --forest`, `ip netns pids`, and foreground `sshd` logs;
- the distinction between server host identity and client authentication identity;
- the normal public-key sequence from authorized-key lookup through proof of private-key possession;
- the difference between `authenticating user` and authenticated user;
- how to locate the last successful layer before diagnosing a failure;
- why an unauthorized-key failure is not a network, listener, or host-trust failure;
- expected connection cleanup and listener survival.

## Honest assistance level

```text
runtime reconstruction:
  performed by learner using a detailed supplied runbook

command execution:
  performed by learner

command purpose, decomposition, and output interpretation:
  heavily guided

cross-source event model:
  demonstrated with guidance

independent reconstruction, diagnosis, and transfer:
  not yet demonstrated
```

Successful execution and detailed notes must not be treated as independent mastery.

## Teaching correction recorded

During the session, the learner correctly challenged a sequence of inspections that lacked a sufficiently visible overall objective.

Future teaching must keep this structure explicit for both commands and outputs:

1. why the action is needed for the current project objective;
2. what question it answers;
3. what each relevant command component means;
4. what the result says;
5. what the result proves and does not prove;
6. how it changes the next decision;
7. what must be understood now versus recognized or deferred.

Avoid continuing evidence collection after the learning value becomes marginal. Keep the main experiment model visible.

## Current practical model

```text
aegis-test
└── ssh client
    └── client-IP:ephemeral-port

        ESTABLISHED TCP/SSH transport

aegis-peer
└── sshd listener on 10.10.0.2:22
    └── privileged per-connection sshd
        └── authenticated-user sshd when authentication succeeds
```

Evidence responsibilities:

```text
ss
→ socket state, endpoints, and owners

ps --forest
→ process identity and ancestry

ip netns pids
→ network-namespace membership

foreground sshd logs
→ server authentication and disconnect decisions

client verbose output
→ client-visible negotiation, trust, identity offer, and final result
```

## Remaining learning gaps

- Explain the complete namespace SSH model with materially reduced prompting.
- Reconstruct or modify the scenario from requirements rather than only following the runbook.
- Predict and diagnose a deliberately broken layer independently.
- State namespace isolation limitations clearly during comparison with containers and VMs.
- Preserve the same success/failure semantics while transferring the scenario to Docker.
- Later formalize fixed counts, time bounds, markers, expected truth, abort conditions, and cleanup for the repeated-failure experiment.

## Handoff to Docker

The namespace implementation now provides a valid guided baseline for transfer:

```text
authorized key
→ authentication succeeds
→ authenticated user context appears

unauthorized key
→ TCP and SSH negotiation succeed
→ public-key authentication fails during preauth
→ no authenticated user context appears

client disconnect
→ connection-specific state disappears
→ listener remains
```

The Docker phase should begin by inspecting the project’s existing Docker plan and artifacts, identifying which behaviors must remain invariant and which isolation/runtime mechanisms will change. Do not begin by blindly translating namespace commands into a Dockerfile or Compose file.
