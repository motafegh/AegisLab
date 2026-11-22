# Explicitly synthetic SSH envelopes

All inputs in this directory are **invented test cases**, not actual `sshd` output or a transcript of July 2026 operations. The July AegisLab worklog contains summaries of guided SSH success/failure observations but does not preserve importable raw log lines, timestamps or an attested source file. The temporary lab state was absent at 2026-11-22 inspection.

Each JSONL line supplies a producer-declared `observed_at` UTC timestamp and a bounded, simplified `message` in the `sshd[pid]: Failed/Accepted publickey ...` decision pattern. This is an **envelope adapter**, not a `journalctl`/syslog parser. Time, identity and host provenance are not independently attested.

The positive file contains three synthetic failure observations within 120 seconds and one later success record; neither the fixture nor the detector establishes whether a successful login belonged to an adversary. A fresh authorized lab collection and independent action/target truth comparison belong to Stage D.
