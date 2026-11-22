# AegisLab Current Learning State

**Updated:** 2026-11-22 | **Status:** v2 capability-led route; guided namespace SSH historical foundation; independent Stage B ownership not yet assessed.
**Authority:** Non-normative, evidence-aware learner handoff. See [Core Charter v2](<../plans/AegisLab — Core Charter v2.0.md>) and [Capability Execution Map v2](<../plans/AegisLab — Capability Execution Map v2.md>).

## Established with guidance (July)

- Created/rebuilt two Linux network namespaces, veth interfaces, IPv4 routes and ICMP path; diagnosed one network-address omission with help.
- Practiced Linux file ownership/modes and separate OpenSSH server host identity, client key authorization and known-host trust.
- Demonstrated authorized public-key SSH authentication, valid unauthorized-key failure, log/packet/socket/process correlation, encrypted-packet visibility limits and clean connection teardown.
- Interpreted the observed SSH execution lifecycle substantially **with assistance**; independent reconstruction, delayed recall and changed-case diagnosis remain unproven.
- Inspected Docker Desktop/engine inventory and networks during former M5 planning. Container lifecycle and adapter operation were **not** demonstrated.
- Formal old M4 repeated-failure contract, fixed threshold/window, independent truth and boundary experiments were deferred rather than passed.

Detailed historical evidence: [July SSH closure worklog](../worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md), [July M5 planning](../worklogs/2026-07-18-1640-m5-docker-planning.md), and versioned Git history of this file. Historical M5 playbook is **not** the active teaching gate.

## Current learning target — first security finding

AegisLab now connects Linux authentication observations to a bounded importer, normalized events and an evidence-linked deterministic incident. New concepts to demonstrate, not merely read about:

1. Which layer owns the timestamp, raw record, parsed event and conclusion; how each identity is generated.
2. Why three log lines do **not** automatically prove three separate client actions, compromise or a clock-synchronized event timeline.
3. Why a negative result differs from an unassessable result when input is missing, malformed or partially quarantined.
4. How a threshold/time-window detector behaves at a boundary and under duplicates/replay.
5. How tests and one changed-case diagnosis challenge an AI-generated implementation.

**Assessment status:** engineering output and any tests run by AI are software verification only; learner has not yet personally predicted, run, explained or independently modified Stage B. Do not mark independent mastery.

## Teaching and contribution policy

Follow [Learning Preferences](../../LEARNING-PREFERENCES.md) and [AI Collaboration Protocol](<../AegisLab — AI Collaboration Protocol.md>). Explain a compact problem/mechanism, ask for one predictive changed-case exercise, observe actual output, interpret support and uncertainty and reduce scaffolding over time. AI may implement routine code and tests, learner personally owns important reasoning and diagnosis. Keep `introduced`, `guided`, `independently diagnosed` and `stable recall` distinct.

## Next learner-owned checkpoint

Before seeing the output for a changed synthetic case, predict whether a third failed-publickey **record** just inside versus just outside the rule window causes a finding. Then run it, identify the exact three evidence IDs/records and explain one conclusion the detector deliberately does **not** claim. No Docker or privileged host action is required.
