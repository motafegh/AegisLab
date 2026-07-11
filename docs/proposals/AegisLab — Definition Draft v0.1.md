

# AegisLab — Definition Draft v0.1

The name is provisional.

## 1. Project definition

> AegisLab is a controlled, reproducible network-security laboratory and intelligent incident-detection platform. It generates and observes realistic network activity, collects telemetry, processes events through a distributed pipeline, detects suspicious behavior using rules and machine learning, correlates evidence into incidents, and supports human-supervised investigation through a constrained AI agent.

The system’s conclusions must always be traceable to evidence.

This gives the project two connected identities:

- **Cyber range:** a safe environment where normal and malicious activity can be generated.
- **Defense platform:** a system that observes, detects, investigates, and evaluates that activity.

The cyber range gives us known ground truth. The defense platform gives us something meaningful to build.

---

## 2. Primary learning goal

The main goal is not merely to finish the software.

> You should become capable of designing, implementing, testing, operating, securing, and explaining an intelligent distributed security system without depending on an AI assistant to make its core decisions.

By the end, you should be able to explain:

- How traffic moves through the network
- How telemetry is produced and transported
- How distributed components communicate and fail
- How detections are created and evaluated
- How raw events become incidents
- How an ML model is trained, validated, deployed, and monitored
- How an agent selects and uses tools
- How untrusted data can manipulate an LLM
- How services, credentials, data, and agent actions are secured
- Why each important architectural decision was made

---

## 3. Initial system boundary

A user should be able to start the lab and run a controlled scenario such as an SSH password attack.

AegisLab should then:

1. Generate both normal and malicious activity.
2. Observe the relevant network and host events.
3. Transport those events reliably.
4. Normalize them into a documented event schema.
5. Detect suspicious behavior.
6. Correlate related alerts into an incident.
7. Preserve the evidence used in the decision.
8. Allow an investigation agent to query that evidence.
9. Produce an evidence-backed incident report.
10. Compare the result against the known scenario ground truth.

That is the complete learning loop.

```text
Scenario definition
       ↓
Controlled execution
       ↓
Network and host telemetry
       ↓
Ingestion and processing
       ↓
Detection and correlation
       ↓
Agent-assisted investigation
       ↓
Evidence-backed report
       ↓
Evaluation against ground truth
```

---

# 4. Core project goals

## Goal 1: Learn networking through observation and implementation

You will learn:

- The TCP/IP model
- Ethernet, IP, TCP, UDP, and ICMP
- Ports, sockets, connections, and sessions
- DNS resolution and common DNS behaviors
- HTTP and TLS fundamentals
- Routing, NAT, firewalls, and network segmentation
- Packet capture versus flow records
- Linux network namespaces and virtual interfaces
- Network traffic analysis

You should eventually be able to inspect a packet capture and explain what occurred without relying entirely on automated tools.

## Goal 2: Learn security engineering through controlled attacks

You will learn:

- Threat modeling
- Attack surfaces and trust boundaries
- Detection engineering
- Indicators versus behavioral detections
- Authentication abuse
- Reconnaissance and scanning
- Command-and-control-like patterns
- Data exfiltration patterns
- Incident response
- Evidence preservation
- False-positive analysis
- Adversarial thinking
- Security controls and their limitations

All offensive activity must remain inside our controlled lab.

## Goal 3: Learn distributed systems by building the telemetry pipeline

You will learn:

- Producers and consumers
- Queues and event streams
- Message ordering
- Partitions and consumer groups
- Backpressure
- Batching
- Retries and exponential backoff
- At-most-once, at-least-once, and effectively-once processing
- Idempotency
- Dead-letter queues
- Schema evolution
- Time synchronization and late events
- Horizontal scaling
- Partial failure and recovery
- Distributed observability

We should first implement a small version ourselves. Only afterward should we introduce a mature event-streaming framework.

## Goal 4: Learn data engineering

You will learn:

- Event collection and normalization
- Raw, normalized, and derived data layers
- Data contracts and schemas
- Validation and quarantine
- Deduplication
- Timestamp handling
- Data lineage
- Dataset versioning
- Ground-truth generation
- Data quality measurements
- Batch versus stream processing
- Retention and privacy considerations

This revisits one of Sentinel’s most important lessons: poor labels and unclear data provenance can invalidate an impressive model.

## Goal 5: Learn ML as an experimental discipline

You will learn:

- Translating security behavior into an ML problem
- Feature engineering from network events
- Supervised classification
- Unsupervised and semi-supervised anomaly detection
- Class imbalance
- Time-based dataset splitting
- Data leakage
- Model baselines
- Threshold selection
- Precision, recall, F1, ROC-AUC, and PR-AUC
- Alert-volume-aware evaluation
- Calibration
- Explainability
- Concept drift
- Model serving and monitoring
- Adversarial evasion

We will not start with deep learning. A simple statistical baseline or tree model must establish what the more complicated model needs to improve.

## Goal 6: Learn LLM and agent engineering

The agent will be an investigator, not the detection engine.

You will learn:

- Tool calling
- Typed tool interfaces
- Agent state and control flow
- Short-term versus persistent memory
- Retrieval-augmented generation
- Query planning
- Evidence grounding
- Structured outputs
- Confidence and uncertainty
- Agent evaluation
- Prompt injection
- Context poisoning
- Tool authorization
- Sandboxing
- Human approval gates
- Audit logging

The agent must distinguish among:

- Observed fact
- Derived fact
- Hypothesis
- Recommendation
- Executed action

That separation will be a major project invariant.

## Goal 7: Learn secure system design

You will learn:

- Authentication and authorization
- Role-based and capability-based access
- Secrets management
- Service identities
- TLS and possibly mutual TLS
- Input validation
- Least privilege
- Secure defaults
- Dependency and supply-chain security
- Container isolation
- Rate limiting
- Audit logging
- Tamper-evident records
- Backup and recovery
- Threat modeling for the platform itself

The security platform must itself be treated as a target.

## Goal 8: Learn software and operational engineering

You will learn:

- Python application design
- Potentially Go or Rust for selected systems components
- API design
- Command-line interfaces
- Relational databases
- Testing strategies
- Property-based testing
- Integration and end-to-end testing
- Containers
- CI
- Configuration management
- Metrics, logs, and traces
- Performance profiling
- Load testing
- Deployment and failure diagnosis

---

# 5. Proposed attack scenarios

The initial project should support five scenarios:

1. **Network reconnaissance**
   - Port scanning
   - Connection patterns
   - Horizontal versus vertical scans

2. **SSH authentication attack**
   - Repeated login failures
   - Distributed attempts
   - Successful login following failures

3. **Web authentication abuse**
   - Credential guessing
   - Suspicious session behavior
   - Rate-limit interaction

4. **Suspicious DNS behavior**
   - High-entropy subdomains
   - Unusual query frequency
   - DNS tunneling-like behavior

5. **Simulated data exfiltration**
   - Unusual outbound volume
   - Rare destination
   - Abnormal transfer timing

Each scenario should include:

- A normal-behavior version
- A malicious version
- A scenario definition
- Expected telemetry
- Known start and end times
- Expected detections
- Ground-truth labels
- Evaluation criteria

---

# 6. Technologies by learning layer

These are candidates, not commitments.

| Layer | Start by learning | Later framework candidates |
|---|---|---|
| Networking | Linux sockets, namespaces, packet capture | Scapy, Zeek, Suricata |
| Event transport | In-memory queue, TCP collector | Kafka or Redpanda |
| Stream processing | Custom workers and windows | Flink, Kafka Streams, or Bytewax |
| Storage | Files and SQLite | PostgreSQL, object storage, time-series/search store |
| APIs | HTTP and API fundamentals | FastAPI |
| Data validation | Manual schema validation | Pydantic, JSON Schema, Avro or Protobuf |
| ML | NumPy and scikit-learn baselines | PyTorch when justified |
| Experiment tracking | Structured experiment records | MLflow |
| Dataset versioning | Hashes and manifests | DVC |
| Agent workflow | Explicit Python state machine | LangGraph only if complexity justifies it |
| Agent tools | Python interfaces | MCP after tool boundaries are understood |
| Observability | Structured logs and counters | OpenTelemetry, Prometheus, Grafana |
| Deployment | Processes and shell scripts | Docker Compose, later Kubernetes only if necessary |
| Security | Manual certificates and permissions | Vault or another secrets system later |

A crucial rule:

> A framework enters the project only after we can name the problem it solves and demonstrate that the problem exists in our current implementation.

---

# 7. What is explicitly outside the initial scope

To stop AegisLab from becoming another uncontrollably large system, version one will exclude:

- Public-cloud deployment
- Kubernetes
- Blockchain
- Zero-knowledge proofs
- Autonomous blocking or retaliation
- Malware execution
- Real external targets
- Training a foundation model
- A large frontend application
- Dozens of attack categories
- Multiple agent personas
- A general-purpose SOC platform
- Production-scale throughput

These can enter later only through a deliberate expansion decision.

---

# 8. The learning rules

I suggest we adopt these as project rules:

### Rule 1: Explain before abstraction

Before adopting a framework, you must explain the underlying problem and implement a minimal form of the mechanism.

### Rule 2: One new difficulty at a time

A phase may introduce one major unfamiliar system concept. For example, we should not introduce Kafka, Kubernetes, online ML, and agents simultaneously.

### Rule 3: Architecture must follow demonstrated requirements

We do not add a service because a diagram looks professional. We add it because an existing requirement cannot be handled cleanly by the current design.

### Rule 4: Every module has a learning record

Each module documents:

- Its responsibility
- Inputs and outputs
- Data model
- Important invariants
- Failure modes
- Security risks
- Tests
- Design alternatives
- What you learned
- What remains unclear

### Rule 5: You own the first explanation

When we finish a module, you explain it to me. I challenge unclear areas and identify knowledge gaps.

### Rule 6: No unexplained code survives

If neither of us can explain why a dependency, abstraction, or block of code exists, we remove it or study it.

### Rule 7: Growth requires a gate

A proposed feature enters the project only if:

- It supports a defined learning goal.
- Its prerequisites are understood.
- The current phase is complete.
- Its cost is recorded.
- Something else is deferred when necessary.

---

# 9. Definition of success

AegisLab is successful when you can independently:

- Draw its architecture from memory
- Explain one event’s entire journey through the system
- Diagnose a missing or duplicated event
- Implement a new rule-based detection
- Train and evaluate a new ML detector
- Explain whether its evaluation contains leakage
- Add a new agent tool with proper permissions
- Demonstrate and mitigate a prompt-injection attempt
- Recover a failed consumer or service
- Threat-model a new feature
- Run a scenario and interpret the result
- Defend the major architectural decisions

The software working is necessary, but your ability to reason about it is the true completion criterion.

# Decisions we should make next

Before turning this into a formal charter, we need to settle four matters:

1. **Primary identity:** I recommend “network-defense learning laboratory,” with ML and agents supporting it—not dominating it.
2. **Language strategy:** Python-only initially, or Python plus a systems language later. I recommend Python first and Go or Rust only when we reach a component that benefits from it.
3. **ML depth:** Applied detection engineering versus deeper model research. I recommend strong ML fundamentals and evaluation, with advanced modeling as a later branch.
4. **Time horizon:** Whether we are designing a focused 4–6 month core or another open-ended long-term system. I recommend a finishable core followed by optional expansion tracks.

My proposed center of gravity is:

> **Network security and distributed systems first; ML second; LLM agents third; all connected through evidence-driven incident investigation.**

That ordering gives us strong fundamentals while still covering every field you named.