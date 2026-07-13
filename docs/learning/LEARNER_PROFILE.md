# AegisLab Learner Profile

**Status:** Active supporting learning record  
**Baseline imported:** 2026-07-13 from the completed introductory networking/Linux foundation labs  
**Authority:** Evidence-aware and non-normative; observed performance and canonical project documents override this profile

## Maintenance contract

- Update this profile after meaningful demonstrated learning, a corrected misconception, a changed assistance level, or a newly identified gap.
- Record what was demonstrated, the context, the assistance used, and whether the knowledge transferred to a new situation.
- Do not raise an evidence level merely because a command succeeded, a topic was explained, or polished text was produced.
- Preserve important corrections and distinguish current ability from historical baseline claims.
- Keep detailed session chronology in [worklogs](../worklogs/README.md); this file summarizes the learner's current durable profile.
- Never store secrets, credentials, sensitive personal data, malicious samples, or unsafe operational details here.

## Imported baseline: Networking and Linux Foundations

**Date:** 2026-07-13  
**Current stage:** End of introductory networking/Linux foundation labs  
**Next planned stage:** First Web/API security lab

## Why I Wrote This

This document describes what I have actually learned and demonstrated so far. It is not intended to make my knowledge look stronger than it is. I distinguish between topics I have heard about, topics I understand conceptually, tasks I completed with guidance, and tasks I could currently repeat independently.

My mentor does not need access to my repository to understand this profile. The practical work, evidence, limitations, and remaining gaps are summarized here.

## How I Describe My Current Levels

I use two separate scales because being taught something is not the same as being able to use it independently.

### Teaching depth

| Level | Meaning |
|---|---|
| D0 | I have not learned the topic. |
| D1 | I learned its name, purpose, or motivation. |
| D2 | I learned how it connects to surrounding components and responsibilities. |
| D3 | I learned some technical mechanics. |
| D4 | I observed or used it in a practical lab. |

### My demonstrated evidence

| Level | Meaning |
|---|---|
| E0 | I have not been assessed or demonstrated it. |
| E1 | I have partial understanding and still mix up some details. |
| E2 | I demonstrated the basic idea with guidance or correction. |
| E3 | I can currently reconstruct and use the idea at a basic level with limited prompting. |
| E4 | I can independently reproduce, debug, explain, and document it in a fresh situation. |

I do not currently claim E4 in any of these areas. My strongest evidence is E3 in basic binding, listener, address, and port experiments. Most of my TCP, HTTP, TLS, and packet-analysis knowledge is currently E2.

## Labs I Have Worked Through

### 1. Read the Handshake

I observed the path from a hostname to an HTTP response. I performed a DNS lookup, used verbose `curl`, ran a small local HTTP service, and compared client output with server logs.

The practical work is complete. My final personal write-up still needs to be rewritten fully in my own wording.

### 2. Who's Listening

I compared a service bound to `127.0.0.1` with the same service bound to `0.0.0.0`. I inspected listeners, tested different local destination addresses, reproduced a bind conflict, identified the owning process, and observed the listener disappear after the process stopped.

I completed a guided knowledge check. This is currently my strongest lab.

### 3. Traffic Inspector

I captured one local plaintext HTTP request and one external HTTPS request. I saved PCAP files, inspected the packet sequence with `tcpdump`, and opened the local capture in Wireshark.

The practical capture and review are complete. My final recall/knowledge check is still pending, and I do not yet consider myself independently proficient with Wireshark.

## Detailed Current Knowledge

| Topic | Teaching | Evidence | My honest current level |
|---|---:|---:|---|
| Client and server roles | D4 | E3 | Stable at introductory depth |
| URL request flow | D3 | E2 | Basic guided understanding |
| DNS purpose and lookup | D4 | E2 | Stable only at a high level |
| IP address and hostname distinction | D4 | E2–E3 | Mostly stable at current depth |
| Server and ephemeral client ports | D4 | E3 | Stable at introductory depth |
| TCP four-tuple | D3 | E2 | Understood with some prompting |
| TCP three-way handshake | D4 | E2 | Basic guided understanding |
| Binding and listening | D4 | E3 | Strongest current topic |
| `127.0.0.1` and `0.0.0.0` | D4 | E3 | Practically demonstrated |
| Process/listener ownership | D4 | E3 | Practically demonstrated |
| Connection refused | D4 | E3 | Observed and basically understood |
| HTTP request and response structure | D4 | E2 | Basic understanding with corrected terminology |
| TLS purpose and visibility boundary | D4 | E2 | Correct high-level understanding |
| `tcpdump` packet capture | D4 | E2 | Completed with guidance |
| PCAP creation and reuse | D4 | E2 | Completed with guidance |
| Wireshark inspection | D3–D4 | E1–E2 | Early developing skill |
| Linux tools such as `ss` and `ps` | D4 | E2–E3 | Basic practical use |
| Security exposure reasoning | D3 | E2 | Developing |
| Python HTTP-server implementation | D2 | E1 | Intentionally shallow |
| Independent technical reporting | D3 | E1–E2 | Developing; documentation was assisted |

## What I Currently Understand

### Client and server roles

I understand that “client” and “server” are roles played by processes. A client such as `curl` initiates an interaction. A server process listens for connections, receives requests, and returns responses. Both processes can run on the same machine.

I have not studied multi-tier architectures, reverse proxies, load balancers, brokers, peer-to-peer systems, or server concurrency models.

### URLs and request destinations

I can separate these basic parts:

```text
scheme://hostname:port/path
```

I understand that:

- the scheme supplies protocol context, such as HTTP or HTTPS;
- the hostname names the destination;
- DNS can resolve the hostname to one or more IP addresses;
- the port selects the transport service;
- the path identifies an application resource or route.

I initially mixed up the HTTP method, path, and protocol version. I was corrected and can now identify:

```text
GET /hello HTTP/1.1

GET       = method
/hello    = path
HTTP/1.1  = protocol version
```

I have not studied full URL parsing, normalization, encoding, fragments, user information, repeated query parameters, or URL-related security edge cases.

### DNS

I used `dig` to resolve `example.com` and observed multiple IPv4 answers. I understand the current high-level sequence:

```text
hostname → DNS lookup → IP address
```

I understand that DNS normally supplies address information and does not simply choose the application server port in the basic web-request model.

I have not learned DNS resolver internals, recursive versus iterative resolution, authoritative servers, root and top-level-domain servers, caching, TTL, DNS record families, DNS over HTTPS, or DNS over TLS.

### IP addresses and ports

I understand that an IP address identifies the network destination/interface at the depth currently taught. A hostname is a name; an IP address is used for addressing and routing.

I understand that a server normally listens on a known port and the client uses a temporary ephemeral source port. I observed connections such as:

```text
127.0.0.1:41335 → 127.0.0.1:8000
10.1.0.59:40815 → 172.66.147.243:443
```

I understand that the response must return to the correct client port, not merely to “the client computer.”

I know the introductory TCP four-tuple:

```text
client IP + client port + server IP + server port
```

I have not learned subnetting, routing tables, gateways, NAT mechanics, IPv6 mechanics, or port-range classifications in depth.

### TCP connection establishment

I understand the introductory three-way handshake:

```text
SYN → SYN-ACK → ACK
```

My current explanation is:

- the client uses SYN to request connection establishment;
- the server uses SYN-ACK to acknowledge and provide its side of the connection state;
- the client uses ACK to confirm;
- application data can then travel through the established TCP connection.

I have observed these flags in `tcpdump` and Wireshark. I do not yet understand sequence and acknowledgment arithmetic deeply, retransmissions, congestion control, duplicate handling, TCP window mechanics, simultaneous open, or the full TCP state machine.

### Binding and listening

This is the topic I have demonstrated most strongly.

I ran the same service with:

```text
127.0.0.1:8000
```

and observed that a request to `127.0.0.1:8000` succeeded while a request addressed to `192.168.70.107:8000` was refused.

I then ran it with:

```text
0.0.0.0:8000
```

and observed that requests addressed to both `127.0.0.1:8000` and `192.168.70.107:8000` succeeded.

My current understanding is:

- `127.0.0.1` creates a loopback/local-only listener;
- `0.0.0.0` is a wildcard bind covering the machine's local IPv4 interfaces;
- `0.0.0.0` does not mean every IP address on the internet;
- binding to `0.0.0.0` expands possible exposure;
- routing, firewalls, NAT, and network policy can still affect remote reachability.

I initially described this as an address being “outside a range.” The more precise explanation is that the service did not own a listener bound to that destination address and port.

### Listener and process ownership

I used `ss` to inspect a TCP listener and identify:

- listening state;
- local bound address;
- server port;
- owning Python process;
- PID and file descriptor where available.

I used `ps` to inspect the identified process. I observed that:

- a process must own a listening socket;
- stopping the process removes the listener;
- a second ordinary process cannot claim the same conflicting address and port;
- Linux returned `Address already in use` for the conflicting bind.

I understand the introductory lifecycle:

```text
create socket → bind → listen → accept connection → handle data → close
```

I do not understand the socket system calls, kernel socket structures, listen backlog behavior, `SO_REUSEADDR`, `SO_REUSEPORT`, network namespaces, or asynchronous server architecture in depth.

### HTTP request and response

I observed a local request:

```text
GET /hello HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: curl/8.5.0
Accept: */*
```

and response:

```text
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 39

{"message": "Hello from the local API"}
```

I understand the method, path, protocol version, headers, status code, and body at a basic level. I understand that the Python server accepted an HTTP/1.1 request but used HTTP/1.0 for its response because of that simple server implementation.

I have not learned HTTP routing internals, persistent connections, HTTP/2 framing, HTTP/3, caching, cookies, content negotiation, authentication headers, or detailed status-code behavior.

### TLS and HTTPS

I understand the required order:

```text
TCP connection → TLS handshake → protected HTTP exchange
```

I understand that TLS protects application data in transit. In the HTTPS capture, I could still observe IP addresses, ports, packet direction, timing, TCP flags, and approximate payload sizes, but I could not read the HTTP method, path, headers, or response body.

I initially compressed TCP and TLS into an unclear order. I was corrected and now understand that TCP establishes the underlying connection before TLS negotiates protection for the application exchange.

I have not learned certificate-chain verification internals, key exchange mathematics, cipher suites, TLS record mechanics, session resumption, mutual TLS, or modern encrypted-handshake extensions.

### Packet capture with tcpdump

I verified `tcpdump`, listed capture interfaces, applied narrow filters, displayed plaintext payload, saved captures to PCAP files, and reopened them.

My first capture on `lo` produced zero packets. With guidance, I used `-i any` and discovered that my environment presented the local request through `loopback0`.

I learned that an empty capture does not prove that no request happened. Possible causes include:

- wrong interface;
- wrong filter;
- capture started too late;
- no matching traffic.

I completed this troubleshooting with guidance. I do not yet claim that I could independently diagnose every capture failure.

### HTTP versus HTTPS in packet captures

In the plaintext HTTP capture, I could read:

- `GET /hello`;
- HTTP request headers;
- `200 OK`;
- response headers;
- the JSON response body.

In the HTTPS capture, I could see the TCP setup, TLS-related payload exchange, traffic direction, packet lengths, and connection close, but not the readable HTTP exchange.

I understand that unreadable HTTPS payload is expected ciphertext, not a failed capture.

### Wireshark

I installed Wireshark and opened the local HTTP PCAP. I inspected one decoded response packet and saw the layer structure:

```text
frame → capture/link information → IPv4 → TCP → HTTP → JSON
```

I identified:

- source port `8000`;
- client ephemeral destination port;
- TCP stream index;
- TCP payload length;
- FIN, PSH, and ACK flags;
- HTTP response and JSON decoding;
- complete conversation status.

The interface and many advanced fields were confusing. I do not yet consider myself comfortable with Wireshark. I can locate basic request/response evidence with guidance, but I cannot independently perform advanced packet analysis.

### Client, server, and packet perspectives

I understand that the same request can be observed from different positions:

```text
curl -v
→ what the client attempted and received

server log
→ what the application parsed and handled

tcpdump / Wireshark / PCAP
→ what crossed the observed network interface
```

These perspectives should correlate, but they do not contain exactly the same information.

### PCAP evidence

I understand that a PCAP preserves captured packets for later inspection, filtering, verification, and review without recreating the original connection.

I also understand that PCAP files may contain plaintext credentials, tokens, headers, or bodies. My lab captures intentionally contained only controlled, nonsensitive requests.

## Practical Tasks I Have Actually Performed

I have personally run or interacted with these tasks:

- DNS lookup using `dig`;
- external verbose HTTPS request using `curl -v`;
- local HTTP requests using `curl`;
- local service binding to `127.0.0.1` and `0.0.0.0`;
- listener inspection using `ss`;
- interface inspection using `ip`;
- process inspection using `ps`;
- bind-conflict observation;
- connection-refused observation;
- local plaintext packet capture;
- external HTTPS packet capture;
- PCAP creation and offline reading;
- basic Wireshark packet inspection.

I performed these tasks with step-by-step guidance and explanations. I should not represent them as fully independent professional-level work.

## Work That Was Assisted

For honesty, the small Python HTTP server and much of the structured review documentation were created or expanded with AI assistance.

I can currently:

- run the service;
- select its host and port through CLI options;
- explain why safe defaults exist;
- use it to generate controlled network traffic;
- connect its behavior to listener and packet evidence.

I cannot currently explain or recreate the full Python server implementation independently. I have not yet learned `ThreadingHTTPServer`, handler inheritance, server concurrency, or the implementation details of its request lifecycle.

The final review documents are more polished and complete than my unaided writing would currently be. My practical evidence is real, but my independent technical-reporting ability is still developing.

## Mistakes and Corrections That Matter

These corrections are part of my current learning state:

1. I initially mixed up `GET`, `/hello`, and `HTTP/1.1`. I now understand method, path, and protocol version separately.
2. I initially introduced ARP into the local `127.0.0.1` request. Loopback traffic stays inside the local networking stack and does not require ARP for this request.
3. I initially described a failed bind-address test as an IP being outside a “range.” The precise issue was that no listener owned that destination address and port.
4. I initially compressed TCP connection establishment and TLS negotiation into an unclear sequence. TCP establishment comes first, followed by TLS, then protected HTTP.
5. I initially stopped a capture before making the request, producing zero packets. I learned that capture timing matters.
6. I expected `lo` to show the traffic, but the environment exposed it through `loopback0` when capturing on `any`. I learned not to treat an empty capture as proof that no request occurred.

I understand these corrections when reviewed. Some still require further recall practice before I would call them permanently stable.

## What I Can Probably Repeat With Limited Guidance

- Start the prepared local server with a selected bind address and port.
- Use `curl -v` to make a local request.
- Use `ss -ltnp` to locate a listener.
- Explain why `127.0.0.1` and `0.0.0.0` behave differently.
- Identify a server port and client ephemeral port.
- Interpret connection refused when no matching listener exists.
- Capture a controlled request with a provided `tcpdump` command.
- Identify SYN, SYN-ACK, ACK, request payload, response payload, and FIN at a basic level.
- Explain the main visibility difference between HTTP and HTTPS.

## What I Still Need Guidance For

- Designing packet-capture filters from scratch.
- Choosing and troubleshooting capture interfaces independently.
- Interpreting detailed TCP fields and abnormal TCP behavior.
- Using Wireshark beyond basic packet selection and decoding.
- Recreating the Python service from scratch.
- Writing a complete technical report without a template or editing assistance.
- Explaining TCP, HTTP, and TLS precisely under interview pressure without review.
- Moving from networking observations into API security code.

## Topics I Have Not Learned Yet

I have not yet learned these in meaningful depth:

- subnetting and CIDR calculations;
- routing tables and gateway behavior;
- IPv6 operation;
- UDP behavior;
- NAT implementation;
- firewall administration;
- TCP retransmission and congestion control;
- full TCP state transitions;
- advanced socket programming;
- DNS resolver architecture;
- TLS cryptography and certificate validation internals;
- advanced Wireshark analysis;
- production API frameworks;
- authentication and authorization implementation;
- API vulnerability exploitation and remediation;
- SQL injection;
- automated security testing.

These omissions are intentional at this point in the roadmap rather than topics I claim to know.

## My Learning Behavior So Far

I learn best when I understand why a command exists before running it and when each important output line is connected to the system behavior that produced it.

I respond well to controlled comparisons, such as:

```text
127.0.0.1 vs. 0.0.0.0
HTTP vs. HTTPS
client output vs. server log
raw tcpdump vs. Wireshark
process running vs. listener absent
```

I tend to question defaults and abstractions. For example, I asked why the server had default host and port values if the CLI could override them, why the local exercise did not repeat DNS, and whether professional tools replace manual packet inspection.

My main learning risks are:

- moving toward project completion before writing my own explanation;
- using approximately correct ideas with imprecise terminology;
- becoming overloaded by raw output or large interfaces;
- confusing exposure to a topic with stable independent recall.

The teaching pattern that currently works best for me is:

```text
one meaningful concept block
→ one practical action
→ explanation of the output
→ concise review
→ small knowledge check
```

## Overall Honest Assessment

I am no longer at a terminology-only level in introductory networking. I have practical beginner evidence for DNS lookup, HTTP requests, local service binding, listener inspection, and packet capture.

My current profile is approximately:

```text
Conceptual networking foundation:       developing to stable at beginner depth
Hands-on Linux networking observation:  stable with familiar commands
Binding and listener analysis:          strongest current skill
HTTP/TLS traffic visibility:            demonstrated with guidance
Packet-analysis independence:           developing
Wireshark independence:                 early developing
Technical terminology precision:        developing
Independent technical reporting:        developing
Python/API implementation:              beginner and assisted
```

My current demonstrated ceiling is around E3 for basic binding/listener work and E2 for TCP, HTTP, TLS, and packet analysis. I have not demonstrated E4 independence.

I believe I have enough foundation to begin an introductory Web/API security lab, provided that the API implementation and security concepts are taught progressively. I should continue revisiting TCP, HTTP, TLS, and packet evidence during later projects rather than pausing now to master every networking detail.

## Immediate Next Steps

1. Complete the final Traffic Inspector recall check in my own words.
2. Rewrite or complete the remaining personal reflections without presenting assisted text as fully independent writing.
3. Review and commit the networking milestone.
4. Begin the first Web/API security project: build one endpoint with a missing authorization check, demonstrate the flaw, patch it, and test the fix.

## AegisLab continuation

The imported immediate next steps describe the source repository's roadmap at the time of transfer. Within AegisLab, the active sequence is controlled by the [Initial Journey Plan](<../plans/AegisLab — Initial Journey Plan.md>) and begins with the namespace-led SSH Core experiment.

Future updates should integrate new evidence into the relevant sections above rather than append a session diary. When a topic materially advances, record the date and evidence source in concise wording and retain unresolved gaps.

