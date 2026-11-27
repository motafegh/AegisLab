# Foundational knowledge rebuild and practical learning sequence

**Adopted:** 2026-11-26, owner instruction. **Authority:** supporting learning execution plan under the [Capability Execution Map v2](<../plans/AegisLab — Capability Execution Map v2.md>) and [Learning and Technology Strategy](../definition/learning-and-technology-strategy.md). Current competence belongs in the [Learning Ledger](LEARNING_LEDGER.md); tool adoption/competence belongs in the [industry register](../plans/INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md). This is not another product roadmap.

## Reset baseline

The learner explicitly reports forgetting all learning and practice before the recent AegisLab return (2026-11-22). Treat ALL pre-return concepts and skills as unavailable prerequisites until personally re-established. Historical records remain truthful historical observations only: do not erase them, promote their learning depth to the present, or resume their old execution route. The reset also covers presumed knowledge from other projects or prior study; verify it when needed. Do not claim that forgotten knowledge was never encountered.

Retain post-return evidence at its specific demonstrated depth; recheck it when later confusion or a new dependency warrants. Existing software and reproducible historical lab designs are assets, not evidence of present learner competence. No wholesale project restart or automatic downgrade of recently demonstrated skills. Before relying on a concept, use a brief open-ended check when appropriate or teach the minimum complete foundation without assuming earlier learning. Do not use a quiz to require answers to an untaught concept.

## Three connected tracks

| Track | Purpose | Typical progress evidence |
|---|---|---|
| Security and systems | Understand the system being defended, its protocols, attack surfaces and evidence | Explain mechanism, operate an isolated service, inspect telemetry, diagnose a changed case |
| AI and software engineering | Build trustworthy, testable investigation capabilities | Implement/review bounded component, test failures, compare baseline and model output, diagnose |
| Industry tools | Operate established tools and compare their mechanisms with the reference implementation | Write/configure, run, interpret, change and troubleshoot; decide exercise vs integration |

Use one project and the same evidence across tracks. Batch connected concepts and meaningful implementation increments, not a fixed daily or weekly allocation. Include security or system foundations regularly; do not let repeated AI tuning crowd out security learning. A tool introduction or AI-operated demo alone cannot close the personal practical checkpoint.

## Retention and increasing lab realism (2026-11-27)

Embed short delayed recall and transfer across R2–R5 and later stages; maintain weak-topic revisit priorities in the ledger, especially evidence absence, fixed/sliding windows and specification/conversion/execution roles. Correct only the missing prerequisite and keep momentum.

Owner raised a preference for more realistic separate client/server systems. Proposed progression: use loopback for minimal unit demonstrations, then separate network endpoints via authorized namespaces, and compare separate Linux guest VMs on an isolated virtual network for operational SSH/telemetry work. Review host readiness and hypervisor options (Hyper-V or Oracle VirtualBox) during R2.2; propose a bounded two-guest lab for D or an earlier approved foundation exercise if justified. Keep WSL development and local inference intact. Separate VM kernels and service identities are valuable, but do not require VM parity to finish B/C. No cloud deployment, bridged/public lab exposure, hypervisor installation, firewall changes or reboot authorized by this planning note. Any deployment requires explicit scope, isolation verification, resource and compatibility checks, cleanup and applicable owner approval. A dedicated monitoring guest may be added later when sensor visibility and resource needs justify it; do not assume a VM sees other guests' unicast traffic without a suitable observation point.

## Near-term ordered sequence

| ID | Session or increment | Concrete outcome / boundary | Status |
|---|---|---|---|
| R1 | Native Sigma practice during C | Repair fixed/sliding window misunderstanding; teach YAML, rules, logsource/field mapping, conditions and correlation; review pySigma/Sigma CLI and suitable backend/version/license, exercise native parse/validation/conversion in isolated environment; inspect query and test positive/negative/duplicate/boundary cases on synthetic data. If backend cannot execute correlation, document the blocker and execute an available supported case; do not call handwritten SQL native conversion. | AI-operated native parse/check/convert/execute verified (10 cases); learner practice and changed-case diagnosis open |
| R2 | Focused foundations rebuild during C, before further security-dependent decisions | Units F1–F4 below at minimum usable depth; relate SSH decisions to source/target roles, transport and evidence. Start with read-only/nonprivileged demonstrations; deeper practice can proceed in D once scope is approved. | In progress: R2.1 F1 AI-operated process/FD/permission/loopback lab verified; learner assessment pending; F2–F4 next |
| R3 | C2–C5 focused investigator increment | Explicit source/target roles, unknown identity and evidence-quality references; concrete operator question, provisional contract decision, request/token budget and independent validation/fallback. Preserve existing baseline; no real collection or model tools. Avoid endless general prompt tuning. | Open; provisional software exists |
| R4 | C6–C8 evaluation | Fixed cases and independently retained expectations, rubric and reproducible local runner, Promptfoo exercise, controlled model/configuration comparison, human review and usefulness decision. If AI fails usefulness gate, preserve AI OFF and record C acceptance as open or explicitly revise the route with owner approval; never claim useful AI without evidence. | Pending |
| R5 | Stage D operational security | Complete F1–F6 at practical depth; rebuild fresh authorized isolated SSH lab, collect actual host/network observations and separate action truth, compare Wazuh/Zeek as scheduled, prove controlled failure and teardown; no prerequisite assumption from July. | Pending |

R1 first requires only the minimum relevant log and detection prerequisites. If native tooling is temporarily blocked, record cause, owner and revisit before broad custom detection expansion, and advance R2 without losing R1. A small early D-style exercise is allowed only under the map and separate applicable authorization; no uncontrolled service exposure or privileged changes. R2 is not a demand to master all networking before AI work; fill remaining foundations in D and deepen across E–G. No calendar promises.

## Foundation units

| Unit | Start from first principles | Practical evidence and learner assessment | Required depth / placement |
|---|---|---|---|
| F1 Linux and processes | Files/directories, shell, users/groups, ownership and modes, processes/PID, file descriptors, service versus process, stdout/stderr, logs, environment | Read-only inspect files/process/socket owner with ps, ss and journalctl; explain missing permissions and missing entries; diagnose a changed safe case | Minimum during R2; personally apply and diagnose in D/E/F |
| F2 Networking | TCP/IP layers, addresses, subnet/prefix, loopback, interfaces, routes, ARP, ICMP, TCP versus UDP, ports, sockets, listen/connect/established, source/destination, DNS, basic NAT/firewall and segmentation | Trace route/socket state and TCP handshake from authorized or offline evidence; predict unreachable/missing listener case; later configure namespace/veth and verify isolation | Minimum R2; hands-on D; deeper routing/DNS/TLS/NAT/firewall F/G as needed |
| F3 Cryptography and trust | Encoding vs hashing vs encryption; symmetric/asymmetric keys, signatures, fingerprints, key exchange, session keys, authenticity/integrity/confidentiality and trust | Demonstrate digest change and signature verification on disposable data; explain why hash alone is not authenticity, why private key stays local, why server and user identities differ | Minimum R2; apply to SSH D; TLS and service identities F/E |
| F4 SSH (Secure Shell) | Client/server, TCP transport, version/algorithm negotiation, key exchange and server host authentication, encrypted transport, user authentication, channels/sessions, host keys, known_hosts, authorized_keys, permissions | Trace stages and expected observations; inspect OpenSSH documentation/config read-only; explain TCP ESTAB versus user auth versus session; identify what source IP and unknown target mean; do not invent real target identity | Minimum R2; personally run and diagnose in D |
| F5 Isolated operational lab | Namespaces/veth/routes, process lifecycle, bind addresses, isolated sshd, disposable keys, trust/permission checks, scope, abort and cleanup | After approval, reconstruct fresh isolated service; authorized success and controlled failure; correlate process, socket, authentication log and packet capture; demonstrate encrypted visibility limits and safe teardown | D gate; use July runbook as reference only, not competence evidence |
| F6 Security investigation and controls | Threat model, authentication abuse, baseline/normal vs abnormal, detection rules vs incident truth, false positives/negatives, evidence lineage, sensor coverage, source authenticity, missing/conflicting evidence, secure hardening | Record independent action/target truth, distinguish log decisions from actions/effects, diagnose missing sensor and external alert discrepancy; compare controls without weakening host security | R2 introductory where needed; D practical, E/G deeper |

At each unit teach full terminology and responsibilities, show actual observation, then ask open-ended explanation, prediction, code/command reading, changed-case diagnosis or design trade-off. Learner personally performs at least one relevant safe action where access permits; otherwise record AI demo and pending ownership. Keep completed recent knowledge, recheck at transition, and record specific help level. No blanket claim of mastery from unit completion.

## Later connected depth

- E: scoped read-only agent queries, tool authorization, least privilege, service identity, prompt injection and audit; rebuild prerequisites as needed.
- F: Docker/Compose, service boundaries, SQL/storage, observability, failure/recovery; practical Elasticsearch/Kibana search and indexing foundation (review local resource and license constraints before setup).
- G: compare external security workflows with AegisLab; Elastic Security and OpenSearch comparison, Splunk/SPL bounded practical exposure and Suricata; compare field mapping, detection semantics, evidence links and failure handling. The industry register defines exact checkpoints and any justified deferral. No obligation to run all platforms simultaneously.
- Post-Core: deeper distributed Elasticsearch/search operation (shards, replicas, scaling, ingestion, lifecycle, access, recovery, performance and Python integration), event streaming, advanced security/DFIR and applied ML. New problem-driven milestones defined when the first Core supplies evidence, not a promise of exhaustive mastery.

The existing A–G capability gates, authorization boundaries and local-first requirements remain controlling. No install or live security action is authorized solely by this plan.
