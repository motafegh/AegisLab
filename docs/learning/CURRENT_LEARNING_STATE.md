# AegisLab Current Learning State

**Updated:** 2026-11-24 | **Status:** Stage B changed-case reasoning demonstrated with guidance; practical ownership open; Stage C exploratory learning active.
**Authority:** Non-normative, evidence-aware learner handoff. See [Core Charter v2](<../plans/AegisLab — Core Charter v2.0.md>) and [Capability Execution Map v2](<../plans/AegisLab — Capability Execution Map v2.md>).

## Established with guidance (July)

- Created/rebuilt two Linux network namespaces, veth interfaces, IPv4 routes and ICMP path; diagnosed one network-address omission with help.
- Practiced Linux file ownership/modes and separate OpenSSH server host identity, client key authorization and known-host trust.
- Demonstrated authorized public-key SSH authentication, valid unauthorized-key failure, log/packet/socket/process correlation, encrypted-packet visibility limits and clean connection teardown.
- Interpreted the observed SSH execution lifecycle substantially **with assistance**; independent reconstruction, delayed recall and changed-case diagnosis remain unproven.
- Inspected Docker Desktop/engine inventory and networks during former M5 planning. Container lifecycle and adapter operation were **not** demonstrated.
- Formal old M4 repeated-failure contract, fixed threshold/window, independent truth and boundary experiments were deferred rather than passed.

Detailed historical evidence: [July SSH closure worklog](../worklogs/2026-07-18-namespace-ssh-auth-lifecycle-closure.md), [July M5 planning](../worklogs/2026-07-18-1640-m5-docker-planning.md), and versioned Git history of this file. Historical M5 playbook is **not** the active teaching gate.

## Current learning target — Stage B ownership and Stage C investigation

November 23–24: learner personally ran WSL socket/process/journal inspection and inspected the synthetic fixture; AI ran later CLI and inference experiments remotely while learner reasoned about them. Correct changed-case predictions: sliding window 0/50/140/171 (no finding), composite grouping (three groups, no finding), distinct observations A/B/D with a duplicated record, and invalid port quarantine with a supported finding. Earlier fixed-window, decoder-versus-accepted-event and duplicate-count misconceptions were corrected. Learner recognized insufficient evidence for compromise, catalog versus inference, and suggested increased generation budget with efficiency trade-offs. First human review of actual AI output: semantic partial, additional value fail, hypotheses partial, investigation fail; precise next observation needs emphasized.

See the [learning ledger](LEARNING_LEDGER.md) for per-concept depth and recall queue and the [reconciliation worklog](../worklogs/2026-11-24-1953-learning-reconciliation-and-stage-c2.md) for experimental evidence.

**Assessment:** guided reasoning and some learner-owned predictions demonstrated. AI-executed software/inference tests do not establish learner practical independence. No stable recall, independent Stage B code modification/diagnosis, or independent Stage C integration mastery claimed.

## Teaching and contribution policy

Follow [Learning Preferences](../../LEARNING-PREFERENCES.md) and [AI Collaboration Protocol](<../AegisLab — AI Collaboration Protocol.md>). Explain a compact problem/mechanism, ask for one predictive changed-case exercise, observe actual output, interpret support and uncertainty and reduce scaffolding over time. AI may implement routine code and tests, learner personally owns important reasoning and diagnosis. Keep `introduced`, `guided`, `independently diagnosed` and `stable recall` distinct.

## Next learner-owned checkpoints

- C2: evaluate the candidate output contract in the [Stage C execution plan](../plans/STAGE-C-EXECUTION.md); explain how missing target identity is represented, scope derived from existing event IDs, and syntactic validity distinguished from semantic support and usefulness.
- B: when PC access permits, personally modify and run a copied fixture, trace supporting events to exact source lines and diagnose one changed or invalid case with reduced assistance. Delayed recall of July networking/SSH skills precedes D.
