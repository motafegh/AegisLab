# 2026-11-27 — R2.2 networking foundations

- Started 17:51 +03:30 (WSL clock); starting revision ce6e228901e8eb0381decd9d60f4f95fd9a7d627, clean synchronized main.
- AI-operated bounded demonstration; learner reasoning and personal execution pending.
- [Experiment](../../examples/network_foundations.py) and [retained evidence](evidence/2026-11-27-r2-f2-network-foundations.json).

## Observations and limits

Read-only ip -brief link/address, ip -4 route show/get and ip -4 neigh show inspected interfaces, prefix and route/neighbor entries. Host-specific IP/MAC/gateway values intentionally omitted from public retained artifacts. Current WSL kernel 6.18.58.1-microsoft-standard-WSL2, active eth8 has IPv4 /24 and default gateway; route get 192.0.2.20 (documentation address, lookup only, no packet sent) selected eth8 via gateway. Route get 127.0.0.1 selected loopback0 via gateway in table 127, source loopback; lo also present. Do not infer exact WSL networking mode or ordinary lo-only topology. Neighbor table has a gateway mapping in REACHABLE state; does not prove end-to-end reachability.

Python example uses own IPv4 loopback sockets, kernel-assigned ports, timeouts, context-manager cleanup, no external connection or config changes. Bind without listen: ConnectionRefusedError errno 111. After listen, ss -ltn showed LISTEN; two ss -tn ESTAB endpoints after connection, client 43149 and server 42998 in final run. Received hello using TCP stream read loop, UDP bound receiver UNCONN on 44031, two separately received datagrams one/two; no general reliability claim from these successes. Subnet exercise uses ipaddress with illustrative 10.20.0.0/24. Initial run succeeded; refined direct subnet membership and stream receive loop, final run succeeded. No source runtime code changed. 55 existing regression tests passed during initial run; final example rerun passed.

tcpdump installed; narrowly scoped own-port nonpromiscuous capture permission probe returned exit 1/permission denial, no packets retained; no sudo/capability alteration or bypass. TCP handshake is a conceptual illustration, not captured evidence. Live packet capture remains D or earlier explicitly approved practical exercise. Do not claim a packet trace or external communication.

## Readiness and proposed VM direction

WSL reports 20 logical CPUs, 50 GiB total and 49 GiB available guest memory at inspection, 714 GiB free reported inside Linux filesystem, but Windows C: mount only 28 GiB free of 303 GiB. Guest filesystem capacity is not physical host free capacity. VirtualBox executable not found at standard Windows path, not proof absent. Windows-side remote device offline and WSL PowerShell query rejected by tool safety parser before execution; did not bypass. Windows edition, hypervisor compatibility, firmware and alternate physical volume availability unverified. Disk headroom is a potential constraint; do not install or create VM disks until host check and scoped approval. Prefer comparing existing Windows hypervisor capabilities vs VirtualBox, retain WSL and model server; two isolated Linux guests candidate, no bridged/public exposure. No deployment performed.

## Handoff

Teach layers, addressing, prefix, interface versus socket, route selection and next hop, MAC/ARP, TCP vs UDP and stream vs datagram, handshake and observation limits, DNS/ICMP/NAT/firewall basics. Mixed open-ended assessment and prior recall; learner assessment pending. R2.3 cryptography next, R2.4 SSH thereafter. F2 deeper hands-on routing, isolation and capture remain D; R1/B/F1 personal practice remains pending. VM readiness partial; revisit Windows-side access and disk capacity before deployment. No competence promotion.

Relative Markdown link targets checked: 92; none missing.
