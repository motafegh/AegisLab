# Learning and Technology Strategy

**Part of:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)
**Status:** Normative part of the accepted definition

## Learning domains

AegisLab connects several learning domains through one system. The project must record the depth reached in each subject rather than marking broad subjects as simply "completed."

The [learning priority hierarchy](identity-and-learning-goals.md#learning-priority-hierarchy) determines the intended emphasis: foundational domains should become strong, secure agent-assisted investigation should provide the differentiating specialization, and supporting domains should reach the depth required by real project problems.

### Networking and network analysis

- TCP/IP model and encapsulation
- Ethernet, Address Resolution Protocol (ARP), Internet Protocol (IP), Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Internet Control Message Protocol (ICMP)
- Ports, sockets, connections, and sessions
- Domain Name System (DNS)
- Hypertext Transfer Protocol (HTTP) and Transport Layer Security (TLS)
- Routing, Network Address Translation (NAT), firewalls, and segmentation
- Packet capture, flow records, and traffic analysis
- Linux network namespaces and virtual interfaces

### Security and detection engineering

- Threat modeling, attack surfaces, and trust boundaries
- Behavioral detections and indicators
- Authentication abuse, reconnaissance, command-and-control-like patterns, and exfiltration patterns
- Incident response and evidence preservation
- False-positive and false-negative analysis
- Detection limitations, evasion, and adversarial thinking

### Distributed systems

- Producers, consumers, queues, and event streams
- Ordering, partitioning, batching, retries, and exponential backoff
- Backpressure and partial failure
- At-most-once, at-least-once, and effectively-once processing
- Idempotency and duplicate handling
- Dead-letter queues and quarantine
- Time synchronization and late events
- Horizontal scaling, recovery, and distributed observability

### Security data and evidence engineering

This is the foundational portion of data engineering required to make security observations, evidence, ground truth, replay, and evaluation trustworthy. Broader general-purpose data engineering remains supporting breadth unless a demonstrated AegisLab requirement demands greater depth.

- Raw, normalized, and derived data layers
- Data contracts, validation, and schema evolution
- Deduplication, timestamps, lineage, and retention
- Dataset versioning and ground-truth generation
- Data-quality measurement
- Batch and stream processing
- Privacy and sensitive-data handling

### Machine learning

- Translating security behavior into an ML problem
- Feature engineering and baseline models
- Supervised, unsupervised, and semi-supervised methods
- Class imbalance, time-based splits, and data leakage
- Precision, recall, F1, Receiver Operating Characteristic Area Under the Curve (ROC-AUC), and Precision–Recall Area Under the Curve (PR-AUC)
- Thresholds, calibration, alert-aware evaluation, and explainability
- Model serving, monitoring, drift, and adversarial evasion

### LLM and agent engineering

- Tool calling and typed tool interfaces
- State, control flow, memory, and retrieval
- Evidence grounding and structured outputs
- Confidence, uncertainty, and agent evaluation
- Prompt injection and context poisoning
- Tool authorization, sandboxing, approval gates, and audit logging

### Secure system design

- Authentication, authorization, and service identities
- Role-Based Access Control (RBAC) and capability-based access
- Secrets management and encrypted communication
- Least privilege, secure defaults, and input validation
- Dependency and supply-chain risk
- Isolation, rate limiting, audit records, backup, and recovery
- Threat modeling for AegisLab itself

### Software and operational engineering

- Python application design and selected use of a systems language when justified
- Application Programming Interface (API) and Command-Line Interface (CLI) design
- Databases, testing strategies, and property-based testing
- Integration and end-to-end testing
- Containers, Continuous Integration (CI), and configuration management
- Metrics, logs, traces, profiling, load testing, deployment, and failure diagnosis

### Digital forensics, incident response, and threat hunting

- Forensic readiness, acquisition planning, artifact integrity, and handling history
- Host, disk, memory, authentication, application, and network artifacts
- Reproducible extraction, validation, enrichment, and timeline construction
- Timestamp provenance, clock behavior, conflicting records, missing evidence, and anti-forensics awareness
- Hypothesis-led hunting, investigative scoping, pivoting, and negative-evidence analysis
- Separation of tool output, technical observation, analyst interpretation, and incident conclusion
- Static malicious-artifact analysis and, only after its maturity gate, controlled dynamic analysis
- Containment, eradication, recovery, lessons learned, and honest limits of a solo laboratory

## Learning-depth and AI-ownership model

### Depth-aware progress

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

### AI collaboration modes

AI assistance may take different explicit roles:

- **Teacher:** explains concepts and tests understanding
- **Reviewer:** critiques the learner's proposal or implementation
- **Pair programmer:** collaborates on implementation while preserving learner participation
- **Debugger:** helps investigate evidence and form hypotheses
- **Evaluator:** challenges explanations and independent capability

For foundational decisions, AI should not silently become the owner of the design.

### Ownership test

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

## Technology strategy

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
| Forensics and hunting | Explicit acquisition records, hashes, artifact copies, timeline notes, and hunt hypotheses | A dedicated forensic toolchain after artifact and interpretation boundaries are understood; a dynamic-analysis sandbox only after its maturity gate |

The framework-entry rule is:

> A framework enters AegisLab only when we can name the problem it solves, explain its core mechanism at the required learning depth, and show why it is appropriate for the current requirement.

A bounded educational implementation should teach a mechanism, not attempt to recreate an entire production framework.

### Mechanism-to-framework comparison cycle

Where safe and useful, learning a major abstraction should follow this cycle:

1. Identify and explain the underlying problem.
2. Build or demonstrate a bounded minimal mechanism.
3. Observe its behavior and limitations.
4. Study and briefly exercise a mature tool that addresses the same problem.
5. Compare the designs, guarantees, failure behavior, operational costs, and trade-offs.
6. Decide whether the mature tool should enter AegisLab now, later, or not at all.
7. Record what was learned and which details remain deferred.

The comparison is educational even when the decision is not to adopt the mature tool.

## External alignment

AegisLab may compare or map selected concepts to established security and AI frameworks without turning standards compliance into the project's main purpose.

Potential alignment includes:

- **MITRE ATT&CK:** adversary tactics, techniques, detection strategies, analytics, and defensive coverage
- **MITRE ATLAS:** threats, attack techniques, and mitigations involving AI-enabled systems
- **Open Cybersecurity Schema Framework (OCSF):** comparison and mapping for normalized cybersecurity events
- **Sigma:** portable representation of suitable log detections and correlations
- **OpenTelemetry:** concepts and conventions for operational telemetry such as metrics, logs, and traces
- **NIST Artificial Intelligence Risk Management Framework (AI RMF):** governance and evaluation concepts for trustworthy AI and generative-AI components

The project should align where doing so improves learning, interoperability, evaluation, or professional relevance. It should not copy a standard without understanding its purpose or distort the architecture merely to claim compliance.
