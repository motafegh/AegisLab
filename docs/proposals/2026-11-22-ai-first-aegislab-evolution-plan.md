# AegisLab — AI-First Security Operations Evolution Plan

**Status:** PROPOSED FOR REVIEW — not an accepted Charter, specification, implementation authorization, or claim of product effectiveness  
**Prepared:** 2026-11-22  
**Base:** AegisLab main at b5f0234840338e2af012c46cfb4ead1ebcec0cad  
**Purpose:** Evolve the existing AegisLab learning and delivery program, preserve real progress, and correct the mismatch between the long-term AI/security mission and the original Core sequence  
**Ownership:** AegisLab; this proposal takes effect only through explicit adoption and reconciliation of the controlling Project Definition, Core Charter and active plans  
**Related discussion:** Independent research in the UpgradePilot research branch, learning-portfolio-project-discovery working-memory record

## 1. Executive decision recommended

**Recommend evolving AegisLab—not abandoning it, not starting a duplicate security lab, and not merely adding an LLM to its current Core.**

AegisLab's accepted Project Definition ALREADY targets network defense, evidence-centric detection, secure distributed systems and human-supervised AI investigation. Preserve that identity, safety and experimental-truth discipline. The problem is the **operational sequencing and learner-visible value** of the first Core. AI agents and security ML are excluded until after Core; the first complete detection/investigation path follows substantial environment replication in namespaces, Docker and separate VMs.

Propose an updated, bounded first product journey where the **security analyst's task** becomes visible early and develops through real system operations, applied AI, and adversarial AI security. The outcome is a local, reproducible, self-contained **AI-assisted security investigation workbench backed by an isolated defensive lab**, not a production SOC, generalized SIEM, autonomous responder, or yet another evidence-only review engine.

Keep AegisLab as the **learning and security-operations flagship** if early end-to-end implementations and independent learner-ownership checks earn that direction. Keep UpgradePilot as a separate, increasingly product-validation-focused portfolio asset. Preserve distinct missions; do not fork or import UpgradePilot's extensive report/CI infrastructure into AegisLab.

**Open decision, not assumed:** after reviewing this proposal, either adopt an evolved Core Charter and execution map, revise these assumptions, or reject the route. No canonical scope is changed by this file.

## 2. Why the prior route should change

**Verified older state:**
- Guided namespace SSH networking, legitimate-key success, unauthorized-key failure, process/socket/log/packet correlation, and teardown were demonstrated. Independent delayed reconstruction and mastery remain unproved.
- The formal remaining M4 scenario contract was explicitly deferred for learning-value reasons; it has not passed.
- M5 Docker object/lifecycle orientation is active. Its implementation and Compose adapter were pending at the last handoff.
- The Core Execution Map spans M0–M17, placing three-environment parity before much of collection, detection, incident and evaluation work.
- The accepted Core Charter excludes ML, LLM investigators/agents, cloud deployment and substantial UI from the original Core. The broader Project Definition DOES include AI-assisted investigation and agent security.

**Learner-reported emerging needs:** broad, repeated exposure to genuinely new engineering concepts; more independent diagnosis and transfer while using AI as a coding partner; AI systems engineering and AI security as practical work; visible, frequent working outputs; an interesting task with plausible user value; and credible job evidence. The learner tentatively recalls insufficient AI engineering and weak perceived progress as factors in AegisLab's pause. The personal cause remains uncertain.

**Diagnosis:** the original ordering was sound for comparing isolation mechanisms and enforcing prerequisites. It is no longer a good default for the newly prioritized combination of AI engineering, practical security operations, interest and short feedback loops. Preserve its technical work as **later cross-environment comparison**, not as mandatory prerequisites to the first detector and investigator. Do not infer that the original effort failed or its documentation was worthless.

## 3. Three distinct outcomes and one product thesis

1. **Engineering/learner outcome:** explain, build, run, operate, secure, change and diagnose Python services, Linux networking, sensor data, detections, bounded model calls, agent tools and recovery. An AI-written system is not evidence of personal ownership by itself.
2. **Portfolio/career outcome:** reproducible repository with realistic task, useful demo, security/threat model, controlled failures, comparative evaluation, honest personal contribution and technical decision stories. The skill set should complement rather than duplicate UpgradePilot/Sentinel.
3. **Product/usefulness outcome:** an operator actually needs help recovering what happened, what is and is not supported, and what evidence to investigate next. Do not claim user demand, analyst time savings or production incident-response effectiveness from a self-run lab alone.

**Provisional user:** a solo homelab defender, security engineer or junior analyst examining authentication/host/network security evidence. The initial task is: "Given suspicious SSH authentication activity, what happened, which evidence supports the finding, what remains unresolved, and what one permitted observation could distinguish plausible explanations?"

The first comparison is **raw logs versus a simple deterministic detection/summary versus the AI-assisted investigation**, on equal available evidence. A better-looking output is not automatically a better investigation. Compare with real practices and tools (e.g., log search, journalctl, baseline alerts) before claiming differentiation. Favor fewer useful claims over elaborate generated narratives.

## 4. Preserve / change / defer

| Treatment | Responsibility | Rationale |
| --- | --- | --- |
| **Preserve** | Existing AegisLab project identity, approved safety boundaries, SSH reference scenario, guided evidence and history, facts/derived facts/hypotheses separation, truth-versus-telemetry separation, provenance, human control, negative/failure tests | These are the project's sound foundations. |
| **Change** | First-Core objective and ordered milestones: reach an end-to-end incident with a bounded AI analysis early; alternate new feature, operations and evaluation rather than completing all three environments first | Improves learning breadth, product coherence, visibility and AI-engineering exposure. |
| **Change** | AI-assisted development contract: let AI implement much of the routine code, while the learner owns intent, diagnosis, verification, security tradeoffs and transfer | Personal capability cannot be inferred from generated source. |
| **Change** | Requirement that namespaces, Docker and VMs all precede pipeline work; instead require one safe operational environment early, then progressively demonstrate Docker, deployment and a later cross-environment comparison | Avoids a long infrastructure-only runway without losing those learning goals. |
| **Admit early, bounded** | Local model interpretation, structured output, source-aware uncertainty, agent tool authorization, adversarial log-content testing, fallback | These are career-relevant first-class responsibilities, not a decorative chatbot. |
| **Defer** | Multi-agent orchestration, broad autonomous tools/response, full SIEM, multi-tenant service, Kubernetes, public cloud, large dashboard, Kafka, advanced ML, malware, unsupported attack families | High cost/risk relative to initial learning and operator value. |
| **Retain as future specialized depths** | Three-environment parity, distributed delivery semantics, DFIR/hunting, applied ML and deployment sophistication | Activate only when the previous learning path produces a concrete reason or explicit deliberate depth milestone. |

## 5. Proposed reference architecture and trust model

**Control/evaluation side (privileged to know experiment truth):**
- Versioned authorized SSH scenario, identities, environment, performed actions, target-observed effects, expected telemetry and independent truth record.
- A truth-based evaluator that **does not hand its answer key** to the normal detector or LLM investigator.

**Evidence path (observable system):**
1. Isolated SSH Linux target(s) and benign controlled normal/failure activity.
2. Host authentication logs and selected network/socket observations.
3. Bounded collector or import adapter, with source/version/time identity and raw record preservation.
4. Normalization/validation, quarantine and explicit missing/conflicting/late information.
5. One understandable deterministic detection and incident/correlation rule.
6. A human-readable compact finding with exact event IDs, source quality, uncertainties and next verification action.
7. A bounded local AI investigation adapter given only permitted evidence/tools and returning typed proposals: grounded explanation, alternate hypotheses, unanswered questions, evidence requests or abstention.
8. A validator/policy layer **outside the model** that verifies evidence references, action permission, structured shape and safe degradation; a human remains the final security decision maker.

**Security authority flow:**
- Raw logs, imported text, tool results and model output are *lower-trust data*, never instructions to the runtime.
- The model may select only registered **read-only** inquiry tools with typed arguments, allowlisted scope, authorization and audit. Initially it may have **zero tools**; add one when a concrete investigation question needs it. No arbitrary shell, network scanning, credential access, file writes, host controls or external API actions.
- Deterministic detector status, evidence identities, stored sources and truth records are not overwritten by generated prose.
- The policy/authorization boundary rejects unauthorized requests regardless of model wording. A valid reference ID is necessary but insufficient: separately score **semantic entailment** of AI claims.
- Model unavailability, malformed outputs, timeouts, budget exhaustion and prompt-injection attempts must degrade to a usable deterministic/human workflow.
- Controlled adversarial payloads stay in explicitly authorized lab/fixture inputs. Never use production targets, private credentials, malware or unapproved active responses.

**Delivery shape:** one Python repository and one coherent core process first; CLI and accessible local report before a UI; small typed components and tests. Files/JSONL first if sufficient, SQLite when persistent indexed queries create the need. Existing local LM Studio HTTP endpoint may be a candidate after fresh verification; no assumed cloud API or paid service. Docker Compose enters when the working path demonstrates actual service/isolation needs, not because the README needs logos. Evaluate OCSF/OpenTelemetry/Sigma compatibility as explicit later interoperability work; do not claim standard conformance prematurely.

## 6. Delivery approach — successive working outcomes, not another 18-gate runway

Stages describe **meaningful outputs and learning boundaries**, not promises of calendar completion. A coherent stage may involve several sessions. Aim for visible runnable output in the earliest practical sessions and no multi-week preparation-only sequence without a compelling blocker.

### Stage A — Adopt a truthful new direction and recover the lab safely

**Outcome:** approved updated Core Charter and execution map; current baseline inventoried without disturbing the existing namespace/SSH work; one permitted source set and truth limitations selected. No implementation before governing scope is reconciled.

- Recover the precise July state, local environment and raw source availability; do not call historical plans current runtime proof.
- Preserve the namespace SSH achievements, explicitly deferred M4 formal work and incomplete M5 Docker implementation as historical facts.
- Pick one controlled SSH evidence set and its source identities; label synthetic complements as synthetic. Avoid publishing real keys, personal host logs or raw private packet capture.
- Decide what the first operator question, baseline and negative/ambiguous counterexample will be.
- Amend normative owners in the order in §10; keep superseded documents discoverable.

**Gate:** one coherent first result described in ordinary user language, input/safety boundaries and executable acceptance checks. The planning record must not become the first month of work.

### Stage B — First complete deterministic incident view

**Working demonstration:** from supported retained *authorized-lab* authentication records, one command shows a normalized incident/finding, source identities and explicit uncertainty. Include a normal/negative case, a relevant repeated-failure or boundary case, and a missing/invalid input case.

**New learning:** Python parsing and interfaces, Linux auth log semantics, time and clock assumptions, scenario truth vs sensor observation, schema validation, bounded CLI design, positive/negative/boundary tests.

**Engineering proof:** exact input identities, simple reproducible runner, defined output semantics, a traceable fact-to-event map and a test that refuses to invent evidence. Keep storage simple.

**Stop/continue rule:** if source records do not support the intended claim, downgrade the result or obtain authorized evidence; never silently manufacture a completed real incident from a fixture.

### Stage C — Local AI investigation with an honest baseline

**Working demonstration:** the same stored incident can be inspected with AI OFF and AI ON; an optional local model returns *bounded structured* investigative notes, plausible alternative explanations, source references, unanswered questions or an explicit unsupported result. The report remains usable if AI is absent.

**New learning:** LLM transport, prompt/context construction, schema and semantic evaluation, retrieval/source selection, model/version identity, token/request/latency budgets, error handling, fallback and human-in-the-loop review.

**Engineering proof:** same-evidence deterministic-versus-model comparison on favorable, ambiguous, missing-source, and contradictory cases. Reject fabricated IDs and invalid output; **human-adjudicate semantic correctness** beyond reference IDs. Record what the model improved (if anything) and what it made worse.

**No cosmetic AI:** if templates handle the chosen task just as well, the milestone can conclude "AI not warranted for this responsibility"; investigate a *different genuine semantic task* before expanding models.

### Stage D — Real controlled operation and security engineering

**Working demonstration:** generate a fresh event in an owned isolated Linux SSH lab and follow it through sensor, collector, normalized incident and operator view. Prefer reusing namespace work first; introduce a small Docker target or deployment only when a new system/operations responsibility is identified.

**New learning:** Linux services/processes, sockets, routing, authentication, host/network visibility, timestamp differences, controlled event collection, trust boundary, Docker object/network/lifecycle, secure configuration and cleanup.

**Engineering proof:** actual performed-vs-observed evidence, an intentionally missing observation, controlled network or collector failure, manual diagnosis and a clean repeatable start/stop. Protect pre-existing Docker objects; do not publish the SSH port without authorized reason.

**Design constraint:** do not require VM parity before a functioning detector or AI investigator. A later environment-comparison slice can study namespaces versus Docker versus VMs deliberately, with actual user-controlled learning gates.

### Stage E — Agent tool security and adversarial evaluation

**Working demonstration:** a constrained investigator may, if required, ask one or two registered read-only questions over approved event IDs; an independent policy engine mediates every tool call. Lower-trust log text attempts to redirect tool use or output; the application refuses unauthorized execution and surfaces unsupported conclusions.

**New learning:** agentic control flow, structured tool calls, least privilege, prompt injection, context/tool-result poisoning, permission checks, audit and revocation, termination and costs.

**Engineering proof:** explicit allowed/denied tests, malformed and out-of-scope arguments, malicious log text, conflicting tool output, missing evidence, looping/over-budget controls and no permitted escape to arbitrary shell/network/write operations. Separate "model attempted bad action" from "application performed bad action." Record actual safety-control behavior and residual uncertainty, not 100% safety.

**Re-evaluation:** compare an explicit Python state machine with a mature agent framework on an actual demonstrated orchestration problem. Adopt LangGraph/MCP only if they solve that problem more clearly and safely, not because AegisLab needs an agent brand.

### Stage F — Operable, observable and diagnosable system

**Working demonstration:** an isolated, reproducible local service/CLI deployment supports the same reference scenario and includes logs, health/readiness indication, bounded budgets, restart/recovery, and a simple operator-facing result. A Docker/Compose or API boundary is justified and tested when adopted.

**New learning:** containers, networks, process lifecycle, configuration/secrets separation, structured operational logs, service identity, monitoring, durable state, retries/duplicate events, partial failure and restore.

**Engineering proof:** setup on a clean environment as available, automated tests, failure/restart/replay tests, one personally debugged outage and a concise operational runbook. Do not promise high availability or production SLOs from a laptop lab.

### Stage G — Generality, real-user comparison and portfolio presentation

**Working demonstration:** at least one additional materially different authorized security context, preferably a small self-hosted HTTP authentication/API misuse case, uses the common investigation interfaces without hard-coded SSH-only rules masquerading as a generic platform.

**New learning:** adapting collection and semantics, realistic threat modeling, contrasting scenarios, false positives, incident interpretation, user interviews and evidence-based product decisions.

**Engineering proof:** fixed case set with normal, positive, ambiguous, incomplete, adversarial and failure variants; measured detection correctness, human-adjudicated AI support, tool-policy violations, latency/cost if measured, and baseline comparison. If only exposed/self-created cases exist, say "development evaluation", not independent analyst validation.

**Portfolio package:** public-safe README, reproducible demo, architecture/trust-boundary diagram, selected test and incident receipts, one controlled-failure postmortem, meaningful AI model-vs-template evaluation, clear human-versus-AI contribution account, and a concise interview case study. Demonstrate what the learner can personally diagnose and defend.

### Later opt-in depths (outside the newly proposed first complete product)

- Virtual-machine parity and full namespace/container/VM isolation comparison.
- Distributed event transport/backpressure/reconciliation after a real multi-producer pressure case.
- Applied ML-based detection only after nontrivial ground-truth data, leakage-aware splits and a meaningful simple baseline.
- DFIR/hypothesis-led hunting, richer evidence types and alternate security scenario families.
- Security of autonomous agents beyond read-only investigation, only with separate permissions, threat model, user authorization and concrete value.
- Cloud IAM, Kubernetes or service mesh only when exposure to cloud security is selected as an independent learning goal. A local simulation can teach some concepts but is not real cloud operations proof.
- External operator testing and richer UX only after the local workflow produces something worth testing.

**Stages are adaptive:** if Stage D exposes an operational premise that Stage C cannot evaluate, bring D forward. Conversely, don't let AI consume months of work before one real live event is exercised. Keep only the minimum prerequisites that protect safety and truth.

## 7. AI-first learning and independent ownership contract

AI assistance is permitted for architecture drafts, implementation, tests, debugging proposals and documentation. The engineering work must still create **human-owned capability** and not become a code-generation contest.

**For each coherent milestone:**
1. **Before:** learner identifies the intended operator task, predicts one input/output and one failure or permission boundary, and understands why the new mechanism is needed.
2. **During:** AI can implement routine code; learner runs the product, inspects artifacts/outputs and personally chooses at least one consequential constraint, test, or source observation. Guidance scales to novelty.
3. **After:** use one changed or initially unfamiliar case for reduced-prompt explanation, modification, diagnosis or transfer; record actual assistance used, unknowns and failures. Do not require hand-coding every line or a quiz for every familiar command.
4. **Proof:** preserve only sufficient reproducible commands, tests, source references and an honest learner-ownership statement. A passing suite or an AI-produced document is not independent mastery.

**Novelty budget:** every major stage must include at least one genuine new capability category (Linux/network operations, live telemetry, model engineering, adversarial tool security, deployment/recovery, new scenario). Stop repetitive polish when it no longer teaches, improves user outcomes or closes material risk.

**Progress visibility:** maintain a compact "works now / worked with guidance / unresolved / next user-visible action" capability snapshot and a runnable single-command demo per stage. Use stage-specific proof rather than invented completeness percentages or feature-count vanity metrics.

## 8. Evaluation, security and utility gates

| Dimension | Initial evaluation | Critical failure / stop condition |
| --- | --- | --- |
| Detection fidelity | Test known normal, abuse, boundary, duplicates and missing-sensor scenarios against separately retained action/target truth | Treating intended action or unobserved event as a proven target effect |
| Incident/evidence validity | Verify identity, source, timeline, derivation and alternative explanation for material claims | Fabricated event, silent quarantine/drop, wrong context or unsupported occurrence |
| AI analysis quality | Human-adjudicated claim entailment, missing important relationships, unsupported hypotheses, calibrated abstention; compare identical inputs with a deterministic/human baseline | Semantically false factual claim promoted merely because IDs/schema passed |
| Agent authorization | Permitted and denied tool requests, prompt-injection attempts, malformed args, result poisoning, audit completeness and limits | Any unauthorized consequential action or external data access |
| Operational reliability | Restart, invalid input, provider loss, delayed/duplicate events, resource budget, cleanup | Hidden loss of important evidence or silent unsafe degradation |
| Learning ownership | One practical changed-case trace/diagnosis/repair and accurate attribution of AI assistance at each stage | Declaring ownership based only on agent-authored code or copied explanations |
| Product utility | Does a specific operator question get answered more accurately or with less investigation effort than a simple baseline? | Expanding a model/UI without evidence of improvement or an explicit new learning objective |

Keep development-case metrics separate from independent human-usefulness claims. Evaluate safety at the application authorization boundary, not only by asking the model whether it intended to comply. Adversarial tests do not prove universal prompt-injection resistance.

## 9. Deliberate architecture and opportunity-cost controls

- **Do not reinvent UpgradePilot.** AegisLab's distinctive work is live system observation, incident workflows and adversarially secured AI operations; reuse the general discipline, not the same proof-heavy ingestion/report complexity.
- **One integrated result before platform architecture.** No independent collector framework, generic agent registry, multitenant auth, graph DB, distributed queue or separate front end as a prerequisite.
- **One new operational challenge per stage.** Use an explicit reason to add the next environment/service/framework.
- **Progress versus documentation:** a milestone is not done when a plan passes review; it is done when the selected real behavior works, fails truthfully, and the learner can explain it.
- **Respect existing evidence:** never reset/rebuild other lab-owned networks, Docker objects, files or credentials without inspecting ownership and obtaining authority.
- **AI-first but not AI-always:** omit a model where deterministic rules are clearly better; a rigorous negative model result is acceptable engineering and learning evidence.
- **Portability:** use local-first/open-source components by default, avoid paid API dependence, and design a clean setup with no hardcoded private paths.
- **Time control:** an initial 30-hour/week personal capacity may be considered only after the portfolio transition is actually selected. Do not allocate all of it to AegisLab until first milestones show both learning and engagement.

## 10. Adoption and document migration sequence (exact owner changes)

The current Project Definition is broadly aligned with this proposal. Its central identity and invariants should be preserved, not rewritten casually. However, the original first-Core Charter and Journey Plan would directly conflict with the proposed early AI and reordered delivery. **Do not silently execute both.**

**First, user decision:** confirm the evolved primary task, early AI/security responsibility, one-environment-before-parity policy, and no-autonomous-response boundary. If material objections arise, revise this proposal before promoting it.

**Then, in the AegisLab repository, using deliberate focused commits:**

1. **Core Charter v2:** write a new accepted, concise first-Core Charter (preserve v1 as historical and mark it superseded by a dated pointer). Amend explicit AI exclusion, core user-facing result, minimal supported scenario, learning/evaluation, negative/security tests, permission boundary and acceptance. Maintain the canonical Project Definition identity, truth and safety rules.
2. **Journey/Execution Map v2:** remove M5 and three-environment parity as prerequisites to the first full incident/investigator workflow. Re-map completed guided namespace achievements, deferred M4, and unbuilt Docker work honestly; adopt capability-led stages A–G with runnable gates. Preserve the historical plan/map or clearly label outdated sections; no false completion.
3. **AegisLab entrypoints:** update AGENTS.md, PROJECT_STATE.md, the canonical definition index only where actual routing changes, and the active learning state so fresh sessions do not accidentally follow the superseded M5 playbook. Retain the old M5 plan for history and later optional reuse with correct status.
4. **Minimal contributor/portfolio documentation:** add a short README if one is still absent, with mission, current supported behavior, correct setup/demo instructions when implemented, security scope and candid capability status. Do not write future features as shipped.
5. **Learning and implementation work:** start Stage B promptly after Charter adoption. Preserve the exact related worklogs and selective tests; do not reopen all historic documentation or import foreign project infrastructure without a demonstrated need.
6. **Verification and handoff:** check all changed crosslinks, contradiction words such as "active M5" or "AI excluded from Core", file status, and accuracy against current source/runtime evidence. Confirm no uncontrolled local modifications, hidden branch loss, or public-safe violation.

**No automatic merge/authority promotion:** this proposal alone cannot revise normative documents. AegisLab's owning repo must make the explicit changes in a separate adoption decision. UpgradePilot's main workstream should only be notified of the high-level learning/portfolio shift if needed; it does not own AegisLab design.

## 11. Key decisions to revisit and rejection conditions

- **What is the first real operator-facing task?** SSH authentication triage is a strong reusable seed, not evidence of market demand. If the next interesting task is richer than raw log explanation, define the needed fact/relationship before adding AI.
- **Where does AI add defensible value?** Choose explanation, evidence selection, hypothesis comparison or bounded next-evidence proposal only where it outperforms a short deterministic baseline without unacceptable false claims.
- **How soon should live Linux/Docker enter?** At latest before claiming any operational security-engineering competence from the new Core. Prefer alternating live and model milestones so neither becomes a deferred fantasy.
- **Does the learner experience tangible progress?** If multiple coherent stages end mainly in architectural documents or repeated CI/provenance work, stop and simplify/re-scope.
- **Are security controls actually exercised?** A red-team case must test the runtime's real permissions and not simply score whether a prompt "looked injected".
- **Does the result teach transferable concepts and create credible public proof?** If the output remains essentially an AI-written log summary without new operations, tested agent permissions or independent diagnosis, reject it as the next flagship direction.
- **Can this have a real user?** Avoid fake demand. After a credible usable local workflow, ask an eligible analyst/operator to perform a fixed task and compare alternatives honestly.

## 12. Near-term next steps after review

1. Accept, reject or revise the strategic objective and tradeoffs in this proposed plan.
2. On explicit adoption, author **Core Charter v2 and a revised executable stage map** before editing implementation source or running a live lab.
3. Bring the current local environment and retained SSH source state forward with read-only inventory and public-safe fixtures.
4. Deliver Stage B's minimal end-to-end deterministic incident, then the first AI comparison and live-operation/agent-security milestones.
5. Independently revisit whether the new track has produced new learner ability, a usable demo, and credible career evidence before expanding its architecture.

**Status at publication:** Design/research proposal only. No AegisLab code, runtime, accepted Charter, current project handoff, or learning evidence was changed by writing this file.

## Reference anchors

- AegisLab [Project Definition](<../AegisLab — Project Definition v1.0.md>), [Identity and Learning Goals](../definition/identity-and-learning-goals.md), [Experimental Model](../definition/experimental-model.md), [Core Charter v1](<../plans/AegisLab — Core Charter v1.0.md>), [Core Execution Map](<../plans/AegisLab — Core Execution Map.md>), [Current Learning State](../learning/CURRENT_LEARNING_STATE.md).
- [NIST NICE Framework v2.2.0 (Apr 2026)](https://www.nist.gov/news-events/news/2026/04/nice-releases-nice-framework-components-v220): skills and cybersecurity work tasks.
- [OWASP GenAI / LLM Top 10](https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/): risks of prompt injection, agent agency, model and tool/data boundaries; use current edition when implementing.
- [MITRE ATLAS](https://atlas.mitre.org/): AI and agentic threat concepts; select only relevant controlled tests.
- [OpenTelemetry event semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/events/): reference for later interoperability comparisons, not a mandatory early ingestion dependency.
