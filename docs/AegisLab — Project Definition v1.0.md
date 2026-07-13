# AegisLab — Project Definition

**Version:** 1.0
**Status:** Accepted Stage 0 project definition; canonical
**Project type:** Long-running, modular flagship learning project
**Name status:** Confirmed

## Purpose and scope

This file is the canonical entrypoint to AegisLab's project definition. It and the linked normative parts together define what AegisLab is, why it exists, what it should eventually be capable of doing, the major logical responsibilities it will contain, the rules that govern its development, and how success will be judged.

This is a project definition, not a detailed implementation plan. It intentionally does not define:

- Exact APIs, classes, database tables, or event fields
- A final network topology, service architecture, or deployment architecture
- The detailed implementation order of every module
- Exact frameworks or infrastructure products
- Complete attack, forensic, agent, or tool procedures

Those details belong in supporting documents when an active experiment or module makes their decisions concrete.

## Executive definition

> **AegisLab is a long-running, modular, evidence-centered network-defense learning laboratory in which controlled activity is observed through imperfect telemetry, transformed into defensible security conclusions, and evaluated against separately maintained, provenance-backed experimental truth.**

Network defense, detection-platform engineering, secure distributed systems, and evidence-centered investigation provide the operational foundation. Applied security ML should reach strong practical competence; DFIR and threat hunting should receive deliberate depth; secure, evidence-grounded AI automation is the integrating specialization.

Deep independent capability takes priority over speed, feature count, architectural appearance, or presentation polish.

## Definition map

Read only the parts relevant to the current task after reading this entrypoint.

| Normative part | Contents | Read when working on |
|---|---|---|
| [Identity and Learning Goals](definition/identity-and-learning-goals.md) | Identity, thesis, learning goal, career direction, and priority hierarchy | Project direction, learning emphasis, or career alignment |
| [Experimental Model](definition/experimental-model.md) | Experimental loop, vocabulary, evidence, and truth model | Events, evidence, provenance, evaluation, or terminology |
| [Capabilities and Logical Modules](definition/capabilities-and-modules.md) | Long-term capabilities and responsibility boundaries | Scope, module boundaries, or capability planning |
| [Governance, Safety, and Boundaries](definition/governance-safety-and-boundaries.md) | Principles, policies, maturity gates, exclusions, and limitations | Safety, authority, architecture growth, resilience, or malware boundaries |
| [Scenario Strategy](definition/scenario-strategy.md) | Evergreen scenario, scenario families, variants, and evaluation expectations | Scenario design, attack simulation, or regression coverage |
| [Learning and Technology Strategy](definition/learning-and-technology-strategy.md) | Learning domains, ownership model, technology adoption, and external alignment | Teaching method, technology choice, ML, agents, or standards |
| [Success and Evolution](definition/success-and-evolution.md) | Success criteria, supporting documents, and Stage 0 completion | Acceptance criteria, capability snapshots, portfolio evidence, or project evolution |

The accepted [Core Charter](<plans/AegisLab — Core Charter v1.0.md>) and active [Initial Journey Plan](<plans/AegisLab — Initial Journey Plan.md>) govern the first implementation journey. They are operational supporting documents, not replacements for this definition.

## Normative relationship

- This entrypoint and all seven linked definition parts form one Project Definition v1.0.
- Each linked part is normative within its stated responsibility.
- The entrypoint summarizes and routes; detailed statements in the relevant normative part control interpretation.
- Files under `docs/proposals/` preserve reasoning history and are not current project requirements.
- Supporting plans and future specifications may refine implementation details but may not silently change the project's identity, invariants, boundaries, or success criteria.

## Accepted Stage 0 understanding

Version 1.0 records the following accepted direction:

1. AegisLab is the confirmed project name and is an evidence-centered network-defense learning laboratory serving an anchored hybrid AI Security Automation Engineer direction.
2. Network defense, detection platforms, secure distributed systems, and security data and evidence engineering provide the shared foundation.
3. Applied security ML should reach strong practical competence; DFIR and threat hunting should receive deliberate depth; secure evidence-grounded AI automation is the integrating specialization.
4. Logical modules describe responsibilities and contracts, not predetermined processes, services, containers, repositories, or deployments.
5. Provenance-backed experimental truth is constructed from fallible, potentially conflicting records and remains separate from the evidence available to evaluated components.
6. Progress is demonstrated through reproducible behavior, tests, failure diagnosis, learning-depth evidence, capability snapshots, and explanations the learner can defend.
7. The SSH authentication-abuse Core remains the first bounded evidence loop. Full DFIR and threat hunting begin through the first major post-Core expansion.
8. Dynamic malware execution is prohibited unless a later dedicated charter satisfies the [dynamic-malware-analysis maturity gate](definition/governance-safety-and-boundaries.md#dynamic-malware-analysis-maturity-gate); it never enters the Core implicitly.
9. Detailed architecture, scenario contracts, event schemas, forensic procedures, and technology selections will be designed only when experiments or active modules require them.

Future evidence may revise this direction, but changes to identity, invariants, capability emphasis, boundaries, or safety gates must be deliberate and versioned.

## Definition maintenance and versioning

After version 1.0, implementation details, tools, procedures, and module-specific requirements belong in the appropriate supporting document rather than continuously expanding the project definition.

The definition should change only when new evidence requires a meaningful revision to AegisLab's identity, thesis, target capabilities, system or learning invariants, boundaries, known limitations, or definition of success.

- Keep this entrypoint below 200 lines.
- Keep each normative part focused and split it again if it grows beyond roughly 300 lines.
- Prefer named relative links over numeric section references.
- Do not duplicate normative detail across parts.
- Record meaningful semantic changes deliberately and version them.
- Structural navigation changes that preserve meaning do not require a new project-definition version.
