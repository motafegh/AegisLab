# Identity and Learning Goals

**Part of:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)
**Status:** Normative part of the accepted definition

## Project identity

> **AegisLab is a long-running, modular, evidence-centered network-defense learning laboratory in which controlled activity is observed through imperfect telemetry, transformed into defensible security conclusions, and evaluated against separately maintained, provenance-backed experimental truth. It progressively studies detection, distributed processing, security data and evidence engineering, applied security machine learning, digital forensics and incident response, threat hunting, and constrained AI-assisted investigation while preserving human understanding, authority, and auditability.**

The project has two connected identities:

- **Cyber range:** a safe and controlled environment where normal, malicious, ambiguous, and failure-related activity can be generated.
- **Defense platform:** a system that observes activity, processes telemetry, detects suspicious behavior, organizes evidence into incidents, supports investigation, and evaluates its conclusions.

These identities depend on each other:

- The cyber range provides controlled experiments and provenance-backed records from which experimental truth can be constructed.
- The defense platform attempts to reconstruct what happened using the telemetry available to it.
- The evaluation process compares the platform's observations and conclusions with what actually occurred.

The distinctive purpose of AegisLab is therefore not merely to generate attacks or produce alerts. It is to study the complete path from real activity to defensible security conclusions.

## Central project thesis

AegisLab is built around the following idea:

> A security conclusion is valuable only when we can explain what evidence supports it, how that evidence was collected and transformed, what reasoning was applied, what uncertainty remains, and how the conclusion compares with what actually occurred.

This makes AegisLab different from:

- A generic Security Information and Event Management (SIEM) clone
- A collection of attack scripts
- A machine-learning intrusion-detection demonstration
- A dashboard over security logs
- A Large Language Model (LLM) wrapper that summarizes arbitrary telemetry
- A collection of technologies added without a shared engineering purpose

Networking, distributed systems, data engineering, machine learning, digital forensics, threat hunting, and AI agents all support the same evidence-driven investigation loop.

The project's center of gravity is:

> **Network security and distributed systems first; data, evidence, detection, and investigation engineering throughout; machine learning when it has a justified problem to solve; and LLM agents as constrained investigators rather than unquestioned decision makers.**

Its intended signature is:

> **Network defense, detection-platform engineering, and evidence-centered investigation provide the operational foundation; secure AI-assisted investigation, strengthened by applied security ML, DFIR, and threat hunting, provides the differentiating specialization.**

The agent-security specialization must grow on top of real networking, telemetry, detection, data, and system-security foundations. It must not become a disconnected LLM demonstration.

## Primary learning goal

The main goal is not merely to finish the software.

> The learner should become capable of designing, implementing, testing, operating, securing, evaluating, and explaining an intelligent distributed security system without depending on an AI assistant to make or explain its core decisions.

Over the lifetime of the project, the learner should become able to explain and demonstrate:

- How traffic moves through the laboratory network
- How host, network, application, and identity telemetry is produced
- How telemetry is collected, transported, transformed, stored, and queried
- How distributed components communicate, fail, recover, and create duplicates or delays
- How detections are designed, tested, tuned, and evaluated
- How raw observations become events, findings, alerts, incidents, and reports
- How forensic artifacts are acquired, preserved, verified, analyzed, and organized into defensible timelines
- How threat-hunting hypotheses are formed, tested, revised, and documented
- How an ML model is trained, validated, deployed, monitored, attacked, and retired
- How an investigation agent selects and uses tools
- How untrusted data can manipulate or mislead an LLM
- How services, identities, credentials, evidence, and agent actions are secured
- Why each important architectural decision was made
- Which parts are understood only at an introductory level and which have been studied and applied in technical depth

### Personal purpose and career direction

AegisLab supports the learner's confirmed long-term direction toward becoming an **AI Security Automation Engineer** with an anchored hybrid capability profile: an engineer who integrates network defense, detection-platform engineering, secure distributed systems, security data and evidence engineering, applied security machine learning, DFIR, threat hunting, and controlled AI agents to build defensible security automation.

The anchor prevents the project from becoming a collection of unrelated job roles. Shared foundations receive independent engineering depth; applied security ML reaches strong practical competence; DFIR and threat hunting receive deliberate investigative depth; and secure, evidence-grounded AI automation remains the distinctive integrating specialization.

The project is intended to develop:

- The security and networking knowledge required to understand the systems being defended
- The software, distributed-systems, and data-engineering knowledge required to build reliable security platforms
- The detection and incident-investigation knowledge required to make defensible security decisions
- The forensic and threat-hunting knowledge required to preserve artifacts, reconstruct activity, test hypotheses, and scope incidents
- The AI and agent-security knowledge required to automate carefully without surrendering evidence, control, accountability, or human judgment

This personal purpose helps determine learning depth. Not every domain must become an equal specialty.

### Learning priority hierarchy

#### Foundational depth

The following domains should become strong enough to support independent engineering and diagnosis:

- Networking and network analysis
- Security and detection engineering
- Distributed systems
- Software engineering
- Secure system design
- Security data and evidence engineering
- Detection-platform engineering

#### Differentiating specialization

The following connected capabilities should become a recognizable AegisLab specialty:

- Secure AI-assisted investigation
- Evidence-grounded agent reasoning
- Agent tool authorization and least authority
- Prompt-injection and context-poisoning resistance
- Human-supervised security automation
- Evaluation of agent claims, tool use, uncertainty, and actions
- Evidence-centered digital forensics and incident reconstruction
- Hypothesis-led threat hunting and investigative scoping

#### Supporting breadth

The following domains should be learned properly and taken to the depth required by actual AegisLab problems, without assuming that every one must become an equal specialty:

- Broader general-purpose data engineering beyond AegisLab's security-evidence needs
- Applied security machine learning, developed to strong practical competence
- Observability and operations
- Deployment infrastructure
- User-interface development where needed

These categories describe intended emphasis, not rigid boundaries. A supporting domain may later become deeper when a meaningful project requirement or career decision justifies it.
