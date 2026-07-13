# Scenario Strategy

**Part of:** [AegisLab — Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)
**Status:** Normative part of the accepted definition

## Initial scenario families

The following scenario families provide long-term experimental coverage. They do not all need to be implemented together.

### Evergreen reference scenario

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

### Network reconnaissance

- Port scanning
- Horizontal and vertical connection patterns
- Slow, distributed, or evasive scanning
- Benign administrative and monitoring activity for comparison

### SSH authentication abuse

- Repeated login failures
- Attempts against multiple users or hosts
- Distributed attempts
- Successful login following failures
- Legitimate user mistakes and administrative behavior for comparison

### Web authentication abuse

- Credential guessing
- Suspicious session behavior
- Rate-limit interaction
- Benign automation and user mistakes for comparison

### Suspicious DNS behavior

- High-entropy or unusually long subdomains
- Unusual query frequency
- DNS tunneling-like patterns
- Legitimate software with unusual DNS behavior for comparison

### Simulated data exfiltration

- Unusual outbound volume
- Rare destinations
- Abnormal transfer timing
- Benign backup, synchronization, and large-transfer behavior for comparison

### Forensic investigation and threat hunting

- Authentication and persistence artifacts from controlled host activity
- Disk, memory, log, and network evidence prepared from authorized scenarios
- Timeline reconstruction across sources with clock, gap, and conflict analysis
- Hypothesis-led scoping of users, hosts, services, sessions, and related activity
- Positive, negative, ambiguous, and incomplete-evidence cases
- Static malicious-artifact analysis before any separately gated dynamic analysis

This family begins after the SSH Core under a dedicated expansion charter. Prepared evidence and benign substitutes should be used before live malicious code is considered.

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
