# Implementation

The current solution is packaged as copyable OpenCode configuration and prompts. Only `opencode.json` and `.opencode/` are copied into a development repo; the `product-breakdown/` tree stays in this repository as product-breakdown source documentation and traceability.

## Implemented Artifacts

- `opencode.json` - copy into the target development repo root as the OpenCode config and entrypoint selector.
- `.opencode/instructions.md` - package-level neutral instructions that preserve the selected agent boundary.
- `.opencode/agents/orchestrator.md` - primary workflow router.
- `.opencode/agents/orchestrator-*.md` - top-level agents for planning, building, reviewing, reflection, and reporting plus directed helper agents owned by planner, builder, reviewer, and reflection.
- `.opencode/dev_harness/prompts/*.md` - reusable prompt templates tied to use cases.
- `.opencode/dev_harness/README.md` - package index for the reusable dev harness folder.
- `.opencode/dev_harness/product-breakdown/` - reusable product breakdown guidance split into small files for copied target-repo agents.
- `.opencode/dev_harness/workflow/` - shared workflow control, information hygiene, and review-output policies referenced by copied agents.
- `.opencode/dev_harness_memories/` - canonical repo-local versioned memory for lessons, reusable patterns, decision pointers, and trust metadata.

## Package Documentation

- `product-breakdown/` - product-breakdown source documentation and traceability retained in this repository only.
- `docs/` - operator and maintainer guidance for install, deploy, usage, verification commands, troubleshooting, and contributor workflow.
- `README.md` - package overview and copy instructions retained in this repository only.

## Mechanism Storage Rules

The implementation keeps each persistence mechanism in one canonical place so copied runtime policy, package source documentation, memory, skills, and backlog data do not drift into parallel stores.

| Information Type | Store In | Update Through |
| --- | --- | --- |
| Product source rationale, commitments, architecture, decisions, verification expectations, operation requirements, and traceability | `product-breakdown/` | Product-breakdown updates in guarded delivery or improvement work. |
| Runnable install, deploy, usage, verification, troubleshooting, and contributor procedures | `docs/` | Documentation updates; link to product-breakdown context instead of copying it. |
| Agent roles, permissions, workflow-stage prompts, helper routing, and copied runtime behavior | `.opencode/agents/*.md`, `.opencode/instructions.md`, `.opencode/dev_harness/` | Package prompt and workflow-policy edits. |
| Repo-local lessons, reusable patterns, decision pointers, trust metadata, and revalidation cues | `.opencode/dev_harness_memories/` | `orchestrator-reflection` triage and `orchestrator-memory-curator` writes. |
| Improvement candidates and future work seeds | Accepted candidates in `product-breakdown/06-evolution/candidates/`, then selected/done evolution files | `orchestrator-builder` in candidate-capture mode. |
| Current task evidence, work orders, verification output, review findings, waivers, and final reports | Active stage outputs; reconcile durable facts into the owning artifact before completion | Owning stage for the active run. |
| External research claims and source notes | `knowledge/agent-reasoning/` plus cited decisions in `product-breakdown/` | Research-backed product work. |
| Skills, plugins, and connector capabilities | Operator environment unless an accepted product decision changes the package | Product decisions only; do not add agent `SKILLS` declarations without superseding AD-004. |

If a change creates information that crosses these boundaries, update the owning artifact instead of duplicating the same content in multiple mechanisms.

## Execution Roles

- `orchestrator-builder` and builder-owned edit helpers are the only stages that may edit implementation files.
- Direct operator-selected `build` execution is outside the guarded orchestrator path and must not inherit the orchestrator prompt through global instructions.
- `orchestrator` is a dispatcher and gate router only; it has no file read, search, list, edit, or shell permissions, does not classify requests, and invokes only planner, builder, reviewer, reflection, and reporter. Directed helpers such as researcher are invoked by their owning top-level stage.
- `orchestrator-planner` owns discovery, contract, architecture, lessons, research helper routing, inline test obligations, product-breakdown placement, durable product behavior impact, workflow-mode selection, and final work-order synthesis; helper use follows adaptive risk triggers and groups independent helpers into parallel-safe packets when possible.
- `orchestrator-builder` owns implementation, candidate-capture persistence, scoped cleanup, documentation/product-breakdown updates, build-error resolution, cleanup-helper routing, and research helper routing.
- `orchestrator-reviewer` owns verifier, review helper, researcher, and deterministic gate routing; helper use follows adaptive risk triggers, groups independent read-only helpers into parallel-safe packets when possible, and may be lightweight for low-risk tasks.
- review agents are read-only and exist to keep approval separate from implementation.
- `orchestrator-reflection` owns final memory-incorporation triage before reporting and may invoke the memory curator for evidenced durable memory candidates.
- `orchestrator-memory` retrieves task-relevant workflow memory without editing it.
- `orchestrator-memory-curator` may edit only workflow memory files and only for evidenced durable memory candidates.
- Incidental improvement findings raised by working agents are reported as `improvement_candidates`; deliberate persistence uses planner, builder, reviewer, reflection, and reporter.

## Stage Map

| Stage | Artifact | Edit | Bash | Responsibility |
| --- | --- | --- | --- | --- |
| Entrypoint | `opencode.json` | n/a | n/a | Selects `orchestrator` as the default primary agent. |
| Package instructions | `.opencode/instructions.md` | no | no | Keeps global instructions neutral so explicitly selected non-orchestrator agents do not inherit the guarded workflow. |
| Orchestration | `.opencode/agents/orchestrator.md` | no | no | Routes planner, builder, reviewer, reflection, and reporter without repository inspection, request classification, or specialist stage work. |
| Planning | `.opencode/agents/orchestrator-planner.md` | no | yes | Normalizes the request, resolves uncertainty, selects delivery or candidate-capture mode, coordinates planning helpers, groups independent helper packets, and emits the builder work order. |
| Planning helpers | `.opencode/agents/orchestrator-discovery.md`, `orchestrator-contract.md`, `orchestrator-architecture.md`, `orchestrator-lessons.md`, `orchestrator-memory.md` | no | yes | Provide directed discovery, requirements, architecture, lessons, and memory support. Planner handles test obligations and product-breakdown placement in the work order. |
| Build | `.opencode/agents/orchestrator-builder.md` | yes | yes | Applies approved changes or persists candidate-capture backlog artifacts, coordinates builder helpers, reconciles changed information, removes stale or duplicate artifacts, and reports implementation evidence. |
| Build helpers | `.opencode/agents/orchestrator-build-error-resolver.md`, `.opencode/agents/orchestrator-cleanup.md` | yes | yes | Resolve assigned build/test/type-check failures and run focused cleanup passes for references, trackers, indexes, duplicate or superseded content, orphaned artifacts, links, and traceability inside the approved scope. |
| Review and gate | `.opencode/agents/orchestrator-reviewer.md` | no | yes | Coordinates verification and review helpers, groups independent read-only helper packets, then produces `approved`, `blocked`, or `waiver_required`. |
| Review helpers | `.opencode/agents/orchestrator-verifier.md`, `.opencode/agents/orchestrator-review-*.md`, `.opencode/agents/orchestrator-memory.md` | no | yes | Independently verify checks and review contract completeness, acceptance criteria, test adequacy, architecture, code quality, cleanliness, information hygiene, lessons, and relevant workflow memory. |
| Reflection | `.opencode/agents/orchestrator-reflection.md` | no | yes | Reviews completed workflow evidence and owns final memory incorporation triage before reporting. |
| Report | `.opencode/agents/orchestrator-reporter.md` | no | no | Produces the final control report. |
| Research | `.opencode/agents/orchestrator-researcher.md` | no | no | Gathers external documentation or dependency context. |
| Memory curation | `.opencode/agents/orchestrator-memory-curator.md` | yes | yes | Evaluates evidenced repeatable findings and persists only durable workflow memory under `.opencode/dev_harness_memories/`. |

## Product Breakdown Context

The product breakdown guidance is implemented as copied agent context under `.opencode/dev_harness/product-breakdown/`.

| Artifact | Purpose |
| --- | --- |
| `.opencode/dev_harness/product-breakdown/README.md` | Entry point, load-on-demand routing table, recommended layered tree, and layer questions. |
| `.opencode/dev_harness/product-breakdown/layers/*.md` | One small context file per layer. |
| `.opencode/dev_harness/product-breakdown/decision-placement.md` | Rule for placing distributed decisions near affected artifacts. |
| `.opencode/dev_harness/product-breakdown/decision-log.md` | Guidance for maintaining the global decision index. |
| `.opencode/dev_harness/product-breakdown/traceability.md` | Cross-layer traceability chain and checklist. |
| `.opencode/dev_harness/product-breakdown/naming.md` | Stable ID and filename prefixes. |
| `.opencode/dev_harness/product-breakdown/templates/decision-template.md` | Reusable decision record template. |
| `.opencode/dev_harness/product-breakdown/templates/decision-log-entry-template.md` | Reusable compact decision-log entry template. |
| `.opencode/dev_harness/product-breakdown/templates/improvement-backlog-overview-template.md` | Reusable overview template for improvement backlogs. |
| `.opencode/dev_harness/product-breakdown/templates/improvement-candidate-template.md` | Reusable per-candidate improvement backlog template. |

## Workflow Policy Context

Shared workflow policies are implemented as copied agent context under `.opencode/dev_harness/workflow/`.

| Artifact | Purpose |
| --- | --- |
| `.opencode/dev_harness/workflow/control-policy.md` | Required stage order, route selection, handoff boundaries, control flags, and waiver rules. |
| `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` | Planner, builder, and reviewer helper-selection triggers. |
| `.opencode/dev_harness/workflow/agent-boundaries.md` | Shared read/write, scope-containment, and no-edit boundaries for agents. |
| `.opencode/dev_harness/workflow/candidate-capture.md` | Candidate-capture ownership, write boundary, required evidence, and valid dispositions. |
| `.opencode/dev_harness/workflow/information-hygiene.md` | Canonical evidence requirements for changed information artifacts. |
| `.opencode/dev_harness/workflow/parallel-helper-execution.md` | Planner and reviewer rules for parallel-safe helper packets. |
| `.opencode/dev_harness/workflow/product-breakdown-work.md` | Product-breakdown loading, placement, traceability, decision, and index evidence rules. |
| `.opencode/dev_harness/workflow/stage-output-schema.md` | Common output fields, `not_applicable`, clarification fields, feedback, candidate, and research request schema. |
| `.opencode/dev_harness/workflow/workflow-memory.md` | Memory retrieval, curation, final reflection, and reporting boundaries. |
| `.opencode/dev_harness_memories/lessons.md` | Persistent lesson memory used by the lessons and lessons-review agents, including trust metadata and decision pointers. |
| `.opencode/dev_harness_memories/patterns.md` | Reusable planning, implementation, review, documentation, and improvement patterns with trust metadata and decision pointers. |
| `.opencode/dev_harness/workflow/review-output.md` | Shared independent-review return protocol. |

## Trace Links

- Implements AD-001 through AD-003, ED-001, IMD-001 through IMD-003, and IMP-001 through IMP-007.
- Satisfies PC-001 through PC-010.
- Covers UC-001 through UC-013.
- Implements the architecture-level persistence and context mechanism boundaries through the mechanism storage rules above.
