# AegisLab — M5 Docker Session Playbook

**Status:** Active mutable playbook  
**Last updated:** 2026-07-18  
**Active milestone:** M5 — Docker adapter reproduction  
**Current phase:** Phase 0 — Docker operating model and current environment  
**Current step:** 0.1 — Confirm and interpret the Docker object/runtime baseline  
**Full plan:** [M5 Docker Learning and Execution Plan](<AegisLab — M5 Docker Learning and Execution Plan.md>)  
**Teaching contract:** [Learning Preferences](../../LEARNING-PREFERENCES.md)

---

## 1. Purpose

This file is the live operational companion to the full M5 plan.

It answers, at any pause or resume point:

- where we are;
- what problem is active;
- what depth is required;
- what has already been proven;
- what the next bounded action is;
- what evidence closes the current step;
- what must not be repeated unnecessarily.

Do not turn this file into a transcript. Keep detailed chronology in worklogs and durable phase rules in the full M5 plan.

---

## 2. Current project decision

The learner explicitly chose to proceed to M5 because the remaining formal M4 work was judged redundant for current learning value.

Record this accurately:

```text
M4 remaining formal scenario-contract work
→ deferred by explicit learner decision
→ not claimed complete

M5 Docker learning and adapter work
→ active
```

The Docker implementation preserves the already demonstrated namespace semantics:

- authorized key succeeds;
- unauthorized key reaches SSH authentication and fails;
- successful connection can be observed;
- connection-specific state disappears after client teardown;
- reusable server state remains until deliberately stopped.

---

## 3. Current environment snapshot

### Repository

- Repository: `motafegh/AegisLab`
- Branch: `main`
- The learner’s local repository was synchronized through commit `27833bc` before these M5 planning documents were added remotely.
- Before local implementation, pull the latest planning commits and inspect `git status` so no local work is overwritten.
- No Docker adapter implementation directory, Dockerfile, or Compose file existed when M5 planning began.

### WSL

- Ubuntu runs under WSL2.
- A WSL networking/resolver failure temporarily removed usable host networking.
- `wsl --shutdown` followed by reopening WSL restored interfaces, routing, DNS, ICMP, and GitHub access.
- The old namespace lab runtime disappeared after WSL shutdown, as expected for volatile state.

### Docker

Observed through `docker version`:

```text
client: Docker Engine 29.6.1
server: Docker Desktop 4.80.0 / Engine 29.6.1
API: 1.55
context: default
architecture: linux/amd64
```

Current object inventory:

- no running containers;
- unrelated stopped containers: `kali`, `juiceshop`, `webgoat`, and `dvwa`;
- multiple unrelated local images;
- `alpine:latest` is available locally, but base-image selection remains an explicit Phase 2 decision;
- existing networks:

```text
bridge             172.17.0.0/16  internal=false
lab-net-nat        172.18.0.0/16  internal=false
lab-net-internal   172.19.0.0/16  internal=true
host
none
```

No AegisLab Docker network has been created yet. Existing containers, images, and custom networks are not project dependencies and must remain untouched.

---

## 4. Live working loop

For each meaningful step:

```text
orient to phase and problem
        ↓
state the question
        ↓
select required depth
        ↓
make a prediction when useful
        ↓
perform one bounded action
        ↓
interpret decisive evidence
        ↓
update model or diagnose failure
        ↓
close step or define exact next action
```

Read-only commands that answer one coherent question may be grouped. State-changing, destructive, security-sensitive, or conceptually important actions should normally be performed one at a time.

---

## 5. Explanation-depth control

Before teaching or explaining, classify the item.

### Brief

Use for familiar, simple, low-risk mechanics.

Required content:

- why now;
- what it does;
- decisive output.

### Standard

Use for new Docker mechanisms required by the active step.

Required content:

- problem and responsibility;
- minimum accurate model;
- important syntax;
- expected result classes;
- evidence meaning.

### Deep

Use only when:

- required depth is D2 or D3;
- a security/isolation boundary is active;
- confusion appears;
- evidence conflicts;
- failure diagnosis or transfer requires it.

Do not give full flag-by-flag explanations for every familiar command. Re-explain a known flag briefly when current recall benefits from it.

---

## 6. Step-card template

Every meaningful step in this playbook should be representable as:

```text
Step:
Phase:
Problem:
Why now:
Question:
Required depth:
Prerequisites:
Prediction:
Action:
Expected output classes:
Decisive evidence:
What it proves:
What it does not prove:
Failure branches:
Completion gate:
Cleanup/preserved state:
Next step:
```

Small commands do not need every heading in chat. The step itself must still have these responsibilities resolved.

---

# Active Phase 0 — Docker operating model

## Phase problem

The learner has used Docker objects before, but the current evidence does not establish a stable model of image, container, process, daemon, namespace, network, and state lifetime.

## Phase objective

Build the minimum complete Docker operating model needed to design the SSH adapter without treating a container as a small VM or relying on memorized commands.

## Required depth

| Concept | Depth | Evidence required |
|---|---|---|
| Docker CLI versus daemon | D1 | Explain requester versus executor |
| Image versus container versus process | D2 | Inspect real objects and explain state/lifetime |
| Container versus VM | D2 | State shared-kernel and isolation differences |
| Stop/start/remove/recreate | D2 | Predict and observe state changes |
| Container filesystem writable layer | D2 | Test one bounded mutation and lifetime |
| PID and network namespace concept | D2 | Correlate one running container with process/network views |
| Docker Desktop/WSL internal architecture | D1 | Recognize boundary; deeper detail deferred |
| cgroup and storage-driver internals | D0/D1 | Deferred unless a real need appears |

## Phase completion gate

Phase 0 closes when the learner can explain, using one observed disposable container:

```text
what came from the image
what exists only in the container
which process makes it running
what stop changes
what removal changes
which kernel is shared
what Docker created automatically
```

No SSH image should be built before this gate.

---

## Step 0.1 — Confirm and interpret the baseline

**Status:** In progress; inspection mostly complete.

### Problem

We need an accurate starting inventory and must avoid colliding with unrelated Docker objects.

### Completed evidence

- Docker client and daemon are reachable.
- No containers are running.
- Existing stopped containers and custom networks are unrelated.
- Existing bridge subnets are known.
- No AegisLab Docker implementation exists.

### Required learner understanding

D1:

- Docker Desktop engine is reachable through the WSL Docker client.
- A stopped container is still a container object but has no running container process.
- An image is not a running container.
- Existing unrelated objects must not be reused or deleted casually.

### Completion gate

The baseline is complete after the latest repository planning commits are pulled locally and `git status` confirms the implementation will start from a known worktree.

### Next action

Pull the latest `main`, inspect `git status --short`, and read this playbook locally before running the first disposable-container exercise.

---

## Step 0.2 — Run one disposable process container

**Status:** Pending.

### Problem

The terms image, container, and process need one direct observable example.

### Question

What changes when an image is used to create a container whose main process is running?

### Required depth

D2 for image/container/process responsibility and lifetime.

### Planned action

Run one clearly named, AegisLab-owned disposable container with a simple long-lived process. Do not use an unrelated existing container.

### Prediction

Before execution, predict:

- which image is used;
- which container object appears;
- which process keeps it running;
- what `docker ps` and `docker ps -a` should show;
- what happens when the main process exits.

### Evidence

Use only the smallest useful set:

- `docker ps` / `docker ps -a`;
- `docker inspect` selected fields;
- one inside-container process view;
- one host/Docker process view where available.

### Completion gate

The learner explains why the container is running and what would make it stop.

### Cleanup

Remove only the disposable AegisLab container after later Phase 0 lifecycle steps are complete.

---

## Step 0.3 — Test image and writable-container state

**Status:** Pending.

### Problem

Image content and container writable state are commonly confused.

### Question

Which filesystem change belongs to the image and which belongs only to one container instance?

### Required depth

D2.

### Planned action

Create one harmless file inside the disposable container, stop/start the same container, then remove/recreate from the same image.

### Prediction

Predict file presence after:

1. stop/start of the same container;
2. removal of that container;
3. creation of a new container from the same image.

### Completion gate

The learner correctly explains why stop/start preserves the writable layer but removal/recreation does not, unless external persistent storage is used.

---

## Step 0.4 — Correlate process and PID views

**Status:** Pending.

### Problem

A container process can have different PID representations depending on the observation position.

### Question

How does the container’s process view relate to Docker’s and the host-side view?

### Required depth

D2 now; D3 later during SSH observability.

### Planned evidence

- main process from `docker inspect`;
- `docker top`;
- `ps` inside the container;
- host-visible process relationship where Docker Desktop/WSL permits useful inspection.

### Completion gate

The learner explains that process isolation changes visibility and identifiers; it does not create a separate kernel.

---

## Step 0.5 — Correlate container networking

**Status:** Pending.

### Problem

Docker automates mechanisms that were manually created in the namespace lab.

### Question

What network namespace, interface, address, route, and network attachment does Docker create for a container?

### Required depth

D2 conceptually; Docker bridge implementation internals remain D1 until needed.

### Planned evidence

- selected `docker inspect` network fields;
- interface/address/route inside the disposable container;
- current attached Docker network;
- comparison with manual namespace/veth work.

### Completion gate

The learner distinguishes Docker-managed network attachment from the earlier manually built veth/namespace topology.

---

## Step 0.6 — Lifecycle and cleanup

**Status:** Pending.

### Problem

We need a controlled model of stop, start, remove, and recreate before introducing multi-container SSH state.

### Question

Which object and state survive each lifecycle operation?

### Required depth

D2.

### Completion gate

The learner predicts and verifies lifecycle behavior, then removes only Phase 0 disposable objects.

### Phase handoff

Update this playbook to Phase 1 and record the demonstrated depth in `CURRENT_LEARNING_STATE.md` only after the gate is actually met.

---

# Later phase queue

## Phase 1 — Adapter design

Pending outputs:

- client/server responsibility decision;
- private network and no-host-publication decision;
- image versus runtime identity/storage decision;
- server main-process and logging decision;
- provisional repository layout confirmed or revised.

## Phase 2 — Server image

Pending outputs:

- base-image decision;
- `.dockerignore`;
- server Dockerfile;
- target user and safe static configuration;
- runtime identity strategy;
- image build/history validation.

## Phase 3 — Manual topology

Pending outputs:

- AegisLab-owned user-defined bridge;
- manual server and client containers;
- name resolution, addresses, routes, reachability;
- no unnecessary published port.

## Phase 4 — SSH semantics

Pending outputs:

- authorized success;
- unauthorized failure;
- trust and authorization separation;
- safe runtime private material;
- deliberate teardown.

## Phase 5 — Observability

Pending outputs:

- logs, inspect, top, process, socket, network, and packet correlation;
- host/container visibility explanation.

## Phase 6 — Failure and persistence

Pending outputs:

- lifecycle persistence matrix;
- one predicted Docker-specific fault;
- diagnosis, repair, and revalidation.

## Phase 7 — Compose

Pending outputs:

- reproducible Compose adapter;
- bounded health/readiness behavior;
- fresh build/run/test/cleanup verification.

## Phase 8 — Comparison

Pending outputs:

- evidence-backed namespace-versus-Docker comparison;
- M5 ownership assessment;
- VM transfer handoff.

---

## 7. Resume protocol

At the start of every M5 session:

1. inspect `git status --short`;
2. pull only when the worktree state makes it safe;
3. read `PROJECT_STATE.md`;
4. read this playbook’s current phase and step;
5. inspect only volatile Docker facts needed by that step;
6. state the current problem, required depth, and completion gate;
7. continue from the exact next action rather than restarting the whole phase.

After Docker Desktop or WSL restart, reinspect:

- Docker client/daemon reachability;
- running and stopped AegisLab containers;
- AegisLab networks;
- runtime files and mounts;
- current images and build state;
- any preserved volumes;
- unrelated objects before cleanup.

---

## 8. Pause and handoff protocol

Before a known pause:

- state which phase/step is active;
- record the last action and decisive evidence;
- distinguish durable files from volatile runtime objects;
- state whether runtime should remain or be cleaned up;
- record blockers and rejected hypotheses;
- set one exact next action;
- update the current worklog;
- update `PROJECT_STATE.md` only for a meaningful project/environment/decision change.

---

## 9. Current exact next action

After the learner pulls these planning changes locally:

```text
Phase 0, Step 0.2
→ choose one disposable base image/process exercise
→ predict image/container/process state
→ run one named AegisLab-only container
→ inspect only the fields needed to establish the model
```

Do not create the final SSH network, Dockerfiles, private-key material, or Compose project before Phase 0 and Phase 1 gates are satisfied.
