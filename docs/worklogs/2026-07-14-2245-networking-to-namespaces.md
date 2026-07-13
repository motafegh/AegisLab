# 2026-07-14 — Networking to namespaces

## Session metadata

- **Started:** 2026-07-14 20:30 +02:00
- **Ended:** 2026-07-14 22:45 +02:00
- **Status:** paused
- **Objective:** Repair the networking prerequisites for the namespace-led SSH Core slice and build a two-endpoint namespace network with observable end-to-end connectivity
- **Primary role:** Teacher
- **Working posture:** Guided discovery
- **Starting revision:** `035cc99`
- **Continues:** [SSH foundations bridge](2026-07-13-1948-ssh-foundations-bridge.md)
- **Project state impact:** Meaningful temporary environment change and learning progress; project handoff should point to study and assessment before SSH

## Live snapshot

- **Current state:** Two named Linux network namespaces, `aegis-test` and `aegis-peer`, were connected by a veth pair. `aegis-test` owns `10.10.0.1/24`; `aegis-peer` owns `10.10.0.2/24`. Three ICMP Echo requests and replies completed with zero observed loss. Matching neighbor entries identify each peer veth MAC address.
- **Active plan:** Pause implementation. The learner studies the [networking-to-namespaces foundations guide](../learning/study-guides/2026-07-14-networking-to-namespaces-foundations.md), then completes an explanation and practical assessment before any SSH configuration.
- **Latest evidence:** `ping -c 3 10.10.0.2` from `aegis-test` returned three replies; namespace neighbor tables matched the MAC addresses previously observed on `veth-test` and `veth-peer`.
- **Blockers:** No technical blocker. Stable recall has not yet been demonstrated; several concepts required repeated reconstruction during the session.
- **Next action:** Reinspect the namespace topology, evaluate the learner's mental model and output interpretation, then proceed to SSH only if the gate is met.

## Scope and success criteria

This session covered only the networking foundation required before SSH:

- interface and address ownership;
- routing-table purpose and route selection;
- selected source addresses and optional gateways;
- ARP/MAC local-link delivery;
- network-namespace isolation;
- veth endpoint ownership;
- address assignment and connected routes;
- basic ICMP connectivity and neighbor evidence.

It excluded SSH, authentication, host logs, packet capture on the veth link, Docker, virtual machines, and pipeline code.

Success for the practical portion meant constructing two isolated networking environments and demonstrating a defensible end-to-end IP path. Learning-slice closure was not claimed because independent explanation and reconstruction remain pending.

## Mini-plan

- [x] Align teaching with the maintained learner profile and learning preferences
- [x] Repair interface, address, route, gateway, source-IP, ARP, and MAC responsibility boundaries
- [x] Inspect the host's real `ip address`, `ip route`, `ip route get`, and `ip neighbor` evidence
- [x] Create and inspect two network namespaces
- [x] Create a veth pair and move one endpoint into each namespace
- [x] Assign addresses, enable interfaces, and inspect connected routes
- [x] Verify ICMP request/reply connectivity and neighbor mappings
- [x] Create a complete study guide
- [ ] Evaluate stable recall and practical reconstruction in the next session
- [ ] Continue to SSH only after the evaluation gate

## Checkpoint timeline

### 20:30 — Teaching scope corrected

- **Observation:** The learner stated that network namespaces, virtual links, and SSH had not been learned and requested alignment with the maintained learner profile.
- **Action:** Reinspected `docs/learning/LEARNER_PROFILE.md` and the supplied `LEARNING-PREFERENCES.md`.
- **Interpretation:** Routing, namespaces, and SSH were missing prerequisites, so assessment before teaching was inappropriate. The session reset to dependency-first instruction.

### 20:45 — Host interfaces and routing inspected

- **Actions:** Ran `ip address`, `ip route`, and three `ip route get` queries.
- **Evidence:**
  - `eth8` owned `192.168.70.107/24`.
  - `eth9` owned `10.1.0.67/32`.
  - `192.168.70.50` selected direct route through `eth8` with source `192.168.70.107`.
  - `104.19.229.21` selected gateway `192.168.70.1` through `eth8`.
  - `8.8.8.8` selected the default route through `eth9` with source `10.1.0.67`.
- **Interpretation:** The real host demonstrated direct, specific-gateway, and default-route outcomes. Source IP selection followed the chosen path. The output did not establish the exact WSL/virtual forwarding or NAT implementation.

### 21:15 — Local-link resolution inspected

- **Action:** Ran `ip neighbor` in the host namespace.
- **Evidence:** `192.168.70.1 dev eth8 lladdr 98:a9:42:92:f1:9e REACHABLE` connected the gateway route to a local-link MAC address. Many `eth9` destinations mapped to one MAC.
- **Interpretation:** Routing selected the next hop before neighbor resolution. The shared `eth9` MAC was consistent with virtual forwarding but did not prove the exact mechanism.

### 21:35 — Network namespaces created

- **Actions:** Created `aegis-test` and `aegis-peer`, inspected their initial interface state, and enabled loopback independently.
- **Evidence:** Each new namespace initially exposed only a down `lo`; after activation each independently owned `127.0.0.1/8`.
- **Interpretation:** Network namespaces isolated interface, address, route, neighbor, and socket state while sharing the host kernel.

### 21:55 — Veth pair constructed and moved

- **Actions:** Created `veth-test` and `veth-peer`, inspected their MACs and peer relationship, then moved one endpoint into each namespace.
- **Evidence:** Host lookups no longer found the endpoints after the move; namespace-local inspection showed `veth-test@if17` linked to `aegis-peer` and `veth-peer@if18` linked to `aegis-test`.
- **Interpretation:** Missing host visibility after the move represented namespace ownership transfer, not deletion.

### 22:15 — Addresses and connected routes configured

- **Actions:** Assigned `10.10.0.1/24` to `veth-test` and `10.10.0.2/24` to `veth-peer`, then enabled both links.
- **Evidence:** Each namespace received a `10.10.0.0/24` directly connected route with its local veth and preferred source address.
- **Interpretation:** The endpoints belonged to one directly connected network, so no gateway was needed.

### 22:25 — End-to-end behavior verified

- **Action:** Ran `sudo ip netns exec aegis-test ping -c 3 10.10.0.2` and inspected neighbor tables in both namespaces.
- **Evidence:** Three requests produced three replies with zero observed packet loss. `aegis-test` mapped `10.10.0.2` to the actual `veth-peer` MAC; `aegis-peer` mapped `10.10.0.1` to the actual `veth-test` MAC.
- **Interpretation:** The complete route-to-local-link-to-peer request/reply path worked for the bounded ICMP test. This did not prove TCP or SSH readiness.

### 22:45 — Study and assessment gate established

- **Action:** Added [Networking to Network Namespaces — Foundations Study Guide](../learning/study-guides/2026-07-14-networking-to-namespaces-foundations.md).
- **Evidence:** The guide records the conceptual dependency chain, commands, decisive outputs, responsibility boundaries, corrections, proof limits, current topology, resumption checks, cleanup commands, and next-session assessment gate.
- **Interpretation:** Implementation should pause. Reading the guide is preparation; the next session must evaluate explanation, output interpretation, reconstruction, and bounded diagnosis before SSH.

## Decisions and reasoning

- Treat the routing and namespace work as a blocking prerequisite for meaningful SSH learning, not as an unrelated networking detour.
- Use the learner's actual host output rather than generic diagrams where possible.
- Separate route selection from ARP/MAC resolution and distinguish final IP destination from local next hop.
- Do not infer an exact NAT, tunnel, proxy-ARP, or WSL mechanism from route and neighbor output alone.
- Leave the namespace topology configured for the next session, but require reinspection because the state is temporary.
- Do not raise durable learner-profile evidence levels until the learner studies and passes the next-session assessment.

## Problems and resolutions

### Concepts became disconnected

- **Symptom:** The learner reported confusion after routing, ARP, MAC, namespace, and SSH questions were introduced too quickly.
- **Affected layer:** Teaching dependency order and mental-model continuity.
- **Resolution:** Stopped questioning, reconstructed the full interface-to-route-to-ARP flow, and resumed with one concept and one practical action at a time.

### “Local or default gateway” model was too coarse

- **Symptom:** The initial mental model placed a binary local check before the routing table.
- **Resolution:** Replaced it with best-route selection, then local delivery, direct route, gateway route, default route, or unreachable outcomes.

### Source IP was mistaken for NAT

- **Symptom:** `src 10.1.0.67` was interpreted as possible translation.
- **Resolution:** Distinguished local source-address selection from later NAT. The exact translation boundary remains unverified.

## Learning and ownership

- **Prior evidence:** Introductory binding, listener, TCP, HTTP, and packet-observation knowledge, strongest around local listeners and ports.
- **Demonstrated with guidance:**
  - interface versus assigned IP address;
  - route purpose and three route outcomes;
  - source-IP selection tied to the chosen path;
  - route before ARP;
  - namespace-specific interfaces and routes;
  - veth pair creation, movement, addressing, and activation;
  - interpretation of successful ICMP and neighbor evidence.
- **Assistance used:** Repeated conceptual reconstruction, exact commands, output interpretation, topology diagrams, and correction of terminology and layer boundaries.
- **Remaining gaps:** Stable recall, independent command reconstruction, route-output interpretation under changed examples, and bounded failure diagnosis.
- **Ownership return:** The next session begins with study-based teach-back and practical assessment before additional implementation.

## Verification

- **Performed:**
  - fetched and used current canonical project, collaboration, worklog, learner-profile, and learning-preference guidance;
  - inspected host interfaces, routes, exact route selections, and neighbor mappings;
  - inspected namespaces before and after loopback activation;
  - inspected veth endpoints before and after namespace transfer;
  - inspected namespace addresses and connected routes;
  - observed three successful ICMP request/reply exchanges;
  - verified peer neighbor mappings against previously observed endpoint MAC addresses;
  - fetched the committed study guide after creation.
- **Not performed:**
  - no TCP/SSH test;
  - no packet capture on the veth path;
  - no controlled failure diagnosis;
  - no independent learner reconstruction;
  - no Docker or VM reproduction;
  - no cleanup.
- **Result:** The bounded two-endpoint IP network worked as observed. Mastery remains unverified.

## Final handoff

- **Outcome:** Paused after successful guided namespace networking experiment and study-guide creation.
- **Repository changes:** Added the study guide and this session worklog.
- **Environment changes:** `aegis-test` and `aegis-peer` remain configured with a live veth pair and addresses `10.10.0.1/24` and `10.10.0.2/24` unless the environment has since restarted or changed.
- **Unresolved work:** Study, evaluation, controlled failure test, then SSH introduction.
- **Next action:** Learner studies the guide and states readiness; evaluator then tests mental model, fresh output interpretation, practical reconstruction, and one bounded failure.
- **Project state update:** Required to reflect the temporary namespace topology and assessment gate.

## Corrections

None beyond the corrections recorded in the checkpoint timeline and study guide.