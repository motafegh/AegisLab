# Networking and Namespace Foundations — Layered Study Edition

**Role:** Primary study path for AegisLab M1 foundations  
**Full reference:** [Networking to Network Namespaces — Foundations Study Guide](../2026-07-14-networking-to-namespaces-foundations.md)  
**Practical reconstruction:** [Namespace SSH Lab Reconstruction Runbook](../../../runbooks/namespace-ssh-lab-reconstruction.md)

## 1. Learning outcome

After this unit, you should be able to explain and safely reconstruct this mechanism:

```text
process chooses destination IP
        ↓
kernel performs route lookup
        ↓
route selects interface, source IP, and next hop
        ↓
ARP resolves the selected IPv4 next hop to a MAC address
        ↓
frame crosses a veth pair
        ↓
peer namespace receives the packet
```

You do not need to memorize every `ip` subcommand. You do need to know which responsibility each object owns and how to validate the resulting state.

---

# Layer 1 — Required mental model

## 2. Interface, address, route, and neighbor are different

### Network interface

A kernel-managed networking connection point.

Examples:

```text
lo
veth-test
veth-peer
```

An interface is not an IP address.

### IP address

A network-layer address assigned to an interface.

```text
veth-test owns 10.10.0.1/24
veth-peer owns 10.10.0.2/24
```

### Route

A kernel rule that matches a destination and selects a path.

A route may identify:

- an outgoing interface;
- a next-hop gateway;
- a suitable source address.

### Neighbor entry

A local-link mapping between an IP next hop and a link-layer address such as a MAC address.

Responsibility chain:

```text
route chooses the next hop
ARP resolves that next hop
```

ARP does not choose the route.

## 3. Directly connected path

The lab endpoints share one IPv4 network:

```text
network:     10.10.0.0/24
aegis-test:  10.10.0.1/24
aegis-peer:  10.10.0.2/24
```

Assigning these addresses causes Linux to create connected routes:

```text
10.10.0.0/24 dev veth-test src 10.10.0.1
10.10.0.0/24 dev veth-peer src 10.10.0.2
```

No gateway is needed because both endpoints are on the same connected network.

## 4. Network namespace

A network namespace isolates networking state inside one Linux kernel.

Each namespace can own separate:

- interfaces;
- addresses;
- routes;
- neighbor state;
- listeners and connected sockets;
- network-related rules.

It does not provide a separate:

- kernel;
- filesystem;
- user database;
- hostname by itself;
- PID namespace.

## 5. Veth pair

A virtual Ethernet pair is two linked virtual interfaces:

```text
aegis-test                         aegis-peer
veth-test  ⇄ virtual Ethernet ⇄   veth-peer
```

Packets entering one endpoint emerge from the other. Each endpoint has its own interface identity and MAC address.

## 6. Loopback

Each namespace has its own `lo` interface.

Both can use `127.0.0.1` because each address belongs to a different network namespace.

```text
aegis-test lo: 127.0.0.1
aegis-peer lo: 127.0.0.1
```

Identical loopback addresses do not mean the namespaces share one loopback interface.

---

# Layer 2 — Minimum practical mechanism

Use the reconstruction runbook for the exact full sequence. The minimum dependency order is:

```text
create namespaces
→ create veth pair
→ move one endpoint into each namespace
→ assign IPv4 addresses
→ bring loopback and veth interfaces up
→ inspect addresses and routes
→ test connectivity
→ inspect neighbor evidence
```

Core command forms:

```bash
sudo ip netns add aegis-test
sudo ip netns add aegis-peer

sudo ip link add veth-test type veth peer name veth-peer
sudo ip link set veth-test netns aegis-test
sudo ip link set veth-peer netns aegis-peer

sudo ip -n aegis-test address add 10.10.0.1/24 dev veth-test
sudo ip -n aegis-peer address add 10.10.0.2/24 dev veth-peer

sudo ip -n aegis-test link set lo up
sudo ip -n aegis-peer link set lo up
sudo ip -n aegis-test link set veth-test up
sudo ip -n aegis-peer link set veth-peer up
```

`ip -n NAME ...` asks `ip` to operate using the named namespace.

Equivalent form:

```bash
sudo ip netns exec NAME ip ...
```

## Validation gate

Inspect before testing:

```bash
sudo ip -n aegis-test -br address
sudo ip -n aegis-test route
sudo ip -n aegis-peer -br address
sudo ip -n aegis-peer route
```

Required state:

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

Then test:

```bash
sudo ip netns exec aegis-test ping -c 2 -W 1 10.10.0.2
```

Successful ping proves that ICMP request/reply traffic worked for that test. It does not prove that SSH exists or port 22 is listening.

---

# Layer 3 — Reading decisive evidence

## `ip address`

Proves:

- the interface exists in that namespace;
- its current administrative/link state;
- the address is assigned.

Does not prove:

- which route a destination will use;
- that the peer is reachable;
- that an application service is available.

## `ip route`

Proves:

- the namespace currently has a route matching the shown destination prefix;
- the route selects the shown interface and source where displayed.

Does not prove:

- that packets successfully cross the path;
- that the peer responds.

## `ping`

Proves:

- the tested ICMP request/reply path worked during the observation.

Does not prove:

- TCP port 22 is open;
- SSH negotiation works;
- authentication succeeds.

## `ip neighbor`

Proves:

- the namespace currently knows a local IP-to-link-address mapping.

Does not prove:

- long-term reachability;
- application success;
- security of the peer.

---

# Layer 4 — Active recall

Close this file before answering.

1. Why does Linux perform a route lookup before ARP?
2. What is the difference between an interface and an IP address?
3. Why do both namespaces have `127.0.0.1` without conflict?
4. Why does assigning `10.10.0.1/24` create a connected route?
5. What does a veth pair provide that two isolated namespaces initially lack?
6. What does successful ping prove, and what does it not prove?
7. Why does moving a veth interface make it disappear from the default namespace's `ip link` output?

## Required own-words explanation

Explain this flow without commands:

```text
A process inside aegis-test sends to 10.10.0.2.
How does Linux select veth-test, use source 10.10.0.1,
resolve the peer MAC, and deliver the packet to aegis-peer?
```

---

# Layer 5 — Changed-case diagnosis

Use one case at a time.

## Case A — Missing address

Observed:

```text
veth-test is UP
but no 10.10.0.1/24 appears
ping: connect: Network is unreachable
```

Reasoning target:

```text
missing address
→ missing connected route
→ no route to 10.10.0.2
→ kernel rejects the send before peer communication
```

## Case B — Interface down

Observed:

```text
address and route exist
veth-test is DOWN
```

Strongest affected layer:

```text
link/interface state
```

Inspect the interface before changing routes or SSH.

## Case C — Wrong destination

Observed:

```text
route covers 10.10.0.0/24
command targets 10.10.1.2
```

The destination does not match the connected `/24` route. Do not diagnose ARP first.

---

# Layer 6 — Mastery gate

This unit is stable enough for the current project when you can:

- draw the two namespaces and veth pair from memory;
- explain interface, address, route, ARP, MAC, namespace, and veth responsibilities;
- interpret fresh address and route output;
- predict the result of one missing-address or link-down case;
- reconstruct the topology using documentation with reduced guidance;
- diagnose one bounded network-path failure without changing unrelated layers.

Passing does not require memorizing every flag.

---

# Optional reference topics

Use the full guide only when needed for:

- host routing and `ip route get` examples;
- default versus host-specific routes;
- source-address selection;
- NAT inference limits;
- WSL-specific observed interfaces;
- extended neighbor-state discussion;
- historical output and corrections;
- full original command chronology.

These are useful reference topics, not mandatory linear study for the namespace SSH substrate.