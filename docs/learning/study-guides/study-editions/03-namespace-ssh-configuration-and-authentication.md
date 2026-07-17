# Namespace SSH Configuration and Authentication — Layered Study Edition

**Role:** Primary study path for the AegisLab namespace SSH control path  
**Prerequisites:** [Networking and Namespace Foundations](01-networking-and-namespace-foundations.md), [SSH Identities and Linux Permissions](02-ssh-identities-and-permissions.md)  
**Full reference:** [Namespace SSH Configuration, Connection, and Authentication — Study Guide](../2026-07-15-namespace-ssh-configuration-connection-and-authentication.md)  
**Practical reconstruction:** [Namespace SSH Lab Reconstruction Runbook](../../../runbooks/namespace-ssh-lab-reconstruction.md)

## 1. Learning outcome

After this unit, you should be able to explain, configure, validate, and diagnose this bounded control path:

```text
network reachability
→ TCP listener
→ SSH protocol negotiation
→ server host verification
→ client public-key authorization
→ proof of private-key possession
→ bounded session policy
```

Each layer answers a different question. Evidence from one layer must not be used to claim success at another.

---

# Layer 1 — Required mental model

## 2. The seven-layer SSH path

### 1. Network reachability

Can the client namespace send IP traffic to `10.10.0.2` and receive replies?

Evidence example:

```text
successful ping
```

This does not prove an SSH listener exists.

### 2. TCP service availability

Is a process listening at `10.10.0.2:22`, and can the client establish TCP?

Evidence examples:

```text
ss shows LISTEN 10.10.0.2:22
client reports Connection established
```

This does not prove the server identity or client authorization.

### 3. SSH protocol negotiation

Did both endpoints exchange SSH versions and negotiate cryptographic transport parameters?

This creates an encrypted SSH transport. Detailed algorithm mathematics are deferred.

### 4. Server host identity verification

Does the presented server host key match the independently expected identity?

```text
server host key
→ client checks fingerprint or known_hosts
```

A host-key match does not authorize the client.

### 5. Client credential authorization

Is the offered client public key listed in the authorization policy for `motafeq`?

```text
auth/authorized_keys
```

### 6. Proof of private-key possession

Can the client create the required cryptographic proof using the matching private key?

The private key is not transmitted.

### 7. Session policy

After authentication, what is the client permitted to do?

The current instructional scaffold forces:

```text
/usr/bin/id
```

This is deliberately not an unrestricted shell and is not the final canonical M4 normal-authentication definition.

---

# Layer 2 — Authorization and trust state

## 3. `authorized_keys`

Role:

```text
public client identities permitted for a target account
```

Lab path:

```text
/tmp/aegislab-namespace-ssh/auth/authorized_keys
```

The authorized client public key is copied there. The client private key remains in `client/id_ed25519`.

Required validation:

```text
fingerprint of client/id_ed25519.pub
=
fingerprint of auth/authorized_keys
```

## 4. `known_hosts`

Role:

```text
expected server host identities
```

Lab path:

```text
/tmp/aegislab-namespace-ssh/client/known_hosts
```

First use:

```text
client has no stored identity
→ displays server fingerprint
→ learner compares independently
→ accepts only if exact match
```

Later use:

```text
server presents identity
→ client compares with stored known_hosts entry
→ matching identity continues automatically
```

Do not automatically bypass a host-key mismatch. A mismatch can mean a rebuilt server, stale trust state, wrong endpoint, or interception condition.

---

# Layer 3 — Lab server policy

## 5. Final instructional configuration

```text
Port 22
AddressFamily inet
ListenAddress 10.10.0.2

HostKey /tmp/aegislab-namespace-ssh/server/ssh_host_ed25519_key
PidFile /tmp/aegislab-namespace-ssh/server/sshd.pid

PubkeyAuthentication yes
AuthorizedKeysFile /tmp/aegislab-namespace-ssh/auth/authorized_keys
StrictModes no

PasswordAuthentication no
KbdInteractiveAuthentication no
PermitEmptyPasswords no
PermitRootLogin no
UsePAM no

AllowUsers motafeq

ForceCommand /usr/bin/id

X11Forwarding no
AllowTcpForwarding no
GatewayPorts no
PermitTunnel no
PermitUserEnvironment no

LogLevel VERBOSE
```

## 6. Responsibility groups

### Listener boundary

```text
AddressFamily inet
ListenAddress 10.10.0.2
Port 22
```

The listener is restricted to the server namespace IPv4 endpoint.

### Server identity

```text
HostKey .../ssh_host_ed25519_key
```

The lab server uses only the temporary host identity, not ordinary system host keys.

### Authentication boundary

```text
PubkeyAuthentication yes
AuthorizedKeysFile ...
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin no
AllowUsers motafeq
```

The experiment is intentionally limited to one user and one authentication family.

### Session boundary

```text
ForceCommand /usr/bin/id
```

Successful authentication does not grant an unrestricted shell.

### Secondary-capability boundary

Forwarding, tunneling, X11 forwarding, and user environment injection are disabled because they are outside the active mechanism.

## 7. `StrictModes no`

This is a lab-specific exception required because the authorization path is nested under `/tmp`, which is broadly writable.

It does not disable ordinary Linux permissions or public-key cryptography.

It must not be generalized into a production recommendation. A production design should normally use conventionally secured paths and retain strict checking.

---

# Layer 4 — Minimum practical mechanism

## 8. Create authorization

```bash
install \
  -o motafeq \
  -g motafeq \
  -m 600 \
  "$LAB_ROOT/client/id_ed25519.pub" \
  "$LAB_ROOT/auth/authorized_keys"
```

Validate ownership, mode, and matching fingerprint before configuring the server.

## 9. Write and inspect configuration

Use the exact final configuration from the reconstruction runbook.

Inspect the resulting file:

```bash
sudo nl -ba "$LAB_ROOT/server/sshd_config"
```

Do not validate a configuration that has not been inspected.

## 10. Ensure runtime prerequisite

```bash
sudo install -d -o root -g root -m 755 /run/sshd
```

`/run/sshd` is a runtime prerequisite used by the installed OpenSSH server. It is not private lab identity state.

## 11. Validate without starting

```bash
sudo /usr/sbin/sshd \
  -t \
  -f "$LAB_ROOT/server/sshd_config"

echo "exit status: $?"
```

Required result:

```text
exit status: 0
```

This proves the selected configuration and required files passed `sshd` validation. It does not prove the address can be bound or authentication works.

## 12. Start the server in `aegis-peer`

```bash
sudo ip netns exec aegis-peer \
  /usr/sbin/sshd \
  -D \
  -e \
  -f "$LAB_ROOT/server/sshd_config"
```

```text
-D  stay in foreground
-e  log to terminal
-f  use selected configuration
```

Keep this terminal open.

## 13. Verify listener

```bash
sudo ip netns exec aegis-peer ss -ltnp
```

Required decisive evidence:

```text
LISTEN ... 10.10.0.2:22 ... sshd
```

The peer column may show `0.0.0.0:*`; that does not mean the listener is bound to every local address. The local column is decisive.

## 14. Connect as the normal client user

```bash
sudo ip netns exec aegis-test \
  sudo -u motafeq \
  ssh \
  -v \
  -i "$LAB_ROOT/client/id_ed25519" \
  -o IdentitiesOnly=yes \
  -o UserKnownHostsFile="$LAB_ROOT/client/known_hosts" \
  motafeq@10.10.0.2
```

Responsibilities:

- privileged namespace entry;
- actual client runs as `motafeq`;
- only the intended private key is offered;
- trust state stays in the lab-specific `known_hosts`.

On first use, independently inspect the current server public-key fingerprint and accept only an exact match.

---

# Layer 5 — Reading decisive evidence

## `Connection established`

Proves:

- TCP reached and connected to the listener.

Does not prove:

- expected server identity;
- client authorization;
- successful authentication.

## Host key prompt

Proves:

- an SSH server responded;
- no trusted identity is currently stored for this endpoint in the selected file.

Does not prove:

- the presented identity is expected;
- authentication failed.

## `Host ... is known and matches`

Proves:

- the presented host identity matches the stored trust record.

Does not prove:

- the client key is authorized.

## `Offering public key`

Proves:

- the client proposed that public identity.

Does not prove:

- the server accepted it.

## `Server accepts key`

Proves:

- the offered public identity matched the authorization policy sufficiently to continue proof.

Final authentication still requires proof of private-key possession.

## `Authenticated ... using "publickey"`

Proves:

- the public identity was authorized;
- the client proved possession of the corresponding private key;
- server policy permitted the requested account.

## `Permission denied (publickey)` after host verification

Proves:

- network, TCP, SSH negotiation, and server host verification succeeded;
- no permitted public-key authentication completed.

It is not a routing failure.

## `/usr/bin/id` output and exit status `0`

Proves:

- authentication completed;
- a session channel was accepted;
- the forced command ran as the shown Linux account;
- the command completed successfully.

Does not prove:

- unrestricted shell access;
- separate filesystem or user namespace isolation.

---

# Layer 6 — Normal and negative cases

## Authorized case

Expected sequence:

```text
TCP connects
→ server host identity matches
→ authorized public key offered
→ server accepts key
→ client proves private-key possession
→ authentication succeeds
→ forced /usr/bin/id runs
```

## Unauthorized-key case

The test identity is valid but absent from `authorized_keys`.

Expected sequence:

```text
TCP connects
→ server host identity matches
→ unauthorized public key offered
→ server does not accept it
→ no other method remains
→ Permission denied (publickey)
```

The negative case isolates authorization while keeping network, listener, protocol, and host identity constant.

---

# Layer 7 — Active recall

Close this file before answering.

1. Why does successful ping not prove SSH works?
2. What does `LISTEN 10.10.0.2:22` prove?
3. What is the difference between `known_hosts` and `authorized_keys`?
4. Why is the first-use fingerprint prompt not an authentication failure?
5. What additional fact is established by `Authenticated ... using "publickey"` beyond `Server accepts key`?
6. Why does an unauthorized key still reach host verification?
7. Why does `ForceCommand /usr/bin/id` not represent an unrestricted shell?
8. Why must `StrictModes no` remain a lab exception?
9. Why does the actual SSH client run as `motafeq` after namespace entry?
10. Which evidence layer should be inspected first after `Connection refused`?

## Required layer explanation

Explain the authorized connection from destination selection through forced-command completion, naming the evidence that supports each transition.

---

# Layer 8 — Changed-case diagnosis

## Case A — `Missing privilege separation directory: /run/sshd`

Affected layer:

```text
server runtime prerequisite
```

It is not evidence that the SSH directives are syntactically wrong. Create the required directory, then rerun full validation.

## Case B — `Connection refused`

Strong initial interpretation:

```text
destination was reachable enough to reject the TCP attempt
but no accepting listener existed at that endpoint
```

Inspect server process and listener state before changing keys or authorization.

## Case C — Host identity changed

Do not disable checking automatically.

Inspect:

- current server public-key fingerprint;
- current `known_hosts` entry;
- whether the server identity was intentionally regenerated;
- whether the expected endpoint is answering.

## Case D — `Permission denied (publickey)`

Inspect in dependency order:

```text
requested account
→ selected client identity
→ offered fingerprint
→ authorized_keys fingerprint/content
→ server authentication log
```

Do not rebuild networking when TCP and host verification already succeeded.

---

# Layer 9 — Mastery gate

This unit is stable enough for the current project when you can:

- draw and explain all seven SSH layers;
- distinguish `known_hosts` and `authorized_keys`;
- explain every directive group in the bounded configuration;
- validate before starting the listener;
- interpret fresh client and listener output;
- predict the authorized and unauthorized-key cases;
- diagnose one bounded failure without changing unrelated layers;
- reconstruct the control path using documentation with materially reduced guidance;
- state the security and isolation limitations of the namespace implementation.

This gate does not require memorizing algorithm negotiation output, fingerprints, PIDs, or every OpenSSH option.

---

# Optional reference topics

Use the full guide only when needed for:

- the historical incorrect authorization placement and its correction;
- detailed here-document and `tee` explanation;
- the historical `sed -i` repair;
- full algorithm-negotiation output;
- historical fingerprints and PIDs;
- complete first and second client traces;
- extended failure tables;
- the original session chronology.

The correct final design should be learned first. Historical corrections remain available as evidence and troubleshooting cases.