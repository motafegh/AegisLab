# 2026-07-16 — Namespace SSH observability handoff

## Session outcome

The temporary WSL runtime had disappeared, so the namespace SSH lab was reconstructed from the documented design. The session then completed live correlation of one authenticated SSH transport across network namespaces, process ancestry, socket ownership, TCP establishment, encrypted traffic visibility, and orderly teardown.

## Runtime rebuilt

- `aegis-test`: `veth-test`, `10.10.0.1/24`
- `aegis-peer`: `veth-peer`, `10.10.0.2/24`
- connected route in both namespaces: `10.10.0.0/24`
- ICMP verification: 2 transmitted, 2 received, 0% loss
- temporary root: `/tmp/aegislab-namespace-ssh`
- lab listener: `10.10.0.2:22`
- ordinary WSL SSH service: untouched

Current public fingerprints:

```text
server host key:
SHA256:W4wUFw9uwvVnz7NrDfCLgWt+Um+N5NeK5hAHdUTU7xs

authorized client key:
SHA256:cZ3muVbww315suKD8+fpNBMRQJZTp64YpNPBALN6osY

unauthorized test key:
SHA256:rA1BVogOYbSx7j5IJ312AyNgWtcxaQ69DOc5QuVGmxg
```

These are runtime-specific public identifiers, not secrets.

## Live connection correlation completed

Authenticated long-lived connection:

```text
10.10.0.1:50420 ↔ 10.10.0.2:22
```

Client:

```text
ssh PID 158898
network namespace: aegis-test
socket FD: 3
```

Server:

```text
listener PID 157590
└── privileged connection PID 158899
    └── authenticated motafeq child PID 159032
```

All three server processes were members of `aegis-peer`. The actual client and its inner sudo wrappers were members of `aegis-test`.

Evidence-source distinctions established:

- `ps --forest` showed ancestry and effective users.
- `ip netns pids` showed current network-namespace membership.
- `ss -tnp` showed TCP endpoints and process ownership.
- Host `ps` could see all PIDs because only networking, not PID state, was namespaced.

## Teardown correlation completed

After stopping only the client:

- both namespace ESTABLISHED tables became empty;
- per-connection `sshd` PIDs exited;
- listener PID `157590` remained;
- `10.10.0.2:22` remained in LISTEN.

This demonstrated the difference between the long-lived server listener and per-connection process lifetime.

## Packet evidence completed

Captured connection:

```text
10.10.0.1:57880 ↔ 10.10.0.2:22
```

Observed:

- TCP SYN, SYN-ACK, ACK;
- client and server SSH identification strings;
- later encrypted SSH packets with visible timing, endpoints, TCP flags, sequence/acknowledgement behavior, and lengths;
- client FIN followed by server FIN;
- no kernel packet drops.

Visibility boundary:

Packet evidence did not reveal username, accepted key fingerprint, authentication result, command, or encrypted payload content. Those require client output, server logs, or host evidence.

## Pause state

At the pause point:

- the client connection had been closed;
- no ESTABLISHED SSH sockets remained;
- no per-connection `sshd` processes remained;
- the foreground listener was still expected to be running unless manually stopped after the session;
- namespaces and `/tmp` state might disappear if WSL stops.

## Exact next step

Resume by inspecting survival of the namespaces, temporary files, and listener. Then collect the foreground server log lines for the captured connection from:

```text
Connection from 10.10.0.1 port 57880
```

through the final disconnect/close line.

Correlate those log events with the already observed client, socket, process, and packet evidence. After that, define the canonical experiment contract before generating further traffic:

1. one normal authorized authentication;
2. a fixed-count repeated unauthorized-key case;
3. explicit start and end markers;
4. separately maintained expected truth;
5. time bounds and abort conditions;
6. cleanup and reconstruction procedure;
7. one bounded failure to predict, diagnose, repair, and revalidate.

Do not move to Docker until the namespace scenario contract, evidence checklist, bounded diagnosis, cleanup, and reduced-prompt explanation are complete.
