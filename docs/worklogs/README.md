# AegisLab Worklogs

## Purpose and authority

Worklogs are version-controlled, human- and agent-readable records of substantial AegisLab sessions. They preserve live resumption context, meaningful actions, evidence, decisions, problems, learning, and handoffs without depending on an agent's context window.

Worklogs are non-normative historical evidence. Current inspection, the canonical Project Definition, accepted charters, active plans, and `PROJECT_STATE.md` remain stronger sources according to `AGENTS.md`. A worklog must never silently override them.

## When to create a worklog

Create one for nearly every substantial repository-focused working or teaching session, including:

- Repository or environment changes
- Experiments, implementation, design, or debugging
- Important reviews or decisions
- Foundational teaching and evaluated learning
- Work that another session may need to resume

Skip greetings, isolated factual answers, and trivial interactions that create no useful project knowledge, evidence, action, decision, or handoff context.

One file represents one substantial session. If work continues later, create a new file and link the previous record through `Continues` rather than reopening the old session.

## Naming and status

Use `YYYY-MM-DD-HHMM-short-title.md`. Use the local date and time for the recorded timezone and keep the title short, specific, and lowercase with hyphens.

Allowed status values are:

- `active` — the session is currently progressing
- `paused` — the session ended with expected continuation work
- `completed` — the session reached its stated outcome
- `abandoned` — the session stopped and will not continue as planned

## Live structure

Start from [TEMPLATE.md](TEMPLATE.md). Each active log has two complementary layers:

- A concise, mutable **Live snapshot** for fast resumption
- A chronological **Checkpoint timeline** preserving the meaningful path taken

Create and index the record after the session is known to be substantial. Write a minimal plan before material implementation or experimentation. Update the log automatically after meaningful evidence, decisions, blockers, solutions, scope changes, verification, and before a known pause or handoff.

## Adaptive detail

Record enough for a competent later reader to reconstruct what mattered without replaying the conversation. Increase detail for:

- Foundational learning and learner-owned decisions
- Security-sensitive, privileged, or consequential actions
- Experiments and difficult-to-reproduce results
- Failures, conflicting observations, and rejected hypotheses
- Changes to scope, architecture, safety, or project direction

Keep routine actions terse. Do not record greetings, repetitive narration, obvious tool mechanics, or transcript-level chatter.

Worklogs contain concise rationale and observable evidence, not hidden chain-of-thought. Summarize long command output and reference safe artifacts or paths when useful.

## Evidence and content safety

- Distinguish observation, inference, hypothesis, recommendation, and executed action.
- Record relevant commands and results, but do not imply that a zero exit status proves intended behavior.
- Preserve uncertainty, missing evidence, and failed checks.
- Never store secrets, credentials, malicious samples, sensitive personal data, unsafe operational detail, or unbounded raw output.
- Treat worklogs as potentially public and ensure claims can be defended.

## Closing and corrections

At session end:

1. Complete the verification and final handoff sections.
2. Set `Ended` and change the status to `completed`, `paused`, or `abandoned`.
3. Update the index outcome below.
4. Update `PROJECT_STATE.md` only if the session caused a meaningful decision, environment change, blocker change, or completed learning slice.

Active logs may be freely maintained. After closure, formatting, wording, and link repairs are allowed when they preserve meaning. Record changed conclusions, material factual corrections, or later-discovered limitations as dated entries under **Corrections** so the original reasoning history remains visible.

## Worklog index

Newest records appear first.

| Started | Worklog | Status | Outcome |
|---|---|---|---|
| 2026-07-14 20:30 +02:00 | [Networking to namespaces](2026-07-14-2245-networking-to-namespaces.md) | paused | Built and verified a two-endpoint namespace network; study and assessment are required before SSH |
| 2026-07-13 19:48 +03:30 | [SSH foundations bridge](2026-07-13-1948-ssh-foundations-bridge.md) | active | Bridging demonstrated HTTP networking knowledge into the first SSH Core concepts |
| 2026-07-13 19:44 +03:30 | [Learner profile integration](2026-07-13-1944-learner-profile-integration.md) | completed | Imported, routed, and verified the maintained evidence-aware learner profile |
| 2026-07-13 19:25 +03:30 | [AI collaboration setup](2026-07-13-1925-ai-collaboration-setup.md) | completed | Added and verified the collaboration protocol and durable worklog system |