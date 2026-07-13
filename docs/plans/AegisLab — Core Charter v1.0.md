# AegisLab — Core Charter

**Version:** 1.0
**Status:** Accepted and active
**Scope:** First bounded vertical slice
**Working profile:** Early-intermediate starting point; 11+ focused hours per week; guided discovery

## 1. Core objective

Build and explain a controlled SSH authentication-abuse experiment that produces host and network telemetry, preserves and normalizes that telemetry with provenance, detects repeated authentication failures within a time window, creates an evidence-backed incident, and evaluates the result against separately maintained experimental truth.

The Core exists to prove AegisLab's complete evidence loop in its smallest useful form. It is not intended to resemble a production SOC platform.

## 2. Core learning objectives

The Core should develop practical understanding of:

- Linux processes, users, services, permissions, logs, and network isolation
- IP addressing, TCP connections, ports, sockets, SSH, and packet or flow observation
- Network namespaces, containers, and virtual machines as different isolation mechanisms
- The difference between performed activity, sensor observation, normalized events, evidence, findings, alerts, incidents, and experimental truth
- Small event collectors, validation, quarantine, timestamps, identity, provenance, and replay
- Time-window detection and positive, negative, boundary, and failure cases
- Testing, structured diagnostics, threat modeling, and controlled failure investigation
- Explaining and defending module boundaries and design decisions

## 3. Environment comparison model

The canonical SSH scenario must be reproduced in three laboratory environments:

1. Linux network namespaces inside WSL
2. Docker containers
3. Separate virtual machines

These are environment-specific scenario adapters, not separate AegisLab platforms. Each adapter is responsible only for preparing the SSH actors and target, establishing the required isolation and network path, exposing the selected host and network observations, and cleaning up safely.

All adapters must use one canonical scenario contract and one evidence checklist. They feed one shared Core path for raw preservation, validation, normalization, evidence handling, detection, incident construction, reporting, replay, and evaluation.

The environments follow a **lead-then-converge** rule:

1. Prove and explain a milestone using network namespaces.
2. Reproduce the same milestone in Docker and virtual machines.
3. Compare topology, isolation, service behavior, observability, evidence differences, failure modes, and operational cost.
4. Record any environment-specific limitation or exception.
5. Close the milestone only after all three variants work or a bounded blocker is documented with evidence and an explicit follow-up gate.

The three environments must not introduce different scenario semantics merely to make a variant easier.

## 4. Required vertical slice

The Core is complete only when the learner can:

1. Prepare isolated SSH client and target endpoints in namespaces, Docker, and virtual machines.
2. Run the same documented normal-login and repeated-failure scenarios safely in all three environments.
3. Record commanded actions, execution attempts, reported outcomes, and independently observable effects without treating them as identical.
4. Capture at least one host telemetry source and one network telemetry source from each environment.
5. Compare the observations and explain which differences arise from the environment rather than the scenario.
6. Preserve raw records and their source and environment information.
7. Validate and normalize relevant records into a documented event structure.
8. Quarantine malformed or unacceptable records explicitly.
9. Preserve evidence identity, provenance, timestamps, and transformation versions.
10. Apply one understandable time-window detection for repeated SSH authentication failures.
11. Produce a finding, alert, and incident linked to their supporting evidence.
12. Produce a human-written report that separates facts, derived facts, hypotheses, and recommendations.
13. Evaluate observations and conclusions against separately maintained experimental truth.
14. Replay recorded telemetry after a component or rule changes.
15. Introduce and diagnose at least one controlled telemetry or processing failure.
16. Demonstrate, modify, test, break, diagnose, and explain the complete shared slice.

## 5. Explicit Core exclusions

The following do not enter the Core:

- Machine learning
- LLM investigators or other agents
- MCP or LangGraph
- Kafka, Redpanda, Flink, or similar distributed frameworks
- Microservice decomposition
- Kubernetes or public-cloud deployment
- A substantial graphical dashboard
- Additional attack families
- Full DFIR, forensic workstation construction, or broad artifact acquisition
- Static or dynamic malware analysis
- Malware acquisition, storage, or execution
- Autonomous response or blocking
- Production-scale throughput claims
- Deploying the complete Core pipeline separately in namespaces, Docker, and virtual machines

These capabilities are deferred, not rejected. DFIR and threat hunting form the first major post-Core expansion. Dynamic malware analysis remains prohibited until the separate [dynamic-malware-analysis maturity gate](../definition/governance-safety-and-boundaries.md#dynamic-malware-analysis-maturity-gate) is satisfied.

## 6. Working and learning method

The Core proceeds through small learning slices. Each slice introduces one principal unfamiliar difficulty and ends with a working observation or experiment.

Guided discovery is the default collaboration mode:

1. The learner states a prediction or explanation before receiving the complete solution.
2. The learner performs foundational commands and implementation work whenever safe and practical.
3. AI teaches mechanisms, structures experiments, reviews proposals, challenges assumptions, and helps debug from evidence.
4. Assistance may increase when blocked, but the learner later modifies, diagnoses, and explains the result.
5. A slice closes through demonstrated understanding, not merely successful execution.

For each important slice, the learner records and explains:

- Responsibility and purpose
- Inputs, outputs, and important state
- Assumptions and invariants
- Failure modes and security risks
- Tests and observed evidence
- Cross-environment similarities and differences
- What is understood and what remains unclear

Documentation should consolidate knowledge produced by implementation. It must not become a substitute for implementation.

## 7. Core completion gate

The Core is complete when the canonical vertical slice works reproducibly across all three scenario environments and the learner can independently trace one scenario action from experimental execution through raw observations, processing, detection, incident construction, reporting, and evaluation.

The learner must also be able to:

- Explain the isolation and observation differences among namespaces, Docker, and virtual machines
- Modify relevant scenario or detection behavior intentionally
- Diagnose a deliberately introduced failure
- Defend the important design choices, evidence limitations, and security boundaries
- Reproduce important behavior without depending on a generated answer

No deferred technology enters merely because the Core works. Expansion requires a demonstrated limitation, a defined learning goal, explicit prerequisites, and a new bounded charter or module decision.

## 8. First learning slice

Create two isolated endpoints with Linux network namespaces, establish an SSH connection between them, observe the connection at the process, socket, host-log, and network levels, and explain what occurred.

Then reproduce the same scenario and evidence checklist using Docker and virtual machines. Compare what each environment exposes, hides, automates, and isolates.

The first slice closes with understanding and recorded comparative observations. It does not require an event pipeline or platform code.
