# AegisLab — Initial Journey Plan

**Status:** Active working plan  
**Purpose:** Preserve the sequence from the accepted project definition to the first bounded implementation journey  
**Canonical definition:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)  
**Execution companion:** [AegisLab — Core Execution Map](<AegisLab — Core Execution Map.md>)  
**Deferred-idea control:** [AegisLab — Deferred Ideas and Review Triggers](<AegisLab — Deferred Ideas and Review Triggers.md>)

---

AegisLab should avoid turning learning by doing into months of project-governance writing.

The project definition and Core Charter are accepted. Understanding will be consolidated continuously at learning-slice and module boundaries through prediction, implementation, observation, comparison, explanation, controlled failure, and debugging.

The operating principle is:

> Define enough to act safely and coherently, build one bounded slice, then consolidate knowledge before expanding.

The Core Execution Map translates this governing sequence into current milestone gates and required evidence. It is supporting guidance rather than a replacement for this plan.

## 1. Starting position

The current working assumptions are:

- The learner begins at an early-intermediate level across Linux, networking, Python, and testing.
- The learner's target capacity is 3 focused hours per day on 5 days per week, for 15 focused hours per week.
- Guided discovery is the default: the learner predicts and attempts first; AI teaches, structures experiments, reviews, challenges, and helps debug from evidence.
- Deep independent capability takes priority over speed, feature count, or presentation polish.

These assumptions should be revised when demonstrated performance provides better evidence than the initial self-assessment.

## 2. Confirmed workstation context

The initial inspection established:

- WSL2 running Ubuntu 24.04 with 20 logical CPU threads, approximately 50 GiB RAM, and ample disk space
- Python 3.12, Git, `ip`, `ss`, `tcpdump`, SSH client and server binaries, systemd, and journaling available
- Unprivileged user and network namespaces available
- Administrative commands requiring deliberate password entry
- Docker Desktop installed on Windows but not yet active or integrated with this WSL distribution
- A Windows hypervisor present, but no confirmed ready-to-use Hyper-V, VirtualBox, VMware, or Multipass workflow
- The ordinary WSL SSH service disabled and inactive

No new infrastructure purchase or public-cloud environment is required for Core.

Environment and runtime facts are volatile. `PROJECT_STATE.md` and direct inspection determine their current value.

## 3. Immediate environment prerequisites

Before closing the first learning slice:

1. Confirm the namespace capabilities and privileged setup steps required for two connected endpoints.
2. Enable and verify Docker Desktop integration for the Ubuntu WSL distribution.
3. Confirm Hyper-V availability and use it as the default VM path when available; select another local VM manager only if Hyper-V cannot provide the required isolated Linux endpoints.
4. Prepare SSH host keys, users, authentication policy, logs, and cleanup procedures separately for each environment.
5. Ensure none of the laboratory targets expose SSH unintentionally to external or ordinary host networks.

Environment setup must be documented as observed behavior, not treated as invisible prerequisite work.

These prerequisites are not required to begin the namespace lead. Docker and VM readiness become blocking only before their respective reproduction milestones.

## 4. Canonical SSH experiment

One canonical experiment governs all three environment adapters.

It will define:

- One SSH client actor and one SSH target
- A normal authentication case and a repeated-failure case
- Explicit commands, execution attempts, reported outcomes, and target-observed effects
- Start and end markers
- Expected process, socket, host-log, and network observations
- One cross-environment evidence checklist
- Safety boundaries, authorized addresses and targets, abort conditions, and cleanup
- Separately maintained expected truth that is not inferred solely from sensor output

The scenario meaning and expected behavior remain constant across environments. Only environment-specific setup, network attachment, sensor access, and cleanup may vary.

## 5. First learning slice: observe SSH across isolation mechanisms

The namespace implementation leads:

1. Create two isolated endpoints.
2. Inspect interfaces, addresses, routes, processes, and listening sockets.
3. Establish normal SSH behavior.
4. Generate repeated authentication failures.
5. Observe process state, socket state, host authentication records, and packets.
6. Explain TCP and SSH behavior and distinguish the performed actions from each observation.
7. Break one bounded part of the path and diagnose it from evidence.
8. Clean up and reconstruct the environment safely.

Then converge:

1. Reproduce the same scenario and observations in Docker.
2. Reproduce them in separate virtual machines.
3. Compare topology, kernel and process boundaries, service lifecycle, routing, packet capture, logging, persistence, cleanup, and isolation.
4. Record differences without changing the scenario semantics.

The slice closes only when the learner can explain what each environment exposes, automates, hides, and isolates. No event-pipeline code is required.

## 6. Lead-then-converge milestone rule

Each environment-sensitive Core milestone follows the same sequence:

1. Predict expected behavior and evidence.
2. Prove the mechanism in network namespaces.
3. Reproduce it in Docker and virtual machines.
4. Feed comparable outputs into the same shared Core path when that path exists.
5. Compare observed differences and test the explanation.
6. Record blockers, limitations, and deferred questions.
7. Close the milestone through explanation and diagnosis.

A bounded environment-specific blocker may be documented, but it must have an explicit follow-up gate. It must not be silently treated as successful convergence.

## 7. Turn the experiment into a reproducible scenario

After the manual cross-environment experiment is understood, create a small versioned scenario containing:

- Environment-independent scenario semantics and evaluation expectations
- Adapter-specific prerequisites and cleanup
- Actors, targets, addresses, and authorization boundaries
- Normal login and repeated failed-login cases
- Commands issued and execution outcomes
- Expected host and network evidence
- Start and end markers
- Evidence checklist and comparison record
- Run identity and an inventory of preserved evidence
- Separately maintained experimental truth and known limitations

The scenario is run manually first. Automation follows only after its mechanics and environment differences can be explained.

## 8. Build the shared Core incrementally

The three scenario adapters feed one shared processing and evaluation path. The implementation sequence is:

1. Collect one host telemetry source from each adapter.
2. Collect one network telemetry source from each adapter.
3. Preserve raw records with source and environment context.
4. Define the first normalized event.
5. Implement validation and quarantine.
6. Create evidence identity and provenance.
7. Implement a time-window SSH-failure detector.
8. Represent a finding and alert.
9. Group the evidence into one incident.
10. Produce a human-written report.
11. Compare it with separately maintained experimental truth.
12. Replay the telemetry.
13. Introduce one controlled telemetry or processing failure.
14. Diagnose and explain the failure.
15. Demonstrate and close AegisLab Core across all three scenario environments.

The processing, storage, detection, reporting, and evaluation path is not deployed three times merely to mirror the environments. A deployment decision may be revisited only when a demonstrated learning or system requirement justifies it.

## 9. Learning and mastery gate

For each important slice, the learner must progressively be able to:

- Predict relevant behavior before execution
- Perform or intentionally modify the work
- Identify and interpret the observed evidence
- Explain purpose, inputs, outputs, state, assumptions, and invariants
- Describe security risks, failure modes, and limitations
- Break a bounded behavior and diagnose it
- Transfer the mechanism across the three laboratory environments where applicable
- Record what is understood and what remains unclear

Successful command output alone does not close a slice. AI assistance may unblock work, but important behavior must later be explained and modified without step-by-step generated instructions.

The current evidence state is maintained separately in [Current Learning State](../learning/CURRENT_LEARNING_STATE.md); this plan should not become a learner-progress diary.

## 10. First post-Core expansion: DFIR and threat hunting

After Core closes, the first major expansion will receive its own bounded charter and will progressively cover:

1. Hypothesis-led hunting over Core evidence
2. Controlled artifact acquisition and integrity verification
3. Preserved originals, working copies, access history, and reproducible observations
4. Cross-source timeline construction and timestamp limitations
5. Host, disk, memory, authentication, application, and network artifacts
6. Investigative scoping, alternative explanations, and negative evidence
7. Static malicious-artifact analysis using prepared and authorized material
8. Incident-response decisions and the limits of a solo laboratory

Dynamic malware analysis is not implied by this progression. It remains prohibited until a separate sandbox charter satisfies every requirement of the [dynamic-malware-analysis maturity gate](../definition/governance-safety-and-boundaries.md#dynamic-malware-analysis-maturity-gate) using benign substitutes first.

## 11. Later capability progression

After Core and the first DFIR/hunting charter, later expansions remain evidence-driven. A likely progression is:

```text
Core evidence loop across three scenario environments
        ↓
DFIR and hypothesis-led threat hunting
        ↓
Multiple scenarios and richer detections
        ↓
Distributed event transport
        ↓
Applied security ML comparison
        ↓
Human investigation tools
        ↓
Constrained LLM investigator
        ↓
Agent-security and adversarial evaluation
        ↓
Strictly gated dynamic malware analysis, only if still justified
```

This ordering may change when demonstrated prerequisites or limitations justify a deliberate revision. ML requires meaningful data and baselines; agents require real evidence, incidents, and tools; dynamic malware analysis requires mature isolation and safety controls.

## 12. Documentation boundary

No separate detailed architecture, event schema, forensic procedure, threat model, or large implementation specification is required before the first experiment creates a concrete need.

Supporting documents should appear only when they own a durable responsibility, prevent a demonstrated continuity problem, or make an active decision testable.

The active supporting controls are:

- [Core Execution Map](<AegisLab — Core Execution Map.md>) for milestone gates, evidence, and transitions;
- [Deferred Ideas and Review Triggers](<AegisLab — Deferred Ideas and Review Triggers.md>) for preserving useful ideas without scope drift;
- [Project State](../../PROJECT_STATE.md) for the current handoff;
- [Current Learning State](../learning/CURRENT_LEARNING_STATE.md) for current evidence and ownership gaps;
- worklogs and study guides for session continuity and consolidated learning.

## 13. Current active sequence

The namespace networking substrate and SSH control path are operational with guidance. The active milestone is namespace SSH observability.

The immediate sequence is:

1. Correlate the live authenticated SSH transport across client output, server logs, process relationships, and both socket-table perspectives.
2. Close the transport deliberately and observe process and socket teardown.
3. Capture one narrow SSH connection and explain what packet evidence reveals or cannot reveal after encryption begins.
4. Define and run the canonical normal-authentication and repeated-failure cases with explicit truth, time bounds, markers, abort conditions, and cleanup.
5. Introduce, diagnose, repair, and revalidate one bounded failure.
6. Demonstrate reduced-prompt explanation or reconstruction sufficient for transfer.
7. Enable and verify Docker Desktop WSL integration, then reproduce the same scenario and evidence checklist.
8. Select and verify the local Linux VM path, reproduce the scenario, and complete the three-environment comparison.
9. Close the first learning slice before beginning the shared Core evidence pipeline.

This section states the current transition, not a permanent schedule. `PROJECT_STATE.md` and direct evidence should update it when the milestone changes.

## 14. Maintenance contract

- Preserve the dependency and lead-then-converge sequence.
- Update the current active sequence when the milestone materially changes; keep detailed chronology in worklogs.
- Do not add later technologies merely to make the roadmap appear more ambitious.
- Move activated ideas from the deferred register into a bounded specification or ADR only when their trigger is satisfied.
- Keep learner-ownership gates honest and evidence-based.