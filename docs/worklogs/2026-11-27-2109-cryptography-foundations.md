# 2026-11-27 — R2.3 cryptography and trust

- Starting revision 4767e3d55b79f8ebeca2e6d4ecb7b44db5b4eb8e; GitHub main and WSL HEAD/origin/main matched, clean at startup.
- Windows and WSL Desktop Commander both online, operating systems confirmed. WSL Python 3.12.3, OpenSSL 3.0.13, OpenSSH 9.6p1, existing cryptography 41.0.7; direct loopback model catalog HTTP 200 (not inference proof).
- AI-operated exercise only; learner assessment and personal execution pending. No product source or dependency changes.

## Experiment and observations

Run from WSL project root: `python3 examples/cryptography_foundations.py`. [Example](../../examples/cryptography_foundations.py) and [retained output](evidence/2026-11-27-r2-f3-cryptography-foundations.json). Synthetic hello/Hello bytes; generated disposable keys in memory only, no private/public key material emitted, no network activity, filesystem keys, service changes, or privilege elevation. No package installation. Existing library used only for exercise, not a product adoption or new dependency.

Base64 hello becomes aGVsbG8= and round-trips without a secret. SHA-256 hello and Hello produce different 64-character hexadecimal digests, repeated input gives same digest. AES-256-GCM decrypts original; changed ciphertext and unrelated key rejected (InvalidTag). RSA-OAEP public-key encryption/private-key decryption round-trips. Ed25519 signature verifies with original public key and bytes; changed bytes and unrelated public key rejected (InvalidSignature); public-key digest comparison differs. X25519 agreement plus HKDF-SHA256 derives equal 32-byte keys on both sides; unrelated peer differs. Identity authentication is not supplied by this key agreement. Demonstration uses library primitives, not an SSH implementation or production protocol. No secure-memory-erasure claim.

Source inspection: ssh_incident.py _sha256 hashes exact bytes; _id truncates hex to 20 characters; record ID includes declared source ID, full file digest and line number, event ID includes parser version. Accepted raw line digest is computed separately; source_kind is a declaration, not attestation. Digest or valid reference alone cannot authenticate source or establish actual event truth. No product source changes.

Regression: `PYTHONPATH=src python3 -m unittest discover -s tests -q` ran 55 tests in 2.274s, OK. Example rerun retained above. No fresh live SSH collection or packet capture, model evaluation, VM deployment or host changes.

## Handoff

R2.3 teaching and learner-owned prediction/assessment are the current checkpoint; do not promote F3 competence from the AI demonstration. Then R2.4 SSH architecture; learner operation and all previous practical checkpoints remain open. Retain Hyper-V proposal and approval boundary. Recall endpoint vs process identity, fixed/sliding windows and absence of evidence in changed cases. R3/R4 remain unchanged.
