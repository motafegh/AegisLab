# 2026-07-14 — Namespace SSH foundations

## Session metadata

- **Started:** 2026-07-14 15:05 +02:00
- **Last updated:** 2026-07-15
- **Ended:** In progress
- **Status:** active
- **Objective:** Design, build, and understand the controlled SSH client/server experiment across `aegis-test` and `aegis-peer`
- **Primary role:** Teacher
- **Working posture:** Guided discovery with embedded evidence checks
- **Starting revision:** `d7933bd`
- **Continues:** [Networking to namespaces](2026-07-14-2245-networking-to-namespaces.md)
- **Related guides:**
  - [SSH Key Identities and Permissions](../learning/study-guides/2026-07-14-ssh-key-identities-and-permissions.md)
  - [Namespace SSH Configuration, Connection, and Authentication](../learning/study-guides/2026-07-15-namespace-ssh-configuration-connection-and-authentication.md)
- **Project state impact:** The learner continued without a standalone assessment; understanding is being evaluated through prediction, command execution, output interpretation, controlled failure, and evidence correlation.

## Live snapshot

- **Current topology:** `aegis-test` owns `veth-test` at `10.10.0.1/24`; `aegis-peer` owns `veth-peer` at `10.10.0.2/24`; both have connected `10.10.0.0/24` routes and successful ICMP exchange.
- **Server state:** Lab-specific `sshd` is running in the foreground inside `aegis-peer`, using the temporary configuration and host key. `ss` showed `10.10.0.2:22` in `LISTEN`, owned by `sshd`.
- **Authentication state:** The intended client key authenticated successfully as `motafeq`; `ForceCommand /usr/bin/id` executed and returned exit status `0`. A separate valid but unauthorized key reached the same server and failed with `Permission denied (publickey)`.
- **Host verification state:** First-use fingerprint was manually compared and stored in the lab `known_hosts`; the second connection matched it automatically.
- **Latest evidence:** Client-side successful and failed authentication traces, including exact server and client fingerprints.
- **Next action:** Correlate successful and failed client traces with server-terminal logs, process relationships, and live socket evidence.

## Scope and success criteria

This session covers the namespace-led SSH portion of the first Core slice: SSH client/server concepts, lab-only identity and authorization files, safe server configuration, configuration validation, process and listener evidence, server host verification, public-key authentication, a bounded forced command, and a controlled authorization failure.

It excludes Docker and VM reproduction, repeated abuse generation, the shared event pipeline, production SSH configuration, and untrusted-code execution.

Success requires more than a working command. The learner must distinguish and interpret:

- network reachability;
- TCP listener availability;
- SSH protocol establishment;
- server host identity;
- client credential authorization;
- private-key possession proof;
- session policy and command execution;
- what a failed authentication does and does not prove.

## Mini-plan

- [x] Reinspect or rebuild the namespace topology and basic connectivity
- [x] Confirm the cross-environment roadmap remains namespaces, Docker, then VMs
- [x] Define the namespace SSH safety boundary and scenario contract
- [x] Inspect OpenSSH client/server availability and existing port-22 state
- [x] Create lab-only server and client key identities
- [x] Create and verify a client authorization file
- [x] Create a lab-specific `sshd_config`
- [x] Correct the authorization path and document the `StrictModes no` lab exception
- [x] Validate configuration without starting the server
- [x] Diagnose and repair the missing `/run/sshd` prerequisite
- [x] Start `sshd` only inside `aegis-peer`
- [x] Observe the namespace-bound listening socket
- [x] Establish the first controlled client connection
- [x] Verify first-use and repeat server host identity behavior
- [x] Complete successful public-key authentication
- [x] Demonstrate intentional unauthorized-key rejection
- [ ] Correlate server logs with successful and failed client events
- [ ] Observe live `ESTABLISHED` socket and `sshd` process relationships
- [ ] Record cleanup and final namespace handoff

## Checkpoint timeline

### 2026-07-14 15:05 — Session resumed and topology reverified

- **Observation:** Both namespaces and veth endpoints persisted, connected routes remained present, and two ICMP requests received two replies.
- **Interpretation:** The network prerequisite was operational and could support the SSH experiment.

### 2026-07-14 15:10 — Cross-environment plan clarified

- **Observation:** The learner asked whether Docker and the installed VM application would be ignored.
- **Action:** Reinspected the active Core Charter and Initial Journey Plan.
- **Interpretation:** The project uses lead-then-converge: namespace SSH first, then the same scenario in Docker and separate VMs, followed by comparison.

### 2026-07-14 15:15 — Assessment integrated into practical work

- **Decision:** The learner requested continuation without a standalone networking assessment.
- **Interpretation:** Continue with SSH while using predictions, fresh output interpretation, and bounded diagnosis as embedded evidence. Do not mark independent mastery solely from reported study completion.

### 2026-07-14 — OpenSSH baseline inspected

- **Observation:** `ssh` and `sshd` were installed; the ordinary host SSH service was inactive; no port-22 listener existed in the default namespace or `aegis-peer`.
- **Interpretation:** The lab began from a clean service baseline and did not depend on the host SSH service.

### 2026-07-14 — Temporary identity boundary designed

- **Action:** Created separate root-controlled server storage and learner-controlled client storage under `/tmp/aegislab-namespace-ssh`.
- **Problem:** A root-owned top directory at mode `700` prevented the normal user from reaching or creating the client directory.
- **Resolution:** Changed the top directory to mode `711`, preserving traversal without general listing, and retained mode `700` on the client and server child directories.
- **Learning:** Directory access depends on suitable permissions on every parent path component.

### 2026-07-14 — Initial key identities created and studied

- **Action:** Generated a root-owned server Ed25519 host key and a `motafeq`-owned Ed25519 client key.
- **Evidence:** Private keys were mode `600`; public keys were mode `644`; fingerprints were distinct.
- **Interpretation:** Server host identity and client authentication identity are separate trust directions.

### 2026-07-15 — Runtime rebuilt after restart

- **Observation:** WSL restart removed named network namespaces and `/tmp` lab state.
- **Action:** Rebuilt namespaces, veth pair, addresses, routes, lab directories, server host key, client key, and authorization file.
- **Evidence:** Two ICMP requests received two replies; current fingerprints were recorded.
- **Interpretation:** Repository documentation persisted while runtime state remained intentionally disposable.

### 2026-07-15 — Authorization path corrected

- **Initial state:** `authorized_keys` was placed inside the root-only server directory.
- **Review finding:** A user-specific authorization list should not depend on a path inaccessible to the target account.
- **Resolution:** Created `auth/authorized_keys` owned by `motafeq`, mode `600`, and updated `AuthorizedKeysFile`.
- **Additional decision:** Added `StrictModes no` because the lab path is nested under broadly writable `/tmp`; documented this as a temporary lab exception, not a production default.

### 2026-07-15 — Server configuration validated

- **Action:** Created a lab-specific `sshd_config` bound to `10.10.0.2:22`, using only the lab host key and public-key authentication.
- **Initial validation:** `sshd -t` failed with `Missing privilege separation directory: /run/sshd`, exit status `255`.
- **Resolution:** Created root-owned `/run/sshd` mode `755`.
- **Final validation:** `sshd -t` returned exit status `0`.

### 2026-07-15 — Listener established inside `aegis-peer`

- **Action:** Started `sshd` with `ip netns exec aegis-peer`, foreground mode, stderr logging, and the lab configuration.
- **Evidence:** `ss -ltnp` inside `aegis-peer` showed `10.10.0.2:22` in `LISTEN`, owned by `sshd`.
- **Interpretation:** The process was using the intended namespace networking and exact local endpoint.

### 2026-07-15 — First controlled SSH connection succeeded

- **Client placement:** `ssh` ran inside `aegis-test` and as user `motafeq`.
- **Server identity:** The presented host fingerprint matched the current lab server key and was stored in the lab `known_hosts` after manual comparison.
- **Authentication:** Only `publickey` was offered; the intended client fingerprint was offered, accepted, and authenticated.
- **Session behavior:** `ForceCommand /usr/bin/id` executed as `motafeq` and returned exit status `0`.
- **Learning:** Network namespaces separated networking but shared the WSL user database and group memberships.

### 2026-07-15 — Repeat host verification succeeded

- **Evidence:** The second connection reported that `10.10.0.2` was known and matched the stored Ed25519 host key at lab `known_hosts` line 1.
- **Interpretation:** First-use trust establishment and later automatic host identity verification are distinct stages.

### 2026-07-15 — Unauthorized key rejected intentionally

- **Action:** Generated a separate valid Ed25519 key and did not add its public key to `authorized_keys`.
- **Evidence:** TCP connected, SSH negotiation completed, and the server host key matched. The unauthorized key was offered, but no `Server accepts key` line appeared; the attempt ended with `Permission denied (publickey)`.
- **Interpretation:** Reachability, service identity, key validity, and authorization are separate conditions.

## Decisions and reasoning

- Do not start or reconfigure the WSL host's ordinary SSH service.
- Bind the lab server only to `10.10.0.2`.
- Use lab-specific host keys, client credentials, configuration, authorization, known-hosts, PID/runtime files, and cleanup.
- Run the SSH client as `motafeq` after privileged namespace entry so client credential ownership remains meaningful.
- Disable password, keyboard-interactive, empty-password, PAM, and root login paths for this first experiment.
- Use `ForceCommand /usr/bin/id` before allowing a normal shell.
- Disable forwarding, tunneling, and unrelated environment features.
- Treat `StrictModes no` as a temporary `/tmp` lab exception only.
- Remember that a network namespace does not isolate the filesystem, users, process namespace, or kernel.
- Preserve the canonical scenario semantics so Docker and VM variants can reproduce them later.

## Problems and resolutions

### Parent directory blocked normal-user client storage

- **Symptom:** `Permission denied` when creating the client directory below a root-owned mode-`700` top directory.
- **Resolution:** Top directory mode changed to `711`; child directories remained mode `700`.

### Authorization file placed under root-only server path

- **Risk:** Target-user authorization access and path policy were poorly modeled.
- **Resolution:** Moved the authorization copy to `auth/authorized_keys`, owned by `motafeq`, and updated the configuration.

### Missing `StrictModes no`

- **Symptom:** Numbered configuration inspection showed the intended directive was absent.
- **Resolution:** Inserted it with `sed -i` and reinspected the exact file.

### Missing `/run/sshd`

- **Symptom:** `sshd -t` failed with exit status `255`.
- **Resolution:** Created `/run/sshd` as `root:root`, mode `755`; validation then returned `0`.

## Learning and ownership

- **Learner actions:** Rebuilt the topology, created directories and keys, verified ownership and fingerprints, created authorization and configuration files, validated `sshd`, started the namespace-bound server, executed successful and failed client connections, and supplied complete outputs.
- **Learner interpretation evidence:** Identified ownership-boundary confusion and paused for first-principles explanation before continuing; distinguished server and client identities; followed fingerprint comparisons; completed a deliberate unauthorized-key experiment.
- **Assistance used:** Dependency sequencing, concept explanation, command construction, safety framing, output interpretation, and bounded failure design.
- **Current gap:** Correlate client-visible events with server logs, process relationships, and live established sockets without relying on guided interpretation alone.

## Verification

### Performed

- Namespace inventory, addresses, connected routes, and ICMP exchange
- Key ownership, modes, and fingerprints
- Authorization file fingerprint comparison
- Exact numbered `sshd_config` inspection
- `sshd -t` failure diagnosis and successful revalidation
- Namespace-bound `LISTEN` socket observation
- First-use server fingerprint verification
- Repeat known-host verification
- Successful public-key authentication
- Forced-command execution as `motafeq`
- Intentional unauthorized-key rejection

### Not yet performed

- Server-log comparison for successful and failed attempts
- Live `ESTABLISHED` socket capture during an open session
- `sshd` parent/child process correlation
- Deliberate host-key mismatch experiment
- Normal interactive login for the canonical scenario
- Docker and VM reproduction
- Final cleanup and handoff

## Current fingerprints

These are runtime-specific evidence from the post-restart lab:

```text
server host key:
SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k

authorized client key:
SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE

unauthorized test key:
SHA256:6EIxVoa8IT5WnaM37dXXY+5bEAL+LlJ48a16xcHw6eI
```

## Final handoff

The namespace SSH service is operational and has demonstrated both successful and failed public-key authentication. Continue by capturing server-side logs and live operating-system evidence for the same events. Do not move to Docker until the learner can correlate the client trace, server trace, process model, and socket model for the namespace implementation.

## Corrections

- The initial authorization-file placement under the root-only server directory was replaced with a separate user-owned authorization directory.
- `StrictModes no` was added only for the temporary `/tmp` path and must not be generalized as a production recommendation.
- Fingerprints from the pre-restart guide are historical; the current runtime fingerprints are recorded above.
