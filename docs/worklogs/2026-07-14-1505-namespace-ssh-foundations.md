# 2026-07-14 — Namespace SSH foundations

## Session metadata

- **Started:** 2026-07-14 15:05 +02:00
- **Last updated:** 2026-07-15
- **Ended:** In progress
- **Status:** active
- **Objective:** Design, build, observe, and understand the controlled SSH client/server experiment across `aegis-test` and `aegis-peer`
- **Primary role:** Teacher
- **Working posture:** Guided discovery with embedded evidence checks
- **Starting revision:** `d7933bd`
- **Continues:** [Networking to namespaces](2026-07-14-2245-networking-to-namespaces.md)
- **Related guides:**
  - [SSH Key Identities and Permissions](../learning/study-guides/2026-07-14-ssh-key-identities-and-permissions.md)
  - [Namespace SSH Configuration, Connection, and Authentication](../learning/study-guides/2026-07-15-namespace-ssh-configuration-connection-and-authentication.md)
- **Related execution control:**
  - [Core Execution Map](<../plans/AegisLab — Core Execution Map.md>)
  - [Current Learning State](../learning/CURRENT_LEARNING_STATE.md)
- **Project state impact:** The namespace SSH control path is operational. The active milestone is now cross-source observability, not initial SSH setup.

## Live snapshot

- **Current topology:** `aegis-test` owns `veth-test` at `10.10.0.1/24`; `aegis-peer` owns `veth-peer` at `10.10.0.2/24`; both have connected `10.10.0.0/24` routes and successful ICMP exchange.
- **Server state:** Lab-specific `sshd` is running in foreground mode inside `aegis-peer`, using a temporary host identity and configuration bound only to `10.10.0.2:22`.
- **Authentication state:** The intended client key authenticated successfully as `motafeq`. A separate valid but unauthorized key reached and verified the same server but failed with `Permission denied (publickey)`.
- **Host verification state:** First-use fingerprint was manually compared and stored in lab `known_hosts`; a later connection matched automatically.
- **Long-lived transport:** `ssh -N -T` authenticated from `aegis-test` and remained open without requesting a shell, command, or pseudo-terminal.
- **Latest server evidence:** The foreground server reported client endpoint `10.10.0.1:54606`, server endpoint `10.10.0.2:22`, accepted authorized client fingerprint, and authenticated user child PID `305861`.
- **Next action:** While the connection remains open, inspect both namespace socket tables, the SSH process tree, and namespace PIDs; then correlate them with the client and server traces.

All names, PIDs, ports, fingerprints, files under `/tmp`, and running processes are runtime-specific and must be reinspected after restart or teardown.

## Scope and success criteria

This session covers the namespace-led SSH portion of the first Core slice:

- SSH client/server and TCP endpoint concepts;
- lab-only identity, authorization, trust, and configuration;
- configuration validation and bounded service startup;
- listener and connection evidence;
- server host verification;
- successful and failed public-key authentication;
- bounded command and long-lived transport behavior;
- process, socket, host-log, and selected packet correlation.

It excludes Docker and VM reproduction, the shared event pipeline, production SSH configuration, untrusted-code execution, and broad attack generation.

Success requires more than a working command. The learner must distinguish and interpret:

- network reachability;
- TCP listener and established connection state;
- SSH protocol establishment;
- server host identity;
- client credential authorization;
- proof of private-key possession;
- session requests and server policy;
- process and socket ownership;
- what client, server, host, and network observations prove or cannot prove.

## Mini-plan

- [x] Reinspect or rebuild the namespace topology and basic connectivity
- [x] Confirm the cross-environment roadmap remains namespaces, Docker, then VMs
- [x] Define the namespace SSH safety boundary
- [x] Inspect OpenSSH availability and clean port-22 baseline
- [x] Create lab-only server and client key identities
- [x] Create and verify a client authorization file
- [x] Create and validate a lab-specific `sshd_config`
- [x] Correct the authorization path and document the `StrictModes no` lab exception
- [x] Diagnose and repair the missing `/run/sshd` prerequisite
- [x] Start `sshd` only inside `aegis-peer`
- [x] Observe the namespace-bound listening socket
- [x] Establish the first controlled client connection
- [x] Verify first-use and repeat server host identity behavior
- [x] Complete successful public-key authentication
- [x] Demonstrate intentional unauthorized-key rejection
- [x] Establish a long-lived authenticated transport without a session channel
- [ ] Observe live `ESTABLISHED` sockets from both namespace perspectives
- [ ] Correlate listener, connection handler, authenticated child, and client processes
- [ ] Correlate successful and failed client events with server authentication records
- [ ] Capture selected SSH network evidence and explain its visibility limits
- [ ] Define and execute canonical normal and repeated-failure cases
- [ ] Introduce, diagnose, repair, and revalidate one bounded failure
- [ ] Record cleanup and final namespace handoff

## Checkpoint timeline

### 2026-07-14 — Topology and roadmap reverified

- **Observation:** Both namespaces and veth endpoints existed with connected routes and successful ICMP exchange.
- **Decision:** Preserve lead-then-converge: namespaces first, then the same scenario in Docker and VMs, followed by evidence-based comparison.
- **Learning decision:** Continue without a separate networking worksheet; use predictions, changed cases, output interpretation, and diagnosis as embedded assessment.

### 2026-07-14 — OpenSSH baseline inspected

- **Observation:** `ssh` and `sshd` were installed; the ordinary WSL SSH service was inactive; no port-22 listener existed in the default namespace or `aegis-peer`.
- **Interpretation:** The lab began from a clean service baseline and does not depend on the ordinary host SSH service.

### 2026-07-14 — Temporary identity boundary designed

- **Action:** Created separate root-controlled server storage and learner-controlled client storage under `/tmp/aegislab-namespace-ssh`.
- **Problem:** A root-owned top directory at mode `700` prevented the normal user from reaching or creating the client directory.
- **Resolution:** Changed the top directory to mode `711`; retained mode `700` on the client and server child directories.
- **Learning:** Access to a child depends on permissions across every parent path component.

### 2026-07-14 — Initial SSH identities created and studied

- **Action:** Generated a root-owned server Ed25519 host key and a `motafeq`-owned Ed25519 client key.
- **Evidence:** Private keys were mode `600`; public keys were mode `644`; fingerprints were distinct.
- **Interpretation:** Server host identity and client authentication identity are separate trust directions.

### 2026-07-15 — Runtime rebuilt after restart

- **Observation:** WSL restart removed named network namespaces and `/tmp` lab state.
- **Action:** Rebuilt namespaces, veth pair, addresses, routes, lab directories, identities, and authorization.
- **Evidence:** Two ICMP requests received two replies; new runtime fingerprints were recorded.
- **Interpretation:** Versioned documentation persisted while runtime state remained intentionally disposable.

### 2026-07-15 — Authorization path corrected

- **Initial state:** `authorized_keys` was placed inside the root-only server directory.
- **Review finding:** User-specific authorization should not depend on a path inaccessible to the target user.
- **Resolution:** Created `auth/authorized_keys` owned by `motafeq`, mode `600`, and updated `AuthorizedKeysFile`.
- **Additional decision:** Added `StrictModes no` because the temporary lab path is nested under broadly writable `/tmp`; recorded this as a lab exception, not a production default.

### 2026-07-15 — Server configuration validated

- **Action:** Created a lab-specific `sshd_config` bound to `10.10.0.2:22`, using only the lab host key and public-key authentication.
- **Initial validation:** `sshd -t` failed with `Missing privilege separation directory: /run/sshd`, exit status `255`.
- **Resolution:** Created root-owned `/run/sshd` mode `755`.
- **Final validation:** `sshd -t` returned exit status `0`.

### 2026-07-15 — Listener established inside `aegis-peer`

- **Action:** Started `sshd` with `ip netns exec aegis-peer`, foreground mode, stderr logging, and the lab configuration.
- **Evidence:** `ss -ltnp` inside `aegis-peer` showed `10.10.0.2:22` in `LISTEN`, owned by `sshd`.
- **Interpretation:** The process used the intended namespace network stack and exact local endpoint.

### 2026-07-15 — First controlled SSH connection succeeded

- **Client placement:** `ssh` ran inside `aegis-test` and as `motafeq`.
- **Server identity:** The presented fingerprint matched the current lab server host key and was stored after manual comparison.
- **Authentication:** Only `publickey` continued; the intended client fingerprint was offered, accepted, and authenticated.
- **Session behavior:** `ForceCommand /usr/bin/id` executed as `motafeq` and returned exit status `0`.
- **Learning:** The namespaces separate networking but share the WSL user database and group memberships.

### 2026-07-15 — Repeat host verification succeeded

- **Evidence:** The second connection reported that `10.10.0.2` was known and matched the stored Ed25519 host key at lab `known_hosts` line 1.
- **Interpretation:** First-use trust establishment and later automatic host identity verification are distinct.

### 2026-07-15 — Unauthorized key rejected intentionally

- **Action:** Generated a separate valid Ed25519 key and did not add its public key to `authorized_keys`.
- **Evidence:** TCP connected, SSH negotiation completed, and the host key matched. The unauthorized key was offered but not accepted; authentication ended with `Permission denied (publickey)`.
- **Interpretation:** Reachability, service identity, key validity, authorization, and private-key proof are separate conditions.

### 2026-07-15 — Long-lived authenticated transport established

- **Action:** Connected with `ssh -N -T`, the authorized client key, lab `known_hosts`, and a 15-second server-alive interval.
- **Client evidence:** TCP established, host identity matched, authorized key was accepted, and authentication completed using public key.
- **Session behavior:** No shell, command, pseudo-terminal, or session channel was requested; `ForceCommand /usr/bin/id` therefore did not run.
- **Server evidence:** The server logged connection from `10.10.0.1:54606` to `10.10.0.2:22`, key lookup at `authorized_keys:1`, pre-authentication postponement, final public-key acceptance, and user child PID `305861`.
- **Interpretation:** The connection is intentionally held open so the same transport can be observed in socket and process tables.

### 2026-07-15 — Project and learning controls reconciled

- **Problem:** `PROJECT_STATE.md` still claimed the stop line was before SSH, and the imported Learner Profile did not provide a concise current view.
- **Action:** Updated Project State; versioned the root Learning Preferences; added Current Learning State, Core Execution Map, and Deferred Ideas and Review Triggers; updated `AGENTS.md` to use them.
- **Decision:** Keep the accepted Core Charter stable. Add supporting execution and idea-control documents instead of expanding normative scope.
- **Interpretation:** Current evidence, milestone gates, teaching quality, and deferred opportunities now have distinct owners.

## Decisions and reasoning

- Do not start or reconfigure the ordinary WSL SSH service.
- Bind the lab server only to `10.10.0.2`.
- Use lab-specific host keys, client credentials, configuration, authorization, `known_hosts`, runtime files, and cleanup.
- Run the SSH client as `motafeq` after privileged namespace entry so client credential ownership remains meaningful.
- Disable password, keyboard-interactive, empty-password, PAM, and root login paths for the initial experiment.
- Use `ForceCommand /usr/bin/id` only as instructional scaffolding before the canonical normal-authentication case.
- Disable forwarding, tunneling, and unrelated environment features.
- Treat `StrictModes no` as a temporary `/tmp` lab exception only.
- Remember that a network namespace does not isolate the filesystem, users, process namespace, hostname, or kernel.
- Use `ssh -N -T` to keep an authenticated transport open without creating a session channel.
- Preserve canonical scenario semantics so Docker and VM variants can reproduce them later.
- Manual evidence understanding precedes automation.

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

### Commands appeared before prerequisite understanding

- **Symptom:** The learner stopped before key generation because directory and key commands had not been taught sufficiently.
- **Resolution:** Returned to first principles, taught variables, `/tmp`, ownership, permissions, `install`, `ssh-keygen`, public/private keys, and fingerprints before continuing.
- **Process change:** Use one concept and one practical action at a time, consistent with the versioned Learning Preferences.

## Learning and ownership

- **Learner actions:** Rebuilt topology, created directories and identities, verified permissions and fingerprints, created authorization and configuration files, validated `sshd`, started the namespace-bound server, ran successful and failed authentication, and established a long-lived transport.
- **Learner interpretation evidence:** Paused at unclear ownership and complexity boundaries; distinguished server and client identities; compared fingerprints; separated network, service, trust, and authorization layers; completed a deliberate negative case.
- **Assistance used:** Dependency sequencing, first-principles teaching, command construction, safety framing, output interpretation, design correction, bounded failure design, and documentation maintenance.
- **Current evidence level:** Strong guided practice; stable unaided reconstruction, live cross-source correlation, deliberate diagnosis, and transfer remain unproven.
- **Current gap:** Correlate the open transport across client output, server log, process tree, socket tables, and packet evidence with reduced guided interpretation.

## Verification

### Performed

- Namespace inventory, addresses, connected routes, and ICMP exchange
- Key ownership, modes, and fingerprints
- Authorization fingerprint comparison
- Exact numbered `sshd_config` inspection
- `sshd -t` failure diagnosis and successful revalidation
- Namespace-bound `LISTEN` socket observation
- First-use and repeat server host verification
- Successful public-key authentication
- Forced-command execution as `motafeq`
- Intentional unauthorized-key rejection
- Long-lived authenticated transport without shell, command, PTY, or session channel
- Foreground server log showing endpoint, key, authentication, and user-child evidence
- Repository state and learning-control reconciliation

### Not yet performed

- Live `ESTABLISHED` socket capture from both namespaces
- SSH parent/child/client process correlation
- Full server-log comparison for successful and failed attempts
- Packet capture and SSH visibility-limit explanation
- Deliberate host-key mismatch or another selected changed failure
- Canonical normal-authentication and repeated-failure run
- Docker and VM reproduction
- Final cleanup and namespace handoff

## Current runtime fingerprints

```text
server host key:
SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k

authorized client key:
SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE

unauthorized test key:
SHA256:6EIxVoa8IT5WnaM37dXXY+5bEAL+LlJ48a16xcHw6eI
```

These are runtime-specific public fingerprints, not secrets. They change when keys are regenerated.

## Final handoff

The namespace SSH control path is operational and a long-lived authenticated transport is available for observation. Continue by capturing both sides of the live TCP socket and the SSH process relationships before stopping either terminal. Then close the transport deliberately, observe teardown, and proceed to a narrow packet capture.

Do not move to Docker until the canonical namespace scenario, evidence checklist, bounded diagnosis, cleanup, and reduced-prompt learner explanation are complete.

## Corrections

- The initial authorization-file placement under the root-only server directory was replaced with a separate user-owned authorization directory.
- `StrictModes no` was added only for the temporary `/tmp` path and must not be generalized as a production recommendation.
- Fingerprints from the pre-restart study guide are historical; the current runtime fingerprints are recorded above.
- `ForceCommand /usr/bin/id` is bounded instructional scaffolding, not the final normal-login scenario.
- The stale pre-SSH Project State was replaced with the current observability milestone and explicit transition gates.
