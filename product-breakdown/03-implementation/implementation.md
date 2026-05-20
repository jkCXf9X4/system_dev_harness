# Implementation

The current solution is packaged as copyable OpenCode configuration and prompts. Only `opencode.json` and `.opencode/` are copied into a development repo; the `product-breakdown/` tree stays in this repository as product-breakdown source documentation and traceability.

## Implemented Artifacts

- `opencode.json` - copy into the target development repo root as the OpenCode config and entrypoint selector.
- `.opencode/agents/orchestrator.md` - primary workflow coordinator.
- `.opencode/agents/orchestrator-*.md` - stage agents for planning, discovery, contract, architecture, lessons, packet, handoff, builder, verifier, review, gate, reporter, research, and improvement discovery.
- `.opencode/known-mistakes.md` - persistent lesson memory.
- `.opencode/templates/prompts/*.md` - reusable prompt templates tied to use cases.
- `.opencode/templates/README.md` - package index for the reusable template folder.
- `.opencode/templates/product-breakdown/` - reusable product breakdown guidance split into small files for copied target-repo agents.
- `.opencode/templates/workflow/` - shared workflow control, information hygiene, and review-output policies referenced by copied agents.

## Package Documentation

- `product-breakdown/` - product-breakdown source documentation and traceability retained in this repository only.
- `README.md` - package overview and copy instructions retained in this repository only.

## Execution Roles

- `orchestrator-builder` is the only edit-capable stage.
- `orchestrator-verifier` is shell-capable for focused checks.
- review agents are read-only and exist to keep approval separate from implementation.
- `orchestrator-improvement` is read-only and exists to feed backlog candidates, not to implement them.

## Stage Map

| Stage | Artifact | Edit | Bash | Responsibility |
| --- | --- | --- | --- | --- |
| Entrypoint | `opencode.json` | n/a | n/a | Selects `orchestrator` as the default primary agent. |
| Orchestration | `.opencode/agents/orchestrator.md` | ask | ask | Chooses guarded delivery or improvement discovery and does not enable shortcut routes that omit workflow stages. |
| Planning | `.opencode/agents/orchestrator-planner.md` | no | no | Normalizes the request and recommends the workflow branch. |
| Discovery | `.opencode/agents/orchestrator-discovery.md` | no | no | Finds the smallest relevant repository context. |
| Contract | `.opencode/agents/orchestrator-contract.md` | no | no | Creates the checklistable requirement contract. |
| Architecture | `.opencode/agents/orchestrator-architecture.md` | no | no | Extracts boundaries, design quality goals, and guardrails. |
| Lessons | `.opencode/agents/orchestrator-lessons.md` | no | no | Applies persistent mistake memory to the task. |
| Packet | `.opencode/agents/orchestrator-packet.md` | no | no | Produces the strict implementation packet. |
| Handoff | `.opencode/agents/orchestrator-handoff.md` | no | no | Turns the packet into a direct coding brief only when external or manual implementation is requested. |
| Build | `.opencode/agents/orchestrator-builder.md` | yes | yes | Applies approved changes, reconciles new or changed information, removes stale or duplicate artifacts, and reports implementation evidence. |
| Verify | `.opencode/agents/orchestrator-verifier.md` | no | yes | Runs focused checks, including information hygiene and stale-reference checks when relevant, and summarizes verification evidence. |
| Review | `.opencode/agents/orchestrator-review-*.md` | no | no | Independently reviews requirements, architecture, QA, completeness, information hygiene, and lessons. |
| Gate | `.opencode/agents/orchestrator-reviewer.md` | no | no | Produces `approved`, `blocked`, or `waiver_required`. |
| Report | `.opencode/agents/orchestrator-reporter.md` | no | no | Produces the final control report. |
| Research | `.opencode/agents/orchestrator-researcher.md` | no | no | Gathers external documentation or dependency context. |
| Improvement | `.opencode/agents/orchestrator-improvement.md` | no | no | Produces backlog-ready cleanup, refactoring, pattern, module responsibility, or tuning candidates. |

## Product Breakdown Context

The product breakdown guidance is implemented as copied agent context under `.opencode/templates/product-breakdown/`.

| Artifact | Purpose |
| --- | --- |
| `.opencode/templates/product-breakdown/README.md` | Entry point, load-on-demand routing table, recommended layered tree, and layer questions. |
| `.opencode/templates/product-breakdown/layers/*.md` | One small context file per layer. |
| `.opencode/templates/product-breakdown/decision-placement.md` | Rule for placing distributed decisions near affected artifacts. |
| `.opencode/templates/product-breakdown/decision-log.md` | Guidance for maintaining the global decision index. |
| `.opencode/templates/product-breakdown/traceability.md` | Cross-layer traceability chain and checklist. |
| `.opencode/templates/product-breakdown/naming.md` | Stable ID and filename prefixes. |
| `.opencode/templates/product-breakdown/templates/decision-template.md` | Reusable decision record template. |
| `.opencode/templates/product-breakdown/templates/decision-log-entry-template.md` | Reusable compact decision-log entry template. |
| `.opencode/templates/product-breakdown/templates/improvement-backlog-overview-template.md` | Reusable overview template for improvement backlogs. |
| `.opencode/templates/product-breakdown/templates/improvement-candidate-template.md` | Reusable per-candidate improvement backlog template. |

## Workflow Policy Context

Shared workflow policies are implemented as copied agent context under `.opencode/templates/workflow/`.

| Artifact | Purpose |
| --- | --- |
| `.opencode/templates/workflow/control-policy.md` | Required stage output, `not_applicable`, handoff boundaries, control flags, and waiver rules. |
| `.opencode/templates/workflow/information-hygiene.md` | Canonical evidence requirements for changed information artifacts. |
| `.opencode/templates/workflow/review-output.md` | Shared independent-review return protocol. |

## Trace Links

- Implements AD-001 through AD-003, IMD-001 through IMD-002.
- Satisfies PC-001 through PC-010.
- Covers UC-001 through UC-013.
