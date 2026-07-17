# AegisLab Study Guide Index

## Purpose

This directory contains two complementary forms of learning material:

1. **Layered study editions** — the primary path for focused study, active recall, practical reconstruction, and mastery checks.
2. **Full reference editions** — preserved detailed records containing historical outputs, corrections, extended explanations, and complete session context.

The full editions are intentionally preserved unchanged. They remain valuable evidence and reference material, but they should not be read linearly by default.

## Primary study path

Study these in dependency order:

1. [Networking and Namespace Foundations — Layered Study Edition](study-editions/01-networking-and-namespace-foundations.md)
2. [SSH Identities and Linux Permissions — Layered Study Edition](study-editions/02-ssh-identities-and-permissions.md)
3. [Namespace SSH Configuration and Authentication — Layered Study Edition](study-editions/03-namespace-ssh-configuration-and-authentication.md)

Each layered edition separates:

```text
core mental model
        ↓
minimum practical mechanism
        ↓
fresh evidence interpretation
        ↓
active recall and prediction
        ↓
bounded diagnosis
        ↓
mastery gate
```

## Full preserved references

Use these when a layered edition points to a topic that needs more detail, when investigating a historical decision, or when reconstructing evidence from the original learning session:

- [Networking to Network Namespaces — Foundations Study Guide](2026-07-14-networking-to-namespaces-foundations.md)
- [SSH Key Identities and Permissions — Study Guide](2026-07-14-ssh-key-identities-and-permissions.md)
- [Namespace SSH Configuration, Connection, and Authentication — Study Guide](2026-07-15-namespace-ssh-configuration-connection-and-authentication.md)

## How to study

Do not measure progress by pages read.

For each unit:

1. Read the **Required model** section.
2. Close the file and explain the mechanism in your own words.
3. Predict the expected result before running a practical action.
4. Run or inspect one bounded action.
5. Identify decisive evidence and state what it proves and does not prove.
6. Complete the changed case or diagnosis exercise.
7. Use the full reference only for unresolved details.
8. Pass the mastery gate before treating the unit as stable knowledge.

## Meaning of completion

A guide is not complete because it was read once or because its commands succeeded.

Use these distinct states:

```text
mentioned
≠ taught
≠ understood
≠ demonstrated with guidance
≠ stable recall
≠ practical independence
```

For the current Core slice, successful study means the learner can:

- explain responsibilities and trust boundaries accurately;
- recover command syntax safely rather than memorizing every flag;
- interpret fresh output;
- predict a changed result;
- diagnose one bounded failure;
- reconstruct the mechanism with materially reduced guidance.

## Runtime evidence warning

PIDs, fingerprints, client ephemeral ports, interface indexes, packet sequence numbers, timestamps, and files under `/tmp` are runtime-specific.

Historical values in the full guides are evidence from earlier sessions. They are never current truth unless reinspected in the active runtime.

## Current gap

The three layered editions cover the completed networking and SSH control-path foundations. A separate SSH observability edition should be created after the remaining server-log correlation work closes the active M3 milestone.