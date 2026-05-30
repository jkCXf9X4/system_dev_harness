# Implementation

The current solution is packaged as copyable OpenCode configuration and prompts. Only `opencode.json` and `.opencode/` are copied into a development repo; the `product-breakdown/` tree stays in this repository as product-breakdown source documentation and traceability.

## Implemented Artifacts

- `opencode.json` - copy into the target development repo root as the OpenCode config and entrypoint selector.
- `.opencode/agents/orchestrator.md` - primary workflow coordinator.
- `.opencode/agents/orchestrator-*.md` - stage agents for planning, discovery, contract, architecture, lessons, packet, handoff, builder, verifier, review, gate, reporter, research, and improvement discovery.
- `.opencode/dev_harness/prompts/*.md` - reusable prompt templates tied to use cases.
- `.opencode/dev_harness/README.md` - package index for the reusable dev harness folder.
- `.opencode/dev_harness/product-breakdown/` - reusable product breakdown guidance split into small files for copied target-repo agents.
- `.opencode/dev_harness/workflow/` - shared workflow control, information hygiene, known-mistakes memory, and review-output policies referenced by copied agents.
- `.opencode/dev_harness/workflow/known-mistakes.md` - persistent lesson memory.

## Package Documentation

- `product-breakdown/` - product-breakdown source documentation and traceability retained in this repository only.
- `README.md` - package overview and copy instructions retained in this repository only.

## Execution Roles

- `orchestrator-builder` is the only stage that may edit implementation files.
- `orchestrator-improvement` may edit only improvement backlog result files under `product-breakdown/06-evolution/backlog/`.
- `orchestrator` is a dispatcher and gate router only; it does not perform preliminary planning, discovery, implementation, verification, shell checks, or edits.
- `orchestrator-discovery` is the only broad repository search stage before implementation.
- `orchestrator-planner` classifies the request and sets initial flags without repository inspection.
- `orchestrator-contract`, `orchestrator-architecture`, `orchestrator-packet`, and `orchestrator-handoff` consume upstream context and read only exact files when their prompt allows it.
- `orchestrator-verifier` is shell-capable for focused checks.
- review agents are read-only and exist to keep approval separate from implementation.
- `orchestrator-improvement` exists to explore improvement opportunities and persist backlog candidates, not to implement them.

## Stage Map

| Stage | Artifact | Edit | Bash | Responsibility |
| --- | --- | --- | --- | --- |
| Entrypoint | `opencode.json` | n/a | n/a | Selects `orchestrator` as the default primary agent. |
| Orchestration | `.opencode/agents/orchestrator.md` | no | no | Routes guarded delivery or improvement discovery stages without doing specialist stage work directly. |
| Planning | `.opencode/agents/orchestrator-planner.md` | no | no | Normalizes the request, recommends the workflow branch, and sets initial flags without repository inspection. |
| Discovery | `.opencode/agents/orchestrator-discovery.md` | no | no | Performs the broad pre-implementation repository search and returns the compact context bundle. |
| Contract | `.opencode/agents/orchestrator-contract.md` | no | no | Creates the checklistable requirement contract from planner and discovery output. |
| Architecture | `.opencode/agents/orchestrator-architecture.md` | no | no | Extracts boundaries, design quality goals, and guardrails from the discovery bundle and contract, or returns `not_applicable`. |
| Lessons | `.opencode/agents/orchestrator-lessons.md` | no | no | Applies persistent mistake memory to the task. |
| Packet | `.opencode/agents/orchestrator-packet.md` | no | no | Synthesizes upstream outputs into the strict implementation packet without rediscovery. |
| Handoff | `.opencode/agents/orchestrator-handoff.md` | no | no | Turns the packet into a direct coding brief only when external or manual implementation is requested or needed as builder input. |
| Build | `.opencode/agents/orchestrator-builder.md` | yes | yes | Applies approved changes, reconciles new or changed information, removes stale or duplicate artifacts, and reports implementation evidence. |
| Verify | `.opencode/agents/orchestrator-verifier.md` | no | yes | Runs focused checks, including information hygiene and stale-reference checks when relevant, and summarizes verification evidence. |
| Review | `.opencode/agents/orchestrator-review-*.md` | no | no | Independently reviews requirements, architecture, QA, completeness, information hygiene, and lessons. |
| Gate | `.opencode/agents/orchestrator-reviewer.md` | no | no | Produces `approved`, `blocked`, or `waiver_required`. |
| Report | `.opencode/agents/orchestrator-reporter.md` | no | no | Produces the final control report. |
| Research | `.opencode/agents/orchestrator-researcher.md` | no | no | Gathers external documentation or dependency context. |
| Improvement | `.opencode/agents/orchestrator-improvement.md` | yes | no | Produces and persists backlog-ready cleanup, refactoring, pattern, module responsibility, or tuning candidates under the evolution backlog only. |

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
| `.opencode/dev_harness/workflow/known-mistakes.md` | Persistent lesson memory used by the lessons and lessons-review agents. |
| `.opencode/dev_harness/workflow/review-output.md` | Shared independent-review return protocol. |

## Trace Links

- Implements AD-001 through AD-003, ED-001, IMD-001 through IMD-002.
- Satisfies PC-001 through PC-010.
- Covers UC-001 through UC-013.
