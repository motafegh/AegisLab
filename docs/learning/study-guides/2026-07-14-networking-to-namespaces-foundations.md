# Networking to Network Namespaces — Foundations Study Guide

**Date:** 2026-07-14  
**Status:** Study and recall guide; not evidence of independent mastery  
**Project position:** Preparation for the first namespace-led SSH Core learning slice  
**Required next gate:** Study this guide, then complete an explanation and practical knowledge check before continuing to SSH

## Purpose

This guide reconstructs the complete learning path and practical experiment from the session. It is designed to be studied before the next AegisLab session.

The session began with familiar process, listener, address, port, and TCP concepts. It then repaired the missing dependency chain needed for the first Core experiment:

```text
network interface and assigned IP address
        ↓
routing-table decision
        ↓
selected interface, source IP, and optional gateway
        ↓
ARP and local-link MAC address
        ↓
network namespace isolation
        ↓
virtual Ethernet pair
        ↓
addresses and connected routes inside two namespaces
        ↓
successful packet exchange and neighbor evidence
```

The objective was not to memorize commands. The objective was to understand which component owns each responsibility, what each command observes, and what the output proves or does not prove.

This guide follows the active [Core Charter](<../../plans/AegisLab — Core Charter v1.0.md>), [Initial Journey Plan](<../../plans/AegisLab — Initial Journey Plan.md>), [AI Collaboration Protocol](<../../AegisLab — AI Collaboration Protocol.md>), and [Learner Profile](../LEARNER_PROFILE.md).

---

# 1. Where this fits in AegisLab

The first Core learning slice will eventually create two isolated endpoints, run an SSH server on one side, connect from the other side, and observe the behavior at process, socket, host-log, and packet levels.

Before SSH can be meaningful, the learner must understand the network beneath it:

```text
SSH client process
        ↓
TCP connection
        ↓
source and destination IP addresses
        ↓
routing decision
        ↓
network interface
        ↓
local-link delivery
        ↓
SSH server process
```

This session completed the first network-infrastructure milestone:

- two Linux network namespaces were created;
- each namespace received its own loopback interface;
- a virtual Ethernet pair connected them;
- each side received an IPv4 address;
- each side received an automatically generated connected route;
- ICMP traffic crossed the link successfully;
- each namespace learned the other endpoint's MAC address.

It did **not** yet cover:

- SSH client and server behavior;
- TCP port `22`;
- SSH host keys;
- user authentication;
- SSH logs;
- repeated authentication failures;
- packet capture on the namespace link;
- Docker or virtual-machine variants;
- the shared AegisLab event pipeline.

---

# 2. Foundational distinctions revisited

## 2.1 Program, process, and service

A **program** is executable code stored on disk.

A **process** is a running instance of a program managed by the operating system. A process has state such as:

- a process identifier, or PID;
- memory;
- file descriptors;
- sockets;
- user and permission context.

A **service** describes a capability provided to other processes or users. A manually started process can still act as a service. A service does not have to be managed by `systemd`, although many long-running Linux system services are.

Example:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Here:

- `python3` is the executable program;
- starting it creates a Python process;
- the process runs the `http.server` module;
- functionally, it provides an HTTP service.

## 2.2 Socket and socket operations

A **socket** is an operating-system networking object owned by a process.

These names describe operations, not the socket object itself:

```text
socket()  → create a socket
bind()    → assign a local address and port
listen()  → prepare a TCP socket to receive connection attempts
accept()  → obtain a connected socket for one accepted connection
```

The listening socket remains available for new connection attempts. An accepted client normally receives a separate connected socket.

```text
server process
│
├── listening socket
│     127.0.0.1:8000
│
└── connected socket
      local 127.0.0.1:8000
      peer  127.0.0.1:<ephemeral-port>
```

## 2.3 URL and TCP recap

For:

```text
http://127.0.0.1:8000/hello
```

The components are:

```text
scheme: http
host:   127.0.0.1
port:   8000
path:   /hello
```

Because the host is already an IP address, this request does not require DNS resolution.

The introductory TCP establishment sequence is:

```text
client → server: SYN
server → client: SYN-ACK
client → server: ACK
```

After establishment, the connection can carry application data such as an HTTP request.

The connection is identified at introductory depth by the TCP four-tuple:

```text
client IP + client port + server IP + server port
```

---

# 3. Network interfaces and `ip address`

## 3.1 The problem a network interface solves

A Linux environment may have several possible networking connection points. Each can lead to a different networking path.

A **network interface** is an operating-system-managed connection point through which networking traffic can enter or leave a networking environment.

Examples observed in the host environment included:

```text
lo
eth8
eth9
```

An interface is not an IP address:

```text
interface ≠ IP address
```

The interface is the networking object. An IP address is an address assigned to that object.

## 3.2 What `ip address` asks

```bash
ip address
```

This asks the Linux kernel:

> Which network interfaces exist, what state are they in, and which addresses are assigned to them?

The relevant observed host output was:

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever

15: eth8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 02:15:de:f5:eb:e9 brd ff:ff:ff:ff:ff:ff
    inet 192.168.70.107/24 brd 192.168.70.255 scope global noprefixroute eth8
       valid_lft forever preferred_lft forever

16: eth9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:03:fa:17 brd ff:ff:ff:ff:ff:ff
    inet 10.1.0.67/32 brd 10.1.0.67 scope global noprefixroute eth9
       valid_lft forever preferred_lft forever
```

Several other `eth*` interfaces existed but were down. They were not required for the active explanation.

## 3.3 Reading the interface header

Example:

```text
15: eth8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
```

Interpretation:

| Field | Meaning at the required depth |
|---|---|
| `15` | Kernel interface index |
| `eth8` | Interface name |
| `UP` | Administratively enabled |
| `LOWER_UP` | Underlying link considered operational |
| `BROADCAST` | Supports broadcast-style local-link traffic |
| `MULTICAST` | Supports multicast traffic |
| `mtu 1500` | Maximum Transmission Unit configured for the interface |

**MTU** means **Maximum Transmission Unit**. At the current depth, it is the largest packet size the interface normally carries without needing fragmentation at that layer. Detailed MTU behavior is deferred.

## 3.4 Reading the IPv4 address line

Example:

```text
inet 192.168.70.107/24 brd 192.168.70.255 scope global noprefixroute eth8
```

Interpretation:

| Field | Meaning |
|---|---|
| `inet` | IPv4 address follows |
| `192.168.70.107` | IPv4 address assigned to `eth8` |
| `/24` | First 24 of 32 IPv4 bits form the network prefix |
| `brd 192.168.70.255` | Broadcast address for this subnet |
| `scope global` | Not restricted to host-only loopback scope |
| `eth8` | Interface owning the address |

For the active depth:

```text
address: 192.168.70.107/24
network: 192.168.70.0/24
```

A `/24` leaves eight bits outside the network prefix. Full subnet calculation, reserved addresses, and address planning are deferred.

## 3.5 Loopback

Observed:

```text
interface: lo
IPv4:     127.0.0.1/8
scope:    host
```

The loopback interface provides networking inside the same Linux networking environment.

```text
127.0.0.1
→ this networking environment itself
→ no ordinary external interface path
→ no ARP required
```

This connects to the previous HTTP listener experiment on `127.0.0.1:8000`.

## 3.6 The `eth9` `/32` address

Observed:

```text
inet 10.1.0.67/32 ... eth9
```

This means `eth9` owns the exact IPv4 address `10.1.0.67`. A `/32` does not describe an ordinary connected subnet like `/24`.

The output did not prove which surrounding technology created this configuration. It may be related to virtual, tunneled, VPN-like, or WSL networking, but that is a hypothesis until independently inspected.

## 3.7 What `ip address` proves and does not prove

It proves:

- the listed interfaces exist;
- their shown state at the time of observation;
- their assigned addresses;
- their MAC addresses and MTUs where displayed.

It does not prove:

- which path Linux will select for a destination;
- which gateway will be used;
- whether the internet is reachable;
- whether a firewall permits traffic;
- whether a remote system is alive.

Those path questions belong to routing.

---

# 4. Routing and `ip route`

## 4.1 The problem routing solves

The host had more than one active network interface:

```text
eth8
eth9
```

When a process wants to reach a destination IP, Linux must select a path. It cannot blindly transmit through every interface.

A **route** is a kernel rule matching a destination to a networking path.

The routing table answers:

```text
For this destination IP:
- which route matches best?
- which interface should be used?
- is there a gateway or next hop?
- which source IP is suitable?
```

The correct model is not simply:

```text
local?  → ARP
remote? → default gateway
```

The correct order is:

```text
destination IP
        ↓
kernel routing-table lookup
        ↓
best matching route
        ↓
local delivery, direct route, gateway route, default route, or unreachable
```

## 4.2 What `ip route` asks

```bash
ip route
```

This asks the kernel to show the current IPv4 routes.

Observed output:

```text
default dev eth9 proto kernel scope link metric 26
104.19.229.21 via 192.168.70.1 dev eth8 proto kernel metric 4256
135.125.201.82 via 192.168.70.1 dev eth8 proto kernel metric 4256
192.168.70.0/24 dev eth8 proto kernel scope link metric 4511
192.168.70.1 dev eth8 proto kernel scope link metric 4256
```

## 4.3 Connected route

```text
192.168.70.0/24 dev eth8 proto kernel scope link metric 4511
```

Interpretation:

```text
destination network: 192.168.70.0/24
outgoing interface:  eth8
gateway:             none shown
```

The route means destinations in `192.168.70.0/24` are directly reachable through `eth8`.

This route corresponds to the address assigned to `eth8`:

```text
ip address:
192.168.70.107/24 on eth8

ip route:
192.168.70.0/24 dev eth8
```

Assigning an address with a prefix can cause Linux to install the corresponding connected route.

## 4.4 Gateway route

```text
104.19.229.21 via 192.168.70.1 dev eth8
```

Interpretation:

```text
final destination: 104.19.229.21
next-hop gateway:   192.168.70.1
outgoing interface: eth8
```

The gateway is the immediate router interface used for this packet. The gateway does not “go through the router”; it is normally the local router address used as the next hop.

A second route established how to reach that gateway:

```text
192.168.70.1 dev eth8 scope link
```

Dependency:

```text
want 104.19.229.21
        ↓
route selects gateway 192.168.70.1
        ↓
gateway is directly reachable through eth8
```

## 4.5 Default route

```text
default dev eth9 proto kernel scope link metric 26
```

`default` means the fallback route used when no more specific route matches.

This default route does not display a conventional `via <gateway>` address. It tells Linux to use `eth9`, while the surrounding virtual network handles onward delivery in a way not fully exposed by this route line.

Do not invent an unseen gateway.

## 4.6 Route specificity and metric

Linux first prefers the most specific matching route.

An exact host route such as:

```text
104.19.229.21 via 192.168.70.1 dev eth8
```

is more specific than:

```text
default dev eth9
```

The exact route therefore wins for `104.19.229.21` even though its metric is numerically higher.

At the current depth:

```text
most specific matching route first
        ↓
metric helps choose among otherwise comparable routes
```

## 4.7 `proto kernel`, `scope link`, and `metric`

| Field | Meaning at current depth |
|---|---|
| `proto kernel` | Route was installed as a consequence of kernel/interface configuration |
| `scope link` | The selected target or next hop is reachable on the associated local link |
| `metric` | Preference value used among comparable routes; lower is generally preferred |

---

# 5. Exact route decisions with `ip route get`

## 5.1 Purpose

```bash
ip route get <destination>
```

This asks:

> Which route would the kernel select for this exact destination?

It performs route selection. It does not need to send an application packet to the destination.

Three cases were tested.

## 5.2 Directly connected destination

Command:

```bash
ip route get 192.168.70.50
```

Output:

```text
192.168.70.50 dev eth8 src 192.168.70.107 uid 1000
    cache
```

Interpretation:

```text
destination:        192.168.70.50
outgoing interface: eth8
source IP:          192.168.70.107
gateway:            none
```

Reason:

```text
192.168.70.50
matches 192.168.70.0/24
therefore use eth8
```

## 5.3 Specific destination through a gateway

Command:

```bash
ip route get 104.19.229.21
```

Output:

```text
104.19.229.21 via 192.168.70.1 dev eth8 src 192.168.70.107 uid 1000
    cache
```

Interpretation:

```text
final destination: 104.19.229.21
next-hop gateway:   192.168.70.1
outgoing interface: eth8
source IP:          192.168.70.107
```

## 5.4 Default route

Command:

```bash
ip route get 8.8.8.8
```

Output:

```text
8.8.8.8 dev eth9 src 10.1.0.67 uid 1000
    cache
```

Interpretation:

```text
destination:        8.8.8.8
outgoing interface: eth9
source IP:          10.1.0.67
explicit gateway:   none shown
```

No more specific route matched, so the default route selected `eth9`.

## 5.5 Why `10.1.0.67` was selected

The host did not have one universal IP address. It owned several addresses:

```text
lo   → 127.0.0.1
eth8 → 192.168.70.107
eth9 → 10.1.0.67
```

After routing selected `eth9`, Linux chose the address assigned to that path as the suitable source:

```text
destination 8.8.8.8
        ↓
default route selects eth9
        ↓
eth9 owns 10.1.0.67
        ↓
source IP becomes 10.1.0.67
```

The source IP is needed because replies require a destination address.

## 5.6 Why not always use `192.168.70.107`

`192.168.70.107` belongs to `eth8`, while the selected path for `8.8.8.8` uses `eth9`.

Using a source address inconsistent with the selected path may cause:

- an unexpected return path;
- source-validation or anti-spoofing rejection;
- firewall or connection-tracking problems;
- NAT or virtual-networking rule mismatch.

Advanced source-specific routing and deliberate source binding exist, but they are deferred.

## 5.7 NAT distinction

**NAT** means **Network Address Translation**.

The line:

```text
8.8.8.8 dev eth9 src 10.1.0.67
```

proves only that Linux selected `10.1.0.67` as its local source IP.

It does not prove where NAT occurs.

A possible later flow is:

```text
inside Linux:
source 10.1.0.67 → destination 8.8.8.8
        ↓
surrounding WSL, Windows, virtual, or router boundary
        ↓
source may be translated before public-network forwarding
```

That is a plausible architecture, but the observed Linux route output alone cannot identify the translating component.

---

# 6. MAC addresses, ARP, and local-link delivery

## 6.1 The problem after routing

Routing selects:

- an outgoing interface;
- a source IP;
- a direct destination or gateway next hop.

On an Ethernet-like local link, Linux still needs a destination MAC address for the frame.

## 6.2 MAC address

**MAC** means **Media Access Control**.

At the required depth, a MAC address identifies a local-link interface target.

Example observed on `eth8`:

```text
link/ether 02:15:de:f5:eb:e9
```

Responsibility distinction:

```text
IP address  → network-layer addressing and routing
MAC address → delivery on the current local Ethernet-like link
```

## 6.3 ARP

**ARP** means **Address Resolution Protocol**.

Its IPv4 responsibility is:

```text
selected next-hop IPv4 address
        ↓
resolve corresponding local-link MAC address
```

Routing happens before ARP:

```text
destination IP
        ↓
routing chooses interface and next hop
        ↓
ARP resolves that next hop when required
        ↓
Ethernet frame is sent
```

ARP does not choose the route.

## 6.4 Direct destination versus gateway

Directly connected case:

```text
final IP destination: 192.168.70.50
next-hop IP:           192.168.70.50
ARP target:            192.168.70.50
frame destination:     destination host MAC
```

Gateway case:

```text
final IP destination: 104.19.229.21
next-hop IP:           192.168.70.1
ARP target:            192.168.70.1
frame destination:     gateway MAC
```

The final IP destination remains remote even when the local Ethernet frame is addressed to a gateway.

## 6.5 Packet inside an Ethernet frame

```text
Ethernet frame
┌─────────────────────────────────────────┐
│ source MAC                              │
│ destination MAC: local host or gateway  │
│                                         │
│   IP packet                             │
│   ┌─────────────────────────────────┐   │
│   │ source IP                       │   │
│   │ final destination IP            │   │
│   │ transport/application payload   │   │
│   └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

Routers replace the local-link frame for each new link while forwarding according to the IP destination.

## 6.6 `ip neighbor`

Command:

```bash
ip neighbor
```

This asks:

> Which local IP-to-link-address mappings does Linux currently know?

The decisive conventional gateway entry was:

```text
192.168.70.1 dev eth8 lladdr 98:a9:42:92:f1:9e REACHABLE
```

Interpretation:

```text
neighbor IP: 192.168.70.1
interface:   eth8
MAC address: 98:a9:42:92:f1:9e
state:       REACHABLE
```

Combined with the route:

```text
104.19.229.21 via 192.168.70.1 dev eth8
```

we obtain:

```text
final IP destination: 104.19.229.21
local next-hop IP:     192.168.70.1
local destination MAC: 98:a9:42:92:f1:9e
```

## 6.7 Unusual `eth9` neighbor behavior

Many public-looking IP addresses on `eth9` mapped to the same MAC address:

```text
172.66.150.169 dev eth9 lladdr 00:15:5d:ae:bf:5e STALE
140.82.114.22 dev eth9 lladdr 00:15:5d:ae:bf:5e STALE
185.125.190.56 dev eth9 lladdr 00:15:5d:ae:bf:5e REACHABLE
104.18.32.47 dev eth9 lladdr 00:15:5d:ae:bf:5e REACHABLE
```

This proves:

```text
many destination IPs
→ one local link-layer MAC
→ interface eth9
```

It is consistent with a surrounding virtual forwarding mechanism. It does not, by itself, prove whether the mechanism is NAT, proxy ARP, a tunnel, WSL virtual networking, or another implementation.

The large unrelated neighbor list is intentionally not reproduced in full because it contained noisy external destination history that was not necessary for the lesson.

## 6.8 Neighbor states

| State | Meaning at current depth |
|---|---|
| `REACHABLE` | Mapping was recently confirmed usable |
| `STALE` | Mapping remains known, but recent reachability confirmation has aged |
| `PERMANENT` | Mapping is fixed rather than dynamically aged in the normal way |

`STALE` does not mean broken.

---

# 7. Network namespaces

## 7.1 The problem namespaces solve

Processes on a normal Linux host usually share one networking environment:

- interfaces;
- IP addresses;
- routes;
- neighbor mappings;
- sockets;
- network-related firewall state.

AegisLab needs two controlled logical endpoints without requiring two physical machines.

A **network namespace** is a Linux-kernel isolation boundary for networking state.

```text
one Linux kernel
│
├── default network namespace
├── aegis-test namespace
└── aegis-peer namespace
```

Each namespace can own its own:

- interfaces;
- IP addresses;
- routes;
- neighbor table;
- listening and connected sockets;
- network-related rules.

A network namespace is not a virtual machine:

```text
network namespace
→ shares the host Linux kernel

virtual machine
→ runs a separate guest kernel
```

## 7.2 Creating the first namespace

Command:

```bash
sudo ip netns add aegis-test
```

Breakdown:

| Part | Meaning |
|---|---|
| `sudo` | Run the privileged namespace operation as administrator |
| `ip` | Linux networking utility |
| `netns` | Network-namespace operations |
| `add` | Create a named namespace |
| `aegis-test` | Namespace name |

The password was entered directly by the learner and was not recorded.

## 7.3 Inspecting inside a namespace

Command:

```bash
sudo ip netns exec aegis-test ip address
```

This means:

```text
run `ip address`
inside `aegis-test`
```

Initial output:

```text
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
```

This proved:

- the namespace had its own `lo` interface;
- it did not automatically expose host interfaces such as `eth8` or `eth9`;
- its loopback interface initially existed in the down state;
- it did not yet have usable external connectivity.

## 7.4 Enabling namespace loopback

Command:

```bash
sudo ip netns exec aegis-test ip link set lo up
```

Inspection:

```bash
sudo ip netns exec aegis-test ip address
```

Result:

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
```

This demonstrated that each namespace has its own independent loopback context.

## 7.5 Creating the second namespace

Commands:

```bash
sudo ip netns add aegis-peer
sudo ip netns list
```

Output:

```text
aegis-peer
aegis-test
```

Then loopback was enabled:

```bash
sudo ip netns exec aegis-peer ip link set lo up
```

Both namespaces independently showed:

```text
lo
└── 127.0.0.1/8
```

The identical address did not mean they shared one loopback interface. Each namespace owned a separate loopback networking object.

At this point:

```text
aegis-test        aegis-peer
   lo                lo
   │                 │
   └── no path ──────┘
```

---

# 8. Virtual Ethernet pair

## 8.1 The problem a veth pair solves

The namespaces were isolated but had no link connecting them.

A **veth pair** means a **virtual Ethernet pair**. It consists of two linked interfaces:

```text
endpoint A ⇄ endpoint B
```

Traffic entering one endpoint appears at the other endpoint.

This can be understood as a virtual cable:

```text
aegis-test                         aegis-peer
    │                                  │
 veth-test  ⇄ virtual connection ⇄  veth-peer
```

## 8.2 Creating the pair

Command:

```bash
sudo ip link add veth-test type veth peer name veth-peer
```

Breakdown:

| Part | Meaning |
|---|---|
| `ip link add` | Create a network interface object |
| `veth-test` | Name of the first endpoint |
| `type veth` | Create a virtual Ethernet pair |
| `peer name veth-peer` | Name of the linked endpoint |

Inspection:

```bash
ip link show veth-test
ip link show veth-peer
```

Output:

```text
18: veth-test@veth-peer: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 5a:f1:66:d6:a0:3b brd ff:ff:ff:ff:ff:ff

17: veth-peer@veth-test: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 12:95:23:0f:13:86 brd ff:ff:ff:ff:ff:ff
```

Evidence:

```text
veth-test ⇄ veth-peer
```

Each endpoint had its own MAC address. Both were down and initially belonged to the host/default namespace.

## 8.3 Moving endpoints into namespaces

Commands:

```bash
sudo ip link set veth-test netns aegis-test
sudo ip link set veth-peer netns aegis-peer
```

Host inspection:

```bash
ip link show veth-test
ip link show veth-peer
```

Output:

```text
Device "veth-test" does not exist.
Device "veth-peer" does not exist.
```

This did **not** mean the interfaces were deleted. Their ownership moved out of the host namespace.

Namespace inspection:

```bash
sudo ip netns exec aegis-test ip link
sudo ip netns exec aegis-peer ip link
```

Relevant output:

```text
# Inside aegis-test
18: veth-test@if17: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 5a:f1:66:d6:a0:3b brd ff:ff:ff:ff:ff:ff link-netns aegis-peer

# Inside aegis-peer
17: veth-peer@if18: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 12:95:23:0f:13:86 brd ff:ff:ff:ff:ff:ff link-netns aegis-test
```

The `@if17` and `@if18` references showed the peer interface indexes. `link-netns` confirmed that the peer lived in the opposite namespace.

---

# 9. Assigning endpoint addresses and enabling the link

## 9.1 Address plan

A small private network was selected:

```text
network:     10.10.0.0/24
aegis-test:  10.10.0.1/24
aegis-peer:  10.10.0.2/24
```

## 9.2 Assigning addresses

Commands:

```bash
sudo ip netns exec aegis-test ip address add 10.10.0.1/24 dev veth-test
sudo ip netns exec aegis-peer ip address add 10.10.0.2/24 dev veth-peer
```

## 9.3 Enabling both veth interfaces

Commands:

```bash
sudo ip netns exec aegis-test ip link set veth-test up
sudo ip netns exec aegis-peer ip link set veth-peer up
```

## 9.4 Inspecting `aegis-test`

Commands:

```bash
sudo ip netns exec aegis-test ip address
sudo ip netns exec aegis-test ip route
```

Relevant output:

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever

18: veth-test@if17: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 5a:f1:66:d6:a0:3b brd ff:ff:ff:ff:ff:ff link-netns aegis-peer
    inet 10.10.0.1/24 scope global veth-test
       valid_lft forever preferred_lft forever
    inet6 fe80::58f1:66ff:fed6:a03b/64 scope link
       valid_lft forever preferred_lft forever

10.10.0.0/24 dev veth-test proto kernel scope link src 10.10.0.1
```

Interpretation:

```text
interface:       veth-test
IPv4 address:    10.10.0.1/24
connected route: 10.10.0.0/24 via veth-test
preferred source: 10.10.0.1
```

## 9.5 Inspecting `aegis-peer`

Commands:

```bash
sudo ip netns exec aegis-peer ip address
sudo ip netns exec aegis-peer ip route
```

Relevant output:

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever

17: veth-peer@if18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 12:95:23:0f:13:86 brd ff:ff:ff:ff:ff:ff link-netns aegis-test
    inet 10.10.0.2/24 scope global veth-peer
       valid_lft forever preferred_lft forever
    inet6 fe80::1095:23ff:fe0f:1386/64 scope link
       valid_lft forever preferred_lft forever

10.10.0.0/24 dev veth-peer proto kernel scope link src 10.10.0.2
```

Interpretation:

```text
interface:        veth-peer
IPv4 address:     10.10.0.2/24
connected route:  10.10.0.0/24 via veth-peer
preferred source: 10.10.0.2
```

## 9.6 Why the routes appeared

Assigning each interface an address with `/24` told Linux that the interface belonged to `10.10.0.0/24`.

Linux installed the directly connected route in each namespace:

```text
10.10.0.0/24 dev <local-veth> proto kernel scope link src <local-address>
```

No gateway was required because both endpoints belonged to the same directly connected network.

---

# 10. End-to-end connectivity test

## 10.1 Purpose of `ping`

`ping` uses **ICMP — Internet Control Message Protocol**.

The active test asked:

> Can the network stack inside `aegis-test` send traffic across `veth-test`, reach `10.10.0.2`, and receive replies from `aegis-peer`?

Command:

```bash
sudo ip netns exec aegis-test ping -c 3 10.10.0.2
```

Breakdown:

| Part | Meaning |
|---|---|
| `ip netns exec aegis-test` | Run inside the first namespace |
| `ping` | Send ICMP Echo Request messages |
| `-c 3` | Send exactly three requests |
| `10.10.0.2` | Peer namespace destination |

## 10.2 Observed output

```text
PING 10.10.0.2 (10.10.0.2) 56(84) bytes of data.
64 bytes from 10.10.0.2: icmp_seq=1 ttl=64 time=35.6 ms
64 bytes from 10.10.0.2: icmp_seq=2 ttl=64 time=0.027 ms
64 bytes from 10.10.0.2: icmp_seq=3 ttl=64 time=0.024 ms

--- 10.10.0.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2088ms
rtt min/avg/max/mdev = 0.024/11.870/35.559/16.750 ms
```

## 10.3 What this proved

It demonstrated that:

- the source namespace had a usable interface and address;
- its connected route selected `veth-test`;
- packets crossed the veth pair;
- `aegis-peer` received the ICMP Echo Requests at `10.10.0.2`;
- `aegis-peer` produced ICMP Echo Replies;
- the replies returned to `aegis-test`;
- all three request/reply exchanges completed;
- no packet loss was observed in this short test.

It did not prove:

- TCP connectivity;
- port `22` availability;
- an SSH server was running;
- SSH authentication would succeed;
- host logs were present;
- packet capture had been performed;
- the path would remain healthy indefinitely.

```text
ping success
≠
SSH success
```

## 10.4 First response delay

The first reply took about `35.6 ms`, while later replies took about `0.027 ms` and `0.024 ms`.

A reasonable hypothesis is that the first exchange included neighbor discovery and setup overhead. The ping timing alone does not conclusively prove ARP was the only cause.

---

# 11. Neighbor evidence inside the namespaces

Commands:

```bash
sudo ip netns exec aegis-test ip neighbor
sudo ip netns exec aegis-peer ip neighbor
```

Output:

```text
10.10.0.2 dev veth-test lladdr 12:95:23:0f:13:86 REACHABLE
10.10.0.1 dev veth-peer lladdr 5a:f1:66:d6:a0:3b REACHABLE
```

## 11.1 From `aegis-test`

```text
peer IP:       10.10.0.2
out interface: veth-test
peer MAC:      12:95:23:0f:13:86
state:         REACHABLE
```

That MAC matched the previously observed MAC of `veth-peer`.

## 11.2 From `aegis-peer`

```text
peer IP:       10.10.0.1
out interface: veth-peer
peer MAC:      5a:f1:66:d6:a0:3b
state:         REACHABLE
```

That MAC matched the previously observed MAC of `veth-test`.

## 11.3 Full demonstrated chain

```text
process in aegis-test chooses 10.10.0.2
        ↓
routing table matches 10.10.0.0/24
        ↓
selects veth-test and source 10.10.0.1
        ↓
ARP/neighbor discovery resolves 10.10.0.2
        ↓
destination MAC = 12:95:23:0f:13:86
        ↓
frame crosses veth-test ⇄ veth-peer
        ↓
aegis-peer receives packet at 10.10.0.2
        ↓
reply follows the reverse path
```

---

# 12. Final topology at session pause

```text
Host Linux kernel
│
├── default network namespace
│   ├── lo
│   ├── eth8: 192.168.70.107/24
│   └── eth9: 10.1.0.67/32
│
├── aegis-test network namespace
│   ├── lo: 127.0.0.1/8
│   ├── veth-test: 10.10.0.1/24
│   ├── MAC: 5a:f1:66:d6:a0:3b
│   └── route: 10.10.0.0/24 dev veth-test src 10.10.0.1
│
└── aegis-peer network namespace
    ├── lo: 127.0.0.1/8
    ├── veth-peer: 10.10.0.2/24
    ├── MAC: 12:95:23:0f:13:86
    └── route: 10.10.0.0/24 dev veth-peer src 10.10.0.2

veth-test ⇄ veth-peer
```

Observed connectivity:

```text
10.10.0.1 → 10.10.0.2
3 ICMP requests sent
3 ICMP replies received
0% observed packet loss
```

---

# 13. Responsibility map

| Component | Responsibility |
|---|---|
| Process | Executes program logic and owns sockets |
| Socket | Kernel networking object used by a process |
| Port | Selects a transport endpoint/listening socket |
| Network interface | Kernel-managed network connection point |
| IP address | Identifies a network-layer source or destination |
| Prefix such as `/24` | Describes which leading address bits form the network prefix |
| Route | Matches destination IPs to a path |
| Gateway | Immediate router next hop for another network |
| Source IP | Address selected for replies to the outgoing packet |
| MAC address | Identifies the local-link frame destination/interface |
| ARP | Resolves a selected IPv4 next hop to a local-link MAC address |
| Network namespace | Isolates networking state inside one Linux kernel |
| veth pair | Connects two virtual Ethernet endpoints |
| ICMP | Provides network-control messages such as Echo Request and Echo Reply |
| `ping` | Uses ICMP Echo to test basic IP request/reply connectivity |

---

# 14. Important corrections made during the session

## Correction 1 — Host and port

Incorrectly compressed:

```text
host = 127.0.0.1:8000
```

More precise:

```text
host = 127.0.0.1
port = 8000
```

## Correction 2 — Listening versus application request

A TCP listening socket waits for connection attempts. HTTP requests arrive after a connection is established and accepted.

## Correction 3 — Socket object versus socket operations

`socket()`, `bind()`, `listen()`, and `accept()` are operations. The socket is the kernel object.

## Correction 4 — Routing before ARP

Incorrect model:

```text
local? → ARP
remote? → default gateway
```

Correct model:

```text
routing-table lookup
        ↓
selected path and next hop
        ↓
ARP if local-link resolution is required
```

## Correction 5 — “Local” ambiguity

These are different:

- destination belongs to this host;
- destination is on a directly connected network.

Host-local loopback does not require ARP. A different directly connected IPv4 host commonly does.

## Correction 6 — ARP and remote destinations

For a remote destination, ARP normally resolves the local gateway or presented next hop, not the remote internet host's physical MAC address.

## Correction 7 — Source address selection

The system does not have one universal IP address. The selected route and interface influence which source address Linux chooses.

## Correction 8 — NAT inference

A private source address does not itself prove NAT. Translation may happen later, but the responsible boundary must be inspected.

## Correction 9 — Missing interface after namespace move

After moving `veth-test` and `veth-peer`, the host reported that the devices did not exist. They were not deleted; they were no longer owned by the host namespace.

## Correction 10 — Successful command versus intended behavior

Creating namespaces and interfaces successfully did not prove communication. The `ping` result and neighbor mappings supplied the end-to-end behavioral evidence.

---

# 15. What is accurate now and what remains simplified

## Accurate at current depth

- Interfaces and IP addresses are separate objects and properties.
- The routing table is consulted before local-link address resolution.
- A route selects an interface and may select a gateway.
- Linux chooses a suitable source IP for the selected path.
- ARP resolves the selected IPv4 next hop to a local-link MAC address.
- A network namespace has isolated networking state inside one kernel.
- A veth pair links two virtual Ethernet interfaces.
- Assigning `/24` endpoint addresses created connected routes.
- Successful ICMP request/reply traffic demonstrated basic IP connectivity.

## Intentionally simplified

- Full subnet and broadcast mathematics;
- longest-prefix matching implementation;
- policy routing;
- reverse-path filtering;
- ARP state machine details;
- Ethernet switching internals;
- namespace implementation details;
- veth queue and offload mechanics;
- ICMP message structure;
- WSL networking implementation;
- NAT location and implementation.

## Deferred until later

- default-gateway configuration inside the lab namespaces;
- namespace-to-internet connectivity;
- Linux bridges;
- firewall rules;
- SSH;
- packet capture on the veth path;
- Docker comparison;
- virtual-machine comparison.

---

# 16. Evidence table

| Observation | What it proves | What it does not prove |
|---|---|---|
| `ip address` shows `eth8` with `192.168.70.107/24` | Address is assigned to that interface at observation time | Which route a destination will use |
| `ip route` shows `192.168.70.0/24 dev eth8` | That network is treated as directly connected through `eth8` | A remote host in that network is alive |
| `ip route get 104.19.229.21` shows `via 192.168.70.1` | Kernel selects that gateway and interface | Gateway successfully forwards the packet |
| `ip neighbor` shows gateway MAC | Kernel knows a local-link mapping | Remote internet delivery succeeds |
| New namespace initially shows only down `lo` | Namespace has separate interface state | Complete isolation of processes/filesystem |
| Veth endpoints disappear from host after move | Host namespace no longer owns them | Interfaces were destroyed |
| Connected routes appear after address assignment | Kernel associated each `/24` address with the local network | Peer connectivity works |
| `ping`: 3 sent, 3 received | Basic ICMP request/reply path worked for that test | SSH or TCP works |
| Namespace neighbor entries match peer MACs | Local-link resolution learned the actual veth peers | Long-term stability or security |

---

# 17. Complete command sequence from the practical lab

The following is the ordered command sequence used during the namespace experiment.

## Inspect host networking

```bash
ip address
ip route
ip route get 192.168.70.50
ip route get 104.19.229.21
ip route get 8.8.8.8
ip neighbor
```

## Create and inspect the first namespace

```bash
sudo ip netns add aegis-test
sudo ip netns exec aegis-test ip address
sudo ip netns exec aegis-test ip link set lo up
sudo ip netns exec aegis-test ip address
```

## Create and prepare the second namespace

```bash
sudo ip netns add aegis-peer
sudo ip netns list
sudo ip netns exec aegis-peer ip link set lo up
sudo ip netns exec aegis-test ip address
sudo ip netns exec aegis-peer ip address
```

## Create and inspect the veth pair

```bash
sudo ip link add veth-test type veth peer name veth-peer
ip link show veth-test
ip link show veth-peer
```

## Move each veth endpoint

```bash
sudo ip link set veth-test netns aegis-test
sudo ip link set veth-peer netns aegis-peer

ip link show veth-test
ip link show veth-peer
sudo ip netns exec aegis-test ip link
sudo ip netns exec aegis-peer ip link
```

## Assign addresses and enable the interfaces

```bash
sudo ip netns exec aegis-test ip address add 10.10.0.1/24 dev veth-test
sudo ip netns exec aegis-peer ip address add 10.10.0.2/24 dev veth-peer

sudo ip netns exec aegis-test ip link set veth-test up
sudo ip netns exec aegis-peer ip link set veth-peer up
```

## Inspect both endpoint configurations

```bash
sudo ip netns exec aegis-test ip address
sudo ip netns exec aegis-test ip route

sudo ip netns exec aegis-peer ip address
sudo ip netns exec aegis-peer ip route
```

## Test and inspect connectivity evidence

```bash
sudo ip netns exec aegis-test ping -c 3 10.10.0.2
sudo ip netns exec aegis-test ip neighbor
sudo ip netns exec aegis-peer ip neighbor
```

---

# 18. Current environment and safe resumption

At the end of the session, the named namespaces and veth link remained configured.

Inspect before relying on them tomorrow:

```bash
sudo ip netns list
sudo ip netns exec aegis-test ip address
sudo ip netns exec aegis-test ip route
sudo ip netns exec aegis-peer ip address
sudo ip netns exec aegis-peer ip route
```

The state is temporary kernel/network configuration. It may not survive a reboot or environment restart. Current evidence must be reinspected before continuing.

Do not assume the topology still exists only because this guide records it.

## Cleanup commands for later

These commands are recorded for controlled cleanup after the learning slice or if the topology must be reset:

```bash
sudo ip netns delete aegis-test
sudo ip netns delete aegis-peer
```

Deleting the namespaces removes their namespace-owned veth endpoints. Before cleanup, verify that no important process is running inside either namespace.

Do **not** run cleanup merely because it is documented here. Cleanup should occur when the active session explicitly decides to remove or rebuild the topology.

---

# 19. Study procedure before the next session

Study this guide in the following order:

1. Reconstruct the responsibility chain without commands:

   ```text
   interface → address → route → next hop → ARP/MAC → namespace → veth → packet exchange
   ```

2. Redraw the final topology from memory.
3. Explain the difference between:
   - interface and IP address;
   - route and ARP;
   - final destination and local next hop;
   - IP address and MAC address;
   - host namespace and network namespace;
   - veth endpoint and veth pair;
   - successful `ping` and successful SSH.
4. Read each command and state the question it answers before reading its output.
5. Explain the decisive output lines in your own words.
6. Record any part that remains unclear rather than memorizing wording.

Do not treat reading once as mastery.

---

# 20. Assessment gate for the next session

The next session must begin with evaluation before continuing to SSH.

The evaluation should include:

## Mental-model explanation

Explain, without reading the guide:

```text
How a process trying to reach 10.10.0.2 causes Linux to select veth-test,
choose source 10.10.0.1, resolve the peer MAC, and deliver the packet.
```

## Responsibility matching

Match each responsibility to:

- interface;
- IP address;
- route;
- gateway;
- ARP;
- MAC address;
- network namespace;
- veth pair.

## Output interpretation

Interpret fresh output from:

```bash
ip address
ip route
ip route get <destination>
ip neighbor
ip netns list
sudo ip netns exec <namespace> ip address
```

## Practical reconstruction

At an appropriate assistance level, verify or reconstruct:

- two namespaces;
- loopback enabled on both;
- one veth endpoint in each namespace;
- endpoint addresses;
- connected routes;
- successful connectivity;
- matching neighbor evidence.

## Failure reasoning

Diagnose one safe bounded failure, such as:

- one veth interface is down;
- one endpoint address is missing;
- the destination address is wrong;
- the peer namespace does not exist.

The test must evaluate taught material only. It must distinguish guided reconstruction from independent capability.

---

# 21. Next movement after the gate

Only after the learner studies this guide and demonstrates the required understanding should the journey continue to the SSH layer:

```text
SSH client and SSH server roles
        ↓
TCP port 22 and listener
        ↓
SSH protocol negotiation
        ↓
server host identity
        ↓
user authentication
        ↓
encrypted session
        ↓
process, socket, host-log, and packet evidence
```

The next practical Core objective will be to prepare an SSH server in the target namespace and connect from the client namespace without changing the already understood network semantics.

---

# 22. Final session conclusion

The session established a real, observed two-endpoint network using Linux network namespaces.

The strongest demonstrated result was not merely that `ping` succeeded. It was the connected evidence chain:

```text
namespace-owned interfaces
        ↓
assigned IPv4 addresses
        ↓
automatically generated connected routes
        ↓
peer MAC resolution
        ↓
three successful ICMP request/reply exchanges
```

The learner completed the commands with step-by-step guidance and repeatedly requested reconstruction of the mental model when concepts became disconnected. Therefore, this guide records **guided practical evidence**, not stable independent mastery.

The session is paused intentionally. The next action is study, then assessment, then SSH.