# AegisLab Repository Guidance

## Purpose

This file gives Codex durable repository-specific working rules. AegisLab is a depth-first learning project: software and documentation matter, but the learner's ability to explain, test, break, diagnose, secure, and defend important work is the primary outcome.

Keep this file below 200 lines. Prefer links to canonical documents over duplicated project detail.

## Instruction and evidence priority

Use the following project-level priority when sources disagree:

1. Explicit instructions in the active user request
2. Current repository and system evidence established through inspection
3. The canonical project definition and its normative parts
4. The accepted Core Charter and active Journey Plan for current Core work
5. `PROJECT_STATE.md` as a non-normative handoff
6. Historical proposals and superseded planning artifacts

Higher-level Codex instructions and safety policies always remain controlling. Do not use this hierarchy to override them.

## Start every task

1. Run `git status --short` and preserve existing user changes.
2. Read `PROJECT_STATE.md`.
3. Read the canonical definition entrypoint at `docs/AegisLab — Project Definition v1.0.md`.
4. Use its document map to load only the normative parts relevant to the task.
5. For Core work, read the Core Charter and the relevant section of the Journey Plan.
6. Inspect discoverable repository or environment facts before asking the user.

Do not load every project document by default. Do not treat stale narrative as stronger evidence than the current workspace or system.

## Working style

Use a context-sensitive collaboration model:

- For foundational networking, security, systems, and evidence-learning slices, use guided discovery. Ask the learner to predict or explain, let them perform important safe steps, then teach, review, challenge, and debug from observed evidence.
- For routine repository maintenance, mechanical refactors, documentation upkeep, and explicitly requested implementation, act directly and verify the result.
- Increase scaffolding when blocked, but return important understanding and ownership to the learner through later modification, diagnosis, and explanation.
- Do not silently make the learner's foundational design decisions or claim learning depth from successful execution alone.

## Security and authorization

- All offensive or adversarial activity must stay within explicitly authorized, isolated AegisLab targets.
- Never target public, external, production, or third-party systems.
- Dynamic malware acquisition, storage, transfer, or execution is prohibited unless a later charter has satisfied the [dynamic-malware-analysis maturity gate](docs/definition/governance-safety-and-boundaries.md#dynamic-malware-analysis-maturity-gate).
- Do not weaken isolation, expose lab services, or broaden network access merely for convenience.
- Consequential response actions require explicit human authorization and an audit trail.
- Never place secrets, credentials, malicious samples, sensitive personal data, or unsafe operational detail in documentation or fixtures.

## Documentation map

| Need | Authoritative source |
|---|---|
| Project identity and accepted direction | [Project Definition entrypoint](<docs/AegisLab — Project Definition v1.0.md>) |
| Career and learning priorities | [Identity and Learning Goals](docs/definition/identity-and-learning-goals.md) |
| Events, evidence, provenance, and truth | [Experimental Model](docs/definition/experimental-model.md) |
| Long-term scope and module responsibilities | [Capabilities and Logical Modules](docs/definition/capabilities-and-modules.md) |
| Principles, safety gates, exclusions, limitations | [Governance, Safety, and Boundaries](docs/definition/governance-safety-and-boundaries.md) |
| Scenario families and variants | [Scenario Strategy](docs/definition/scenario-strategy.md) |
| Learning ownership and technology adoption | [Learning and Technology Strategy](docs/definition/learning-and-technology-strategy.md) |
| Success criteria and evolution | [Success and Evolution](docs/definition/success-and-evolution.md) |
| First bounded vertical slice | [Core Charter](<docs/plans/AegisLab — Core Charter v1.0.md>) |
| Current implementation sequence | [Initial Journey Plan](<docs/plans/AegisLab — Initial Journey Plan.md>) |
| Current handoff and next checkpoint | [Project State](PROJECT_STATE.md) |

## Documentation maintenance

- Put normative changes in the relevant definition part; keep the entrypoint concise.
- Put implementation details in active supporting documents after experiments make them concrete.
- Prefer named relative links over numeric section references.
- Link to a statement instead of copying it into multiple files.
- Leave `docs/proposals/` unchanged unless the user explicitly requests historical corrections.
- Update `PROJECT_STATE.md` after a meaningful decision, environment change, blocker change, or completed learning slice.
- Do not update project state for routine formatting, transient command output, or ordinary session history.
- Keep both `AGENTS.md` and `PROJECT_STATE.md` below 200 lines. Compress or move history before crossing the limit.

## Worktree and change control

- Preserve unrelated and pre-existing changes; never assume an untracked file is disposable.
- Use focused edits and avoid broad rewrites without evidence that they are needed.
- Do not use destructive Git operations.
- Do not stage, commit, push, create branches, or open pull requests unless the user asks.
- Do not add a framework, service, dependency, or infrastructure layer without a demonstrated requirement and understood learning purpose.

## Verification

- Verify changes in proportion to their risk and scope.
- For documentation changes, check links, headings, code fences, tables, whitespace, line limits, and cross-document consistency.
- For implementation changes, run the narrowest relevant tests first, then broader checks when justified.
- Report what was verified, what was not, and any remaining uncertainty.
- Never claim success solely because a command exited successfully; inspect the resulting behavior or artifact.

## Nested guidance

Do not add nested `AGENTS.md` or `AGENTS.override.md` files until a specialized subtree has genuinely different commands, safety boundaries, or review rules. When one is added, keep it narrow and document why the root guidance is insufficient.
