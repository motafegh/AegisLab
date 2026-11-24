# AegisLab

**Status (2026-11-24):** Core v2 adopted; Stage B deterministic SSH finding CLI runs on explicitly synthetic evidence. Learner changed-case reasoning demonstrated with guidance; independent practical ownership open. Stage C local inference and contract probes are exploratory, not integrated into the CLI. Fresh telemetry, Docker/VM parity, agent tools and production use are **not implemented**.

AegisLab is an evidence-centered network-defense and security-operations learning laboratory. Its first operator question: *Which SSH authentication decisions were observed, does a defined pattern warrant attention, which records support it, and what remains unknown?*

## Quick demonstration (Python 3.10+; standard library only)

From the repository root:

    PYTHONPATH=src python3 -m aegislab analyze \
      --input examples/fixtures/ssh-auth-burst.synthetic.jsonl \
      --source-id fixture:ssh-burst-v1 \
      --source-kind synthetic

    PYTHONPATH=src python3 -m aegislab analyze \
      --input examples/fixtures/ssh-auth-normal.synthetic.jsonl \
      --source-id fixture:ssh-normal-v1

    PYTHONPATH=src python3 -m aegislab analyze \
      --input examples/fixtures/ssh-auth-burst.synthetic.jsonl \
      --source-id fixture:ssh-burst-v1 --json

    PYTHONPATH=src python3 -m unittest discover -s tests -v

No virtual environment, server, network port, Docker object, root privilege, model, dependency install or key material is required. Running the CLI only reads the specified local file and prints a report.

## Data contract and architecture

    local JSONL (declared source ID/kind)
       → bounded input, explicit parsing and quarantine
       → normalized SSH public-key decision events with source/record IDs
       → deterministic 3-failure / 120-second inclusive rule
       → finding with supporting event IDs, uncertainty and next observation

Each JSONL line is an object with exactly two keys:

    {"observed_at":"2026-11-22T10:00:00Z","message":"sshd[201]: Failed publickey for labuser from 10.10.0.1 port 51001 ssh2"}

The timestamp is UTC **as declared by the input producer**, not independently verified system time. The message parser recognizes a restricted OpenSSH public-key decision form (with optional supported key fingerprint suffix), not full syslog/journald, all SSH versions or arbitrary SSH telemetry. Real host ingestion needs a separate provenance-aware adapter. Source kind is a declaration, never an attestation.

Per-source SHA-256 and per-record hash, source line, record ID and event ID let a reviewer locate the original input line for each event. These hashes identify bytes; they do not authenticate who produced them. No input text is executed as code or used as an instruction.

The versioned rule groups failed public-key decisions by source IP and username, counts distinct transport-identity observations at declared times and emits one first qualifying finding when at least **3** occur within **120 inclusive seconds**. An exact replay-like duplicate does not inflate the count; it remains visible as an accepted event. Input is bounded to 256 KiB, 1,000 records and 2,048 bytes per record. Unsupported/bad lines are quarantined with reason and original line identity, never silently interpreted as valid events.

Report states: **finding_present** means matching accepted records; **finding_present_with_gaps** means a supported finding with quarantined data; **no_finding_observed** means no match, not proof of benign activity; **incomplete_evidence** means accepted data without a finding plus quarantine; **unassessable** means zero accepted events.

A finding means observed failure records, **not** unique human attempts, a verified attacker, independent truth, successful compromise or live detection effectiveness. Even a corresponding accepted public-key record must not be interpreted as malicious without independent context.

## Source authenticity and historical boundary

All files in [examples/fixtures](examples/fixtures/README.md) are **synthetic**. In July, the learner demonstrated an authorized key success, an unauthorized key failure and SSH process/socket/packet/log views in an isolated WSL namespace lab **with guidance**. The retained worklog summarizes those events; it does not contain importable raw sshd log records or a separate truth ledger. The old temporary lab directory was absent at the 2026-11-22 read-only inventory. Stage B makes no claim of live sensor collection or independent learner proficiency.

## Learning challenge

Before running it, predict: if the third failed-publickey record moves from 120 to 121 seconds after the first while the middle record remains at 60 seconds, should a finding appear? Create a **copy** of the synthetic fixture, adjust only the UTC timestamp, use a new source ID, and inspect the status and event-to-source-line mapping. Then explain which missing evidence prevents concluding that a real attack occurred. This practical exercise, not an AI-written explanation, is the first learner-ownership gate.

## Project authority and safe scope

- [Project Definition v1.0](<docs/AegisLab — Project Definition v1.0.md>) — enduring mission and safety/truth invariants.
- [Core Charter v2](<docs/plans/AegisLab — Core Charter v2.0.md>) — accepted scope and completion boundaries.
- [Capability Execution Map v2](<docs/plans/AegisLab — Capability Execution Map v2.md>) — stages A–G and executable gates.
- [Stage C execution plan](docs/plans/STAGE-C-EXECUTION.md) and [Learning Ledger](docs/learning/LEARNING_LEDGER.md) — active detail, learning depth and remaining work.
- [Industry tools and product strategy](docs/plans/INDUSTRY-TOOLS-AND-PRODUCT-STRATEGY.md) — stage-linked practical tool exposure, adoption decisions and usefulness comparisons.
- [Project State](PROJECT_STATE.md) — actual implementation/learning handoff.
- [Evolution proposal](docs/proposals/2026-11-22-ai-first-aegislab-evolution-plan.md) — decision rationale.

Next: bounded local AI ON/OFF comparison on identical evidence, structured output, grounded references, semantic adjudication and fallback. Later: fresh authorized isolated SSH telemetry, independent agent tool-policy enforcement, operational recovery and usefulness evaluation. No lab port publication, automatic security response, external targeting or cloud API is authorized.
