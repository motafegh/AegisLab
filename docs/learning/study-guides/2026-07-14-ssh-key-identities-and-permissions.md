# SSH Key Identities and Permissions — Study Guide

**Date:** 2026-07-14  
**Status:** Learner-facing study guide  
**Project position:** Namespace-led SSH Core slice  
**Scope:** Temporary lab directories, Linux permissions, SSH key generation, fingerprints, and the distinction between server identity and client authentication

---

## 1. Purpose

This guide records the SSH identity stage of the AegisLab namespace experiment.

The current topology is:

```text
aegis-test namespace                    aegis-peer namespace
10.10.0.1                               10.10.0.2

ssh client process
        │
        │ TCP connection to 10.10.0.2:22
        ▼
                                      sshd server process
```

The network path already works. The next problem is identity:

```text
Which SSH server answered?
Which client credential is allowed to authenticate?
```

SSH uses separate key pairs for these two questions.

---

## 2. Two independent SSH identities

### 2.1 Server host identity

The SSH server owns a host key pair:

```text
ssh_host_ed25519_key
ssh_host_ed25519_key.pub
```

Responsibility:

```text
client verifies the server
```

The server private key remains secret. The client later receives and verifies the corresponding public identity.

### 2.2 Client authentication identity

The SSH client owns a separate key pair:

```text
id_ed25519
id_ed25519.pub
```

Responsibility:

```text
server verifies that the client possesses an authorized private key
```

The client private key remains on the client side. The server receives only the public key.

### 2.3 The central distinction

```text
server host key
≠
client authentication key
```

| Key pair | Verification direction | Question answered |
|---|---|---|
| Server host key | Client verifies server | “Which SSH server answered?” |
| Client authentication key | Server verifies client credential | “Does this client possess an authorized private key?” |

---

## 3. Temporary lab storage

The lab files are stored outside the repository:

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh
```

This command creates a shell variable only. It does not create a directory.

After the assignment:

```bash
"$LAB_ROOT/server"
```

means:

```text
/tmp/aegislab-namespace-ssh/server
```

### Why `/tmp`?

The SSH keys and configuration are:

- temporary;
- lab-specific;
- not source code;
- not intended for Git;
- safe to remove during cleanup.

Keeping private keys outside the repository reduces the risk of accidental commits.

### Why quote variables?

```bash
"$LAB_ROOT"
```

Quoting tells the shell to treat the expanded path as one argument. It is a safe general habit for paths and variable expansions.

---

## 4. Lab directory layout

The intended structure is:

```text
/tmp/aegislab-namespace-ssh/
├── client/
└── server/
```

The observed permissions were:

```text
drwx--x--x root    root    /tmp/aegislab-namespace-ssh
drwx------ motafeq motafeq /tmp/aegislab-namespace-ssh/client
drwx------ root    root    /tmp/aegislab-namespace-ssh/server
```

### 4.1 Top directory

```text
drwx--x--x
```

Numeric mode:

```text
711
```

Meaning:

```text
owner:  read + write + traverse
group:  traverse only
others: traverse only
```

The normal user can traverse to a known child such as `client`, but cannot freely list the top directory.

### 4.2 Client directory

```text
drwx------ motafeq motafeq
```

Numeric mode:

```text
700
```

Only `motafeq` can enter, list, create, read, modify, or delete entries inside it.

### 4.3 Server directory

```text
drwx------ root root
```

Also mode `700`.

Only root can access the server directory and its private host key.

---

## 5. Linux permission model

Permissions are evaluated for three categories:

```text
user | group | others
```

Permission symbols:

```text
r = read
w = write
x = execute or traverse
```

For directories:

- `r` allows listing names;
- `w` allows creating, deleting, or renaming entries, normally together with `x`;
- `x` allows traversing the directory using a known name.

Numeric values:

```text
read    = 4
write   = 2
execute = 1
```

Examples:

```text
7 = 4 + 2 + 1 = rwx
6 = 4 + 2     = rw-
5 = 4 + 1     = r-x
1 = 1         = --x
0             = ---
```

Modes used in this lab:

```text
700 = rwx------
711 = rwx--x--x
600 = rw-------
644 = rw-r--r--
```

---

## 6. Directory creation commands

The corrected directory creation sequence was:

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh

sudo rm -rf "$LAB_ROOT"

sudo install -d \
  -o root \
  -g root \
  -m 711 \
  "$LAB_ROOT"

sudo install -d \
  -o root \
  -g root \
  -m 700 \
  "$LAB_ROOT/server"

sudo install -d \
  -o "$USER" \
  -g "$(id -gn)" \
  -m 700 \
  "$LAB_ROOT/client"
```

### `sudo rm -rf`

```text
rm  = remove
-r  = recursive
-f  = force; do not prompt and tolerate a missing target
sudo = run with elevated privileges
```

This command is destructive. Before running it, verify the variable:

```bash
printf '%s\n' "$LAB_ROOT"
```

Expected value:

```text
/tmp/aegislab-namespace-ssh
```

### `install -d`

Here, `install` is not a package manager. It creates directories while assigning ownership and permissions.

```text
-d = create directory
-o = owner user
-g = owner group
-m = permission mode
```

### `$USER`

Normally expands to the current username:

```text
motafeq
```

### `$(id -gn)`

Command substitution runs `id -gn` and replaces the expression with the current primary group name.

In this environment:

```text
motafeq
```

---

## 7. Why the first directory attempt failed

The initial top directory was created as root-owned mode `700`:

```text
root owns directory
normal user has no traversal permission
```

Then the normal user tried to create:

```text
/tmp/aegislab-namespace-ssh/client
```

The result was:

```text
Permission denied
```

The important rule is:

> Accessing or creating an item inside a directory requires suitable permissions on every parent directory in the path.

Mode `711` on the top directory permits traversal while keeping directory listing restricted.

---

## 8. Server host key generation

The server host key was generated with:

```bash
sudo ssh-keygen \
  -t ed25519 \
  -N '' \
  -C 'AegisLab namespace SSH server host key' \
  -f "$LAB_ROOT/server/ssh_host_ed25519_key"
```

### Command meaning

```text
sudo
→ run as root because the server directory is root-owned

ssh-keygen
→ OpenSSH key generation and inspection utility

-t ed25519
→ create an Ed25519 key pair

-N ''
→ use an empty private-key passphrase for this disposable lab key

-C '...'
→ add a human-readable comment

-f <path>
→ place the private key at the exact path
```

The command created:

```text
ssh_host_ed25519_key
ssh_host_ed25519_key.pub
```

Observed output:

```text
Your identification has been saved in /tmp/aegislab-namespace-ssh/server/ssh_host_ed25519_key
Your public key has been saved in /tmp/aegislab-namespace-ssh/server/ssh_host_ed25519_key.pub
```

In this message, “identification” means the private cryptographic key file.

---

## 9. Server host key files

Observed listing:

```text
-rw------- 1 root root 444 ssh_host_ed25519_key
-rw-r--r-- 1 root root 120 ssh_host_ed25519_key.pub
```

### Private server host key

```text
ssh_host_ed25519_key
```

Permissions:

```text
600 = rw-------
```

Only root can read or modify it.

Responsibility:

```text
sshd uses it to prove server identity
```

It must not be pasted, committed, or shared.

### Public server host key

```text
ssh_host_ed25519_key.pub
```

Permissions:

```text
644 = rw-r--r--
```

The public key is not secret. It allows clients to verify proofs made using the private host key.

---

## 10. Server fingerprint

The observed server fingerprint was:

```text
SHA256:k+o04IpUdU/XqiFAy9P8E5Udai6CYsd3AgLoiBJkC0Y
```

Inspection command:

```bash
sudo ssh-keygen \
  -lf "$LAB_ROOT/server/ssh_host_ed25519_key.pub"
```

Options:

```text
-l = list fingerprint
-f = specify key file
```

A fingerprint is a compact identifier derived from a public key:

```text
public key
→ cryptographic hash
→ compact fingerprint
```

Later, the SSH client should display this same fingerprint when it first reaches the server at `10.10.0.2`.

A matching fingerprint supports this conclusion:

```text
the responding server possesses the private key corresponding to the expected public host identity
```

It does not prove user authentication.

---

## 11. Client authentication key generation

The client key was generated as the normal user:

```bash
ssh-keygen \
  -t ed25519 \
  -N '' \
  -C 'AegisLab namespace SSH client key' \
  -f "$LAB_ROOT/client/id_ed25519"
```

There was no `sudo` because the SSH client process will run as `motafeq` and must be able to read its private key.

The command created:

```text
id_ed25519
id_ed25519.pub
```

Observed output:

```text
Your identification has been saved in /tmp/aegislab-namespace-ssh/client/id_ed25519
Your public key has been saved in /tmp/aegislab-namespace-ssh/client/id_ed25519.pub
```

---

## 12. Client key files

Observed listing:

```text
-rw------- 1 motafeq motafeq 432 id_ed25519
-rw-r--r-- 1 motafeq motafeq 115 id_ed25519.pub
```

### Private client key

```text
id_ed25519
```

Permissions:

```text
600 = rw-------
```

Only `motafeq` can read or modify it.

Responsibility:

```text
client uses it to prove possession of an authentication credential
```

The private key is never copied to the server.

### Public client key

```text
id_ed25519.pub
```

Permissions:

```text
644 = rw-r--r--
```

This public key will later be copied into the server-side authorization file.

---

## 13. Client fingerprint

The observed client fingerprint was:

```text
SHA256:SwOoqkQccznuRKZVH/DA1+YBpY+bXYuBB9LV9/G9qc0
```

Inspection command:

```bash
ssh-keygen \
  -lf "$LAB_ROOT/client/id_ed25519.pub"
```

This fingerprint identifies the client authentication key pair.

Later, the SSH server may record a successful authentication using this fingerprint:

```text
Accepted publickey for motafeq ... ED25519 SHA256:SwOoqkQccznuRKZVH/DA1+YBpY+bXYuBB9LV9/G9qc0
```

That would connect server-side authentication evidence to the exact client credential created in this lab.

---

## 14. Fingerprint comparison

Server fingerprint:

```text
SHA256:k+o04IpUdU/XqiFAy9P8E5Udai6CYsd3AgLoiBJkC0Y
```

Client fingerprint:

```text
SHA256:SwOoqkQccznuRKZVH/DA1+YBpY+bXYuBB9LV9/G9qc0
```

They are different because they represent different key pairs and responsibilities.

```text
server fingerprint
→ identifies server host identity

client fingerprint
→ identifies client authentication credential
```

---

## 15. How public-key proof works

The private key is not transmitted to the other side.

Conceptually:

```text
server has client public key
        ↓
client claims possession of matching private key
        ↓
client signs SSH protocol data with private key
        ↓
server verifies signature with public key
        ↓
authentication can succeed if authorization and policy also permit it
```

For server identity, the direction is reversed:

```text
server proves possession of host private key
        ↓
client verifies using server public identity
```

The complete direction map is:

```text
client verifies server
→ server host key

server verifies client credential
→ client authentication key
```

---

## 16. Key comments

The `-C` option added comments:

```text
AegisLab namespace SSH server host key
AegisLab namespace SSH client key
```

Comments help humans identify a key’s intended purpose.

They do not:

- affect the cryptographic key;
- grant access;
- identify a Linux account by themselves;
- prove possession;
- replace fingerprint comparison.

---

## 17. Empty passphrase tradeoff

Both lab private keys were generated with:

```bash
-N ''
```

This means no passphrase protects the private-key files.

For this experiment, the tradeoff is deliberate because the keys are:

- temporary;
- stored locally;
- protected by filesystem permissions;
- limited to the controlled lab;
- removed during cleanup;
- intended for repeatable testing.

For long-lived personal or production keys, an empty passphrase may be inappropriate.

---

## 18. Ed25519 at current depth

`ed25519` is the selected SSH public-key signature algorithm.

At this stage, the important properties are:

- modern SSH support;
- compact public keys;
- small key files;
- fast signing and verification;
- appropriate strength for this lab.

The elliptic-curve mathematics is intentionally deferred.

---

## 19. Randomart

`ssh-keygen` displayed visual blocks such as:

```text
+--[ED25519 256]--+
|    .+.o+o.      |
|       ...       |
+----[SHA256]-----+
```

Randomart is a visual representation derived from the fingerprint.

It is not:

- the private key;
- the public key;
- a password;
- encrypted session data;
- a substitute for exact fingerprint comparison.

The SHA256 fingerprint is the precise identity value.

---

## 20. The number `256`

Fingerprint output began with:

```text
256
```

For an Ed25519 key, OpenSSH reports the nominal key size as 256 bits.

It is not:

- the file size;
- the password length;
- the number of transmitted bytes;
- the printed fingerprint length.

The actual files were larger because key files include encoding, structure, metadata, and comments.

---

## 21. Why file sizes differ

Observed sizes:

```text
server private key: 444 bytes
server public key:  120 bytes
client private key: 432 bytes
client public key:  115 bytes
```

The private-key file includes:

- private key material;
- related public information;
- OpenSSH private-key format structure;
- formatting and metadata.

The public-key file contains a compact textual line:

```text
key type
encoded public-key data
comment
```

The size differences are normal.

---

## 22. Current authorization state

The client key exists, but it is not yet authorized.

Current state:

```text
client private key exists
client public key exists
server host key exists
```

Missing state:

```text
server authorization file containing the client public key
```

Therefore:

```text
credential created
≠
credential authorized
```

Having a valid key pair does not automatically permit login.

---

## 23. Current complete identity inventory

### Server host identity

```text
Private key:
/tmp/aegislab-namespace-ssh/server/ssh_host_ed25519_key

Public key:
/tmp/aegislab-namespace-ssh/server/ssh_host_ed25519_key.pub

Fingerprint:
SHA256:k+o04IpUdU/XqiFAy9P8E5Udai6CYsd3AgLoiBJkC0Y

Owner:
root:root

Purpose:
prove SSH server identity
```

### Client authentication identity

```text
Private key:
/tmp/aegislab-namespace-ssh/client/id_ed25519

Public key:
/tmp/aegislab-namespace-ssh/client/id_ed25519.pub

Fingerprint:
SHA256:SwOoqkQccznuRKZVH/DA1+YBpY+bXYuBB9LV9/G9qc0

Owner:
motafeq:motafeq

Purpose:
prove possession of an authorized client credential
```

---

## 24. What has been demonstrated

```text
✓ temporary lab path isolated from the repository
✓ deliberate directory ownership and permissions
✓ separate root-owned server area
✓ separate user-owned client area
✓ one server host key pair
✓ one client authentication key pair
✓ restrictive private-key permissions
✓ shareable public-key permissions
✓ distinct fingerprints
✓ server identity separated from client authentication
```

Not yet demonstrated:

```text
✗ client public-key authorization
✗ sshd configuration
✗ configuration validation
✗ TCP port 22 listener
✗ SSH connection
✗ server host-key verification by the client
✗ client authentication
✗ remote command execution
✗ SSH logs and socket evidence
```

---

## 25. Next learning step

The next step is to create a server-side `authorized_keys` file containing only the client public key.

The purpose will be:

```text
client public key
        ↓
server authorization rule
        ↓
client may attempt to prove possession of matching private key
```

The private client key will remain in the client directory and will not be copied.

The next unit should include:

1. inspect the public-key file format;
2. copy only the public key into the root-owned server authorization file;
3. inspect ownership, mode, and fingerprint;
4. explain the difference between identity, possession, authorization, and successful authentication.
