# AegisLab Project State

**Last meaningful update:** 2026-07-14
**Current stage:** Accepted Project Definition v1.0; first Core networking foundations built, study and assessment pending before SSH
**Authority:** Non-normative handoff; current evidence and canonical documents override this file

## Current objective

Begin the practical AegisLab journey with one canonical two-endpoint SSH experiment reproduced across Linux network namespaces, Docker containers, and virtual machines.

The namespace variant leads. Docker and VM variants must converge on the same scenario semantics and evidence checklist before the first learning slice closes.

The current stop line is before SSH configuration: the learner must first study and demonstrate the interface, routing, ARP/MAC, namespace, veth, and basic-connectivity model established in the first namespace networking session.

## Next checkpoint

The next checkpoint is complete when:

- The learner studies the [Networking to Network Namespaces Foundations Study Guide](docs/learning/study-guides/2026-07-14-networking-to-namespaces-foundations.md)
- The learner passes a focused explanation, output-interpretation, practical-reconstruction, and bounded-failure assessment
- Docker Desktop integration with the Ubuntu WSL distribution is confirmed
- A usable Windows VM path is confirmed
- The canonical SSH experiment and cross-environment evidence checklist are defined
- The namespace variant runs and produces understood process, socket, host-log, and packet observations
- Docker and VM variants reproduce the scenario and their differences are explained

No event-pipeline implementation is required before this checkpoint.

## Learner working profile

The detailed evidence-aware baseline and its maintenance contract are in the [Learner Profile](docs/learning/LEARNER_PROFILE.md).

- Early-intermediate starting point across Linux, networking, Python, and testing
- More than 11 focused hours available per week
- Guided discovery for foundational learning
- Deep independent capability prioritized over speed, feature count, or presentation polish
- AI may teach, structure experiments, review, challenge, and debug; foundational ownership must return to the learner
- The namespace networking experiment was completed with step-by-step guidance; durable evidence levels remain unchanged until the next-session assessment

## Active project decisions

- AegisLab develops an anchored hybrid AI Security Automation Engineer profile.
- Network defense, detection platforms, secure distributed systems, and evidence engineering form the foundation.
- Applied security ML should reach strong practical competence.
- DFIR and threat hunting receive deliberate depth and form the first major post-Core expansion.
- Secure evidence-grounded AI investigation remains the integrating specialization.
- The SSH authentication-abuse scenario is the Core evergreen reference scenario.
- Scenario labs run in namespaces, Docker, and VMs; processing, detection, reporting, and evaluation use one shared Core path.
- Environment-sensitive milestones follow lead-then-converge: namespaces first, then Docker and VM comparison.
- Dynamic malware analysis remains prohibited until a separate charter satisfies the maturity gate with benign substitutes first.
- Substantial AI-assisted sessions use the active collaboration protocol and indexed worklogs; learner ownership and current evidence remain controlling.
- SSH implementation will not begin until the networking-to-namespaces assessment gate is passed.

## Verified workstation and namespace facts

- WSL2 with Ubuntu 24.04
- 20 logical CPU threads, approximately 50 GiB RAM, and ample available disk
- Python 3.12 and Git available
- `ip`, `ss`, `tcpdump`, SSH client/server binaries, systemd, and journaling available
- Rootless user and network namespace creation verified with `unshare`
- Docker Desktop installed on Windows but stopped; its WSL distribution is stopped and integration is unavailable to Ubuntu
- Hyper-V services and cmdlets available; two internal switches exist, but no lab VM has been created
- WSL SSH service disabled and inactive; host-key files exist, while root-level validation and lab configuration remain pending
- Privileged setup requires deliberate password entry
- Named network namespaces `aegis-test` and `aegis-peer` were created
- `aegis-test` was configured with `veth-test` at `10.10.0.1/24`
- `aegis-peer` was configured with `veth-peer` at `10.10.0.2/24`
- Each namespace received a directly connected `10.10.0.0/24` route
- Three ICMP Echo requests from `aegis-test` to `aegis-peer` received three replies with zero observed packet loss
- Neighbor mappings matched the previously observed peer veth MAC addresses

The namespace state is temporary and may change or disappear after restart. Reinspect every fact before relying on it.

## Active blockers and risks

- Stable recall and independent reconstruction of the networking-to-namespace mechanism have not yet been demonstrated.
- Docker Desktop must be started and its Ubuntu WSL integration verified.
- Hyper-V is available, but a Linux lab image and VM have not been selected or created.
- SSH identities, authentication policy, root-level configuration validation, logging, and cleanup are not yet designed.
- A fresh Codex CLI run discovers the root `AGENTS.md`, but its read-only shell sandbox cannot execute until `bubblewrap` is available; this does not block the current desktop workflow.
- Lab endpoints must not become unintentionally reachable from external or ordinary host networks.
- Parallel environment learning can multiply setup work; keep scenario semantics and the evidence checklist shared.

## Immediate next actions

1. Study the networking-to-namespaces guide before the next working session.
2. Reinspect whether `aegis-test`, `aegis-peer`, their addresses, routes, and veth link still exist.
3. Evaluate the learner's mental model, fresh output interpretation, practical reconstruction, and one bounded failure.
4. Introduce SSH client/server, port `22`, host identity, user authentication, and encrypted-session concepts only after the gate passes.
5. Define the canonical SSH actors, target, cases, safety boundary, observations, and cleanup.
6. Build and explain the namespace SSH variant.
7. Start Docker Desktop and verify Ubuntu WSL integration before reproducing the experiment there.
8. Select a Linux image, create the Hyper-V lab VM, and reproduce the experiment.
9. Record the comparison before designing the shared Core pipeline.

## AI collaboration handoff

- The [AI Collaboration Protocol](<docs/AegisLab — AI Collaboration Protocol.md>) defines roles, guided discovery, direct execution, evidence discipline, and session handoff.
- [Worklogs](docs/worklogs/README.md) provide detailed session continuity without turning this file into a diary.
- The current session evidence and assistance record are in [Networking to namespaces](docs/worklogs/2026-07-14-2245-networking-to-namespaces.md).
- The learner-facing review and next-session gate are in the [Networking to Network Namespaces Foundations Study Guide](docs/learning/study-guides/2026-07-14-networking-to-namespaces-foundations.md).

## Authoritative references

- [Project Definition v1.0](<docs/AegisLab — Project Definition v1.0.md>)
- [Core Charter v1.0](<docs/plans/AegisLab — Core Charter v1.0.md>)
- [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>)
- [Governance, Safety, and Boundaries](docs/definition/governance-safety-and-boundaries.md)

## Maintenance contract

- Update this file only after a meaningful decision, environment change, blocker change, or completed learning slice.
- Keep it below 200 lines by removing stale state or moving durable knowledge to the correct canonical or supporting document.
- Do not use it as a session diary, backlog, Git-status snapshot, or substitute for direct inspection.
- Do not store secrets, credentials, malicious samples, personal data, or unverified claims.
- Link to authoritative decisions rather than duplicating their full rationale.
- If this file conflicts with current evidence or a canonical document, correct it as part of the active work.