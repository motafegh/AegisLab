# Namespace SSH Configuration, Connection, and Authentication — Study Guide

**Date:** 2026-07-15  
**Status:** Learner-facing study guide  
**Project position:** Namespace-led SSH Core slice  
**Prerequisite guide:** [SSH Key Identities and Permissions](2026-07-14-ssh-key-identities-and-permissions.md)  
**Scope:** Client authorization, lab-specific `sshd` configuration, validation, namespace-bound listening, SSH negotiation, host verification, successful public-key authentication, forced-command execution, and controlled authentication failure

---

## 1. Purpose

This guide records the next complete learning unit in the AegisLab namespace SSH experiment.

The previous guide established two independent key pairs:

```text
server host key
→ lets the client verify the SSH server

client authentication key
→ lets the server verify client possession of an authorized credential
```

This guide answers the next questions:

```text
How does the server authorize the client public key?
How is sshd configured without changing the ordinary host SSH service?
How do we prove sshd is listening in the intended namespace?
How does first-use server trust differ from later verification?
How does successful public-key authentication differ from an unauthorized-key failure?
```

The experiment topology is:

```text
aegis-test namespace                    aegis-peer namespace
10.10.0.1                               10.10.0.2

ssh client process
uses client private key
        │
        │ TCP destination 10.10.0.2:22
        ▼
                                      sshd server process
                                      uses server host private key
                                      reads authorized client public keys
```

Important precision:

```text
namespace
→ networking environment

ssh
→ client process

sshd
→ server process
```

The namespace itself is not a client or server. Processes inside it perform those roles.

---

## 2. Runtime-specific evidence after restart

The WSL restart removed the temporary namespace and `/tmp` state. The lab was rebuilt before this guide's connection evidence was produced.

The current runtime identities were:

### Server host identity

```text
SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k
```

### Authorized client identity

```text
SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE
```

### Unauthorized test identity

```text
SHA256:6EIxVoa8IT5WnaM37dXXY+5bEAL+LlJ48a16xcHw6eI
```

These values are evidence from this particular runtime. Regenerating a key pair creates a new cryptographic identity and therefore a new fingerprint.

The earlier guide contains fingerprints from the pre-restart runtime. Those remain historical evidence, but they are not the identities used in this guide's SSH connection.

---

## 3. Network prerequisite rebuilt and verified

The two namespaces were rebuilt as:

```text
aegis-test
├── lo
└── veth-test  10.10.0.1/24

aegis-peer
├── lo
└── veth-peer  10.10.0.2/24
```

Observed connected routes:

```text
10.10.0.0/24 dev veth-test proto kernel scope link src 10.10.0.1
10.10.0.0/24 dev veth-peer proto kernel scope link src 10.10.0.2
```

Connectivity check:

```bash
sudo ip netns exec aegis-test ping -c 2 10.10.0.2
```

Observed result:

```text
2 packets transmitted, 2 received, 0% packet loss
```

This proved:

```text
interfaces were operational
IPv4 addressing was correct
connected routing worked
neighbor discovery worked
ICMP crossed the veth pair
```

It did not prove:

```text
TCP port 22 was listening
an SSH protocol endpoint existed
server identity verification would succeed
a user credential would be authorized
```

This distinction remains central:

```text
ping success
≠
SSH success
```

---

## 4. Authorization is different from key creation

The client key pair existed at:

```text
/tmp/aegislab-namespace-ssh/client/id_ed25519
/tmp/aegislab-namespace-ssh/client/id_ed25519.pub
```

Creating that pair produced a credential, but did not grant access.

```text
credential exists
≠
credential is authorized
```

The server needed an authorization list containing the client public key.

OpenSSH conventionally calls this file:

```text
authorized_keys
```

Its role is:

> List public keys that may be accepted as authentication credentials for the target account.

The private key must remain on the client side.

```text
client private key
→ never copied to the server

client public key
→ copied into a server-side authorization list
```

---

## 5. Initial authorization file

The first authorization file was created with:

```bash
sudo install \
  -o root \
  -g root \
  -m 600 \
  "$LAB_ROOT/client/id_ed25519.pub" \
  "$LAB_ROOT/server/authorized_keys"
```

This safely copied only the public key and created a root-controlled file.

Observed fingerprint:

```text
SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE
```

That matched the client public-key fingerprint exactly.

Therefore:

```text
client/id_ed25519.pub
        ↓ copied
server/authorized_keys
        ↓ fingerprint verified
same public key
```

However, a later design review found that placing the file inside a root-only server directory was not a good fit for target-user authentication file access.

---

## 6. Correcting the authorization boundary

### 6.1 Why the initial path was changed

The initial path was:

```text
/tmp/aegislab-namespace-ssh/server/authorized_keys
```

The containing directory was:

```text
root:root
mode 700
```

The file was:

```text
root:root
mode 600
```

The server configuration was authenticating the Linux account:

```text
motafeq
```

OpenSSH authorization handling applies target-account and path-access rules. A root-only directory and root-only file are not a clean model for a user-specific authorization list in this lab.

The lab was corrected to separate three responsibilities:

```text
client/
→ client-owned private credential

server/
→ root-owned server identity and server policy

auth/
→ target-user-owned authorization policy for motafeq
```

### 6.2 Corrected directory layout

```text
/tmp/aegislab-namespace-ssh/
├── client/                         motafeq:motafeq 700
│   ├── id_ed25519                  motafeq:motafeq 600
│   └── id_ed25519.pub              motafeq:motafeq 644
├── auth/                           motafeq:motafeq 700
│   └── authorized_keys             motafeq:motafeq 600
└── server/                         root:root 700
    ├── ssh_host_ed25519_key        root:root 600
    ├── ssh_host_ed25519_key.pub    root:root 644
    └── sshd_config                 root:root 644
```

### 6.3 Commands used

```bash
sudo install -d \
  -o "$USER" \
  -g "$(id -gn)" \
  -m 700 \
  "$LAB_ROOT/auth"
```

Then:

```bash
install \
  -o "$USER" \
  -g "$(id -gn)" \
  -m 600 \
  "$LAB_ROOT/client/id_ed25519.pub" \
  "$LAB_ROOT/auth/authorized_keys"
```

Observed state:

```text
drwx------ motafeq motafeq /tmp/aegislab-namespace-ssh/auth
-rw------- motafeq motafeq /tmp/aegislab-namespace-ssh/auth/authorized_keys
```

Observed fingerprint:

```text
SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE
```

The corrected file still authorized the intended client credential.

---

## 7. Lab-specific SSH server configuration

The server configuration was written to:

```text
/tmp/aegislab-namespace-ssh/server/sshd_config
```

Final content:

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

This configuration is intentionally lab-specific. It does not replace or reconfigure the ordinary host SSH service.

---

## 8. Creating a root-owned multiline configuration

The file was created with a here-document and `tee`:

```bash
sudo tee "$LAB_ROOT/server/sshd_config" >/dev/null <<'EOF'
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
EOF
```

### 8.1 Why `sudo tee` was used

This tempting command is unreliable for a root-owned destination:

```bash
sudo echo "text" > root-owned-file
```

The shell performs `>` redirection before `sudo` elevates `echo`. The redirection may therefore fail as the normal user.

This pattern works:

```bash
sudo tee root-owned-file
```

because `tee` itself runs with elevated privileges and opens the destination.

### 8.2 Why `>/dev/null` was used

`tee` normally writes its input to both:

```text
the destination file
and
the terminal
```

This redirection suppresses the duplicate terminal output:

```bash
>/dev/null
```

### 8.3 What the here-document means

```bash
<<'EOF'
...
EOF
```

This supplies a multiline text block as standard input.

The quoted delimiter:

```text
'EOF'
```

prevents shell expansions inside the body.

---

## 9. Listener directives

```text
Port 22
AddressFamily inet
ListenAddress 10.10.0.2
```

### `Port 22`

Requests the conventional SSH TCP port.

### `AddressFamily inet`

Restricts the listener to IPv4 for this experiment.

### `ListenAddress 10.10.0.2`

Requests a listener only on the server namespace address:

```text
10.10.0.2:22
```

This is different from:

```text
0.0.0.0:22
```

`0.0.0.0` would request all available IPv4 local addresses visible to that process.

Because `10.10.0.2` exists only inside `aegis-peer`, `sshd` must be started in that network namespace.

---

## 10. Server identity directives

```text
HostKey /tmp/aegislab-namespace-ssh/server/ssh_host_ed25519_key
```

This forces the lab server to use the temporary host identity rather than ordinary system host keys under `/etc/ssh`.

The expected runtime fingerprint was:

```text
SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k
```

```text
PidFile /tmp/aegislab-namespace-ssh/server/sshd.pid
```

A PID file records a process identifier when daemonized operation uses it.

Do not confuse:

```text
PID
→ process identity inside the operating system

host key
→ cryptographic SSH server identity
```

---

## 11. Authentication directives

```text
PubkeyAuthentication yes
```

Enables public-key authentication.

```text
AuthorizedKeysFile /tmp/aegislab-namespace-ssh/auth/authorized_keys
```

Points this lab server to the lab-specific user authorization file rather than the ordinary default location.

```text
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitEmptyPasswords no
UsePAM no
```

These directives narrow the experiment to public-key authentication.

Observed client evidence later confirmed:

```text
Authentications that can continue: publickey
```

No password prompt or fallback method was offered.

```text
PermitRootLogin no
```

Disallows SSH authentication as `root`.

```text
AllowUsers motafeq
```

Restricts permitted login requests to the named Linux account.

Successful authentication therefore required:

```text
requested account is motafeq
AND
public key is authorized
AND
client proves possession of matching private key
```

---

## 12. `StrictModes no`: a lab-specific exception

The authorization file was placed under:

```text
/tmp/aegislab-namespace-ssh/auth/authorized_keys
```

The nested lab directories and file had restrictive ownership and permissions. However, `/tmp` itself is intentionally writable by all users and protected using the sticky bit.

OpenSSH normally performs additional ownership and path-safety checks for authorization files.

The configuration therefore included:

```text
StrictModes no
```

This disables OpenSSH's additional strict ownership/path-policy check for this lab server.

It does not disable:

```text
ordinary Linux permission enforcement
public-key cryptography
signature verification
AllowUsers
password restrictions
server host verification
```

This is a controlled exception for a disposable experiment under `/tmp`.

It is not the preferred production design.

A production-oriented system should normally use a conventional, securely owned authorization path and retain strict mode checking.

---

## 13. Controlled session behavior

```text
ForceCommand /usr/bin/id
```

After authentication, the server ignores the client's requested shell or command and executes:

```bash
/usr/bin/id
```

This gives direct evidence of which Linux account executed the remote process.

Expected shape:

```text
uid=1000(motafeq) gid=1000(motafeq) groups=...
```

This deliberately avoids opening an unrestricted interactive shell during the first connection.

Important distinction:

```text
SSH session request accepted
≠
unrestricted shell granted
```

The server can accept a session channel while still replacing the requested command with `ForceCommand`.

---

## 14. Disabled secondary SSH capabilities

The first experiment did not require forwarding or tunneling features:

```text
X11Forwarding no
AllowTcpForwarding no
GatewayPorts no
PermitTunnel no
PermitUserEnvironment no
```

SSH can provide much more than remote command execution. These directives reduced ambiguity and kept the first experiment bounded.

---

## 15. Configuration inspection

The generated file was inspected with:

```bash
sudo ls -l "$LAB_ROOT/server/sshd_config"
sudo nl -ba "$LAB_ROOT/server/sshd_config"
```

Observed file state:

```text
-rw-r--r-- root root ... /tmp/aegislab-namespace-ssh/server/sshd_config
```

`nl -ba` means:

```text
nl
→ number lines

-b a
→ number all lines, including blank lines
```

Numbered inspection made it possible to verify every directive and identify that `StrictModes no` was initially missing.

The missing line was inserted with:

```bash
sudo sed -i \
  '/^AuthorizedKeysFile /a StrictModes no' \
  "$LAB_ROOT/server/sshd_config"
```

Meaning:

```text
sed
→ stream/text transformation utility

-i
→ edit the file in place

/^AuthorizedKeysFile /
→ find a line beginning with that directive

a StrictModes no
→ append the new line after the match
```

---

## 16. Validating without starting the server

The configuration was tested with:

```bash
sudo /usr/sbin/sshd \
  -t \
  -f "$LAB_ROOT/server/sshd_config"

echo "exit status: $?"
```

Options:

```text
-t
→ test configuration and required files; do not start listening

-f
→ use the specified configuration rather than the normal system configuration
```

### Initial validation result

```text
Missing privilege separation directory: /run/sshd
exit status: 255
```

This was a runtime-prerequisite failure, not evidence of a bad SSH directive.

### Exit status meaning

```text
0
→ success

nonzero
→ failure
```

The value `255` indicated that `sshd -t` did not complete successfully.

---

## 17. `/run/sshd` and privilege separation

The installed OpenSSH server required:

```text
/run/sshd
```

It was created with:

```bash
sudo install -d \
  -o root \
  -g root \
  -m 755 \
  /run/sshd
```

Mode `755` is:

```text
rwxr-xr-x
```

Conceptually, privilege separation reduces how much SSH processing must occur with full root privileges.

```text
small privileged portion
→ performs operations that require root

less-privileged handling
→ performs other connection work with reduced privilege
```

After creating the directory, validation was repeated and returned:

```text
exit status: 0
```

This proved:

```text
configuration syntax was accepted
server host key was readable
required runtime directory existed
basic server prerequisites were accepted
```

It did not prove that the listener could bind or that authentication would work.

---

## 18. Starting `sshd` in `aegis-peer`

The server was started in foreground mode:

```bash
sudo ip netns exec aegis-peer \
  /usr/sbin/sshd \
  -D \
  -e \
  -f "$LAB_ROOT/server/sshd_config"
```

### Namespace placement

```text
ip netns exec aegis-peer
→ run the process using aegis-peer's networking state
```

The process therefore saw:

```text
lo
veth-peer
10.10.0.2
aegis-peer routing table
```

### `-D`

```text
do not detach into the background
```

This kept `sshd` attached to the terminal for direct observation and simple shutdown using `Ctrl+C`.

### `-e`

```text
write server logs to standard error
```

This made connection and authentication messages visible in the server terminal.

### `-f`

Used the lab-specific server configuration.

---

## 19. Listener evidence

The server namespace socket table was inspected with:

```bash
sudo ip netns exec aegis-peer ss -ltnp
```

Observed line:

```text
LISTEN 0 128 10.10.0.2:22 0.0.0.0:* users:(("sshd",pid=28472,fd=3))
```

The PID was runtime-specific and is not expected to remain stable.

### Field interpretation

```text
LISTEN
→ waiting for incoming TCP connection attempts

10.10.0.2:22
→ local bound address and port

0.0.0.0:*
→ no single remote peer is associated with this listening socket

sshd
→ process owning the socket

pid=28472
→ observed process identifier in that runtime

fd=3
→ file descriptor 3 in the process refers to the socket
```

Important precision:

```text
0.0.0.0:* in the peer column
≠
listening on every local address
```

The local column already proved the exact bind:

```text
10.10.0.2:22
```

This established:

```text
sshd started
sshd used aegis-peer networking
sshd owned a TCP listener
listener was bound to the intended address and port
```

---

## 20. First SSH client command

The first connection used:

```bash
sudo ip netns exec aegis-test \
  sudo -u motafeq \
  ssh \
  -vv \
  -i "$LAB_ROOT/client/id_ed25519" \
  -o IdentitiesOnly=yes \
  -o UserKnownHostsFile="$LAB_ROOT/client/known_hosts" \
  motafeq@10.10.0.2
```

### `ip netns exec aegis-test`

Runs the SSH client using the client namespace network stack.

### `sudo -u motafeq`

Entering a named namespace requires privilege, but the SSH client credential belongs to the normal user.

This nested command changes the process identity back to:

```text
motafeq
```

### `-vv`

Enables detailed SSH diagnostics.

### `-i`

Selects the exact lab client private key.

### `IdentitiesOnly=yes`

Prevents unrelated keys from an SSH agent or default files from being offered.

### `UserKnownHostsFile=...`

Keeps host-verification state isolated from the normal user file:

```text
~/.ssh/known_hosts
```

The lab used:

```text
/tmp/aegislab-namespace-ssh/client/known_hosts
```

---

## 21. TCP and SSH protocol establishment

Observed client lines:

```text
Connecting to 10.10.0.2 [10.10.0.2] port 22.
Connection established.
```

This proved the TCP connection reached the listener.

Version exchange:

```text
Local version string SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.18
Remote protocol version 2.0, remote software version OpenSSH_9.6p1 Ubuntu-3ubuntu13.18
```

Both sides used SSH protocol version 2.

Observed algorithm negotiation included:

```text
kex: algorithm: sntrup761x25519-sha512@openssh.com
kex: host key algorithm: ssh-ed25519
server->client cipher: chacha20-poly1305@openssh.com
client->server cipher: chacha20-poly1305@openssh.com
compression: none
```

At a high level:

```text
key exchange
→ establishes fresh shared session secrets

server host key
→ authenticates the server identity

cipher
→ protects subsequent connection traffic
```

The detailed mathematics is intentionally deferred.

---

## 22. First-use server identity verification

The server presented:

```text
Server host key: ssh-ed25519 SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k
```

The lab `known_hosts` file did not yet exist, so the client displayed:

```text
The authenticity of host '10.10.0.2 (10.10.0.2)' can't be established.
ED25519 key fingerprint is SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

This was not an authentication failure.

It meant:

```text
the client reached an SSH server
but
had no previously stored host identity for 10.10.0.2
```

The displayed fingerprint matched the server key generated earlier.

After manual verification, `yes` was entered.

Observed result:

```text
Warning: Permanently added '10.10.0.2' (ED25519) to the list of known hosts.
```

“Permanently” means stored in the selected file until that file is modified or removed. Because the file is under `/tmp`, it is still disposable.

---

## 23. What `known_hosts` records

Conceptually:

```text
server address or hostname
        ↓
expected server public identity
```

The lab record was written to:

```text
/tmp/aegislab-namespace-ssh/client/known_hosts
```

On future connections, the client compares the presented host key against the stored value.

A matching value permits continuation.

A changed value can produce:

```text
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Possible causes include:

```text
server rebuilt with a new key
stale known_hosts record
wrong server answering
possible interception condition
```

Even in a lab, such a warning should be investigated rather than automatically bypassed.

---

## 24. Public-key authentication success

The server advertised:

```text
Authentications that can continue: publickey
```

The client prepared the explicitly selected identity:

```text
Will attempt key: /tmp/aegislab-namespace-ssh/client/id_ed25519 ED25519 SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE explicit
```

Then:

```text
Offering public key: ... SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE
Server accepts key: ... SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE
Authenticated to 10.10.0.2 ([10.10.0.2]:22) using "publickey".
```

These are separate stages.

### Offering the public key

```text
client proposes a public identity
```

### Server accepts the key

```text
server finds that public key in the authorization policy
```

### Authentication completes

```text
client proves possession of the corresponding private key
server verifies the cryptographic proof
```

The private key was not copied or transmitted to the server.

---

## 25. Successful forced command

The client requested a session and an interactive shell shape, but server policy contained:

```text
ForceCommand /usr/bin/id
```

Observed remote output:

```text
uid=1000(motafeq) gid=1000(motafeq) groups=1000(motafeq),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),1001(docker)
```

This proved:

```text
authentication completed
session channel opened
remote process executed as motafeq
ForceCommand replaced unrestricted shell behavior
/usr/bin/id completed
```

The session then ended:

```text
Connection to 10.10.0.2 closed.
Exit status 0
```

Exit status `0` means the forced command completed successfully.

---

## 26. Namespace isolation limitation revealed by `id`

The remote output included the same WSL user and group memberships, including groups such as:

```text
sudo
docker
adm
```

This demonstrates:

```text
network namespace isolation
≠
user namespace isolation
≠
filesystem isolation
≠
separate operating system
```

The remote SSH process used `aegis-peer` networking, but still used the shared WSL:

```text
user database
filesystem
process environment
kernel
```

This is a major comparison point for later Docker and VM reproductions.

---

## 27. Second connection: stored host verification

The second client command reduced debug verbosity to `-v` but otherwise used the same identity and known-hosts path.

Observed decisive lines:

```text
Server host key: ssh-ed25519 SHA256:bfk+Wl3y2se0v0eAg6REcmLT0tBzGryWETyYMfyRB7k
Host '10.10.0.2' is known and matches the ED25519 host key.
Found key in /tmp/aegislab-namespace-ssh/client/known_hosts:1
```

No manual prompt appeared.

The sequence was:

```text
server presents host key
        ↓
client loads stored known_hosts entry
        ↓
stored and presented identities match
        ↓
connection continues automatically
```

This demonstrates the difference between:

```text
first-use trust establishment
and
later identity verification
```

Authentication and `ForceCommand` again succeeded with exit status `0`.

---

## 28. Controlled unauthorized-key experiment

A second client key pair was generated but deliberately not added to `authorized_keys`.

Fingerprint:

```text
SHA256:6EIxVoa8IT5WnaM37dXXY+5bEAL+LlJ48a16xcHw6eI
```

The connection attempt used:

```bash
sudo ip netns exec aegis-test \
  sudo -u motafeq \
  ssh \
  -v \
  -i "$LAB_ROOT/client/unauthorized_id_ed25519" \
  -o IdentitiesOnly=yes \
  -o UserKnownHostsFile="$LAB_ROOT/client/known_hosts" \
  -o PasswordAuthentication=no \
  -o KbdInteractiveAuthentication=no \
  motafeq@10.10.0.2
```

The client-side options explicitly prevented password or keyboard-interactive fallback in addition to the server restrictions.

---

## 29. What succeeded in the failed-authentication experiment

Observed lines:

```text
Connecting to 10.10.0.2 [10.10.0.2] port 22.
Connection established.
```

Therefore TCP still succeeded.

Then:

```text
Host '10.10.0.2' is known and matches the ED25519 host key.
```

Therefore server identity verification still succeeded.

The failure occurred after:

```text
network reachability
TCP connection
SSH negotiation
server host verification
```

This is why the final `Permission denied` message must not be misdiagnosed as a routing or listener failure.

---

## 30. Why the unauthorized key failed

The client offered:

```text
SHA256:6EIxVoa8IT5WnaM37dXXY+5bEAL+LlJ48a16xcHw6eI
```

The authorized file contained:

```text
SHA256:etYCEDrbFAGE5iHS7CLT5RLctsDxQLWr58+sCXPx9zE
```

These identities were different.

Observed sequence:

```text
Will attempt key: ... unauthorized_id_ed25519 ... SHA256:6EIx...
Offering public key: ... SHA256:6EIx...
Authentications that can continue: publickey
No more authentication methods to try.
motafeq@10.10.0.2: Permission denied (publickey).
```

The successful connection had included:

```text
Server accepts key
Authenticated
```

The failed connection did not include either line.

The authorization logic was:

```text
client offers public identity B
        ↓
server checks authorization list
        ↓
public identity B is absent
        ↓
server does not accept the key
        ↓
no other permitted method remains
        ↓
authentication fails
```

This proved:

```text
valid key pair
≠
authorized key pair
```

---

## 31. The most important layer model

The experiments established distinct layers:

```text
1. Network reachability
2. TCP service availability
3. SSH protocol negotiation
4. Server host identity verification
5. User credential authorization
6. Proof of private-key possession
7. Session policy and command execution
```

A success or failure at one layer does not automatically describe the others.

### Example: successful ping

```text
proves network-layer reachability
```

It does not prove an SSH listener exists.

### Example: connection refused

```text
may mean destination is reachable but no process is listening
```

### Example: host key match

```text
proves the expected server identity answered
```

It does not prove the client credential is authorized.

### Example: `Permission denied (publickey)` after host match

```text
network, TCP, SSH negotiation, and server identity succeeded
client authorization failed
```

### Example: `Authenticated ... using "publickey"`

```text
server accepted the public identity
client proved possession of the matching private key
```

---

## 32. Command and output interpretation reference

### `sshd -t -f FILE`

```text
test the selected server configuration without starting a listener
```

### `ip netns exec NAME COMMAND`

```text
run COMMAND using NAME's network namespace
```

### `ss -ltnp`

```text
-l  listening sockets
-t  TCP sockets
-n  numeric addresses and ports
-p  owning process information
```

### `ssh -v` and `ssh -vv`

```text
show progressively more detailed client diagnostics
```

### `-i PRIVATE_KEY`

```text
select the client private key file
```

### `-o IdentitiesOnly=yes`

```text
use explicitly configured identities rather than unrelated defaults or agent keys
```

### `-o UserKnownHostsFile=FILE`

```text
read and write expected server host identities in the selected file
```

### `sudo -u motafeq`

```text
run the following process with the normal user's identity after privileged namespace entry
```

---

## 33. Failure interpretation table

| Evidence | Most likely layer reached | What it does not prove |
|---|---|---|
| Ping reply | Network reachability | TCP listener or SSH |
| `Connection refused` | Destination reachable; no accepting listener at that endpoint | Authentication state |
| `Connection timed out` | Connection did not complete | Exact cause without more evidence |
| Host fingerprint prompt | SSH server reached; no stored identity yet | User authentication |
| Host key match | Expected server identity verified | Client authorization |
| `Offering public key` | Client proposed a credential | Server accepted it |
| `Server accepts key` | Public key recognized as authorized | Final signature proof until authentication completes |
| `Authenticated ... publickey` | Credential authorization and proof succeeded | Filesystem or kernel isolation |
| `Permission denied (publickey)` after host match | SSH server reached and verified; credential rejected | Network failure |
| `Exit status 0` after `id` | Forced command succeeded | Unrestricted shell access |

---

## 34. Security and learning boundaries

This experiment was intentionally bounded:

```text
listener bound only to 10.10.0.2
no namespace default route added
ordinary host SSH service not started or reconfigured
lab-specific host key used
lab-specific client key used
lab-specific known_hosts used
password and keyboard-interactive authentication disabled
root login disabled
first session forced to /usr/bin/id
forwarding and tunneling features disabled
```

However, network namespaces are not complete sandboxes.

They do not provide separate:

```text
kernel
filesystem
user database
host identity
full machine lifecycle
```

This experiment is suitable for controlled networking and SSH learning. It is not a containment environment for untrusted code or hostile activity.

---

## 35. Evidence established in this unit

```text
✓ rebuilt namespace topology
✓ verified ICMP connectivity
✓ created target-user authorization path
✓ verified authorized client fingerprint
✓ created lab-specific sshd configuration
✓ corrected authorization path design
✓ added and understood lab-specific StrictModes exception
✓ validated configuration
✓ diagnosed and repaired missing /run/sshd
✓ started sshd in aegis-peer
✓ observed 10.10.0.2:22 LISTEN owned by sshd
✓ completed TCP and SSH negotiation
✓ manually verified first-use server fingerprint
✓ stored server identity in lab known_hosts
✓ automatically verified the same identity on second connection
✓ proved only public-key authentication was available
✓ authenticated using the intended client key
✓ executed ForceCommand as motafeq
✓ observed normal exit status 0
✓ offered a valid but unauthorized key
✓ proved TCP and host verification still succeeded
✓ observed controlled Permission denied (publickey)
```

---

## 36. What remains unproven or incomplete

```text
✗ correlated server-side log lines for successful and failed attempts
✗ observed a live ESTABLISHED socket while a session remains open
✗ captured process parent/child relationships during authentication
✗ demonstrated deliberate server host-key mismatch behavior
✗ replaced the forced command with the canonical normal-login scenario
✗ captured host-log and network evidence for the full canonical scenario
✗ reproduced the same scenario in Docker
✗ reproduced the same scenario in separate VMs
✗ compared isolation, topology, observability, failure modes, and cost
✗ completed cleanup and final namespace handoff
```

---

## 37. Next learning unit

The next unit should correlate client-visible results with server-side and operating-system evidence.

Minimum next observations:

```text
successful connection log
failed unauthorized-key log
sshd parent and child processes
LISTEN socket versus ESTABLISHED socket
client endpoint 10.10.0.1:<ephemeral-port>
server endpoint 10.10.0.2:22
session creation and closure
```

A useful target model is:

```text
client debug output
        ↕ correlate
server sshd logs
        ↕ correlate
process table
        ↕ correlate
socket table
```

Only after those layers are connected should the namespace slice move toward the full normal-login scenario and then the Docker reproduction.

---

## 38. Compact review

### Which key verifies the server?

```text
server host key
```

### Which key authenticates the client credential?

```text
client private key proves possession
server-side authorized public key verifies the proof
```

### What does `known_hosts` store?

```text
expected server host identities
```

### What does `authorized_keys` store?

```text
client public identities permitted for an account
```

### What did `LISTEN 10.10.0.2:22` prove?

```text
sshd owned a TCP listener at the intended namespace endpoint
```

### What did the first fingerprint prompt mean?

```text
the SSH server was reached, but its identity had not yet been stored
```

### What did the second connection prove?

```text
the stored server identity matched automatically
```

### What did `Authenticated ... using "publickey"` prove?

```text
the public key was authorized and the client proved possession of the matching private key
```

### Why did the unauthorized key fail?

```text
its public fingerprint was absent from authorized_keys
```

### Did the failed authentication indicate a network failure?

```text
no; TCP, SSH negotiation, and server host verification had already succeeded
```

### What did `/usr/bin/id` reveal about namespaces?

```text
networking was isolated, but the WSL user database and group memberships were shared
```
