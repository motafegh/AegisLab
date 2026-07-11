# AegisLab — Project Definition

**Version:** 0.3  
**Status:** Final consolidated Stage 0 draft  
**Project type:** Long-running, modular flagship learning project  
**Name status:** Provisional

---

## 0. Purpose of this document

This document defines what AegisLab is, why it exists, what it should eventually be capable of doing, the major logical parts it will contain, the permanent principles that should guide its development, and how its success will be judged.

This is a **project-definition document**, not a detailed implementation plan.

It intentionally does not yet define:

- Exact APIs, classes, database tables, or event fields
- A final network topology
- A final service or deployment architecture
- The detailed implementation order of every module
- Exact frameworks or infrastructure products
- Complete attack procedures
- Complete agent prompts or tool definitions

Those details will be designed in later documents when their corresponding modules are ready to be studied and implemented.

---

# 1. Project identity

> **AegisLab is a long-running, modular, evidence-centered network-defense laboratory. It provides a controlled environment for generating normal and malicious activity, observing that activity through network and host telemetry, detecting and correlating suspicious behavior, and investigating incidents using deterministic methods, machine learning, and constrained AI assistance. Its results are evaluated against known scenario ground truth, and every important conclusion must remain traceable to supporting evidence.**

The project has two connected identities:

- **Cyber range:** a safe and controlled environment where normal, malicious, ambiguous, and failure-related activity can be generated.
- **Defense platform:** a system that observes activity, processes telemetry, detects suspicious behavior, organizes evidence into incidents, supports investigation, and evaluates its conclusions.

These identities depend on each other:

- The cyber range provides controlled experiments and known ground truth.
- The defense platform attempts to reconstruct what happened using the telemetry available to it.
- The evaluation process compares the platform's observations and conclusions with what actually occurred.

The distinctive purpose of AegisLab is therefore not merely to generate attacks or produce alerts. It is to study the complete path from real activity to defensible security conclusions.

---

# 2. Central project thesis

AegisLab is built around the following idea:

> A security conclusion is valuable only when we can explain what evidence supports it, how that evidence was collected and transformed, what reasoning was applied, what uncertainty remains, and how the conclusion compares with what actually occurred.

This makes AegisLab different from:

- A generic Security Information and Event Management (SIEM) clone
- A collection of attack scripts
- A machine-learning intrusion-detection demonstration
- A dashboard over security logs
- A Large Language Model (LLM) wrapper that summarizes arbitrary telemetry
- A collection of technologies added without a shared engineering purpose

Networking, distributed systems, data engineering, machine learning, and AI agents all support the same evidence-driven investigation loop.

The project's center of gravity is:

> **Network security and distributed systems first; data and detection engineering throughout; machine learning when it has a justified problem to solve; and LLM agents as constrained investigators rather than unquestioned decision makers.**

Its intended signature is:

> **Network defense provides the operational foundation; secure, evidence-grounded agent-assisted investigation provides the differentiating specialization.**

The agent-security specialization must grow on top of real networking, telemetry, detection, data, and system-security foundations. It must not become a disconnected LLM demonstration.

---

# 3. Primary learning goal

The main goal is not merely to finish the software.

> The learner should become capable of designing, implementing, testing, operating, securing, evaluating, and explaining an intelligent distributed security system without depending on an AI assistant to make or explain its core decisions.

Over the lifetime of the project, the learner should become able to explain and demonstrate:

- How traffic moves through the laboratory network
- How host, network, application, and identity telemetry is produced
- How telemetry is collected, transported, transformed, stored, and queried
- How distributed components communicate, fail, recover, and create duplicates or delays
- How detections are designed, tested, tuned, and evaluated
- How raw observations become events, findings, alerts, incidents, and reports
- How an ML model is trained, validated, deployed, monitored, attacked, and retired
- How an investigation agent selects and uses tools
- How untrusted data can manipulate or mislead an LLM
- How services, identities, credentials, evidence, and agent actions are secured
- Why each important architectural decision was made
- Which parts are understood only at an introductory level and which have been studied and applied in technical depth

## 3.1 Personal purpose and career direction

AegisLab supports the learner's long-term direction toward becoming an **AI Security Automation Engineer**: an engineer who combines strong cybersecurity and software foundations with the ability to design, secure, evaluate, and operate AI-assisted security automation.

The project is intended to develop:

- The security and networking knowledge required to understand the systems being defended
- The software, distributed-systems, and data-engineering knowledge required to build reliable security platforms
- The detection and incident-investigation knowledge required to make defensible security decisions
- The AI and agent-security knowledge required to automate carefully without surrendering evidence, control, accountability, or human judgment

This personal purpose helps determine learning depth. Not every domain must become an equal specialty.

## 3.2 Learning priority hierarchy

### Foundational depth

The following domains should become strong enough to support independent engineering and diagnosis:

- Networking and network analysis
- Security and detection engineering
- Distributed systems
- Software engineering
- Secure system design

### Differentiating specialization

The following connected capabilities should become a recognizable AegisLab specialty:

- Secure AI-assisted investigation
- Evidence-grounded agent reasoning
- Agent tool authorization and least authority
- Prompt-injection and context-poisoning resistance
- Human-supervised security automation
- Evaluation of agent claims, tool use, uncertainty, and actions

### Supporting breadth

The following domains should be learned properly and taken to the depth required by actual AegisLab problems, without assuming that every one must become an equal specialty:

- Data engineering
- Applied machine learning
- Observability and operations
- Deployment infrastructure
- User-interface development where needed

These categories describe intended emphasis, not rigid boundaries. A supporting domain may later become deeper when a meaningful project requirement or career decision justifies it.

---

# 4. The complete experimental loop

AegisLab should eventually support the following complete loop:

```text
Scenario definition and expected truth
                ↓
Controlled environment and execution
                ↓
Network, host, application, and identity activity
                ↓
Sensors and raw telemetry
                ↓
Collection, validation, normalization, and storage
                ↓
Detection and correlation
                ↓
Human- and agent-assisted investigation
                ↓
Evidence-backed claims and incident report
                ↓
Evaluation against expectations and ground truth
                ↓
Improvement and reproducible re-evaluation
```

A controlled scenario such as an SSH password attack should eventually allow AegisLab to:

1. Generate relevant normal and malicious behavior.
2. Record what actions were actually performed.
3. Observe relevant network and host activity.
4. Collect and transport telemetry.
5. Validate and normalize telemetry into documented event structures.
6. Preserve the origin and transformation history of important evidence.
7. Detect suspicious behavior using explicit methods.
8. Correlate related evidence and alerts into an incident.
9. Allow a human investigator and a constrained AI agent to query the evidence.
10. Produce a report that distinguishes facts, derived conclusions, hypotheses, recommendations, and actions.
11. Compare the system's results with scenario expectations and actual execution truth.
12. Reproduce or replay the experiment after a rule, parser, model, or system component changes.

Not every early version or individual module must implement this entire loop. Each module should contribute clearly to it.

---

# 5. Target capabilities

The following are long-term target capabilities. They describe the direction of the flagship project; they are not all requirements for its first working version.

## 5.1 Controlled scenario execution

AegisLab should be able to:

- Define repeatable normal, malicious, ambiguous, failure, and evasion scenarios
- Create or prepare the required isolated environment
- Execute only explicitly authorized activity against controlled targets
- Record scenario configuration, versions, timing, actors, targets, and performed actions
- Stop, clean up, and rerun scenarios safely

## 5.2 Telemetry generation and observation

AegisLab should be able to:

- Observe selected network, host, application, authentication, and identity activity
- Preserve raw records when appropriate
- Identify which sensor and source produced each record
- Recognize missing, malformed, duplicated, delayed, or contradictory telemetry
- Distinguish what occurred from what the sensors managed to observe

## 5.3 Reliable event processing

AegisLab should eventually be able to:

- Collect events from multiple producers
- Validate and normalize different record formats
- Handle retries, duplicates, reordering, backpressure, and partial failure
- Quarantine invalid data rather than silently accepting or discarding it
- Evolve schemas without silently changing the meaning of historical evidence
- Explain the journey of an event through the system

## 5.4 Evidence preservation and provenance

**Provenance** means the origin and history of a piece of data: where it came from, when it was collected, and how it was transformed.

AegisLab should be able to:

- Give important records stable identities
- Link derived information to its source records
- Record important transformations and their versions
- Preserve enough context to audit an alert or conclusion later
- Detect or reveal inappropriate modification of important records where feasible
- Trace a report claim backward to the evidence supporting it

## 5.5 Detection engineering

AegisLab should be able to:

- Express rule-based and behavioral detections
- Apply detections over individual events and time windows
- Document the behavior, assumptions, data requirements, and limitations of each detection
- Test positive, negative, boundary, and evasion cases
- Measure false positives, false negatives, detection latency, and alert volume
- Compare revised detections against earlier versions

## 5.6 Incident correlation

AegisLab should be able to:

- Connect related events, findings, alerts, entities, and evidence
- Group activity into a coherent investigative case
- Record why two objects were considered related
- Preserve alternative explanations and uncertainty
- Reevaluate incidents when new or late evidence arrives

## 5.7 Machine-learning experimentation

Machine learning is an analytical method within AegisLab, not the identity of the project.

AegisLab should eventually be able to:

- Build versioned datasets from documented sources
- Compare ML models against simple rule-based or statistical baselines
- Prevent obvious data leakage
- Use time-aware and scenario-aware evaluation where appropriate
- Account for class imbalance and operational alert volume
- Select and justify thresholds
- Explain model inputs, outputs, limitations, and important errors
- Monitor performance and data changes
- Test realistic forms of evasion or manipulation

Advanced models should be introduced only when a simpler method has established a meaningful baseline and a concrete limitation justifies additional complexity.

## 5.8 Human-supervised agent investigation

The AI agent is an investigator, not the primary detection engine and not an unquestioned authority.

AegisLab should eventually be able to:

- Give the agent typed and documented investigation tools
- Restrict the agent to explicitly authorized capabilities
- Require evidence references for factual claims
- Separate observed facts, derived facts, hypotheses, recommendations, and executed actions
- Represent confidence and uncertainty
- Record tool calls, results, failures, approvals, and important decisions
- Evaluate the agent repeatedly using known cases
- Test prompt injection, context poisoning, misleading evidence, and unauthorized tool use
- Require human approval before consequential actions

## 5.9 Secure platform operation

AegisLab should eventually be able to:

- Authenticate users and services
- Authorize access according to role and capability
- Protect secrets and service identities
- Apply least privilege and secure defaults
- Validate untrusted inputs
- Isolate components and controlled offensive activity
- Record security-relevant actions
- Recover from failures and restore important state
- Threat-model the platform itself as a target

## 5.10 Reproducible evaluation and replay

AegisLab should eventually be able to:

- Reproduce controlled experiments
- Replay recorded telemetry through new parsers, detections, models, and investigation logic
- Compare results across versions
- Identify which layer caused a missed or incorrect conclusion
- Preserve the relationship between results and the exact scenario, data, configuration, code, rule, model, prompt, and tool versions used

## 5.11 Resilience experimentation

**Resilience** means the ability to continue operating appropriately, degrade in a controlled way, or recover when failures occur.

AegisLab should eventually be able to:

- Inject controlled network, process, dependency, data, timing, and resource failures
- Terminate components at defined processing points and observe the consequences
- Replay telemetry using defined arrival-rate, event-time, and burst modes
- Generate controlled load and backpressure
- Measure data loss, duplication, latency, recovery time, and degraded behavior
- Reconstruct scaled-down failure patterns described in credible public engineering postmortems
- Run bounded game-day exercises after the required observability, safety, and recovery mechanisms exist
- Record the hypothesis, fault, measurements, safety boundary, abort procedure, cleanup, and result of each experiment

These practices provide real experience with failure mechanisms, but they must not be presented as equivalent to operating a large production system.

---

# 6. Logical modules

At this stage, a **logical module** means an area with a clear responsibility and contract. It does not automatically mean a separate process, service, container, repository, or deployment.

The architecture may begin simply and evolve as demonstrated requirements justify stronger separation.

| Logical module | Primary responsibility | Representative outputs |
|---|---|---|
| Scenario Registry | Defines scenarios, actors, targets, assumptions, expected observations, and evaluation criteria | Versioned scenario definitions |
| Range Orchestrator | Prepares the controlled environment and executes authorized scenario actions | Execution and action records |
| Sensor Layer | Observes network, host, application, authentication, and identity activity | Raw telemetry |
| Collection and Transport | Receives and moves telemetry while handling delivery and failure concerns | Received records and delivery state |
| Validation and Normalization | Checks records and converts accepted data into documented event structures | Normalized events and quarantined records |
| Evidence and Storage | Preserves evidence, identity, provenance, integrity information, lineage, and retention state | Addressable evidence objects |
| Detection Engine | Applies rules, statistics, and justified ML methods | Findings and alerts |
| Correlation and Incident Engine | Relates alerts, events, entities, evidence, and hypotheses | Incidents and relationships |
| Investigation Layer | Provides controlled query and reasoning capabilities to humans and agents | Queries, claims, hypotheses, and investigation history |
| Reporting Layer | Produces structured, evidence-backed conclusions | Versioned incident reports |
| Evaluation Engine | Compares execution, observations, detections, incidents, and reports with expectations and truth | Metrics and failure analyses |
| Control Plane | Manages configuration, identities, permissions, versions, and administrative actions | Auditable control state |

Cross-cutting concerns such as security, testing, observability, documentation, and learning evidence apply to every module.

---

# 7. Foundational vocabulary

The detailed data model will be designed later, but the project needs an initial shared language.

| Term | Initial practical meaning |
|---|---|
| Scenario | A versioned definition of a controlled experiment |
| Action record | A trusted record of an action the scenario system actually performed |
| Raw record | Sensor output preserved close to its original representation |
| Event | A normalized representation of something observed |
| Evidence | An event or artifact used to support or challenge an investigative conclusion |
| Feature | A measurable value derived from one or more events for analysis or ML |
| Finding | A technical result produced by a detector |
| Alert | A finding promoted for attention or investigation |
| Incident | A case organizing related alerts, evidence, entities, claims, and hypotheses |
| Observed fact | A statement directly supported by recorded evidence |
| Derived fact | A statement produced from explicit processing or calculation over evidence |
| Hypothesis | A possible explanation that has not been established as fact |
| Recommendation | A proposed next step that has not been executed |
| Action | An approved and executed operation |
| Report | A versioned collection of evidence-backed claims, uncertainty, conclusions, and recommendations |
| Ground truth | Trusted information about what actually occurred in a controlled experiment |
| Capability snapshot | A versioned measurement of what AegisLab can do at a particular point in its development |
| Golden case | A carefully reviewed evaluation case with known or agreed expected results |
| Postmortem | A blameless review of a significant failure, incorrect decision, or abandoned approach |
| Failure injection | The deliberate introduction of a controlled fault to study system behavior |
| Chaos engineering | Controlled experimentation used to test hypotheses about system resilience under disruption |
| Blast radius | The portion of the system, data, or environment that an experiment or failure can affect |
| Game day | A scheduled exercise for practicing failure detection, diagnosis, response, and recovery |
| External calibration | Comparison with established specifications, artifacts, or external feedback to challenge internal assumptions |

These definitions are provisional. Later specifications may refine them, but changes must be deliberate and documented.

---

# 8. Ground-truth model

Ground truth is not a single label. AegisLab should eventually distinguish:

- **Intent truth:** what the scenario was designed to simulate
- **Action truth:** what actions were actually executed
- **Environment truth:** what systems, identities, configurations, and relationships existed
- **Telemetry expectation:** what correctly functioning sensors were expected to observe
- **Observed telemetry:** what the sensors and pipeline actually captured
- **Detection expectation:** what detections were expected to produce
- **Investigation expectation:** what conclusions the available evidence reasonably supports

These distinctions help locate failure correctly.

For example, an attack action may execute successfully while a sensor fails to observe it. Alternatively, telemetry may be collected correctly while a parser rejects it or a detector misses it. AegisLab should avoid treating all these cases as the same failure.

Scenario ground truth used by the evaluator must not be silently exposed to the detection or investigation components being evaluated.

---

# 9. Permanent project principles

These principles are intended to remain true as technologies and architectures change. A permanent principle of this kind may also be called an **invariant**.

## Principle 1: Evidence traceability

Every important alert, incident, report claim, and agent conclusion must be traceable to the evidence and reasoning that produced it.

## Principle 2: Ground-truth separation

Ground truth used for evaluation must remain separate from the ordinary evidence available to the detector or investigator unless a particular experiment explicitly states otherwise.

## Principle 3: Fact and hypothesis separation

Observed facts, derived facts, hypotheses, recommendations, and executed actions must remain distinguishable.

## Principle 4: Explicit uncertainty

Missing, incomplete, delayed, or contradictory evidence must not be silently converted into certainty.

## Principle 5: Reproducibility

Controlled experiments must record enough information about their environment, configuration, inputs, timing, and versions to be rerun or meaningfully reconstructed.

## Principle 6: Versioned meaning

Schemas, scenarios, detections, datasets, models, prompts, tools, and important configurations must have identifiable versions when their changes can affect results.

## Principle 7: Explain before abstraction

Before adopting an important framework or abstraction, the learner must understand the underlying problem and, where safe and educationally useful, implement or demonstrate a bounded minimal form of the mechanism.

This does not mean recreating an entire production framework or implementing cryptographic primitives.

Understanding before adoption is only the first half of the learning cycle. After implementing a bounded educational mechanism, the learner should deliberately study and, where practical, exercise a mature tool that addresses the same problem. The comparison should explain what the mature tool adds, what trade-offs it introduces, and whether AegisLab currently needs it.

## Principle 8: Architecture follows demonstrated requirements

A component or service is added because it solves an understood requirement, learning goal, limitation, security boundary, or operational problem—not merely because it makes the architecture look more advanced.

## Principle 9: One principal unfamiliar difficulty at a time

Each learning slice should identify one principal new difficulty. Supporting concepts may also be required, but Kafka, Kubernetes, online ML, and autonomous agents should not be introduced together as one undifferentiated challenge.

## Principle 10: Least authority

Users, services, models, and agents receive only the permissions and capabilities required for their responsibilities.

## Principle 11: Human control of consequential actions

The agent may investigate and recommend within its permissions, but consequential security actions require explicit authorization and must be auditable.

## Principle 12: No unrecorded important action

Security-relevant configuration changes, agent tool calls, approvals, and executed response actions must be recorded sufficiently for later review.

## Principle 13: Independent evaluation

The component producing a result must not be the sole judge of whether that result is correct.

## Principle 14: No unexplained code survives

If an important dependency, abstraction, configuration, or block of code cannot be explained, it must be studied, simplified, replaced, or removed.

## Principle 15: Growth requires a reason

A new feature or technology must support a defined learning goal, system capability, security requirement, experiment, or demonstrated limitation. Its prerequisites and expected cost must be understood.

## Principle 16: Significant failures become learning artifacts

Important failures, wrong assumptions, difficult bugs, misleading evaluations, abandoned designs, and security mistakes should be examined through short, blameless postmortems.

A postmortem should explain what happened, why it happened, how it was discovered, what corrected it, what should change, and what was learned. Routine minor mistakes do not require formal postmortems.

## Principle 17: Preserve the project's reasoning history

Important decisions, experiments, failures, capability changes, and learning discoveries should be recorded while they are still understood. Documentation should be maintained as though useful parts may later be shown publicly.

Public release remains selective. Material should be reviewed for secrets, personal or sensitive information, unsafe offensive detail, misleading claims, and conclusions the learner cannot independently defend.

Important decisions should be recorded when they are made and reviewed again later with fresh evidence. A delayed review may add overlooked alternatives or revise the decision, but it must not erase or rewrite the original reasoning as though hindsight had been available from the beginning.

## Principle 18: Test resilience deliberately

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

## Principle 19: Seek disconfirming and external evidence

Important designs, detections, models, evaluations, and agent behaviors should be challenged through adversarial review, negative and boundary tests, delayed self-review, standards calibration, and focused external feedback when available.

The purpose is to search for evidence that an assumption or conclusion is wrong, not merely to confirm the preferred design.

The source and independence of review must be described honestly:

- Adversarial AI review is an internal stress test, not independent expert review.
- Public availability is not proof that meaningful review occurred.
- Comparison with a standard or public artifact demonstrates calibration or conformance, not automatic correctness.
- Accountability from a non-expert supports consistency and explanation but is not technical validation.

---

# 10. Initial scenario families

The following scenario families provide long-term experimental coverage. They do not all need to be implemented together.

## 10.1 Evergreen reference scenario

An **evergreen reference scenario** is a stable, repeatedly maintained scenario used to demonstrate and reevaluate AegisLab as the system grows.

The initial evergreen reference scenario should be **SSH authentication abuse**. It can begin as a small experiment involving normal logins and repeated authentication failures, then progressively exercise additional capabilities:

- Host and network observation
- Collection and normalization
- Evidence provenance
- Time-window detection
- Alert and incident correlation
- Delayed, duplicated, or missing telemetry
- Detection evaluation
- ML comparison when justified
- Human and agent investigation
- Prompt injection or misleading content in untrusted evidence
- Authorization, approval, and audit controls

The reference scenario should be rerun when an important module matures and should always provide a current answer to: "What can AegisLab demonstrate today?"

The scenario must remain understandable and realistic. Features that do not naturally belong in SSH authentication abuse should be evaluated through other scenarios rather than forced into it.

## 10.2 Network reconnaissance

- Port scanning
- Horizontal and vertical connection patterns
- Slow, distributed, or evasive scanning
- Benign administrative and monitoring activity for comparison

## 10.3 SSH authentication abuse

- Repeated login failures
- Attempts against multiple users or hosts
- Distributed attempts
- Successful login following failures
- Legitimate user mistakes and administrative behavior for comparison

## 10.4 Web authentication abuse

- Credential guessing
- Suspicious session behavior
- Rate-limit interaction
- Benign automation and user mistakes for comparison

## 10.5 Suspicious DNS behavior

- High-entropy or unusually long subdomains
- Unusual query frequency
- DNS tunneling-like patterns
- Legitimate software with unusual DNS behavior for comparison

## 10.6 Simulated data exfiltration

- Unusual outbound volume
- Rare destinations
- Abnormal transfer timing
- Benign backup, synchronization, and large-transfer behavior for comparison

Over time, an individual scenario may have several variants:

- **Positive:** expected to trigger a particular detection
- **Negative:** expected not to trigger it
- **Boundary:** close to a decision threshold
- **Ambiguous:** supports more than one plausible explanation
- **Failure:** includes a sensor or pipeline malfunction
- **Evasion:** modifies behavior to avoid detection
- **Agent-adversarial:** contains untrusted content intended to mislead an LLM
- **Regression:** protects behavior that was previously corrected
- **Load:** examines volume, burstiness, or backpressure

Every implemented scenario should eventually document its purpose, authorized targets, preconditions, actions, expected telemetry, expected detections, timing, truth records, evaluation criteria, cleanup, and safety controls.

Failure and load variants should become mandatory for scenarios used to validate a module's reliability, recoverability, resilience, or performance claims. They remain optional when an early scenario is intended only to teach or demonstrate a simpler mechanism.

All offensive activity must remain inside explicitly controlled and authorized laboratory boundaries.

---

# 11. Learning domains

AegisLab connects several learning domains through one system. The project must record the depth reached in each subject rather than marking broad subjects as simply "completed."

The priority hierarchy in Section 3 determines the intended emphasis: foundational domains should become strong, secure agent-assisted investigation should provide the differentiating specialization, and supporting domains should reach the depth required by real project problems.

## 11.1 Networking and network analysis

- TCP/IP model and encapsulation
- Ethernet, Address Resolution Protocol (ARP), Internet Protocol (IP), Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Internet Control Message Protocol (ICMP)
- Ports, sockets, connections, and sessions
- Domain Name System (DNS)
- Hypertext Transfer Protocol (HTTP) and Transport Layer Security (TLS)
- Routing, Network Address Translation (NAT), firewalls, and segmentation
- Packet capture, flow records, and traffic analysis
- Linux network namespaces and virtual interfaces

## 11.2 Security and detection engineering

- Threat modeling, attack surfaces, and trust boundaries
- Behavioral detections and indicators
- Authentication abuse, reconnaissance, command-and-control-like patterns, and exfiltration patterns
- Incident response and evidence preservation
- False-positive and false-negative analysis
- Detection limitations, evasion, and adversarial thinking

## 11.3 Distributed systems

- Producers, consumers, queues, and event streams
- Ordering, partitioning, batching, retries, and exponential backoff
- Backpressure and partial failure
- At-most-once, at-least-once, and effectively-once processing
- Idempotency and duplicate handling
- Dead-letter queues and quarantine
- Time synchronization and late events
- Horizontal scaling, recovery, and distributed observability

## 11.4 Data engineering

- Raw, normalized, and derived data layers
- Data contracts, validation, and schema evolution
- Deduplication, timestamps, lineage, and retention
- Dataset versioning and ground-truth generation
- Data-quality measurement
- Batch and stream processing
- Privacy and sensitive-data handling

## 11.5 Machine learning

- Translating security behavior into an ML problem
- Feature engineering and baseline models
- Supervised, unsupervised, and semi-supervised methods
- Class imbalance, time-based splits, and data leakage
- Precision, recall, F1, Receiver Operating Characteristic Area Under the Curve (ROC-AUC), and Precision–Recall Area Under the Curve (PR-AUC)
- Thresholds, calibration, alert-aware evaluation, and explainability
- Model serving, monitoring, drift, and adversarial evasion

## 11.6 LLM and agent engineering

- Tool calling and typed tool interfaces
- State, control flow, memory, and retrieval
- Evidence grounding and structured outputs
- Confidence, uncertainty, and agent evaluation
- Prompt injection and context poisoning
- Tool authorization, sandboxing, approval gates, and audit logging

## 11.7 Secure system design

- Authentication, authorization, and service identities
- Role-Based Access Control (RBAC) and capability-based access
- Secrets management and encrypted communication
- Least privilege, secure defaults, and input validation
- Dependency and supply-chain risk
- Isolation, rate limiting, audit records, backup, and recovery
- Threat modeling for AegisLab itself

## 11.8 Software and operational engineering

- Python application design and selected use of a systems language when justified
- Application Programming Interface (API) and Command-Line Interface (CLI) design
- Databases, testing strategies, and property-based testing
- Integration and end-to-end testing
- Containers, Continuous Integration (CI), and configuration management
- Metrics, logs, traces, profiling, load testing, deployment, and failure diagnosis

---

# 12. Learning-depth and AI-ownership model

## 12.1 Depth-aware progress

Learning records should use explicit depth states such as:

1. **Not encountered** — not yet studied.
2. **Introduced** — the basic name and purpose are recognized.
3. **Explained with guidance** — the concept can be explained with assistance.
4. **Practiced with guidance** — the concept has been used with assistance.
5. **Applied independently** — it can be used without step-by-step help.
6. **Diagnosed independently** — failures and incorrect behavior can be investigated and repaired.
7. **Transferred to a new context** — the knowledge can be applied in a different situation.
8. **Studied in technical depth** — mechanisms, important edge cases, limitations, and trade-offs can be explained.

A topic must not be marked as fully covered merely because it appeared during one module.

Each important learning record should state:

- Required prerequisite depth
- Current depth
- Target depth for the current module
- Practical evidence demonstrating that depth
- Important gaps and deliberately deferred details

## 12.2 AI collaboration modes

AI assistance may take different explicit roles:

- **Teacher:** explains concepts and tests understanding
- **Reviewer:** critiques the learner's proposal or implementation
- **Pair programmer:** collaborates on implementation while preserving learner participation
- **Debugger:** helps investigate evidence and form hypotheses
- **Evaluator:** challenges explanations and independent capability

For foundational decisions, AI should not silently become the owner of the design.

## 12.3 Ownership test

For an important component to count as genuinely owned by the learner, the learner should progressively become able to:

- Explain what it does and why it exists
- Run it and observe its behavior
- Modify it intentionally
- Test it
- Break it deliberately and safely
- Diagnose and fix it
- Describe its failure modes and security risks
- Recreate or transfer its core mechanism without depending on generated answers
- Defend the important design choices and alternatives

The required ownership depth may differ by module, but it must be recorded honestly.

---

# 13. Technology strategy

Technologies are candidates, not commitments.

| Learning layer | Begin by understanding | Later candidates when justified |
|---|---|---|
| Networking | Linux sockets, namespaces, packet capture | Scapy, Zeek, Suricata |
| Event transport | In-memory queue and small collector | Kafka or Redpanda |
| Stream processing | Explicit workers, state, and time windows | Flink, Kafka Streams, or Bytewax |
| Storage | Files and SQLite | PostgreSQL, object storage, search or time-series storage |
| APIs | HTTP and API fundamentals | FastAPI |
| Data validation | Explicit validation and documented structures | Pydantic, JSON Schema, Avro, or Protocol Buffers |
| ML | NumPy, statistics, and scikit-learn baselines | PyTorch when a justified problem requires it |
| Experiment tracking | Structured experiment records | MLflow |
| Dataset versioning | Hashes and manifests | DVC |
| Agent workflow | Explicit Python control flow or state machine | LangGraph when demonstrated complexity justifies it |
| Agent tools | Typed Python interfaces | Model Context Protocol (MCP) after tool boundaries are understood |
| Observability | Structured logs, counters, and explicit diagnostics | OpenTelemetry, Prometheus, and Grafana |
| Deployment | Processes and scripts | Docker Compose; Kubernetes only if a later requirement justifies it |
| Security | Explicit permissions, certificates, and secret handling | Dedicated secret-management systems when justified |
| Resilience and load | Explicit fault scripts and a small replay harness | Linux traffic control/network emulation, Locust, or other tools when justified |

The framework-entry rule is:

> A framework enters AegisLab only when we can name the problem it solves, explain its core mechanism at the required learning depth, and show why it is appropriate for the current requirement.

A bounded educational implementation should teach a mechanism, not attempt to recreate an entire production framework.

## 13.1 Mechanism-to-framework comparison cycle

Where safe and useful, learning a major abstraction should follow this cycle:

1. Identify and explain the underlying problem.
2. Build or demonstrate a bounded minimal mechanism.
3. Observe its behavior and limitations.
4. Study and briefly exercise a mature tool that addresses the same problem.
5. Compare the designs, guarantees, failure behavior, operational costs, and trade-offs.
6. Decide whether the mature tool should enter AegisLab now, later, or not at all.
7. Record what was learned and which details remain deferred.

The comparison is educational even when the decision is not to adopt the mature tool.

---

# 14. External alignment

AegisLab may compare or map selected concepts to established security and AI frameworks without turning standards compliance into the project's main purpose.

Potential alignment includes:

- **MITRE ATT&CK:** adversary tactics, techniques, detection strategies, analytics, and defensive coverage
- **MITRE ATLAS:** threats, attack techniques, and mitigations involving AI-enabled systems
- **Open Cybersecurity Schema Framework (OCSF):** comparison and mapping for normalized cybersecurity events
- **Sigma:** portable representation of suitable log detections and correlations
- **OpenTelemetry:** concepts and conventions for operational telemetry such as metrics, logs, and traces
- **NIST Artificial Intelligence Risk Management Framework (AI RMF):** governance and evaluation concepts for trustworthy AI and generative-AI components

The project should align where doing so improves learning, interoperability, evaluation, or professional relevance. It should not copy a standard without understanding its purpose or distort the architecture merely to claim compliance.

---

# 15. Explicitly outside the intended initial direction

The following are outside the intended direction unless a later, deliberate project decision establishes a strong learning or system reason:

- Public-cloud deployment as an early requirement
- Kubernetes without a demonstrated orchestration problem
- Blockchain
- Zero-Knowledge Machine Learning (zkML)
- Zero-knowledge proofs
- Training a foundation model
- Autonomous blocking, retaliation, or destructive response
- Malware execution
- Real external attack targets
- Uncontrolled offensive activity
- A large frontend application
- Multiple agent personas added for appearance rather than need
- Dozens of attack categories without deep scenario evaluation
- A general-purpose commercial Security Operations Center (SOC) replacement
- Production-scale throughput as an early success requirement

These exclusions protect AegisLab's center of gravity. They do not prevent carefully justified future expansion.

---

# 16. Known limitations and compensating practices

AegisLab is a controlled, solo learning laboratory. It must represent its achievements honestly and preserve the difference between simulated experience and production experience.

## 16.1 Limited production scale and operational pressure

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

## 16.2 Limited continuous external review

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

---

# 17. Definition of success

Because AegisLab is a long-running flagship, success exists at several levels. The project does not need to reach one final endpoint before producing meaningful results.

## 17.1 Learning success

The learner can increasingly:

- Explain an event's complete journey through the system
- Draw and defend the relevant architecture from memory
- Implement and evaluate a new rule-based detection
- Diagnose a missing, delayed, malformed, or duplicated event
- Explain whether an ML evaluation contains leakage
- Train and evaluate a justified ML detector against a baseline
- Add an agent tool with appropriate permissions and tests
- Demonstrate and mitigate prompt injection or misleading evidence
- Recover a failed component
- Threat-model a new feature
- Explain current knowledge depth and remaining gaps honestly
- Design and conduct a bounded resilience experiment
- Distinguish internal AI review, external calibration, and independent expert review

## 17.2 Engineering success

The system increasingly becomes:

- Reproducible
- Testable
- Observable
- Diagnosable
- Recoverable
- Versioned
- Secure by explicit design
- Understandable at module boundaries
- Tested under controlled failures appropriate to its reliability claims

## 17.3 Security and evaluation success

AegisLab can increasingly:

- Run a scenario and establish what actually occurred
- Show which telemetry was expected and which was observed
- Measure detection and investigation correctness
- Identify the layer responsible for a failure
- Preserve evidence and uncertainty
- Resist or reveal manipulation attempts
- Compare revised components against previous versions
- Search deliberately for disconfirming evidence and record review limitations

## 17.4 Longitudinal capability snapshots

**Longitudinal** means measured repeatedly across time. AegisLab should periodically freeze a version of the system, run a versioned evaluation suite, and record a capability snapshot.

A snapshot may include, when the corresponding capability exists:

- Supported scenario and variant counts
- Expected telemetry coverage
- Missing, duplicate, invalid, and late-event rates
- Detection precision, recall, false-positive rate, and latency
- Alert volume under defined workloads
- Incident-grouping correctness
- Agent factual-support rate against golden cases
- Unsupported-claim rate
- Tool-use and authorization-policy violations
- Prompt-injection or adversarial-case results
- Recovery and performance measurements
- Current module maturity and learning-depth evidence

Metric definitions, scenario versions, datasets, configurations, and evaluation conditions must be recorded. Results should not be compared as though they used the same benchmark when the benchmark or metric meaning has changed.

Capability snapshots should make AegisLab's growth visible without reducing the project to one misleading overall score.

## 17.5 Portfolio success

The project produces credible evidence of capability, including:

- Clear project and module documentation
- Architecture and data-flow explanations
- Reproducible scenarios
- Detection and evaluation reports
- Automated tests
- Threat models and security decisions
- Architecture Decision Records (ADRs)
- Failure and false-positive analyses
- Demonstrations of improvement across versions
- Versioned capability snapshots showing development over time
- Selected postmortems demonstrating honest technical learning
- A maintained evergreen reference-scenario demonstration
- Selected resilience experiments and game-day reports
- External calibration records that distinguish conformance from correctness
- Explanations that the learner can defend independently

## 17.6 Module success

Each module should eventually document:

- Responsibility and boundaries
- Inputs, outputs, and data contracts
- Important invariants
- Failure modes and recovery behavior
- Security risks and controls
- Tests and evaluation criteria
- Design alternatives and decisions
- Learning prerequisites and achieved depth
- Known limitations and deferred work

Software operation is necessary, but the learner's ability to reason about, diagnose, secure, and explain it is the true completion criterion.

---

# 18. Future supporting documents

This project definition should remain the stable center of AegisLab. Detailed supporting documents will be created only when needed.

Likely future documents include:

- System context and high-level architecture
- Module specifications
- Scenario specification format
- Canonical event and evidence model
- Threat model
- Detection specification and evaluation method
- Agent trust, tool, and authorization model
- Learning roadmap and depth-aware progress tracker
- Architecture Decision Records
- Development journal or devlog
- Significant failure postmortems
- Versioned capability-snapshot reports
- Evergreen reference-scenario demonstrations
- Selective public portfolio and publication plan
- Resilience experiment and game-day reports
- External review and standards-calibration log
- Test, replay, and experiment strategy
- Operational and security runbooks

The existence of this list does not mean all documents must be created before implementation. Each document should appear when it supports an active design or learning need.

---

# 19. Stage 0 completion criteria

The project-definition stage is complete enough to move into high-level architecture and planning when:

- The central identity is accepted and can be explained clearly.
- The target capabilities reflect the desired long-term flagship.
- The logical modules cover the important responsibilities without prematurely requiring specific deployment choices.
- The permanent principles represent the project's intended engineering and learning values.
- The success criteria cover learning, engineering, security, evaluation, and portfolio outcomes.
- Known limitations and compensating practices are represented honestly.
- Important unclear terms or disagreements are recorded as open decisions.
- The document is internally consistent.

Stage 0 completion does not make every decision permanent. Future changes are allowed, but significant changes to the project's identity, invariants, or center of gravity should be deliberate and documented.

---

# 20. Decisions for the next definition review

Before declaring the project definition version 1.0, the following should be reviewed together rather than assumed:

1. Is the proposed central identity—an evidence-centered network-defense laboratory—the correct long-term identity?
2. Are any target capabilities missing or inconsistent with the intended future career direction?
3. Are the logical module boundaries understandable and sufficient at this level?
4. Which principles are truly permanent, and which belong in later implementation guidance?
5. Are the initial scenario families appropriate for the kinds of networking, security, data, ML, and agent skills the project should develop?
6. What evidence should demonstrate progress at the project, module, and learning levels?
7. Do the known limitations and compensating practices accurately describe what AegisLab can and cannot teach?

These decisions should be settled step by step. Detailed architecture, implementation sequencing, and technology selection will follow in later stages.
