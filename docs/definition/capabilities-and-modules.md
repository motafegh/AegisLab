# Capabilities and Logical Modules

**Part of:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)
**Status:** Normative part of the accepted definition

## Target capabilities

The following are long-term target capabilities. They describe the direction of the flagship project; they are not all requirements for its first working version.

### Controlled scenario execution

AegisLab should be able to:

- Define repeatable normal, malicious, ambiguous, failure, and evasion scenarios
- Create or prepare the required isolated environment
- Execute only explicitly authorized activity against controlled targets
- Record scenario configuration, versions, timing, actors, targets, and performed actions
- Stop, clean up, and rerun scenarios safely

### Telemetry generation and observation

AegisLab should be able to:

- Observe selected network, host, application, authentication, and identity activity
- Preserve raw records when appropriate
- Identify which sensor and source produced each record
- Recognize missing, malformed, duplicated, delayed, or contradictory telemetry
- Distinguish what occurred from what the sensors managed to observe

### Reliable event processing

AegisLab should eventually be able to:

- Collect events from multiple producers
- Validate and normalize different record formats
- Handle retries, duplicates, reordering, backpressure, and partial failure
- Quarantine invalid data rather than silently accepting or discarding it
- Evolve schemas without silently changing the meaning of historical evidence
- Explain the journey of an event through the system

### Evidence preservation and provenance

**Provenance** means the origin and history of a piece of data: where it came from, when it was collected, and how it was transformed.

AegisLab should be able to:

- Give important records stable identities
- Link derived information to its source records
- Record important transformations and their versions
- Preserve enough context to audit an alert or conclusion later
- Detect or reveal inappropriate modification of important records where feasible
- Trace a report claim backward to the evidence supporting it

### Detection engineering

AegisLab should be able to:

- Express rule-based and behavioral detections
- Apply detections over individual events and time windows
- Document the behavior, assumptions, data requirements, and limitations of each detection
- Test positive, negative, boundary, and evasion cases
- Measure false positives, false negatives, detection latency, and alert volume
- Compare revised detections against earlier versions

### Incident correlation

AegisLab should be able to:

- Connect related events, findings, alerts, entities, and evidence
- Group activity into a coherent investigative case
- Record why two objects were considered related
- Preserve alternative explanations and uncertainty
- Reevaluate incidents when new or late evidence arrives

### Machine-learning experimentation

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

The intended ML ceiling is strong **applied ML competence**, not a requirement to invent novel model architectures. Success means the learner can:

- Formulate a defensible security ML problem
- Construct, version, and audit the dataset and labels
- Establish rule-based, statistical, or simple-model baselines
- Detect and prevent common forms of data leakage
- Use evaluation splits and metrics appropriate to the operational problem
- Deploy and monitor a justified model
- Analyze important errors, drift, and evasion
- Explain when ML is inferior to a simpler rule or statistical method

Novel model research may be explored later only through a separate, deliberate expansion decision.

### Human-supervised agent investigation

The AI agent is an investigator, not the primary detection engine and not an unquestioned authority.

AegisLab should eventually be able to:

- Give the agent typed and documented investigation tools
- Restrict the agent to explicitly authorized capabilities
- Require evidence references for factual claims
- Separate observed facts, derived facts, hypotheses, recommendations, and executed actions
- Represent claim support, conflicting evidence, missing evidence, alternative hypotheses, tool failures, and uncertainty
- Avoid treating an LLM's self-reported numeric confidence as a meaningful probability unless that confidence method has been evaluated and calibrated against suitable cases
- Record tool calls, results, failures, approvals, and important decisions
- Evaluate the agent repeatedly using known cases
- Test prompt injection, context poisoning, misleading evidence, and unauthorized tool use
- Require human approval before consequential actions

### Secure platform operation

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

### Reproducible evaluation and replay

AegisLab should eventually be able to:

- Reproduce controlled experiments
- Replay recorded telemetry through new parsers, detections, models, and investigation logic
- Compare results across versions
- Identify which layer caused a missed or incorrect conclusion
- Preserve the relationship between results and the exact scenario, data, configuration, code, rule, model, prompt, and tool versions used

### Resilience experimentation

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

### Asset, identity, and environment context

AegisLab should eventually be able to:

- Describe relevant hosts, services, users, service identities, network zones, addresses, roles, and criticality
- Record relationships such as IP-to-host, user-to-session, service-to-host, and host-to-zone
- Preserve the time interval during which a relationship or attribute was valid
- Distinguish scenario-defined context from context inferred through telemetry
- Provide historical context to detections and investigations
- Represent missing, stale, conflicting, or uncertain contextual information

Context is necessary because an observation such as an IP address connecting to a port has limited security meaning until the system can determine what the entities represented at the relevant time.

### Digital forensics and threat hunting

AegisLab should eventually be able to:

- Form explicit hunting and investigative hypotheses and record why they were accepted, revised, or rejected
- Acquire selected host, disk, memory, log, and network artifacts through documented, authorized procedures
- Record acquisition source, operator or mechanism, time, tool and version, integrity hashes, custody transitions, and known limitations
- Preserve original artifacts separately from working copies and derived results
- Construct evidence-backed timelines while retaining timestamp provenance, clock uncertainty, conflicts, and gaps
- Relate forensic observations to assets, identities, scenarios, alerts, incidents, hypotheses, and experimental truth without collapsing those categories
- Scope affected entities and activity while preserving alternative explanations and negative evidence
- Reproduce important analysis steps and distinguish tool output from analyst interpretation
- Evaluate hunting and forensic conclusions against controlled cases and independently maintained truth when available

Full DFIR and threat hunting form a deliberate depth track, but they do not enter the initial SSH Core. They begin through a separately bounded post-Core expansion so that forensic breadth does not overwhelm the first evidence loop.

## Logical modules

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
| Asset, Identity, and Environment Context | Maintains time-aware knowledge about hosts, services, users, addresses, roles, zones, criticality, and their relationships | Versioned contextual entities and relationships |
| Forensic Acquisition and Analysis | Acquires authorized artifacts, preserves originals and integrity records, produces reproducible observations and timelines, and supports hypothesis-led hunting | Acquisition records, forensic artifacts, observations, timelines, and hunt records |
| Detection Engine | Applies rules, statistics, and justified ML methods | Findings and alerts |
| Correlation and Incident Engine | Relates alerts, events, entities, evidence, and hypotheses | Incidents and relationships |
| Investigation Layer | Provides controlled query and reasoning capabilities to humans and agents | Queries, claims, hypotheses, and investigation history |
| Reporting Layer | Produces structured, evidence-backed conclusions | Versioned incident reports |
| Evaluation Engine | Compares execution, observations, detections, incidents, and reports with expectations and truth | Metrics and failure analyses |
| Control Plane | Manages configuration, identities, permissions, versions, and administrative actions | Auditable control state |

Cross-cutting concerns such as security, testing, observability, documentation, and learning evidence apply to every module.
