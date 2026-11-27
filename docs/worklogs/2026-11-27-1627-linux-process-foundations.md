# 2026-11-27 — R2.1 Linux process foundations

- Started: 2026-11-27 16:27 +03:30 (WSL clock).
- Status: completed AI-operated demonstration; F1 learner reasoning and personal operation open; R2 continues.
- Starting revision: 036d0c2bd0e3c605d84821fbe81d7aeccffc1fd1, clean and synchronized.
- Role: teacher and implementation partner, direct bounded demonstration. Learner last reported PC inaccessible; no personal execution assumed.

## Previous R1 assessment

Learner correctly explained IP-only grouping as a different detection objective, representational mismatch between equivalent failure/method fields, and source-dependent case-sensitive identity. Sigma specification, CLI, conversion library/backend and database execution responsibilities remained confused; corrected with pipeline explanation. Sliding-window response named both correct sets A/B/C and C/D/E but did not consistently associate them with endpoints and confused fixed buckets with accumulating records; corrected with explicit intervals. Changed-case recall remains open. Personal native tool operation deferred because learner reported no PC access. Do not claim R1 independent closure; revisit in bounded practical transfer rather than repeat the entire lesson.

## Objective, design and observed evidence

[Reproducible foundations example](../../examples/linux_process_foundations.py) uses ordinary Python 3.12.3 and existing ps, ss and journalctl. No sudo, installations, host SSH change, live sensor acquisition, external connections or unrelated service inspection. Child binds only 127.0.0.1, port 0 (kernel selects port), accepts one connection, exchanges x/y, exits. Parent captures output pipes, inspects only own child and relevant port; operations bounded with timeouts, child killed/reaped in finally if still running; temporary directory automatically removed. This is a TCP teaching exchange, not actual SSH or a real security incident. No change under src/ or tests/.

Command: python3 examples/linux_process_foundations.py. [Observed output](evidence/2026-11-27-r2-f1-process-foundations.json):
- Temporary file owned by effective user; Python stat mode 0600, read succeeded; mode 0000 read raised PermissionError even for owner; restored 0600. Directory removed. Demonstrates ordinary discretionary access check on a new open, not all Linux permission mechanisms.
- ps -p 10979 -o pid,ppid,stat,comm showed child 10979, parent 10978, S+ python3. Snapshot, not permanent identity or diagnosis of all process states.
- ss -ltnp sport = :44116 showed LISTEN at 127.0.0.1:44116, child PID 10979 FD 3; wildcard peer is not wildcard local bind.
- /proc/10979/fd: stdin /dev/null, stdout and stderr separate pipes, FD 3 socket inode 85838. After accept FD 4 socket inode 85839. Per-process descriptor identity, not global number.
- ss -tnp filtered sport/dport 44116 showed both endpoints ESTAB (child 44116 FD 4, parent 43591 FD 3); one loopback TCP connection, two visible endpoints. Parent received y after sending x. TCP connection alone does not prove authentication; application exchange provides separate evidence.
- Child returncode 0 and stderr "completed controlled exchange": stderr is a stream, not an automatic error judgment. After exit ps returned 1/header only and ss listener query returned 0/header only. Child reaped and no listener observed at inspection time; no global service absence claim.
- journalctl --no-pager -n 2 -t aegislab-r2-f1-no-emitter: exit 0, -- No entries --. No journal emitter configured for tag; stdout/stderr were pipes. This is a bounded query result, not proof that no activity occurred or that all logging works.

## Teaching and handoff

Introduce user/kernel space, system calls, program/process/service/daemon, PID/PPID and process state, standard streams/pipes, descriptors and listening versus accepted sockets, ordinary owner/group/other permission bits, filesystem metadata, observation versus inference. Link to inference worker IPC and SSH source/PID limitations. Learner open-ended prediction, permission diagnosis, code reading, and delayed recall of window boundaries pending. F1 minimum foundations introduced, AI-operated experiment verified, not learner competence promotion. Continue R2.2 networking (addresses, interfaces, routes, TCP/UDP and packet visibility); deeper personal Linux permission/service diagnosis D/E/F. R1/B personal gates retained. No need to block R2 on unavailable PC.

Verification: actual example executed successfully; 55/55 existing regression tests passed. No product feature changes; example and evidence support learning. Runtime PIDs/ports/inodes are historical and must be reinspected on rerun.

Relative Markdown link targets checked: 87; none missing.
