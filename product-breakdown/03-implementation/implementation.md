# Implementation

The current solution is packaged as copyable OpenCode configuration and prompts. Only `opencode.json` and `.opencode/` are copied into a development repo; the `product-breakdown/` tree stays in this repository as product-breakdown source documentation and traceability.

## Implemented Artifacts

- `opencode.json` - copy into the target development repo root as the OpenCode config and entrypoint selector.
- `.opencode/agents/orchestrator.md` - primary workflow router.
- `.opencode/agents/orchestrator-*.md` - top-level agents for planning, building, reviewing, reporting, research, and improvement discovery plus directed helper agents owned by planner, builder, and reviewer.
- `.opencode/dev_harness/prompts/*.md` - reusable prompt templates tied to use cases.
- `.opencode/dev_harness/README.md` - package index for the reusable dev harness folder.
- `.opencode/dev_harness/product-breakdown/` - reusable product breakdown guidance split into small files for copied target-repo agents.
- `.opencode/dev_harness/workflow/` - shared workflow control, information hygiene, and review-output policies referenced by copied agents.
- `.opencode/dev_harness_memories/` - canonical repo-local versioned memory for lessons, reusable patterns, and decision pointers.

## Package Documentation

- `product-breakdown/` - product-breakdown source documentation and traceability retained in this repository only.
- `docs/` - operator and maintainer guidance for install, deploy, usage, verification commands, troubleshooting, and contributor workflow.
- `README.md` - package overview and copy instructions retained in this repository only.

## Execution Roles

- `orchestrator-builder` and builder-owned edit helpers are the only stages that may edit implementation files.
- `orchestrator-improvement` may edit only improvement backlog result files under `product-breakdown/06-evolution/candidates/`.
- `orchestrator` is a dispatcher and gate router only; it has no file read, search, list, edit, or shell permissions, does not classify requests, and invokes only planner, builder, reviewer, reporter, and the improvement entrypoint. Directed helpers such as researcher are invoked by their owning top-level stage.
- `orchestrator-planner` owns discovery, contract, architecture, lessons, research helper routing, inline test obligations, product-breakdown placement, durable product behavior impact, and final work-order synthesis; helper use follows adaptive risk triggers.
- `orchestrator-builder` owns implementation, scoped cleanup, documentation/product-breakdown updates, build-error resolution, cleanup-helper routing, and research helper routing.
- `orchestrator-reviewer` owns verifier, review helper, researcher, and deterministic gate routing; helper use follows adaptive risk triggers and may be lightweight for low-risk tasks.
- review agents are read-only and exist to keep approval separate from implementation.
- `orchestrator-memory` retrieves task-relevant workflow memory without editing it.
- `orchestrator-memory-curator` may edit only workflow memory files and only for evidenced durable memory candidates.
- `orchestrator-improvement` exists to explore improvement opportunities and persist backlog candidates, not to implement them.
- `orchestrator-improvement-evaluator` evaluates focused findings raised by working agents and persists qualifying backlog candidates without expanding the current task.

## Stage Map

| Stage | Artifact | Edit | Bash | Responsibility |
| --- | --- | --- | --- | --- |
| Entrypoint | `opencode.json` | n/a | n/a | Selects `orchestrator` as the default primary agent. |
| Orchestration | `.opencode/agents/orchestrator.md` | no | no | Routes planner, builder, reviewer, reporter, or improvement discovery without repository inspection, request classification, or specialist stage work. |
| Planning | `.opencode/agents/orchestrator-planner.md` | no | yes | Normalizes the request, resolves uncertainty, coordinates planning helpers, and emits the builder work order. |
| Planning helpers | `.opencode/agents/orchestrator-discovery.md`, `orchestrator-contract.md`, `orchestrator-architecture.md`, `orchestrator-lessons.md`, `orchestrator-memory.md` | no | yes | Provide directed discovery, requirements, architecture, lessons, and memory support. Planner handles test obligations and product-breakdown placement in the work order. |
| Build | `.opencode/agents/orchestrator-builder.md` | yes | yes | Applies approved changes, coordinates builder helpers, reconciles changed information, removes stale or duplicate artifacts, and reports implementation evidence. |
| Build helpers | `.opencode/agents/orchestrator-build-error-resolver.md`, `.opencode/agents/orchestrator-cleanup.md` | yes | yes | Resolve assigned build/test/type-check failures and run focused cleanup passes for references, trackers, indexes, duplicate or superseded content, orphaned artifacts, links, and traceability inside the approved scope. |
| Review and gate | `.opencode/agents/orchestrator-reviewer.md` | no | yes | Coordinates verification and review helpers, then produces `approved`, `blocked`, or `waiver_required`. |
| Review helpers | `.opencode/agents/orchestrator-verifier.md`, `.opencode/agents/orchestrator-review-*.md`, `.opencode/agents/orchestrator-memory.md` | no | yes | Independently verify checks and review contract completeness, acceptance criteria, test adequacy, architecture, code quality, cleanliness, information hygiene, lessons, and relevant workflow memory. |
| Report | `.opencode/agents/orchestrator-reporter.md` | no | no | Produces the final control report. |
| Research | `.opencode/agents/orchestrator-researcher.md` | no | no | Gathers external documentation or dependency context. |
| Memory curation | `.opencode/agents/orchestrator-memory-curator.md` | yes | yes | Evaluates evidenced repeatable findings and persists only durable workflow memory under `.opencode/dev_harness_memories/`. |
| Improvement | `.opencode/agents/orchestrator-improvement.md` | yes | no | Produces and persists backlog-ready cleanup, refactoring, pattern, module responsibility, or tuning candidates under the evolution backlog only. |
| Focused improvement evaluation | `.opencode/agents/orchestrator-improvement-evaluator.md` | yes | yes | Evaluates one noteworthy finding raised by a working agent and persists it only when it has evidence, impact, and a scoped future task seed. |

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
| `.opencode/dev_harness/workflow/control-policy.md` | Required stage output, `not_applicable`, handoff boundaries, control flags, and waiver rules. |
| `.opencode/dev_harness/workflow/information-hygiene.md` | Canonical evidence requirements for changed information artifacts. |
| `.opencode/dev_harness_memories/lessons.md` | Persistent lesson memory used by the lessons and lessons-review agents. |
| `.opencode/dev_harness_memories/patterns.md` | Reusable planning, implementation, review, documentation, and improvement patterns. |

| `.opencode/dev_harness/workflow/review-output.md` | Shared independent-review return protocol. |

## Trace Links

- Implements AD-001 through AD-003, IMD-001 through IMD-003.
- Satisfies PC-001 through PC-010.
- Covers UC-001 through UC-013.
