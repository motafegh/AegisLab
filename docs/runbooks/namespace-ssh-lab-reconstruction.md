# Namespace SSH Lab Reconstruction Runbook

## Purpose

Use this runbook when WSL or the laptop has restarted and the temporary namespace SSH lab may have disappeared.

The runbook reconstructs the namespace implementation of the AegisLab SSH experiment in dependency order:

```text
inspect surviving state
        ↓
network namespaces and veth pair
        ↓
addresses, routes, and ICMP validation
        ↓
temporary ownership boundary
        ↓
server and client SSH identities
        ↓
client authorization and server trust state
        ↓
lab-specific sshd configuration
        ↓
configuration validation
        ↓
namespace-bound listener
        ↓
authenticated long-lived transport
        ↓
process, socket, log, and packet observation
```

This is a lab reconstruction procedure, not a production SSH deployment guide.

## Safety and scope

- Do not start, stop, or reconfigure the ordinary WSL SSH service.
- The lab server binds only to `10.10.0.2:22` inside `aegis-peer`.
- Keep all temporary identities and trust state below `/tmp/aegislab-namespace-ssh`.
- Never commit private keys or copy their contents into the repository, chat, logs, or screenshots.
- `StrictModes no` is a temporary exception caused by using a path below `/tmp`. Do not generalize it to production.
- Network namespaces isolate networking. They do not provide separate users, filesystems, kernels, hostnames, or PID namespaces.
- Stop at the first failed validation gate. Diagnose that layer before continuing.

## Fixed lab design

```text
aegis-test                         aegis-peer
client role                        server role

veth-test                          veth-peer
10.10.0.1/24      ← veth pair →   10.10.0.2/24
                                    TCP 22
```

Temporary root:

```text
/tmp/aegislab-namespace-ssh
```

Target account:

```text
motafeq
```

## Runtime-specific values

The following values change after reconstruction and must be reinspected:

- key fingerprints;
- PIDs;
- client ephemeral ports;
- veth interface indexes;
- packet sequence numbers;
- timestamps.

Do not reuse these values from an earlier worklog as current truth.

---

# Part I — Inspect before rebuilding

## 1. Define the temporary root

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh
```

This assigns a shell variable. It does not create a directory.

## 2. Inspect the current runtime

```bash
echo "=== NETWORK NAMESPACES ==="
sudo ip netns list

echo
echo "=== TEMPORARY LAB FILES ==="
if sudo test -e "$LAB_ROOT"; then
  sudo find "$LAB_ROOT" \
    -maxdepth 2 \
    -printf '%M %u:%g %p\n' |
    sort
else
  echo "MISSING: $LAB_ROOT"
fi

echo
echo "=== SSH-RELATED PROCESSES ==="
ps -eo user,pid,ppid,stat,cmd --forest |
  grep -E '(^USER|[s]shd|[s]sh .*10\.10\.0\.2)'
```

This answers three separate questions:

- Do the named network namespaces exist?
- Does temporary identity/configuration state exist?
- Are lab SSH client or server processes still running?

## 3. Decide the path

### Everything is missing

Follow the complete reconstruction beginning at Part II.

### Namespaces are missing but `/tmp` state survives

Rebuild only the networking substrate, then verify the existing keys and configuration before starting the server.

### Namespaces survive but `/tmp` state is missing

Keep the network substrate, recreate the temporary directories, identities, authorization, and server configuration.

### Most state survives

Do not regenerate keys. Validate the existing configuration, restart only missing processes, and reinspect all runtime-specific values.

### State is inconsistent and you want a clean reconstruction

First stop any lab client and foreground lab server processes. Do not use broad commands such as `pkill sshd`, because they could affect unrelated SSH processes.

After confirming no lab SSH processes remain:

```bash
sudo ip netns del aegis-test 2>/dev/null || true
sudo ip netns del aegis-peer 2>/dev/null || true

case "$LAB_ROOT" in
  /tmp/aegislab-namespace-ssh)
    sudo rm -rf -- "$LAB_ROOT"
    ;;
  *)
    echo "Refusing to remove unexpected LAB_ROOT: $LAB_ROOT" >&2
    return 1 2>/dev/null || exit 1
    ;;
esac
```

Deleting the namespaces also removes their veth endpoints. Leave `/run/sshd` alone; it is a general OpenSSH runtime directory, not private lab state.

---

# Part II — Verify prerequisites

## 4. Confirm required commands

```bash
for cmd in ip ssh ssh-keygen ss tcpdump install stat ping; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf 'FOUND   %-12s %s\n' "$cmd" "$(command -v "$cmd")"
  else
    printf 'MISSING %-12s\n' "$cmd"
  fi
done

if sudo test -x /usr/sbin/sshd; then
  echo "FOUND   sshd         /usr/sbin/sshd"
else
  echo "MISSING sshd         /usr/sbin/sshd"
fi

id motafeq
```

Required responsibilities:

- `ip`: namespaces, links, addresses, and routes;
- `ssh`: client;
- `sshd`: server;
- `ssh-keygen`: identities and fingerprints;
- `ss`: socket inspection;
- `tcpdump`: packet observation;
- `install`: controlled directory/file creation;
- `stat`: ownership and permission inspection;
- `ping`: basic network validation.

Do not proceed if `motafeq` does not exist or a required tool is missing.

---

# Part III — Rebuild the namespace network

## 5. Create the namespaces

```bash
sudo ip netns add aegis-test
sudo ip netns add aegis-peer
```

A network namespace owns an independent network stack: interfaces, addresses, routes, neighbor state, and sockets.

## 6. Create the veth pair

```bash
sudo ip link add veth-test type veth peer name veth-peer
```

A veth pair is a connected pair of virtual Ethernet interfaces. Packets entering one endpoint emerge from the other.

## 7. Move one endpoint into each namespace

```bash
sudo ip link set veth-test netns aegis-test
sudo ip link set veth-peer netns aegis-peer
```

## 8. Assign IPv4 addresses

```bash
sudo ip -n aegis-test address add 10.10.0.1/24 dev veth-test
sudo ip -n aegis-peer address add 10.10.0.2/24 dev veth-peer
```

Assigning each `/24` address also creates a directly connected route for `10.10.0.0/24`.

## 9. Bring interfaces up

```bash
sudo ip -n aegis-test link set lo up
sudo ip -n aegis-peer link set lo up
sudo ip -n aegis-test link set veth-test up
sudo ip -n aegis-peer link set veth-peer up
```

## Validation gate A — topology and routes

```bash
echo "=== NAMESPACES ==="
sudo ip netns list

echo
echo "=== AEGIS-TEST ==="
sudo ip -n aegis-test -br address
sudo ip -n aegis-test route

echo
echo "=== AEGIS-PEER ==="
sudo ip -n aegis-peer -br address
sudo ip -n aegis-peer route
```

Required evidence:

```text
aegis-test:
  veth-test UP
  10.10.0.1/24
  10.10.0.0/24 dev veth-test

aegis-peer:
  veth-peer UP
  10.10.0.2/24
  10.10.0.0/24 dev veth-peer
```

`lo` may display state `UNKNOWN`; that is normal for loopback and does not mean failure.

## Validation gate B — bidirectional network path

```bash
sudo ip netns exec aegis-test \
  ping -c 2 -W 1 10.10.0.2
```

Required evidence:

```text
2 packets transmitted, 2 received, 0% packet loss
```

This proves basic IPv4/ICMP communication. It does not prove that SSH is configured or listening.

---

# Part IV — Recreate the temporary ownership boundary

## 10. Create the directory structure

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh

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
  -o motafeq \
  -g motafeq \
  -m 700 \
  "$LAB_ROOT/client" \
  "$LAB_ROOT/auth"
```

Responsibilities:

```text
LAB_ROOT  711 root:root
→ permits traversal to known child paths without general listing/modification

server    700 root:root
→ protects the server private host identity and configuration

client    700 motafeq:motafeq
→ protects the client private identities and known_hosts

auth      700 motafeq:motafeq
→ protects the target account authorization file
```

## Validation gate C — directory ownership and permissions

```bash
sudo stat \
  -c '%A %a %U:%G %n' \
  "$LAB_ROOT" \
  "$LAB_ROOT/server" \
  "$LAB_ROOT/client" \
  "$LAB_ROOT/auth"
```

Required evidence:

```text
drwx--x--x 711 root:root       /tmp/aegislab-namespace-ssh
drwx------ 700 root:root       .../server
drwx------ 700 motafeq:motafeq .../client
drwx------ 700 motafeq:motafeq .../auth
```

---

# Part V — Recreate SSH identities

## 11. Generate the server host identity

```bash
sudo ssh-keygen \
  -q \
  -t ed25519 \
  -N '' \
  -f "$LAB_ROOT/server/ssh_host_ed25519_key"
```

This identity lets the client verify the server.

## 12. Generate the authorized client identity

```bash
sudo -u motafeq ssh-keygen \
  -q \
  -t ed25519 \
  -N '' \
  -f "$LAB_ROOT/client/id_ed25519"
```

This identity is allowed to authenticate as `motafeq`.

## 13. Generate the unauthorized test identity

```bash
sudo -u motafeq ssh-keygen \
  -q \
  -t ed25519 \
  -N '' \
  -f "$LAB_ROOT/client/unauthorized_id_ed25519"
```

This is a valid key pair that is deliberately excluded from authorization. It supports a controlled negative case.

`-N ''` creates unencrypted private keys. This is acceptable only because these keys are disposable, local lab identities stored in restricted directories.

## Validation gate D — key modes and ownership

```bash
sudo stat \
  -c '%A %a %U:%G %n' \
  "$LAB_ROOT/server/ssh_host_ed25519_key" \
  "$LAB_ROOT/server/ssh_host_ed25519_key.pub" \
  "$LAB_ROOT/client/id_ed25519" \
  "$LAB_ROOT/client/id_ed25519.pub" \
  "$LAB_ROOT/client/unauthorized_id_ed25519" \
  "$LAB_ROOT/client/unauthorized_id_ed25519.pub"
```

Required evidence:

```text
server private key:       600 root:root
server public key:        644 root:root
client private keys:      600 motafeq:motafeq
client public keys:       644 motafeq:motafeq
```

## Validation gate E — record public fingerprints

```bash
echo "=== SERVER HOST KEY ==="
sudo ssh-keygen -lf \
  "$LAB_ROOT/server/ssh_host_ed25519_key.pub"

echo
echo "=== AUTHORIZED CLIENT KEY ==="
ssh-keygen -lf \
  "$LAB_ROOT/client/id_ed25519.pub"

echo
echo "=== UNAUTHORIZED CLIENT KEY ==="
ssh-keygen -lf \
  "$LAB_ROOT/client/unauthorized_id_ed25519.pub"
```

Record the three fingerprints in the active worklog. They are public identifiers, not secrets. They must all be distinct.

---

# Part VI — Create client authorization

## 14. Install the authorized public key

```bash
install \
  -o motafeq \
  -g motafeq \
  -m 600 \
  "$LAB_ROOT/client/id_ed25519.pub" \
  "$LAB_ROOT/auth/authorized_keys"
```

Only the authorized client's public key is copied. Do not add the unauthorized test key.

## Validation gate F — authorization identity

```bash
echo "=== ORIGINAL AUTHORIZED CLIENT KEY ==="
ssh-keygen -lf \
  "$LAB_ROOT/client/id_ed25519.pub"

echo
echo "=== AUTHORIZED_KEYS ENTRY ==="
ssh-keygen -lf \
  "$LAB_ROOT/auth/authorized_keys"

echo
echo "=== FILE OWNERSHIP AND MODE ==="
stat \
  -c '%A %a %U:%G %n' \
  "$LAB_ROOT/auth/authorized_keys"
```

Required evidence:

- both fingerprints match;
- `authorized_keys` is `600 motafeq:motafeq`.

---

# Part VII — Create the lab SSH server configuration

## 15. Write `sshd_config`

```bash
sudo tee "$LAB_ROOT/server/sshd_config" > /dev/null <<EOF
Port 22
AddressFamily inet
ListenAddress 10.10.0.2

HostKey $LAB_ROOT/server/ssh_host_ed25519_key
PidFile $LAB_ROOT/server/sshd.pid

PubkeyAuthentication yes
AuthorizedKeysFile $LAB_ROOT/auth/authorized_keys
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

Configuration responsibilities:

- listen only on the namespace server address;
- use only the temporary server host key;
- use only the temporary authorization file;
- allow public-key authentication only;
- prohibit root login and password-based paths;
- allow only `motafeq`;
- use `/usr/bin/id` as bounded instructional scaffolding;
- disable forwarding and tunneling features;
- emit verbose authentication logs.

`ForceCommand /usr/bin/id` is not the final canonical normal-login design. It remains temporary scaffolding until that scenario is formally defined.

## Validation gate G — inspect exact configuration

```bash
sudo nl -ba "$LAB_ROOT/server/sshd_config"
```

Do not validate a configuration you have not inspected.

## 16. Ensure the OpenSSH runtime directory exists

```bash
sudo install -d \
  -o root \
  -g root \
  -m 755 \
  /run/sshd
```

## Validation gate H — validate configuration and required files

```bash
sudo /usr/sbin/sshd \
  -t \
  -f "$LAB_ROOT/server/sshd_config"

echo "exit status: $?"
```

Required evidence:

```text
exit status: 0
```

No output before the status is normal. A nonzero status means stop and diagnose before starting the server.

---

# Part VIII — Start and verify the server

Use separate terminals so the foreground server log remains visible.

## Terminal 1 — start the namespace-bound server

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh

sudo ip netns exec aegis-peer \
  /usr/sbin/sshd \
  -D \
  -e \
  -f "$LAB_ROOT/server/sshd_config"
```

Options:

- `-D`: remain in the foreground;
- `-e`: log to standard error in this terminal;
- `-f`: use the lab configuration.

Keep Terminal 1 open.

Expected initial evidence:

```text
Server listening on 10.10.0.2 port 22.
```

## Terminal 2 — verify the listener

```bash
sudo ip netns exec aegis-peer \
  ss -ltnp
```

Required evidence:

```text
LISTEN ... 10.10.0.2:22 ... users:(("sshd",pid=<runtime-pid>,fd=3))
```

This proves a listener exists. It does not prove authentication works.

---

# Part IX — Establish the long-lived authenticated transport

## 17. Reconfirm the server fingerprint

Before accepting any first-use host prompt:

```bash
sudo ssh-keygen -lf \
  "$LAB_ROOT/server/ssh_host_ed25519_key.pub"
```

Compare this exact fingerprint with the fingerprint displayed by the client.

## Terminal 3 — connect from `aegis-test`

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh

sudo ip netns exec aegis-test \
  sudo -u motafeq \
  ssh \
  -v \
  -N \
  -T \
  -i "$LAB_ROOT/client/id_ed25519" \
  -o IdentitiesOnly=yes \
  -o UserKnownHostsFile="$LAB_ROOT/client/known_hosts" \
  -o ServerAliveInterval=15 \
  motafeq@10.10.0.2
```

Responsibilities:

- namespace entry occurs with privilege;
- the actual SSH client runs as `motafeq`;
- only the specified client identity is offered;
- server trust is stored in the lab-specific `known_hosts`;
- `-N` requests no remote command;
- `-T` requests no pseudo-terminal;
- the connection remains available for observation.

On the first connection after key generation:

1. read the displayed server fingerprint;
2. compare it with the independently inspected server public-key fingerprint;
3. type `yes` only when they match exactly.

After authentication, the terminal appears to wait. That is expected: `-N -T` created a live authenticated transport without a shell or command.

`ForceCommand /usr/bin/id` does not run because no session channel or command was requested.

## Validation gate I — inspect both views of one connection

```bash
echo "=== SERVER VIEW: aegis-peer ==="
sudo ip netns exec aegis-peer \
  ss -tnp state established

echo
echo "=== CLIENT VIEW: aegis-test ==="
sudo ip netns exec aegis-test \
  ss -tnp state established
```

Required relationship:

```text
client local:  10.10.0.1:<ephemeral-port>
client peer:   10.10.0.2:22

server local:  10.10.0.2:22
server peer:   10.10.0.1:<same-ephemeral-port>
```

The two rows are opposite views of one TCP connection.

---

# Part X — Optional observability checks

These checks restore the evidence needed for the current AegisLab milestone.

## 18. Process ancestry

```bash
ps -eo user,pid,ppid,stat,cmd --forest |
  grep -E '(^USER|[s]shd|[s]sh .*10\.10\.0\.2)'
```

Expected server shape:

```text
sshd listener
└── sshd: motafeq [priv]
    └── sshd: motafeq
```

Expected client shape:

```text
sudo/ip-netns wrappers
└── sudo -u motafeq wrappers
    └── ssh
```

## 19. Network-namespace membership

```bash
echo "=== AEGIS-PEER PIDS ==="
sudo ip netns pids aegis-peer

echo
echo "=== AEGIS-TEST PIDS ==="
sudo ip netns pids aegis-test
```

`ps --forest` proves ancestry. `ip netns pids` proves current network-namespace membership. They answer different questions.

## 20. Narrow packet capture for connection establishment

Start capture before starting a new client connection:

```bash
sudo ip netns exec aegis-peer \
  tcpdump \
  -i veth-peer \
  -nn \
  -tttt \
  -c 20 \
  'tcp port 22'
```

This can show:

- SYN, SYN-ACK, ACK;
- SSH identification strings;
- endpoints, timestamps, flags, sequence/acknowledgement behavior, and lengths;
- later encrypted traffic metadata.

It cannot reveal encrypted usernames, accepted key fingerprints, authentication results, commands, or payload contents.

## 21. Narrow packet capture for teardown

With a long-lived client connection open:

```bash
sudo ip netns exec aegis-peer \
  tcpdump \
  -i veth-peer \
  -nn \
  -tttt \
  -c 10 \
  'tcp port 22 and (tcp[tcpflags] & (tcp-fin|tcp-rst) != 0)'
```

Then press `Ctrl+C` in the client terminal.

Expected orderly close:

```text
client FIN
server FIN
```

ACK-only packets are excluded by this filter.

---

# Part XI — Stop the lab cleanly

## 22. Stop the client first

In the terminal running the long-lived `ssh -N -T` command, press:

```text
Ctrl+C
```

Expected consequences:

- client ESTABLISHED socket disappears;
- server ESTABLISHED socket disappears;
- per-connection `sshd` processes exit;
- the listener remains.

## 23. Verify teardown while the server remains running

```bash
echo "=== SERVER LISTENER ==="
sudo ip netns exec aegis-peer \
  ss -ltnp

echo
echo "=== SERVER ESTABLISHED ==="
sudo ip netns exec aegis-peer \
  ss -tnp state established

echo
echo "=== CLIENT ESTABLISHED ==="
sudo ip netns exec aegis-test \
  ss -tnp state established

echo
echo "=== SSH PROCESS TREE ==="
ps -eo user,pid,ppid,stat,cmd --forest |
  grep -E '(^USER|[s]shd|[s]sh .*10\.10\.0\.2)'
```

Expected evidence:

- `10.10.0.2:22` remains in LISTEN;
- no ESTABLISHED sockets remain;
- only the listener-side `sshd` process chain remains.

## 24. Stop the server second

In Terminal 1, press:

```text
Ctrl+C
```

Then verify no namespace listener remains:

```bash
sudo ip netns exec aegis-peer \
  ss -ltnp
```

---

# Part XII — Optional complete cleanup

Only run this after stopping the client, server, and packet captures.

```bash
LAB_ROOT=/tmp/aegislab-namespace-ssh

sudo ip netns del aegis-test
sudo ip netns del aegis-peer

case "$LAB_ROOT" in
  /tmp/aegislab-namespace-ssh)
    sudo rm -rf -- "$LAB_ROOT"
    ;;
  *)
    echo "Refusing to remove unexpected LAB_ROOT: $LAB_ROOT" >&2
    return 1 2>/dev/null || exit 1
    ;;
esac
```

Verify cleanup:

```bash
sudo ip netns list
sudo test ! -e "$LAB_ROOT" && echo "temporary lab root removed"
```

Do not remove `/run/sshd`, stop the ordinary SSH service, or delete normal user SSH state.

---

# Troubleshooting by evidence layer

## `ip netns add ...` reports that the namespace already exists

Affected layer: namespace inventory.

Action:

```bash
sudo ip netns list
```

Either reuse and inspect the surviving namespace or perform the clean-reset procedure. Do not blindly continue with duplicate creation commands.

## `ip link add ...` reports that the file exists

Affected layer: veth ownership or partial previous construction.

Inspect:

```bash
ip -br link
sudo ip -n aegis-test -br link 2>/dev/null || true
sudo ip -n aegis-peer -br link 2>/dev/null || true
```

Determine where each endpoint exists before repairing or resetting.

## Ping reports `Network is unreachable`

Affected layer: address/route/interface state.

Inspect:

```bash
sudo ip -n aegis-test -br address
sudo ip -n aegis-test route
sudo ip -n aegis-peer -br address
sudo ip -n aegis-peer route
```

Do not debug SSH until the network layer passes.

## Ping sends requests but receives no replies

Affected layer: veth/interface or peer configuration.

Check that both veth interfaces are UP and both addresses are present.

## `sshd -t` reports `Missing privilege separation directory: /run/sshd`

Repair:

```bash
sudo install -d -o root -g root -m 755 /run/sshd
```

Then rerun the complete validation command.

## `sshd -t` reports a key or configuration permission error

Inspect the exact path and every parent component:

```bash
namei -l "$LAB_ROOT/server/ssh_host_ed25519_key"
namei -l "$LAB_ROOT/auth/authorized_keys"
```

Also inspect:

```bash
sudo stat -c '%A %a %U:%G %n' \
  "$LAB_ROOT" \
  "$LAB_ROOT/server" \
  "$LAB_ROOT/auth" \
  "$LAB_ROOT/server/ssh_host_ed25519_key" \
  "$LAB_ROOT/auth/authorized_keys"
```

## Client reports `Connection refused`

The network path reached the endpoint, but no listener accepted the connection.

Inspect:

```bash
sudo ip netns exec aegis-peer ss -ltnp
```

Then inspect the foreground server terminal and rerun `sshd -t` if necessary.

## Client reports `No route to host` or `Network is unreachable`

Return to topology, addresses, routes, interface state, and ping. Do not change SSH configuration first.

## Client reports a changed host key

This may be expected if the temporary server key was regenerated while an older lab `known_hosts` survived.

First independently inspect the new server fingerprint:

```bash
sudo ssh-keygen -lf \
  "$LAB_ROOT/server/ssh_host_ed25519_key.pub"
```

Only after confirming that regeneration was intentional, remove the lab-specific trust entry:

```bash
rm -f "$LAB_ROOT/client/known_hosts"
```

Reconnect and verify the newly displayed fingerprint. Never bypass the mismatch without understanding why it changed.

## Client ends with `Permission denied (publickey)`

Separate the possible layers:

1. Did TCP connect?
2. Did the server host key verify?
3. Which client key fingerprint was offered?
4. Does that fingerprint match `authorized_keys`?
5. What did the foreground server log report?

Compare:

```bash
ssh-keygen -lf "$LAB_ROOT/client/id_ed25519.pub"
ssh-keygen -lf "$LAB_ROOT/auth/authorized_keys"
```

Also confirm that `IdentitiesOnly=yes` and the intended `-i` path were used.

## The long-lived client appears to hang after authentication

With `-N -T`, this is expected. The client is deliberately maintaining an authenticated transport without a shell, command, or PTY.

Verify with `ss -tnp state established` instead of terminating it as a suspected failure.

## `/usr/bin/id` does not run during the long-lived connection

Expected. `ForceCommand` applies when a session/command channel is requested. `ssh -N -T` requests neither.

## Host `ps` can see processes in both namespaces

Expected. The experiment uses network namespaces only, not PID namespaces.

## Packet capture shows metadata but not authentication details

Expected. After SSH transport encryption begins, packet capture still exposes timing, endpoints, TCP flags, and lengths, but not encrypted authentication or session content.

---

# Reconstruction completion checklist

Do not call the runtime restored until all required statements are supported by current output:

```text
[ ] aegis-test and aegis-peer exist
[ ] veth-test is UP with 10.10.0.1/24
[ ] veth-peer is UP with 10.10.0.2/24
[ ] both namespaces have connected 10.10.0.0/24 routes
[ ] ping from aegis-test to 10.10.0.2 succeeds
[ ] directory owners and modes match the design
[ ] three distinct Ed25519 fingerprints were recorded
[ ] authorized_keys matches the intended client fingerprint
[ ] sshd_config was inspected and validated with exit status 0
[ ] sshd listens only on 10.10.0.2:22 inside aegis-peer
[ ] the client verifies the current server fingerprint
[ ] public-key authentication succeeds with the intended key
[ ] both namespaces show opposite views of one ESTABLISHED four-tuple
[ ] current PIDs and ephemeral port were reinspected rather than reused
```

Passing this checklist means the main namespace SSH lab runtime is restored. It does not by itself complete the canonical repeated-failure scenario, evidence preservation, bounded diagnosis, Docker reproduction, or VM reproduction.