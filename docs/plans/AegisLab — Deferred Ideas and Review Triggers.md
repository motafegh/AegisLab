# AegisLab — Deferred Ideas and Review Triggers

**Status:** Active parking and review register  
**Last meaningful update:** 2026-07-15  
**Authority:** Non-normative; no item here enters scope without satisfying its trigger and the governing Charter or a later bounded charter

## 1. Purpose

AegisLab is expected to generate many useful ideas while foundational mechanisms are being learned.

This file preserves those ideas without allowing them to interrupt the dependency order or silently expand the active slice.

An entry here means:

```text
worth remembering
≠
approved now
≠
required for Core
```

## 2. Review rule

A deferred idea may move into active planning only when all of these are true:

1. a current requirement or demonstrated limitation names the problem;
2. the learner has enough prerequisite depth to evaluate the choice;
3. the idea fits the active Charter or receives a new bounded decision;
4. its smallest educational form is identified;
5. safety, evidence, testing, and stop conditions are defined;
6. adding it does not bypass an unfinished ownership gate.

Framework familiarity, novelty, portfolio appearance, or industry popularity alone are not sufficient entry reasons.

## 3. High-value Core ideas with explicit triggers

### 3.1 Namespace lab bootstrap and cleanup script

**Idea:** Create a small script that builds, verifies, and cleans the namespace SSH environment.

**Why useful:** Improves reproducibility and makes later repeated scenarios less error-prone.

**Do not start before:** The learner can reconstruct and explain the important manual steps with materially reduced prompting.

**Entry trigger:** The canonical namespace scenario is stable and has been completed manually at least once from a clean state.

**Required safeguard:** The script must verify target namespace names, addresses, listener scope, and cleanup outcomes rather than blindly assuming success.

### 3.2 Scenario manifest

**Idea:** Represent scenario identity, actors, target, cases, expectations, safety bounds, and cleanup in a small versioned data file.

**Why useful:** Preserves one scenario meaning across namespaces, Docker, and VMs.

**Entry trigger:** The normal-authentication and repeated-failure semantics are stable in the namespace adapter.

**Initial form:** A human-readable YAML or JSON document may be considered only after the learner understands the fields; format choice is not yet committed.

### 3.3 Run identifier and evidence bundle

**Idea:** Give each scenario execution a unique run identifier and an evidence directory containing bounded records.

**Potential contents:**

```text
run metadata
command attempts
expected truth
host records
socket snapshots
process snapshots
network capture
collection notes
checksums
cleanup result
```

**Entry trigger:** The first complete canonical namespace run is ready to preserve, or cross-environment evidence becomes difficult to associate reliably.

**Design requirement:** Do not treat a folder of files as evidence without source, time, environment, and provenance metadata.

### 3.4 Start and end markers

**Idea:** Generate explicit scenario markers that bound relevant telemetry.

**Why useful:** Helps distinguish experiment activity from unrelated system records and supports later truth construction.

**Entry trigger:** Before the first preserved repeated-failure run.

**Open question:** Select marker mechanisms only after observing available host logs and packet evidence; do not assume one marker reaches every sensor.

### 3.5 Environment capability matrix

**Idea:** Record which environment exposes or isolates users, filesystems, kernels, processes, logs, packet-capture points, service lifecycle, persistence, and cleanup.

**Entry trigger:** Begin when the Docker adapter starts; complete after the VM adapter.

**Output:** The three-environment comparison required by the first-slice gate.

### 3.6 Adapter contract

**Idea:** Define a small common interface for preparing, running, observing, and cleaning a scenario in namespaces, Docker, and VMs.

**Entry trigger:** All three manual adapters have been understood and their true commonality is visible.

**Do not do early:** Do not invent an abstraction based only on the namespace implementation.

### 3.7 Experimental-truth manifest

**Idea:** Preserve attempted actions, expected effects, observed execution outcomes, and known limitations separately from sensor telemetry.

**Why useful:** Prevents logs from being treated as ground truth merely because they exist.

**Entry trigger:** The first canonical scenario contract is written.

**Later use:** Evaluation, false-negative diagnosis, replay, and report support.

### 3.8 Evidence checksum manifest

**Idea:** Hash preserved raw evidence files and record algorithm, time, and file identity.

**Entry trigger:** Raw evidence begins to be preserved beyond one terminal session.

**Required depth:** Teach hashes as integrity identifiers and explain what they do and do not prove before implementation.

### 3.9 Clock and timestamp inventory

**Idea:** Record source clocks, time zones, timestamp precision, and collection time for each evidence source.

**Entry trigger:** Before comparing Docker and VM evidence or implementing a time-window detector.

**Why useful:** Cross-source correlation and repeated-failure detection can be invalidated by misunderstood clocks.

### 3.10 Sensor coverage and limitation matrix

**Idea:** For each required fact, identify which source can observe it, which source cannot, and where evidence may be missing or ambiguous.

**Entry trigger:** Host and network evidence are both available.

**Example distinction:** A packet can show a connection to TCP port 22 but normally cannot prove which Linux account authenticated after SSH encryption.

### 3.11 Cleanup verifier

**Idea:** Add explicit post-run checks for listeners, processes, namespaces, containers, VMs, temporary keys, and evidence finalization.

**Entry trigger:** Scenario automation begins or repeated manual cleanup becomes unreliable.

**Safety value:** Prevents lab services and privileged processes from remaining unintentionally active.

### 3.12 Compact portfolio evidence packet

**Idea:** At major gates, create a defensible artifact containing architecture, experiment contract, selected evidence, findings, limitations, and learner ownership disclosure.

**Entry trigger:** Three-environment Slice 1 closure, first evidence-linked detection, controlled-failure postmortem, or Core graduation.

**Do not do early:** Portfolio polish must not replace unfinished evidence or independent explanation.

## 4. Learning-system ideas

### 4.1 Unknown and deferred-question queue

**Idea:** Maintain a bounded list of questions discovered during work that are useful but non-blocking.

**Entry trigger:** When multiple parked questions are repeatedly being lost or reopened.

**Rule:** Every item needs a reason for deferral and a review trigger; remove resolved or irrelevant items.

### 4.2 Reduced-prompt reconstruction checkpoints

**Idea:** Periodically ask the learner to rebuild or diagnose a changed case with less scaffolding.

**Entry trigger:** After a mechanism has been taught and practiced, before claiming transfer or independence.

**Current use:** Required before the namespace scenario transfers to Docker.

### 4.3 Own-words technical summaries

**Idea:** The learner writes a concise explanation after selected study guides are produced.

**Entry trigger:** At meaningful milestone boundaries, not after every command.

**Purpose:** Separate assisted documentation quality from independent explanation ability.

### 4.4 Interview and portfolio transfer checks

**Idea:** Ask the learner to explain the mechanism without terminal output, then reconnect the explanation to evidence.

**Entry trigger:** After practical evidence is stable enough that recall work will not replace missing implementation.

### 4.5 Spaced diagnosis cases

**Idea:** Revisit a mechanism later using a changed symptom rather than repeating the same command.

**Entry trigger:** A topic is being treated as stable but independent diagnosis has not been demonstrated.

## 5. Engineering ideas for later Core milestones

### 5.1 Deterministic scenario runner

**Trigger:** The versioned manual scenario and adapter responsibilities are understood.

**Constraint:** It records attempted actions and outcomes; it must not manufacture truth from intended actions.

### 5.2 Raw-evidence inventory and provenance graph

**Trigger:** Multiple source records and transformations exist.

**Constraint:** Begin with explicit identifiers and parent links; do not introduce a graph database without a demonstrated query need.

### 5.3 Negative-evidence representation

**Idea:** Record expected evidence that was not observed without claiming absence of activity.

**Trigger:** Evaluation begins comparing expected and collected telemetry.

### 5.4 Quarantine with reason codes

**Trigger:** The first malformed or unacceptable raw/normalized record exists.

**Constraint:** Preserve rejected input and reason without silently dropping it.

### 5.5 Detection boundary test generator

**Trigger:** The repeated-failure threshold and time window are implemented and understood manually.

**Cases:** Below, at, and above threshold; just inside/outside window; duplicate; late; missing.

### 5.6 Evidence-linked report claim checker

**Trigger:** A deterministic report exists.

**Idea:** Verify that factual report claims reference evidence or an explicit derivation.

### 5.7 Replay manifest

**Trigger:** Fixed raw records can be processed through normalization and detection.

**Requirement:** Record code/configuration/schema/rule versions that influence replay.

### 5.8 One real producer–collector boundary

**Trigger:** The complete local evidence loop works and a runtime-boundary learning goal is active.

**Constraint:** Begin with a small understandable transport; Kafka or similar frameworks remain deferred until a demonstrated need exists.

## 6. Architecture Decision Records to create only when triggered

Potential decisions include:

- VM manager selection;
- scenario manifest format;
- evidence directory layout;
- raw evidence identifier strategy;
- timestamp and clock policy;
- first normalized event representation;
- initial storage mechanism;
- producer–collector transport;
- duplicate-handling semantics.

Create an ADR only when alternatives exist, the decision has durable consequences, and enough evidence exists to evaluate the trade-off.

Do not create ADRs for routine commands or reversible details.

## 7. Later capability tracks already deferred by the project

These remain outside Core unless a later charter deliberately activates them:

- DFIR and hypothesis-led threat hunting beyond the bounded Core evidence loop;
- multiple attack families;
- applied security ML;
- LLM investigation agents;
- prompt-injection and agent-tool security experiments;
- mature distributed event frameworks;
- substantial dashboards;
- Kubernetes or public cloud;
- dynamic malware analysis, which remains prohibited until its separate maturity gate is satisfied.

## 8. Ideas rejected for the current stage

The following should not enter the active namespace slice:

- a web dashboard;
- Kafka, Redpanda, Flink, or Kubernetes;
- cloud deployment;
- an LLM investigator;
- machine-learning detection;
- multiple SSH attack variants beyond what is needed to establish the canonical repeated-failure case;
- a generalized plugin framework;
- extensive scenario automation before manual ownership;
- production-hardening claims based on the temporary `/tmp` lab configuration.

## 9. Review cadence

Review this file only when:

- a milestone closes;
- a demonstrated limitation appears;
- the learner reaches the prerequisite depth for a parked decision;
- an idea is being repeatedly reconsidered;
- the Core or a later charter changes scope.

Do not review it during every live command sequence.

## 10. Current highest-value deferred items

The next likely activations, in order, are:

```text
start/end marker design
        ↓
canonical scenario and truth record
        ↓
run identifier and evidence bundle
        ↓
Docker/VM capability matrix
        ↓
manual three-environment comparison
        ↓
namespace bootstrap and cleanup automation
        ↓
versioned adapter contract
```

These remain deferred until their stated triggers are met.

## 11. Maintenance contract

- Every idea must include a problem, reason, trigger, and important constraint.
- Remove ideas that no longer support the project’s goals.
- Move activated decisions into the appropriate specification or ADR rather than implementing from this file directly.
- Keep rejected-current-stage items visible when they are likely sources of scope pressure.
- Never store secrets, credentials, private keys, unsafe operational details, or malicious samples.
