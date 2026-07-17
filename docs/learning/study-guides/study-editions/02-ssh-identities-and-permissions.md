# SSH Identities and Linux Permissions — Layered Study Edition

**Role:** Primary study path for the SSH identity and ownership layer  
**Prerequisite:** [Networking and Namespace Foundations](01-networking-and-namespace-foundations.md)  
**Full reference:** [SSH Key Identities and Permissions — Study Guide](../2026-07-14-ssh-key-identities-and-permissions.md)  
**Practical reconstruction:** [Namespace SSH Lab Reconstruction Runbook](../../../runbooks/namespace-ssh-lab-reconstruction.md)

## 1. Learning outcome

After this unit, you should be able to distinguish and safely create:

```text
server host identity
→ client verifies the server

client authentication identity
→ server verifies possession of an authorized credential
```

You should also be able to explain why ownership and permissions must match the process that uses each private key.

---

# Layer 1 — Required mental model

## 2. SSH uses two independent trust directions

### Server host key

Owned by the SSH server.

Question answered:

```text
Which SSH server answered?
```

The server proves possession of the host private key. The client verifies the corresponding public identity.

### Client authentication key

Owned by the SSH client user.

Question answered:

```text
Does this client possess a private key matching an authorized public key?
```

The client private key stays on the client side. The server stores only the authorized public key.

### Central distinction

```text
server host key
≠ client authentication key
```

| Identity | Private key used by | Public identity checked by | Purpose |
|---|---|---|---|
| Server host | `sshd` | SSH client | Verify the server |
| Client authentication | `ssh` | SSH server | Authenticate an authorized client credential |

## 3. Identity, authorization, possession, and authentication

These are different states:

```text
key pair exists
≠ public key is authorized
≠ private-key possession was proved
≠ authentication succeeded
```

A valid key pair can still be rejected if its public key is absent from the server authorization policy.

## 4. Private key and public key

### Private key

- must remain secret;
- performs cryptographic signing;
- must be readable by the process that owns the identity;
- must not be committed, pasted, or copied to the other endpoint.

### Public key

- is not secret;
- allows verification of signatures from the matching private key;
- may be copied into `authorized_keys` or used to derive a fingerprint.

## 5. Fingerprint

A fingerprint is a compact identifier derived from a public key:

```text
public key
→ cryptographic hash
→ fingerprint
```

A fingerprint is useful for exact identity comparison. It is not a password, secret, authorization rule, or proof of private-key possession by itself.

Runtime warning:

```text
regenerated key pair
→ new identity
→ new fingerprint
```

Never expect a historical fingerprint to match a newly generated key.

---

# Layer 2 — Ownership and permissions

## 6. Directory responsibilities

The lab uses:

```text
/tmp/aegislab-namespace-ssh/
├── server/    root:root       700
├── client/    motafeq:motafeq 700
└── auth/      motafeq:motafeq 700
```

Top directory:

```text
/tmp/aegislab-namespace-ssh  root:root 711
```

### Why `711` on the top directory?

```text
owner:  read + write + traverse
group:  traverse only
others: traverse only
```

The normal user may traverse to a known child path but cannot list or modify the root-owned top directory freely.

### Why `700` on private directories?

Only the owner can list, enter, create, modify, or remove entries.

## 7. File modes used

```text
600 = rw-------
644 = rw-r--r--
700 = rwx------
711 = rwx--x--x
```

Lab intent:

```text
private keys       600
public keys        644
private directories 700
top traversal boundary 711
```

## 8. Directory traversal rule

Access to a child depends on every parent component.

```text
/tmp
→ /tmp/aegislab-namespace-ssh
→ client
→ id_ed25519
```

A readable file cannot be reached if a required parent directory denies traversal.

## 9. Process identity must match file access

```text
root-owned server private key
→ read by root-started sshd

motafeq-owned client private key
→ read by ssh running as motafeq
```

Using `sudo` for namespace entry does not mean the SSH client should remain root. The actual client is deliberately returned to `motafeq` before reading the client credential.

---

# Layer 3 — Minimum practical mechanism

## 10. Define the temporary root

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh
```

This creates a shell variable only. It does not create a directory. Shell variables must be set again in each new terminal unless exported through another mechanism.

Verify before destructive or path-sensitive work:

```bash
printf 'LAB_ROOT=%s\n' "$LAB_ROOT"
```

Expected exact value:

```text
LAB_ROOT=/tmp/aegislab-namespace-ssh
```

## 11. Create the ownership boundary

Use the reconstruction runbook for the complete validated commands.

The intended result is:

```text
711 root:root       LAB_ROOT
700 root:root       server
700 motafeq:motafeq client
700 motafeq:motafeq auth
```

Validate with:

```bash
sudo stat -c '%A %a %U:%G %n' \
  "$LAB_ROOT" \
  "$LAB_ROOT/server" \
  "$LAB_ROOT/client" \
  "$LAB_ROOT/auth"
```

## 12. Generate identities

Server host identity:

```bash
sudo ssh-keygen \
  -q \
  -t ed25519 \
  -N '' \
  -f "$LAB_ROOT/server/ssh_host_ed25519_key"
```

Authorized client identity:

```bash
sudo -u motafeq ssh-keygen \
  -q \
  -t ed25519 \
  -N '' \
  -f "$LAB_ROOT/client/id_ed25519"
```

Unauthorized test identity:

```bash
sudo -u motafeq ssh-keygen \
  -q \
  -t ed25519 \
  -N '' \
  -f "$LAB_ROOT/client/unauthorized_id_ed25519"
```

Important options:

```text
-t ed25519  select key algorithm
-N ''       empty passphrase for disposable local lab keys
-f PATH     exact output path
-q          suppress nonessential generation output
```

An empty passphrase is a controlled lab tradeoff, not a general recommendation for long-lived personal or production keys.

## 13. Validate ownership and modes

Required relationship:

```text
server private key       600 root:root
server public key        644 root:root
client private keys      600 motafeq:motafeq
client public keys       644 motafeq:motafeq
```

## 14. Record current fingerprints

```bash
sudo ssh-keygen -lf "$LAB_ROOT/server/ssh_host_ed25519_key.pub"
ssh-keygen -lf "$LAB_ROOT/client/id_ed25519.pub"
ssh-keygen -lf "$LAB_ROOT/client/unauthorized_id_ed25519.pub"
```

Required evidence:

- three fingerprints are present;
- all three are distinct;
- current values are recorded as runtime evidence, not memorized facts.

---

# Layer 4 — Reading decisive evidence

## Private key mode `600`

Proves:

- only the file owner receives ordinary read/write permission from the mode bits.

Does not prove:

- the key is authorized;
- the corresponding process is currently using it;
- privileged root access is impossible.

## Matching fingerprint

Proves:

- two inspected public-key representations identify the same cryptographic public key.

Does not prove:

- a client currently possesses the private key;
- authentication succeeded;
- the key is safe from theft.

## Different fingerprints

Proves:

- the public identities differ.

This is expected for server host, authorized client, and unauthorized client key pairs.

---

# Layer 5 — Active recall

Close this file before answering.

1. Which key pair lets the client verify the server?
2. Which private key must remain readable by `ssh` running as `motafeq`?
3. Why is a valid client key not automatically authorized?
4. Why is the client private key never copied into `authorized_keys`?
5. What does a fingerprint prove and not prove?
6. Why can mode `700` on a parent directory block access to a child file?
7. Why does `LAB_ROOT` sometimes expand to an empty string in a new terminal?
8. Why are historical fingerprints not reusable as current truth?

## Responsibility exercise

For each file, state owner, secrecy, and responsibility:

```text
server/ssh_host_ed25519_key
server/ssh_host_ed25519_key.pub
client/id_ed25519
client/id_ed25519.pub
auth/authorized_keys
```

---

# Layer 6 — Changed-case diagnosis

## Case A — Empty `LAB_ROOT`

Observed error:

```text
/server/ssh_host_ed25519_key.pub: No such file or directory
```

Reasoning:

```text
expected path begins with /tmp/aegislab-namespace-ssh
actual path begins with /server
→ LAB_ROOT expanded to an empty string
```

Repair the shell variable, not the key file.

## Case B — Client private key owned by root

Potential symptom:

```text
ssh running as motafeq cannot read the selected private key
```

Affected layer:

```text
filesystem ownership and process identity
```

Do not regenerate networking or change server authorization first.

## Case C — Unauthorized key pair is valid

The key has correct structure, ownership, and permissions but is absent from `authorized_keys`.

Expected:

```text
key can be offered
server does not accept it
public-key authentication fails
```

This is an authorization result, not evidence of an invalid cryptographic key.

---

# Layer 7 — Mastery gate

This unit is stable enough for the current project when you can:

- draw both SSH trust directions from memory;
- classify private/public key files correctly;
- explain identity, authorization, possession, and authentication as separate states;
- inspect current ownership, modes, and fingerprints;
- diagnose an unset variable or ownership failure from the path/output;
- recreate the identity layer using documentation with reduced guidance;
- avoid exposing or committing private keys.

Passing does not require memorizing fingerprint values or file byte sizes.

---

# Optional reference topics

Use the full guide only when needed for:

- detailed permission arithmetic;
- the original parent-directory failure;
- key comments;
- randomart;
- OpenSSH's displayed `256` value;
- historical file sizes and fingerprints;
- the full original command chronology.

Those details are preserved, but they are not mandatory linear study for the current Core.