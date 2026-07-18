# AegisLab — M5 Docker Learning and Execution Plan

**Status:** Active supporting plan  
**Started:** 2026-07-18  
**Milestone:** M5 — Docker adapter reproduction and Docker-specific learning  
**Authority:** Non-normative active plan; explicit user direction, current evidence, the Project Definition, Core Charter, Initial Journey Plan, and safety boundaries remain controlling  
**Live companion:** [M5 Docker Session Playbook](<AegisLab — M5 Docker Session Playbook.md>)  
**Teaching contract:** [Learning Preferences](../../LEARNING-PREFERENCES.md)  
**Current evidence:** [Current Learning State](../learning/CURRENT_LEARNING_STATE.md)

---

## 1. Purpose

This plan defines the complete bounded Docker learning and engineering path for the first AegisLab cross-environment slice.

It exists to prevent three recurring failure modes:

1. running commands before the purpose and end state are clear;
2. mixing environment construction, concept learning, and evidence collection until the main objective becomes invisible;
3. explaining every small action at maximum depth even when that depth is unnecessary.

The plan must keep both learner and AI oriented to:

```text
current phase
    ↓
problem being solved
    ↓
question being answered
    ↓
required learning depth
    ↓
practical action
    ↓
expected evidence
    ↓
completion gate
    ↓
next justified phase
```

This is not a day-by-day schedule. Work proceeds through focused sessions and evidence-backed phase gates.

---

## 2. Entry decision and relationship to the namespace baseline

The namespace implementation produced a complete guided baseline containing:

- working two-endpoint networking;
- an SSH listener isolated to the target endpoint;
- authorized public-key authentication success;
- a valid but unauthorized key failure;
- client and server authentication evidence;
- process, socket, namespace, packet, and teardown observations;
- clean connection teardown while the listener survived.

The learner explicitly directed the project to move to M5 rather than complete the remaining formal M4 repeated-count scenario contract. That remaining M4 work is therefore **deferred**, not falsely claimed as completed.

M5 will preserve the already demonstrated semantic core:

```text
authorized client identity
→ reaches the intended SSH target
→ verifies the server identity
→ authenticates successfully

unauthorized client identity
→ reaches the same target
→ verifies the same server identity
→ fails at public-key authentication

client disconnect
→ connection-specific state disappears
→ reusable server listener remains
```

M5 must not silently claim that fixed-count repeated failures, formal time bounds, start/end markers, independent expected truth, or threshold cases were completed in namespaces. Those remain later requirements when the detector/evaluation path materially needs them.

---

## 3. M5 outcome

M5 is complete when the learner has built, operated, inspected, broken, repaired, and explained a Docker implementation of the SSH client/server baseline and can compare it with the manual namespace version.

The result must include:

- a Docker-specific implementation owned by the repository;
- one client container and one server container on a private project network;
- no unnecessary SSH port publication to Windows, WSL, or external interfaces;
- authorized-key success and unauthorized-key failure;
- lab-specific server trust and client authorization state;
- safe handling of private keys and temporary identity material;
- process, socket, network, filesystem, log, and lifecycle observations;
- at least one predicted Docker-specific failure, diagnosis, repair, and revalidation;
- manual understanding before Compose automation;
- a reproducible Compose-based interface after the manual mechanism is understood;
- an evidence-backed namespace-versus-Docker comparison;
- an honest record of assistance and remaining ownership gaps.

---

## 4. Explicit non-goals

M5 is not a complete Docker administration or production container-security course.

Unless a demonstrated blocker requires them, defer:

- Kubernetes or other orchestrators;
- Swarm;
- public registries and image publication;
- CI/CD pipelines;
- production secret-management platforms;
- image signing and software-supply-chain frameworks;
- rootless Docker migration;
- advanced seccomp/AppArmor policy authoring;
- cgroup internals beyond the depth needed to explain resource boundaries;
- overlay filesystem internals beyond the depth needed to explain image layers and writable container state;
- multi-host container networking;
- production SSH exposure or hardening claims;
- broad vulnerability scanning suites;
- unrelated vulnerable application containers already present in Docker Desktop.

Useful non-blocking ideas belong in the deferred-ideas register with a concrete trigger.

---

## 5. Safety and environment boundaries

1. Use only local, explicitly authorized AegisLab containers and networks.
2. Do not expose the SSH server through host port publishing unless a later comparison explicitly requires it and the blast radius is explained first.
3. Never copy private keys into Git, chat, screenshots, logs, or committed image layers.
4. Never use unrelated stopped containers or custom networks as project dependencies.
5. Do not delete, modify, or reuse unrelated Docker objects without explicit user authorization.
6. Keep the ordinary WSL SSH service untouched.
7. Treat Docker Desktop, WSL, containers, images, networks, volumes, and host files as distinct state boundaries.
8. Reinspect volatile state after Docker Desktop restart, WSL shutdown, container recreation, or image rebuild.
9. Explain consequential cleanup before running it; cleanup must target only AegisLab-owned objects.
10. Do not generalize educational SSH configuration as production guidance.

---

## 6. Teaching-depth system

### 6.1 Depth levels

Every important concept or mechanism receives one required depth level for the active phase.

| Level | Name | Required learner capability | Typical treatment |
|---|---|---|---|
| D0 | Orientation | Know that the concept exists and where it fits | One concise explanation; no assessment unless confusion appears |
| D1 | Recognition and operation | Recognize the object/output and safely use the provided operation | Brief explanation, one real example, output interpretation |
| D2 | Working mental model | Explain responsibility, state, lifetime, interactions, and common failure classes | First-principles explanation, prediction, guided practice, concise teach-back |
| D3 | Diagnosis and transfer | Use evidence to diagnose changed behavior and transfer the mechanism to a new case | Changed case, debugging, repair, delayed recall, reduced prompting |
| D4 | Advanced internals | Explain implementation internals or production-grade trade-offs | Deferred unless required by an active blocker or later milestone |

D0 and D1 do not imply superficial or inaccurate teaching. They mean the advanced implementation detail is not currently required.

### 6.2 Explanation calibration

AI must choose explanation length based on novelty, risk, confusion, and project importance.

#### Brief explanation

Use when the action is familiar, low-risk, and mechanically simple.

Include only:

- why it is the next action;
- what the command or operation does;
- the decisive result.

Do not repeat a full flag-by-flag lecture unless the learner asks or the syntax contains a new or security-relevant element.

#### Standard explanation

Use for a new project-relevant mechanism.

Include:

- problem and responsibility;
- minimum accurate concept;
- important command components;
- expected result classes;
- what the result proves and does not prove.

#### Deep explanation

Use when:

- the concept is a D2 or D3 milestone requirement;
- a security or isolation boundary is involved;
- the learner expresses confusion;
- evidence conflicts;
- a failure must be diagnosed;
- transfer depends on an accurate model.

Deep explanation may include diagrams, lifecycle models, failure branches, and comparison with the namespace baseline.

### 6.3 Command explanation rule

Do not apply the maximum command-explanation template by default.

For each command, choose one of:

```text
known + simple + low risk
→ purpose and decisive fields only

new syntax or important mechanism
→ explain important components and output classes

security-sensitive, destructive, confusing, or diagnostic
→ full effect, blast radius, abort condition, cleanup, and evidence interpretation
```

Previously explained flags should receive a short reminder only when it helps current recall. Do not repeatedly restate obvious flags at full length.

### 6.4 Output explanation rule

For simple expected output, explain only the decisive evidence and next conclusion.

Use a detailed output walkthrough when:

- multiple layers are represented;
- one line can be misinterpreted;
- a failure layer must be isolated;
- the output changes the plan;
- the evidence is part of a milestone gate.

Always keep the main question visible. Stop collecting additional views when their marginal learning or evidentiary value is low.

---

## 7. Re-exposure, repetition, recall, and assessment

### 7.1 Re-exposure policy

Re-exposure should strengthen a reusable model, not replay identical explanations.

Use progressive re-exposure:

```text
first exposure
→ guided explanation and action

second exposure
→ shorter reminder and learner prediction

third exposure
→ changed context or reduced prompting

later exposure
→ diagnosis, transfer, or delayed reconstruction
```

Do not repeat a concept merely because time passed. Repeat when current reasoning shows instability, the concept becomes important in a new context, or delayed recall is being intentionally assessed.

### 7.2 Assessment triggers

Assessment is appropriate at:

- the end of a meaningful phase;
- before relying on a concept at a higher depth;
- after a corrected misconception;
- before automation replaces a manual mechanism;
- during a changed or broken case;
- after a delay when stable recall matters;
- before claiming transfer or independence.

### 7.3 Preferred assessments

Prefer:

- prediction before execution;
- one-sentence responsibility explanations;
- compare-and-contrast with namespaces;
- identifying the last successful layer before failure;
- explaining what selected evidence proves and does not prove;
- modifying one bounded variable;
- diagnosing from logs and state;
- reconstructing a small mechanism with reduced prompting.

Avoid repetitive worksheets, trivia, memorization of flags, exact PIDs, transient IPs, image IDs, container IDs, or exhaustive output recitation.

### 7.4 Ownership states

Record concepts using these distinct states:

```text
introduced
→ taught
→ interpreted with guidance
→ practiced with guidance
→ recalled after delay
→ diagnosed in a changed case
→ transferred
→ independently reproduced
```

A successful container run proves runtime behavior, not learner ownership.

---

## 8. Phase map

| Phase | Principal problem | Main Docker expansion | Target depth | Durable output |
|---|---|---|---|---|
| 0 | Build an accurate container operating model | Client/daemon, image/container/process, lifecycle, namespaces | D2 for core objects; D1 for engine internals | Verified mental model and bounded observations |
| 1 | Define the adapter before implementation | Roles, boundaries, storage, identity, network, no host exposure | D2 | Docker adapter design decision |
| 2 | Build a safe server image | Dockerfile, layers, build context, PID 1, foreground `sshd` | D2; D3 for build/debug path | Server image and validated configuration |
| 3 | Create the runtime topology manually | User-defined bridge, DNS, routes, container lifecycle | D2 | Manually operated client/server topology |
| 4 | Reproduce SSH semantics | Trust, authorization, mounts, users, IDs, persistence | D2/D3 | Authorized success and unauthorized failure |
| 5 | Correlate Docker-specific observability | Logs, inspect, top, PIDs, sockets, network namespaces | D2/D3 | Cross-view evidence record |
| 6 | Test lifecycle, persistence, and one fault | Restart/recreate/remove/build boundaries, health, repair | D3 | Predicted failure and validated repair |
| 7 | Encode understood behavior in Compose | Declarative services, network, mounts, health, cleanup | D2 | Reproducible Compose adapter |
| 8 | Compare namespaces and Docker | Isolation, automation, visibility, persistence, cleanup | D3 | Evidence-backed comparison and M5 handoff |

---

# Phase 0 — Docker operating model and current environment

## Problem

Prior Docker use does not establish an accurate model of what the Docker client, daemon, image, container, process, network, and storage each own.

## Questions

1. What does the Docker CLI request, and what does the daemon perform?
2. What is immutable image state versus mutable container state?
3. Is a container a machine, a process, or a managed set of Linux isolation/resource mechanisms?
4. Which kernel is shared?
5. What survives stop, restart, removal, and rebuild?
6. Which namespace and cgroup responsibilities Docker creates automatically?
7. How do host and container process views differ?

## Required depth

- Docker client versus daemon: D1.
- Image versus container versus process: D2.
- Container versus VM boundary: D2.
- Linux namespaces/cgroups as Docker building blocks: D2 conceptually; kernel implementation D4 deferred.
- Docker Desktop/WSL internals: D1 now; deeper internals deferred unless debugging requires them.

## Work

- inspect current client/server versions and context;
- inventory containers, images, and networks without modifying unrelated objects;
- run one disposable process container;
- inspect it from Docker, inside the container, and the host where available;
- demonstrate stop, start, remove, and recreate semantics;
- observe a small filesystem mutation and determine its lifetime;
- clean up only the disposable object.

## Expected outcomes

The learner can explain:

```text
image
→ reusable filesystem/configuration template

container
→ runtime instance with writable state and isolation configuration

container process
→ actual executing Linux process using the host-side kernel boundary
```

## Evidence gate

- Docker client and daemon communicate.
- One disposable container is created and inspected.
- The learner distinguishes image, stopped container, and running process.
- A small state-lifetime prediction is tested.
- Cleanup removes only the disposable AegisLab object.

## Stop line

Do not start the SSH Dockerfile until the image/container/process/lifecycle model is sufficiently accurate.

---

# Phase 1 — Docker adapter design

## Problem

A mechanical translation of namespace commands could create an insecure or confusing container layout.

## Questions

1. Should the client and server be separate containers? Why?
2. Which scenario properties are invariant?
3. Which namespace-specific mechanisms should Docker replace?
4. Should port 22 be exposed or published?
5. Where do server host keys, client private keys, `authorized_keys`, and `known_hosts` live?
6. Which state should persist through container recreation?
7. Which process should be the server container’s main process?
8. Which user should run each operation?

## Required depth

- Service/container responsibility boundaries: D2.
- Port expose versus publish: D2.
- Bind mount versus named volume versus image content: D2.
- Production secret systems: D0, deferred.

## Proposed baseline design

```text
Docker network: aegislab-ssh

client container
    │
    │ container DNS + private bridge
    ▼
server container:22

no host port publication
```

Both client and server are containers so the environment preserves two observable endpoints.

## Expected design rules

- The server image contains packages, a lab user, safe static configuration, and startup logic.
- Private identities are generated or mounted at runtime and never committed into image layers.
- The server binds inside its container network namespace.
- The client reaches the server by stable service/container name rather than relying on transient container IPs.
- Runtime-specific values are reinspected.
- The design preserves authorized success and unauthorized failure.

## Evidence gate

A concise adapter decision records:

- actors and responsibilities;
- network boundary;
- identity and storage boundary;
- lifecycle owner;
- logging path;
- non-exposure decision;
- cleanup ownership.

## Stop line

Do not write a Dockerfile until the identity, storage, network, and process-lifecycle decisions are explicit.

---

# Phase 2 — Build the server image manually

## Problem

The server needs a reproducible runtime environment without placing volatile or secret state in committed image layers.

## Questions

1. Which base image gives the clearest learning and operational trade-off?
2. What does each Dockerfile instruction add to image state?
3. What is the build context and why can it leak files?
4. What must `.dockerignore` exclude?
5. How is the target user represented inside the image?
6. Why must `sshd` remain in the foreground?
7. What becomes PID 1, and why does that matter?
8. Which configuration can be validated during build versus runtime?

## Required depth

- `FROM`, `RUN`, `COPY`, `WORKDIR`, `USER`, `EXPOSE`, `CMD`, and `ENTRYPOINT`: D2 for used instructions; D0 for unused instructions.
- Build layers/cache and context: D2.
- Multi-stage builds: D1 unless a demonstrated requirement appears.
- PID 1 and foreground service lifecycle: D2.
- Signal forwarding/zombie reaping internals: D1 initially, D3 only if a lifecycle bug appears.

## Work

- select and justify a base image;
- create the adapter directory and `.dockerignore`;
- write the smallest understandable server Dockerfile;
- install OpenSSH server and only necessary diagnostic tools;
- create the target user;
- add safe static configuration or a runtime template;
- validate image contents and history;
- confirm no private keys or unrelated repository files entered the image;
- start the image in a bounded validation mode before enabling the full topology.

## Expected outcomes

- deterministic image build;
- understandable layer history;
- validated `sshd` configuration;
- foreground server process;
- no committed private identity;
- no reliance on host system SSH.

## Evidence gate

- build exits successfully;
- image inspection matches intended configuration;
- `docker history` contains no secret material;
- the container validates configuration;
- the main process and exit behavior are understood.

---

# Phase 3 — Manual runtime topology

## Problem

Before Compose automates the setup, the learner must understand the Docker objects and relationships manually.

## Questions

1. What does a user-defined bridge network provide?
2. How does container DNS resolve names?
3. Which interface, route, and address appear inside each container?
4. Which bridge and veth-like objects are visible outside Docker Desktop/inside its Linux environment?
5. What does `EXPOSE` document, and what does `-p` publish?
6. How do container start/stop/remove operations affect the network attachment?

## Required depth

- User-defined bridge and service-name DNS: D2.
- Container IP assignment and routes: D2.
- Docker bridge implementation internals: D1; deeper host bridge/iptables/nftables internals deferred unless diagnosing.
- Static container IPs: D1 and generally avoided unless comparison requires them.

## Work

- create an AegisLab-owned user-defined bridge with a non-conflicting subnet or allow Docker-managed IPAM after inspection;
- start the server container without host port publishing;
- start a client container on the same network;
- inspect names, addresses, routes, DNS, sockets, and reachability;
- stop and recreate one endpoint and observe which identifiers change;
- clean up manually created objects when the phase closes.

## Expected outcomes

The learner can map:

```text
manual namespace lab
→ manually created namespace, veth, addresses, routes

Docker adapter
→ daemon-created container namespaces, endpoints, addressing, routes, DNS, and bridge attachment
```

## Evidence gate

- client resolves the server by name;
- both endpoints are attached only to the intended project network;
- no host SSH port is published;
- network and lifecycle observations match predictions;
- unrelated Docker networks remain unchanged.

---

# Phase 4 — SSH success and controlled failure

## Problem

The Docker adapter must preserve the semantic baseline while introducing container-specific filesystem, user, and persistence behavior.

## Questions

1. How is the server host identity supplied and preserved?
2. How is the authorized client public key supplied?
3. How are authorized and unauthorized client private keys kept outside committed image layers?
4. Which UID/GID owns mounted files inside the container?
5. What happens to `known_hosts` and host-key trust after server recreation?
6. How do bind mounts and volumes affect permissions and portability?
7. Where should client debug and server logs be observed?

## Required depth

- Server identity versus client identity/trust directions: D2 with concise re-exposure, not complete reteaching.
- Bind mounts, named volumes, and writable layers: D2.
- UID/GID and permission behavior across mounts: D2/D3.
- Docker secret objects/production orchestration secrets: D0, deferred.

## Work

- generate disposable identities outside committed paths;
- inject or mount the authorized public key and server host identity safely;
- verify fingerprints independently;
- run authorized authentication;
- run unauthorized authentication with only the selected key;
- keep one successful transport open for observation;
- close it deliberately and verify cleanup.

## Expected outcomes

- authorized identity succeeds;
- unauthorized identity reaches the SSH authentication layer and fails;
- server trust is explicit and isolated;
- no alternative host or agent key invalidates the test;
- no private key exists in Git or a committed image layer;
- connection-specific state disappears while the containerized server remains available.

## Evidence gate

Client and server evidence correlate by endpoint, username, fingerprint, and lifecycle.

---

# Phase 5 — Docker-specific observability

## Problem

Docker introduces additional observation positions and namespace boundaries. The learner must know which source answers which question.

## Questions

1. What does `docker inspect` prove?
2. What does `docker top` show versus `ps` inside a container?
3. How do container PIDs map to host-side PIDs?
4. What does `docker logs` contain, and why?
5. Where do sockets appear from client, server, and host observation positions?
6. Which network namespace owns each endpoint?
7. Where can packet capture run, and what does encryption still hide?
8. Which evidence is Docker metadata rather than target-observed behavior?

## Required depth

- `docker inspect`, `docker logs`, `docker top`, `docker exec`: D2.
- PID namespace and host/container PID mapping: D2/D3.
- Network namespace ownership: D2/D3.
- Log driver architecture: D1; advanced drivers deferred.
- `nsenter` and direct namespace entry: D1 initially, D3 only when needed for comparison.

## Work

Correlate one connection across:

```text
client SSH output
server stdout/stderr logs
docker logs
docker inspect
docker top
inside-container ps and ss
host-visible process state where accessible
Docker network attachment
selected packet observation
```

## Evidence gate

The learner explains what each source proves and does not prove, with no assumption that Docker metadata, process output, target logs, and network evidence are interchangeable.

## Stop line

Do not collect every available Docker field. Preserve only fields needed to answer the active question.

---

# Phase 6 — Lifecycle, persistence, and controlled failure

## Problem

Docker’s disposable-container model changes state lifetime and introduces new failure classes.

## Questions

What survives:

- process exit;
- container stop/start;
- container removal/recreation;
- image rebuild;
- volume removal;
- network removal;
- Docker Desktop or WSL restart?

## Required depth

- Container lifecycle and writable layer: D2.
- Volume and bind-mount persistence: D2.
- Restart policies and health checks: D2 for used behavior.
- Storage-driver internals: D0/D1, deferred.

## Candidate controlled failures

Choose one primary fault for D3 diagnosis and optionally inspect others at D1/D2:

1. server container stopped;
2. wrong network attachment;
3. missing or incorrect authorization mount;
4. wrong file owner/mode;
5. regenerated host key with persisted client trust;
6. invalid server configuration;
7. server process exits and container stops;
8. health check detects a degraded service.

## Failure workflow

```text
predict symptom and last successful layer
→ introduce one bounded fault
→ observe client, Docker, and target evidence
→ isolate the failed responsibility
→ repair only that layer
→ revalidate success and negative case
→ clean up
```

## Evidence gate

At least one Docker-specific failure is predicted, diagnosed, repaired, and validated with materially reduced prompting.

---

# Phase 7 — Compose reproducibility

## Problem

Manual commands teach the mechanism but are error-prone as the durable project interface.

## Questions

1. How does Compose represent services, networks, mounts, health checks, dependencies, and cleanup?
2. Which values belong in Compose versus images versus runtime-generated files?
3. What does `depends_on` prove and not prove?
4. How should readiness be represented?
5. How do project names and object labels prevent collisions?
6. How do we ensure private material remains outside Git?

## Required depth

- Compose services/networks/volumes/configuration used by this adapter: D2.
- Health checks/readiness: D2.
- Profiles, extensions, advanced merge behavior: D0/D1, deferred.

## Work

After manual operation is understood:

- encode client and server services;
- encode the private network;
- encode safe mounts or generated runtime paths;
- add the minimum justified health/readiness check;
- provide build, start, inspect, test, stop, and cleanup commands;
- verify fresh recreation;
- verify no unrelated Docker objects are touched.

## Proposed repository shape

```text
adapters/
└── docker/
    └── ssh-baseline/
        ├── compose.yaml
        ├── .dockerignore
        ├── README.md
        ├── server/
        │   ├── Dockerfile
        │   ├── sshd_config
        │   └── entrypoint.sh
        ├── client/
        │   └── Dockerfile
        ├── scripts/
        └── runtime/        # ignored, disposable local state
```

This structure is provisional until Phase 1 confirms responsibilities.

## Evidence gate

A clean environment can build, run, verify success/failure, inspect, and clean up through documented Compose commands.

---

# Phase 8 — Namespace versus Docker comparison

## Problem

M5 is not complete merely because SSH works in containers.

## Questions

1. What did Docker automate?
2. Which isolation boundaries became stronger or newly visible?
3. Which kernel and host resources remain shared?
4. How did process visibility change?
5. How did network setup, DNS, routing, and packet observation change?
6. How did filesystem, identity, and persistence change?
7. How did service lifecycle and cleanup change?
8. Which Docker defaults simplify the lab but can hide important mechanisms?
9. Which risks are new: image content, mount scope, daemon privilege, port publication, stale volumes, or mutable container state?

## Required depth

D3 comparison and transfer for the mechanisms actually used.

## Comparison dimensions

- endpoint topology;
- kernel boundary;
- network namespace ownership;
- PID namespace and process visibility;
- filesystem isolation and shared mounts;
- user/UID/GID behavior;
- address and DNS stability;
- listener and connection lifecycle;
- log access;
- packet capture access;
- persistence;
- reconstruction;
- cleanup;
- attack surface and trust boundaries;
- evidence limitations.

## Evidence gate

A concise comparison uses observed outputs rather than generic claims and identifies:

```text
invariant scenario behavior
environment-specific mechanism
Docker automation
Docker-hidden detail
new Docker failure class
remaining learner gap
```

---

## 9. Session design and pacing

A focused session should normally own one coherent subproblem, not an arbitrary number of commands.

At session start, the playbook must state:

- current phase and step;
- the problem;
- the question;
- required depth;
- prerequisites already satisfied;
- expected end state;
- stop condition.

During the session:

- teach only blocking concepts;
- use one practical action at a time when the action changes state or reveals a key dependency;
- group read-only inspection commands when they answer one coherent question;
- do not ask for repeated output that no longer changes the model;
- record important decisions and evidence;
- adapt explanation depth to demonstrated understanding.

At session end:

- state what was built or learned;
- identify evidence level honestly;
- update the playbook current position;
- update learning state only after meaningful demonstrated change;
- record unresolved questions and the exact next action;
- clean up or explicitly preserve runtime state.

---

## 10. Phase-gate checklist

A phase can close only when:

- the phase problem was answered;
- required practical behavior was observed;
- the learner reached the declared depth for core concepts;
- important negative or changed behavior was interpreted when required;
- artifacts are verified;
- safety boundaries were preserved;
- runtime and durable state are distinguished;
- the next phase does not rely on an untaught prerequisite;
- remaining uncertainty is recorded rather than hidden.

A phase does not require perfect memory of all commands or internals.

---

## 11. M5 completion gate

M5 is complete when all of the following are supported by current evidence:

```text
[ ] Docker core object and lifecycle model demonstrated at D2
[ ] client/server adapter responsibilities explicitly designed
[ ] safe server image built and inspected
[ ] private project network created without unnecessary host publication
[ ] authorized SSH authentication succeeds
[ ] unauthorized SSH key reaches authentication and fails
[ ] server trust and client authorization state are isolated
[ ] process, socket, network, filesystem, and logs are correlated
[ ] one Docker-specific failure is predicted, diagnosed, repaired, and revalidated
[ ] manual operation is understood before Compose automation
[ ] Compose adapter builds, runs, verifies, and cleans up from a fresh state
[ ] namespace-versus-Docker comparison is evidence-backed
[ ] learning depth and remaining gaps are recorded honestly
[ ] unrelated Docker objects remain untouched
```

M5 completion does not imply production Docker expertise or independent mastery of every concept. It means the Docker adapter is sufficiently understood and reproducible to proceed to the VM transfer.

---

## 12. Maintenance contract

- Keep this file focused on the complete M5 route, phase responsibilities, depth, and gates.
- Keep live runtime state and immediate next actions in the session playbook.
- Keep chronology and detailed evidence in worklogs.
- Keep demonstrated learner depth in `CURRENT_LEARNING_STATE.md`.
- Update this plan only for a material change in M5 scope, sequence, safety, depth, or completion criteria.
- Do not expand M5 merely because a Docker feature is interesting.
- When this plan conflicts with current evidence, inspect first and record the correction explicitly.
