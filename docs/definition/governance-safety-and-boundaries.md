# Governance, Safety, and Boundaries

**Part of:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)
**Status:** Normative part of the accepted definition

## Governing principles, policies, and maturity gates

The following rules do not all have the same role or severity. They are classified so that a violation of a system invariant is not treated as equivalent to postponing a development practice.

| Classification | Purpose | Included rules |
|---|---|---|
| System invariants | Properties required for trustworthy system behavior | Principles 1–6 and 10–13 |
| Learning invariants | Properties required to preserve genuine learner understanding | Principles 7, 9, and 14 |
| Development policies | Rules governing how the project evolves and records decisions | Principles 8, 15–17, and 19 |
| Maturity and evaluation gates | Practices required before claiming a corresponding capability level | Principle 18, capability snapshots, external calibration when applicable, and the dynamic-malware-analysis gate |

An **invariant** is a property intended to remain true as the architecture and technologies change. A **policy** guides project behavior and decision-making. A **maturity gate** becomes mandatory before a module or system can claim a particular quality such as resilience or evaluated performance.

### Principle 1: Evidence traceability

Every important alert, incident, report claim, and agent conclusion must be traceable to the evidence and reasoning that produced it.

### Principle 2: Ground-truth separation

Ground truth used for evaluation must remain separate from the ordinary evidence available to the detector or investigator unless a particular experiment explicitly states otherwise.

### Principle 3: Fact and hypothesis separation

Observed facts, derived facts, hypotheses, recommendations, and executed actions must remain distinguishable.

### Principle 4: Explicit uncertainty

Missing, incomplete, delayed, or contradictory evidence must not be silently converted into certainty.

Initially, uncertainty should be represented through observable support conditions such as evidence presence, evidence quality, conflicts, missing telemetry, alternative hypotheses, and tool failures. Numeric confidence may be used only when its meaning and calibration have been evaluated for the relevant task.

### Principle 5: Reproducibility

Controlled experiments must record enough information about their environment, configuration, inputs, timing, and versions to be rerun or meaningfully reconstructed.

### Principle 6: Versioned meaning

Schemas, scenarios, detections, datasets, models, prompts, tools, and important configurations must have identifiable versions when their changes can affect results.

### Principle 7: Explain before abstraction

Before adopting an important framework or abstraction, the learner must understand the underlying problem and, where safe and educationally useful, implement or demonstrate a bounded minimal form of the mechanism.

This does not mean recreating an entire production framework or implementing cryptographic primitives.

Understanding before adoption is only the first half of the learning cycle. After implementing a bounded educational mechanism, the learner should deliberately study and, where practical, exercise a mature tool that addresses the same problem. The comparison should explain what the mature tool adds, what trade-offs it introduces, and whether AegisLab currently needs it.

### Principle 8: Architecture follows demonstrated requirements

A component or service is added because it solves an understood requirement, learning goal, limitation, security boundary, or operational problem—not merely because it makes the architecture look more advanced.

### Principle 9: One principal unfamiliar difficulty at a time

Each learning slice should identify one principal new difficulty. Supporting concepts may also be required, but Kafka, Kubernetes, online ML, and autonomous agents should not be introduced together as one undifferentiated challenge.

### Principle 10: Least authority

Users, services, models, and agents receive only the permissions and capabilities required for their responsibilities.

### Principle 11: Human control of consequential actions

The agent may investigate and recommend within its permissions, but consequential security actions require explicit authorization and must be auditable.

### Principle 12: No unrecorded important action

Security-relevant configuration changes, agent tool calls, approvals, and executed response actions must be recorded sufficiently for later review.

### Principle 13: Independent evaluation

The component producing a result must not be the sole judge of whether that result is correct.

### Principle 14: No unexplained code survives

If an important dependency, abstraction, configuration, or block of code cannot be explained, it must be studied, simplified, replaced, or removed.

### Principle 15: Growth requires a reason

A new feature or technology must support a defined learning goal, system capability, security requirement, experiment, or demonstrated limitation. Its prerequisites and expected cost must be understood.

### Principle 16: Significant failures become learning artifacts

Important failures, wrong assumptions, difficult bugs, misleading evaluations, abandoned designs, and security mistakes should be examined through short, blameless postmortems.

A postmortem should explain what happened, why it happened, how it was discovered, what corrected it, what should change, and what was learned. Routine minor mistakes do not require formal postmortems.

### Principle 17: Preserve the project's reasoning history

Important decisions, experiments, failures, capability changes, and learning discoveries should be recorded while they are still understood. Documentation should be maintained as though useful parts may later be shown publicly.

Public release remains selective. Material should be reviewed for secrets, personal or sensitive information, unsafe offensive detail, misleading claims, and conclusions the learner cannot independently defend.

Important decisions should be recorded when they are made and reviewed again later with fresh evidence. A delayed review may add overlooked alternatives or revise the decision, but it must not erase or rewrite the original reasoning as though hindsight had been available from the beginning.

### Principle 18: Test resilience deliberately

A component that claims reliability, recoverability, or resilience must be tested under controlled failure conditions appropriate to that claim.

Each resilience experiment must define:

- The normal or steady state
- The hypothesis being tested
- The fault being introduced
- The expected behavior
- The measurements to collect
- The permitted blast radius
- The abort and cleanup procedures
- The observed result and remaining uncertainty

Failure and load variants become required when a module claims the corresponding maturity. They are not mandatory for every early prototype.

### Principle 19: Seek disconfirming and external evidence

Important designs, detections, models, evaluations, and agent behaviors should be challenged through adversarial review, negative and boundary tests, delayed self-review, standards calibration, and focused external feedback when available.

The purpose is to search for evidence that an assumption or conclusion is wrong, not merely to confirm the preferred design.

The source and independence of review must be described honestly:

- Adversarial AI review is an internal stress test, not independent expert review.
- Public availability is not proof that meaningful review occurred.
- Comparison with a standard or public artifact demonstrates calibration or conformance, not automatic correctness.
- Accountability from a non-expert supports consistency and explanation but is not technical validation.

### Dynamic-malware-analysis maturity gate

Dynamic malware execution is prohibited in the Core and in ordinary AegisLab environments. It may become an authorized future capability only through a separate charter after all of the following exist and have been tested with benign substitutes:

- A dedicated sandbox isolated from the host, personal data, ordinary project services, and production or public targets
- Default-deny external networking with any simulated or inspected network services explicitly controlled
- Revertible machine state and verified reset procedures
- Host and network monitoring sufficient to observe containment failures and unexpected behavior
- Controlled sample provenance, storage, access, transfer, retention, and destruction procedures
- Explicit authorization, permitted objectives, safety boundaries, abort conditions, and emergency cleanup procedures for each experiment class
- A threat model and safety review covering hypervisor, shared-folder, clipboard, credential, management-plane, and data-exfiltration risks
- A demonstrated reason that static analysis, prepared artifacts, or recorded execution evidence cannot answer the learning question

Passing this gate permits only the bounded activity defined by the later charter. It is not a general authorization to acquire or execute arbitrary malware.

## Explicitly outside the intended initial direction

The following are outside the intended direction unless a later, deliberate project decision establishes a strong learning or system reason:

- Public-cloud deployment as an early requirement
- Kubernetes without a demonstrated orchestration problem
- Blockchain
- Zero-Knowledge Machine Learning (zkML)
- Zero-knowledge proofs
- Training a foundation model
- Autonomous blocking, retaliation, or destructive response
- Dynamic malware execution before the dedicated maturity gate and separate expansion charter are satisfied
- Real external attack targets
- Uncontrolled offensive activity
- A large frontend application
- Multiple agent personas added for appearance rather than need
- Dozens of attack categories without deep scenario evaluation
- A general-purpose commercial Security Operations Center (SOC) replacement
- Production-scale throughput as an early success requirement

These exclusions protect AegisLab's center of gravity. They do not prevent carefully justified future expansion.

## Known limitations and compensating practices

AegisLab is a controlled, solo learning laboratory. It must represent its achievements honestly and preserve the difference between simulated experience and production experience.

### Limited production scale and operational pressure

AegisLab cannot fully reproduce:

- Large and diverse production workloads
- Multi-region or large multi-host infrastructure
- Independent hardware, power, and provider failures
- Real customer impact and service-level obligations
- Large-team communication and incident coordination
- Long-running configuration drift and organizational pressure
- The full diversity and uncertainty of production data

The project will partially compensate through:

- Controlled failure injection
- Real process and network boundaries when justified by the learning goal
- Arrival-rate, event-time, and burst replay
- Load and backpressure experiments
- Failure-pattern reconstruction based on credible public postmortems
- Capability-triggered game days
- Blameless postmortems and recovery measurements

These practices teach authentic failure mechanisms and engineering responses. They do not remove the production-experience limitation and must not be described as doing so.

### Limited continuous external review

A solo project does not naturally receive the continuous skeptical review available within a strong engineering or security team.

The project will partially compensate through:

- AI used in explicitly adversarial reviewer and evaluator roles
- Negative, boundary, evasion, and regression tests
- Delayed second-pass review of important decisions
- Comparison with current specifications and credible public artifacts
- Focused external requests covering narrow, reviewable artifacts
- Selective public documentation that permits scrutiny without exposing sensitive or unsafe material
- A recurring accountability relationship when available

These practices have different levels of independence:

- AI review may share assumptions and blind spots with earlier AI assistance.
- A public repository may receive no meaningful review.
- Conformance with a standard does not prove semantic correctness, detection quality, or operational suitability.
- A non-expert accountability partner provides motivation and explanatory pressure but not expert validation.

External reviews and comparisons should record what was reviewed, by whom or by what method, which version was examined, what feedback was received, what changed, and what uncertainty remains.

### Limited forensic, incident-response, and malware-analysis realism

A solo laboratory cannot reproduce formal legal evidence processes, a staffed incident-response organization, enterprise authority boundaries, victim impact, or every containment failure possible during malicious-code analysis.

The project will partially compensate through:

- Documented artifact acquisition, integrity, access, transfer, and analysis histories
- Controlled cases with independently maintained truth and known limitations
- Reproducible timelines, tool-version records, and separation of observations from interpretations
- Prepared disk and memory images, recorded traffic, and benign substitutes before live malicious code
- A dedicated dynamic-analysis maturity gate, separate charter, default-deny isolation, monitoring, and recovery tests

These practices support technical learning. AegisLab must not claim legal admissibility, professional forensic accreditation, enterprise incident-command experience, or absolute malware containment.
