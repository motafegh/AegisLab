# Industry tooling, interoperability and product usefulness

**Recorded:** 2026-11-24. **Authority:** supporting execution/learning plan under the [Core Charter v2](<AegisLab — Core Charter v2.0.md>), [Capability Execution Map v2](<AegisLab — Capability Execution Map v2.md>) and [Learning and Technology Strategy](../definition/learning-and-technology-strategy.md). Records owner-endorsed direction from the tooling/product discussion. Specific implementations, packages, versions and deployment changes require their own decision and applicable authorization. No change to Core identity or existing safety gates.

## Direction and scope

AegisLab remains an evidence-centered cyber range and defense/investigation workbench. Its candidate product positioning is a local-first, evidence-verifiable investigation and automation layer interoperating with existing security infrastructure, not a replacement for an entire SIEM, IDS, IPS, EDR, NDR, SOAR or SOC. This is a product hypothesis, not demonstrated uniqueness, user demand or production readiness. Preserve the cyber range, independent scenario truth, deterministic baseline, explicit uncertainty, evidence lineage and human control. Develop transferable security/AI engineering competence and practical familiarity with professional tools alongside the product.

Build a bounded reference implementation to learn a mechanism when needed; do not recreate mature general-purpose systems unnecessarily. Reuse established sensors, runtimes, validators, persistence and evaluation tools when fit is demonstrated. Own security-specific data contracts, evidence/claim semantics, independent evaluation and authorization policy even when reusing libraries or enforcement components.

## Adoption and exposure decision register

Three modes: **build** (own a necessary mechanism or distinctive responsibility); **integrate** (use a mature component via a documented boundary); **exercise** (gain hands-on competence, compare, then decide whether to adopt). A tool can move between modes. Required exercise means do it with learner participation or explicitly record a justified deferral/equivalent exercise, not necessarily install permanently. Candidates must not be silently forgotten or treated as mandatory dependencies.

| Responsibility | Default decision | Initial disposition / review trigger |
|---|---|---|
| SSH finding, provenance and evidence-linked verification | Build bounded reference; compare | Stage B reference verified; compare external rule semantics before broadening custom detector |
| General SIEM, network IDS/IPS, EDR, protocol capture | Exercise/integrate, not rebuild | D/G sensor/platform comparison |
| Validation and schema | Exercise/integrate mature library if fit | C3/C5 compare Pydantic or JSON Schema validation with explicit checks |
| Inference serving | Integrate | LM Studio experimentally used; C7 alternative runtime comparison |
| Security-specific evaluation rubric and independent truth | Build/own | C6; compare evaluation runner, not outsource correctness |
| Generic LLM evaluation runner | Exercise/integrate if fit | C6 compare Promptfoo; retain reproducible local baseline |
| Agent orchestration | Build small explicit workflow; exercise framework | E/F compare LangGraph when state/control needs justify |
| Tool authorization and audit | Own policy; integrate enforcement where justified | E external-to-model policy; never unrestricted shell/MCP |
| Storage, service API, event transport, observability | Integrate mature components after mechanism learning | F/post-Core based on real requirements |
| General forensic collection, hunting queries, threat intelligence | Exercise/integrate | E/G/later forensic depth; avoid rebuilding endpoint collector |

For each adoption decision record problem, alternatives, actual exercise/evidence, build/integrate/exercise/defer disposition, version/license, maintenance and vulnerability review, data and network boundaries (including outbound telemetry/remote providers), permissions, resource footprint, failure/recovery, reproducibility and removal path. Review official docs/license and current maintenance when acting, not assumed from discussion. No blanket dependency approval; local-only and scoped authorized lab rules remain.

## Industry competency matrix and stage-linked work

Status is independent of the [concept learning ledger](../learning/LEARNING_LEDGER.md). Depth: purpose understood; run/inspect with guidance; configure independently; integrate programmatically; diagnose/secure; retain actual evidence and help level. No numeric score or mastery from AI execution. **Core checkpoint** = scheduled practical exercise/review; if unsuitable or unsafe, record reason, equivalent learning or explicit later owner-approved destination. **Candidate** = deliberately review on trigger, not a mandatory exercise for first Core. Status below is initial evidence, not claims of current installations.

| Stage / checkpoint | Tool(s) and priority | Practical outcome / target depth | Current evidence |
|---|---|---|---|
| B-to-C comparison | Sigma (Core checkpoint) | Represent supported SSH pattern and temporal/count correlation; inspect conversion/backend limitations, compare grouping/window/duplicate semantics with reference detector; retain a small reproducible example or explain unsupported backend | Not exercised in AegisLab |
| C1/C4 | LM Studio (Core checkpoint) | Inspect API, model serving, structured responses, timeout/truncation and local proxy failure; learner personally run/diagnose | AI-operated exploratory trials; learner reasoning, practical independence open |
| C3/C5 | Pydantic / JSON Schema (Core checkpoint: at least one mature validator exercise) | Define types, missing values and cross-field constraints; compare invalid IDs/shape and distinguish semantic limits | AI exercised installed jsonschema 4.10.3 with valid/invalid schema and membership cases; optional probe integration; learner practical exercise and dependency adoption review pending |
| C6/E | Promptfoo (Core checkpoint review/exercise) | Run fixed local cases; compare with Python runner; evaluate format, grounding rubric and injection tests; ensure no cloud, remote generation, telemetry or data transfer without authorization | Pending |
| C7/F | Ollama or another compatible local runtime (candidate) | Compare same-case outputs, resource/latency and failure behavior with LM Studio; avoid unnecessary duplicate model downloads | Pending |
| D | tcpdump / Wireshark (Core checkpoint) | Capture/inspect isolated traffic, reconstruct TCP/SSH connection and encrypted visibility limits; learner diagnose one changed case | July guided packet observation; Wireshark operation and current independent recall unestablished |
| D/F | Wazuh (Core checkpoint; first platform candidate) | Inspect decoders/rules, replay synthetic or authorized SSH evidence, trace source→alert, compare with Stage B and decide alert/raw/normalized adapter boundary; minimal lab or offline exercise first | Pending |
| D/G | Zeek (Core checkpoint) | Process authorized capture offline or scoped lab traffic, inspect connection metadata, correlate with host observations; state what cannot establish authentication | Pending |
| D/G | MITRE ATT&CK and OCSF (Core checkpoint review/exercise) | Map observed behavior and limitations, compare a normalized event with OCSF; do not equate mapping with attack attribution | Pending |
| E | osquery (Core checkpoint) | Run bounded read-only OS queries, examine scope, result provenance, missing evidence and authorization | Pending |
| E | MCP (Core checkpoint) | Exercise typed scoped tool interface, explicit policy outside model, deny/malformed/injection tests; protocol not an authority grant | Pending |
| E/F | LangGraph (candidate) | Compare explicit Python workflow with framework state, limits/checkpointing and human approval when warranted | Pending |
| E/G/later | Velociraptor (candidate) | Examine endpoint acquisition and query controls; safe read-only artifact collection only when justified | Pending |
| F | Docker / Compose (Core checkpoint) | Configure bounded services, inspect networking/volumes/resources, diagnose failure and recover; never require Docker/VM parity before B/C | July inventory only; no Compose implementation |
| F | FastAPI (candidate), SQLite/PostgreSQL (Core checkpoint: SQL/persistence exercise), Redis (candidate) | Exercise HTTP service, typed contracts, persistence/transactions, failure modes and caching/state where needed | Pending in AegisLab |
| F | Git/GitHub Actions (Core checkpoint), Trivy/Semgrep (candidate) | Run and interpret CI, dependency/container or static-analysis results; no claim of safety solely from checks | Git used; learner CI/security scanning not assessed here |
| F | OpenTelemetry, Prometheus/Grafana (Core checkpoint: at least one observability exercise; others candidates) | Inspect service telemetry, diagnose timeout/restart and compare instrumented evidence; avoid full stack by default | Pending |
| G | Suricata (Core checkpoint) | Replay authorized capture, inspect EVE JSON and rule behavior, compare with Zeek/host evidence and evaluate false positives/negatives | Pending |
| G | OpenSearch Security Analytics or Elastic Security; Security Onion (candidates) | Explore existing platform query/correlation/operator workflow, compare integration costs; licensing/features/resources checked at use time | Pending |
| G/later | YARA, Volatility, Timesketch, MISP (candidates) | Artifact matching, memory analysis, timeline and intelligence; choose authorized public-safe examples; maturity gates control | Pending |
| G/later | Atomic Red Team (candidate) | Select explicitly authorized isolated defensive coverage experiments, predefine scope/truth/abort/cleanup; no external targeting or unsafe malware | Pending |
| Post-Core distributed systems | Kafka or Redpanda, OpenSearch or Elasticsearch (deliberate future review) | Exercise producers/consumers, replay, offsets, ordering, duplicates, failures, search/indexing and resource limits once a real workload exists | Pending |
| Post-Core applied ML | scikit-learn, PyTorch, MLflow (deliberate future review) | Baseline feature/evaluation design, leakage, drift, deployment and experiment tracking; only justified models | Prior external experience not AegisLab competency |

## Execution checkpoints (do not silently skip)

- At each stage planning/closure, review applicable rows, choose a bounded exercise, state required learner depth, record commands/config, outputs, failure case, comparison and disposition. If PC unavailable, separate AI-operated demonstration from learner ownership and keep the latter pending.
- Near-term: after C2 design checkpoint, schedule a bounded Sigma rule/correlation comparison before broad custom detection expansion (can run alongside C without blocking C2); plan Wazuh comparison before or during D/F, using safe synthetic/offline material first. Do not install a full stack just to satisfy a checklist.
- C3/C5 validator exercise and C6 evaluation-runner comparison must be reviewed in the C execution plan; C7 alternate runtime remains conditional.
- D: genuine host/network evidence and sensor comparison; E: secure read-only query and typed tool authorization; F: reproducibility, deployment and diagnosis; G: materially different security context and external-platform interoperability comparison. The first Core should include at least one demonstrable third-party security evidence import/adapter or documented blocker and explicit follow-up; do not falsely declare it implemented.
- At G closure review all Core checkpoints and post-Core candidates; preserve unfinished ones with reason, owner, revisit trigger and next stage. No silent deletion, automatic mastery or mandatory all-tools install. Separate software and learner gates.

## Product and ecosystem review

Prior discussion identified Wazuh, Zeek, Suricata, Security Onion, OpenSearch Security Analytics and Elastic Security as relevant established platform references. Candidate AI investigation projects for selective architecture review: [Vigil SOC](https://github.com/Vigil-SOC/vigil), [AiSOC](https://github.com/dedibagus/aisoc), [AI-SOC-Agent](https://github.com/kunalbhoria1/AI-SOC-Agent), [Triagewall](https://github.com/aaronphifer/triagewall), [Casewright](https://github.com/chanchalvdev/casewright). These are discovery leads from the prior discussion, not independently executed, verified current features, license approvals, or endorsements. Recheck existence, docs, licenses, maintenance and actual capabilities at evaluation time; drop unsuitable references explicitly. Do not claim novelty merely from combining AI with deterministic detection.

Initial operator task: from an existing alert or attributable observations, identify supporting records, plausible explanations, missing evidence and a specific authorized next observation. Candidate future workflow: Wazuh alert/host records + Zeek or Suricata network evidence → adapters and provenance → deterministic verification → local AI hypotheses → external policy-mediated read-only checks (E only) → traceable operator report. This is not a shipped integration.

Compare against (1) the existing same-evidence deterministic baseline, (2) an operator using mature platform queries/rules directly and, when feasible, (3) a comparable AI tool. Use fixed operator questions and identical available evidence, independently held truth or adjudicated expected properties, record supported/unsupported claims, actionable next steps, omissions, operator effort/time, token/latency/resource costs, failure and permission behavior. Avoid claiming demand until credible external operator testing. If a mature tool solves the task adequately, integrate it or narrow AegisLab's contribution instead of cloning it. If AI does not add value, retain AI OFF and revise/reject the candidate.

Production-minded, not production-ready: documented interoperability, maintainability, versioned contracts, least privilege, local privacy, dependency/license/supply-chain review, observable failures and recovery, resource/latency measurement, operator-oriented acceptance and safe rollback. Introduce infrastructure incrementally under the available local hardware budget. No production SLO, real-world effectiveness or market demand claim without suitable evidence.

## Next review

C2 remains active; no new tool installation or product implementation authorized by recording this plan. Review C3/C5/C6 candidates when those milestones open, and book the bounded Sigma/Wazuh comparison in the next relevant stage worklog. Update this register with evidence rather than creating duplicate checklists. See [current project state](../../PROJECT_STATE.md).
