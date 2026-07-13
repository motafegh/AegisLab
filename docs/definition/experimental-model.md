# Experimental Model

**Part of:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)
**Status:** Normative part of the accepted definition

## The complete experimental loop

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

## Foundational vocabulary

The detailed data model will be designed later, but the project needs an initial shared language.

| Term | Initial practical meaning |
|---|---|
| Scenario | A versioned definition of a controlled experiment |
| Action record | A versioned record describing a commanded action, execution attempt, reported outcome, or verified effect; its evidentiary status must be explicit |
| Commanded action | What the scenario instructed an executor to do |
| Execution attempt | Evidence that execution of a commanded action began or was attempted |
| Executor-reported outcome | What the executing component reports happened |
| Target-observed effect | What the target or another relevant observer recorded as an effect |
| Independently verified effect | An effect supported through a separately maintained observation or cross-check |
| Raw record | Sensor output preserved close to its original representation |
| Event | A normalized representation of something observed |
| Evidence | An event or artifact used to support or challenge an investigative conclusion |
| Forensic artifact | A preserved host, disk, memory, log, network, or related object acquired for investigation |
| Acquisition record | A record of how, when, from where, by whom or what, and with which tool version an artifact was collected, including integrity and limitation information |
| Custody record | A record of possession, transfer, access, or transformation relevant to an artifact's handling history; AegisLab uses this for traceability and does not claim legal admissibility without an applicable external process |
| Forensic observation | A reproducible technical result obtained from an artifact; analyst interpretation remains separate |
| Investigation timeline | An ordered, provenance-backed representation of relevant activity that preserves timestamp sources, uncertainty, conflicts, and gaps |
| Hunt hypothesis | A testable investigative proposition with stated rationale, required evidence, results, and disposition |
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
| Experimental truth | The best provenance-backed account of what occurred in a controlled experiment, constructed from action, environment, target, and independent verification records with limitations preserved |
| Capability snapshot | A versioned measurement of what AegisLab can do at a particular point in its development |
| Golden case | A carefully reviewed evaluation case with known or agreed expected results |
| Postmortem | A blameless review of a significant failure, incorrect decision, or abandoned approach |
| Failure injection | The deliberate introduction of a controlled fault to study system behavior |
| Chaos engineering | Controlled experimentation used to test hypotheses about system resilience under disruption |
| Blast radius | The portion of the system, data, or environment that an experiment or failure can affect |
| Game day | A scheduled exercise for practicing failure detection, diagnosis, response, and recovery |
| External calibration | Comparison with established specifications, artifacts, or external feedback to challenge internal assumptions |

These definitions are provisional. Later specifications may refine them, but changes must be deliberate and documented.

## Ground-truth model

Experimental truth is not a single perfect label. AegisLab should eventually distinguish:

- **Intent truth:** what the scenario was designed to simulate
- **Action truth:** what actions were actually executed
- **Environment truth:** what systems, identities, configurations, and relationships existed
- **Telemetry expectation:** what correctly functioning sensors were expected to observe
- **Observed telemetry:** what the sensors and pipeline actually captured
- **Detection expectation:** what detections were expected to produce
- **Investigation expectation:** what conclusions the available evidence reasonably supports

The scenario system must not declare that an intended effect occurred merely because it issued a command. Experimental truth should distinguish:

1. What was commanded
2. What execution was attempted
3. What the executor reported
4. What the target observed
5. What a separate mechanism verified

These sources may disagree because a process failed midway, a target rejected an operation, a network path dropped traffic, a clock was incorrect, or a logger was faulty. The truth record must preserve those disagreements and the provenance of each claim.

Ground truth is therefore a practical shorthand for the best-supported experimental account available to the evaluator. It is constructed through trusted mechanisms and cross-checks; it is not assumed to be infallible.

These distinctions help locate failure correctly.

For example, an attack action may execute successfully while a sensor fails to observe it. Alternatively, telemetry may be collected correctly while a parser rejects it or a detector misses it. AegisLab should avoid treating all these cases as the same failure.

Scenario ground truth used by the evaluator must not be silently exposed to the detection or investigation components being evaluated.
