# AegisLab — Core Charter v2.0

**Version:** 2.0 | **Status:** Accepted 2026-11-22 by explicit owner authorization | **Scope:** First complete security-operations/AI investigation Core
**Supersedes:** [Core Charter v1.0](<AegisLab — Core Charter v1.0.md>) for active execution, without erasing its historical learning results.
**Normative parent:** [Project Definition v1.0](<../AegisLab — Project Definition v1.0.md>)

## Operator task and result

Given bounded, attributable SSH authentication observations from an authorized lab or explicitly synthetic case, show what was observed, whether a defined suspicious pattern exists, precisely which records support it, what the evidence cannot establish, and which permitted observation would be useful next. The final Core adds an **evaluated**, optional local AI investigator, safe lab operations, bounded read-only investigation tools when justified, and a reproducible local workflow.

This is an evidence-centered **learning and investigation workbench**, not a production SOC/SIEM, autonomous responder, general-purpose agent platform, or assertion of real-user demand. Preserve experiment truth independently of detector/investigator inputs.

## Operating invariants

- Isolated, authorized local security activity only. No external targeting, credential exposure, published lab service, destructive response, or unapproved privileged action.
- Preserve source/record/event identity, transformations, detection version, observed versus derived claims, incomplete/contradictory evidence, and uncertainty. Do not infer attempted actions or effects from intention.
- Lower-trust telemetry and model output are data, never instructions. A deterministic authorization layer outside any model mediates future tools; only scoped, audited read-only tools may be proposed initially. Humans authorize consequential actions.
- Experimental/action truth stays outside the normal detection and model input. Do not promote structured model output to factual truth merely because reference IDs exist; evaluate semantic support independently.
- No required cloud or paid API. AI OFF must remain useful, and AI failure must degrade safely to the deterministic finding.
- AI may implement code and tests, but learner independence requires separately observed explanation, changed-case diagnosis and transfer.

## First-Core acceptance (stages in the [Capability Execution Map v2](<AegisLab — Capability Execution Map v2.md>))

**A — Direction and source:** adopt and cross-link this Charter and active stage map; preserve July namespace SSH proof and its limits; inventory current state without altering lab controls; select source provenance and label any fixture as synthetic.

**B — Deterministic incident:** one documented CLI reads bounded authentication observations with stable source/event IDs; rejects/quarantines malformed input explicitly; generates a reproducible repeated-failure finding tied to exact evidence; distinguishes absence of a finding from incomplete observation. Demonstrate positive, normal/negative, threshold/time-bound, duplicate and missing/invalid-input tests. No claim of actual compromise or independently established scenario truth from logs alone.

**C — Local AI:** optionally inspect the same finding with a local model through bounded structured output; verify evidence IDs, assess factual entailment through independent/human adjudication, record model identity and budgets, compare against a no-model baseline, and preserve usable fallback. Do not add a cosmetic chatbot.

**D — Live operation:** run an approved, isolated SSH case; capture a fresh target-side observation through the evidence path and separately record performed-versus-observed effects. Prove one missing-sensor/fault case and safe cleanup. Docker only on demonstrated operational/learning need.

**E — Agent security:** introduce only useful scoped read-only investigation queries, enforce policy outside the model, record allowed/denied/malformed and prompt-injection tests, and prevent uncontrolled shell/network/write/response authority.

**F — Operability:** reproducible local deploy/CLI or service, controlled failures, logs, readiness or health as appropriate, restart/replay recovery and a personally diagnosed outage; no unsupported production reliability claim.

**G — Transfer and utility:** materially different authorized security context through shared interfaces, fixed positive/normal/ambiguous/failure cases, baseline comparison and human-adjudicated AI evaluation. Produce public-safe portfolio evidence with truthful learner/AI attribution; avoid demand or independent-user claims without external testing.

**Stop rule for each stage:** do not promote a capability when evidence does not support it, a material safety boundary fails, required verification is unavailable, or learner ownership is untested. Record the actual partial state and smallest justified next check. Gate completion for software and learner mastery are **different** statuses.

## Scope choices and deferrals

One coherent Python CLI/evidence path first; storage simple, no speculative framework, distributed bus, database, multitenant API, general agent registry, large frontend or advanced ML. Cross-environment namespace/Docker/VM comparison is valuable **later**, but is **not** a prerequisite to B or C. The July guided SSH baseline survives; formal old M4 scenario-contract remainder is deferred, not passed; old M5 Docker adapter never reached implementation. Advanced DFIR/hunting and applied ML remain later separately justified depths. Dynamic malware work retains its independent prohibition and maturity gate.

## Learning and evaluation contract

Owner-approved learning reset (2026-11-26): historical engineering records survive, but no competence acquired before the November 22 return is assumed available. Follow the [foundations rebuild](../learning/FOUNDATION-REBUILD.md) and current learning ledger for prerequisites; retain recent evidence at its demonstrated depth. This does not change the A–G capability acceptance gates.

At each material gate: state the operator question and predict a meaningful behavior; run and inspect actual evidence; challenge a negative/changed case; capture what was AI-built versus learner-tested; revisit an unfamiliar failure with reduced prompting. Do not equate generated code, passing tests, or guided success with independent learner mastery. Prefer new system mechanisms and demonstrated utility over redundant documentation.
