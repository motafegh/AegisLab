# 2026-07-14 — Namespace SSH foundations

## Session metadata

- **Started:** 2026-07-14 15:05 +02:00
- **Ended:** In progress
- **Status:** active
- **Objective:** Design and begin the controlled SSH client/server experiment across the existing `aegis-test` and `aegis-peer` network namespaces
- **Primary role:** Teacher
- **Working posture:** Guided discovery with embedded evidence checks
- **Starting revision:** `d7933bd`
- **Continues:** [Networking to namespaces](2026-07-14-2245-networking-to-namespaces.md)
- **Project state impact:** The learner elected to continue without a standalone assessment; understanding will be evaluated through the practical SSH work before any mastery claim

## Live snapshot

- **Current state:** `aegis-test` and `aegis-peer` still exist. Their veth endpoints remain up at `10.10.0.1/24` and `10.10.0.2/24`, both connected routes exist, and two fresh ICMP Echo exchanges completed with zero observed loss.
- **Active plan:** Define a bounded SSH experiment, inspect the installed OpenSSH components and inactive host service, create lab-only server identity and configuration, start `sshd` only inside `aegis-peer`, and inspect process/listener evidence before connecting.
- **Latest evidence:** Fresh namespace address, route, and ping output supplied by the learner.
- **Blockers:** SSH identity, authentication policy, logging path, restricted session behavior, and cleanup are not yet finalized.
- **Next action:** Teach the namespace isolation boundary relevant to `sshd`, then perform read-only OpenSSH availability and listener inspection.

## Scope and success criteria

This session begins the SSH portion of the first namespace-led Core slice. It covers the minimum SSH client/server model, safe lab-specific server configuration, process and listening-socket evidence, and the first controlled connection when prerequisites are verified. It excludes Docker, virtual machines, repeated authentication abuse, the shared event pipeline, and production SSH configuration.

Success requires more than a running command: the learner must identify which process listens, which namespace owns the socket, which address and port are reachable, which identity is the server host identity, and what the evidence proves or does not prove.

## Mini-plan

- [x] Reinspect the namespace topology and basic connectivity
- [x] Confirm the cross-environment roadmap remains namespaces, Docker, then VMs
- [ ] Define the namespace SSH safety boundary and scenario contract
- [ ] Inspect OpenSSH client/server availability and existing port-22 state
- [ ] Create lab-only host identity, client identity, configuration, and runtime paths
- [ ] Validate configuration without starting the server
- [ ] Start `sshd` only inside `aegis-peer`
- [ ] Observe process and listening-socket evidence
- [ ] Establish the first controlled client connection
- [ ] Record evidence, learning, cleanup, and handoff

## Checkpoint timeline

### 15:05 — Session resumed and topology reverified

- **Observation:** Both namespaces and veth endpoints persisted, connected routes remained present, and two ICMP requests received two replies.
- **Interpretation:** The network prerequisite is currently operational and can support the SSH experiment.

### 15:10 — Cross-environment plan clarified

- **Observation:** The learner asked whether Docker and the installed VirtualBox application would be ignored.
- **Action:** Reinspected the active Core Charter and Initial Journey Plan.
- **Interpretation:** The project uses lead-then-converge: namespace SSH first, then the same scenario in Docker and separate VMs, followed by comparison. Hyper-V remains the default VM candidate; VirtualBox is an alternative if evidence justifies it.

### 15:15 — Assessment integrated into practical work

- **Decision:** The learner requested continuation without a standalone networking assessment.
- **Interpretation:** Continue with SSH while using predictions, fresh output interpretation, and bounded diagnosis as embedded evidence. Do not mark independent networking mastery solely from reported study completion.

## Decisions and reasoning

- Do not start or reconfigure the WSL host's ordinary SSH service.
- Bind the lab server only to the namespace target address.
- Use lab-specific host keys, client credentials, configuration, PID/runtime files, and cleanup.
- Remember that a network namespace does not isolate the host filesystem or user database; restrict the initial SSH behavior accordingly.
- Preserve the canonical scenario semantics so Docker and VM variants can reproduce them later.

## Problems and resolutions

None yet.

## Learning and ownership

- **Prior evidence:** The learner completed the namespace topology with step-by-step guidance and later reported studying the full guide.
- **Current evidence:** Fresh topology interpretation and SSH evidence are pending.
- **Assistance used:** Concept sequencing, safety framing, command explanation, and evidence checklist design.
- **Remaining gap:** Demonstrate the SSH process/listener/identity/authentication distinctions and trace them through observed output.

## Verification

- **Performed:** Namespace inventory, addresses, routes, and two-packet ICMP exchange.
- **Not performed:** OpenSSH availability inspection, configuration validation, server startup, socket inspection, connection, authentication, logging, or cleanup.
- **Result:** Networking prerequisite currently operational; SSH work not yet started.

## Final handoff

Pending.

## Corrections

None.
