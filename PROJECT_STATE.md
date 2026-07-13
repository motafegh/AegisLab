# AegisLab Project State

**Last meaningful update:** 2026-07-13
**Current stage:** Accepted Project Definition v1.0; preparing the first Core learning slice
**Authority:** Non-normative handoff; current evidence and canonical documents override this file

## Current objective

Begin the practical AegisLab journey with one canonical two-endpoint SSH experiment reproduced across Linux network namespaces, Docker containers, and virtual machines.

The namespace variant leads. Docker and VM variants must converge on the same scenario semantics and evidence checklist before the first learning slice closes.

## Next checkpoint

The next checkpoint is complete when:

- Docker Desktop integration with the Ubuntu WSL distribution is confirmed
- A usable Windows VM path is confirmed
- The canonical SSH experiment and cross-environment evidence checklist are defined
- The namespace variant runs and produces understood process, socket, host-log, and packet observations
- Docker and VM variants reproduce the scenario and their differences are explained

No event-pipeline implementation is required before this checkpoint.

## Learner working profile

- Early-intermediate starting point across Linux, networking, Python, and testing
- More than 11 focused hours available per week
- Guided discovery for foundational learning
- Deep independent capability prioritized over speed, feature count, or presentation polish
- AI may teach, structure experiments, review, challenge, and debug; foundational ownership must return to the learner

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

## Verified workstation facts

- WSL2 with Ubuntu 24.04
- 20 logical CPU threads, approximately 50 GiB RAM, and ample available disk
- Python 3.12 and Git available
- `ip`, `ss`, `tcpdump`, SSH client/server binaries, systemd, and journaling available
- Unprivileged user and network namespaces available
- Docker Desktop installed on Windows but not active or integrated with this WSL distribution at last inspection
- Windows reports a hypervisor present; no ready VM workflow has been confirmed
- WSL SSH service disabled and inactive; host keys not yet prepared
- Privileged setup requires deliberate password entry

Reinspect these facts before relying on them for implementation; environment state can change.

## Active blockers and risks

- Docker WSL integration is not yet verified.
- Hyper-V or an alternative local VM manager is not yet confirmed ready.
- SSH identities, host keys, authentication policy, logging, and cleanup are not yet designed.
- A fresh Codex CLI run discovers the root `AGENTS.md`, but its read-only shell sandbox cannot execute until `bubblewrap` is available; this does not block the current desktop workflow.
- Lab endpoints must not become unintentionally reachable from external or ordinary host networks.
- Parallel environment learning can multiply setup work; keep scenario semantics and the evidence checklist shared.

## Immediate next actions

1. Reinspect Docker Desktop and Windows virtualization state.
2. Choose and verify the local VM path, preferring Hyper-V when available.
3. Define the canonical SSH actors, target, cases, safety boundary, observations, and cleanup.
4. Build and explain the namespace variant.
5. Reproduce the experiment in Docker and VMs.
6. Record the comparison before designing the shared Core pipeline.

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
