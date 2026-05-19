# Implementation

The current solution is packaged as copyable OpenCode configuration and prompts. Only `opencode.json` and `.opencode/` are copied into a development repo; the `docs/` tree stays in this repository as package documentation and source references.

## Implemented Artifacts

- `opencode.json` - copy into the target development repo root as the OpenCode config and entrypoint selector.
- `.opencode/agents/orchestrator.md` - primary workflow coordinator.
- `.opencode/agents/orchestrator-*.md` - stage agents for planning, discovery, contract, architecture, lessons, packet, handoff, builder, verifier, review, gate, reporter, research, and improvement discovery.
- `.opencode/known-mistakes.md` - persistent lesson memory.
- `.opencode/templates/prompts/*.md` - reusable prompt templates tied to use cases.
- `.opencode/templates/README.md` - package index for the reusable template folder.
- `.opencode/templates/others/improvement-backlog-template.md` - reusable backlog template for accepted improvement candidates.

## Package Documentation

- `docs/` - package documentation and source references retained in this repository only.
- `README.md` - package overview and copy instructions retained in this repository only.

## Execution Roles

- `orchestrator-builder` is the only edit-capable stage.
- `orchestrator-verifier` is shell-capable for focused checks.
- review agents are read-only and exist to keep approval separate from implementation.
- Small bounded tasks are handed off to OpenCode's built-in `build` primary agent instead of a package-specific shortcut agent.
- `orchestrator-improvement` is read-only and exists to feed backlog candidates, not to implement them.

## Stage Map

| Stage | Artifact | Edit | Bash | Responsibility |
| --- | --- | --- | --- | --- |
| Entrypoint | `opencode.json` | n/a | n/a | Selects `orchestrator` as the default primary agent. |
| Orchestration | `.opencode/agents/orchestrator.md` | ask | ask | Chooses guarded delivery, improvement discovery, or small-task handoff. |
| Planning | `.opencode/agents/orchestrator-planner.md` | no | no | Normalizes the request and recommends the workflow branch. |
| Discovery | `.opencode/agents/orchestrator-discovery.md` | no | no | Finds the smallest relevant repository context. |
| Contract | `.opencode/agents/orchestrator-contract.md` | no | no | Creates the checklistable requirement contract. |
| Architecture | `.opencode/agents/orchestrator-architecture.md` | no | no | Extracts boundaries, design quality goals, and guardrails. |
| Lessons | `.opencode/agents/orchestrator-lessons.md` | no | no | Applies persistent mistake memory to the task. |
| Packet | `.opencode/agents/orchestrator-packet.md` | no | no | Produces the strict implementation packet. |
| Handoff | `.opencode/agents/orchestrator-handoff.md` | no | no | Turns the packet into a direct coding brief. |
| Build | `.opencode/agents/orchestrator-builder.md` | yes | yes | Applies approved changes, performs cleanup for moved or altered information, and reports implementation evidence. |
| Verify | `.opencode/agents/orchestrator-verifier.md` | no | yes | Runs focused checks, including stale-reference cleanup checks when relevant, and summarizes verification evidence. |
| Review | `.opencode/agents/orchestrator-review-*.md` | no | no | Independently reviews requirements, architecture, QA, completeness, and lessons. |
| Gate | `.opencode/agents/orchestrator-reviewer.md` | no | no | Produces `approved`, `blocked`, or `waiver_required`. |
| Report | `.opencode/agents/orchestrator-reporter.md` | no | no | Produces the final control report. |
| Research | `.opencode/agents/orchestrator-researcher.md` | no | no | Gathers external documentation or dependency context. |
| Improvement | `.opencode/agents/orchestrator-improvement.md` | no | no | Produces backlog-ready cleanup, refactoring, pattern, module responsibility, or tuning candidates. |
| Small tasks | OpenCode built-in `build` primary agent | yes | yes | Executes compact handoffs for small low-risk tasks. |

## Trace Links

- Implements ADR-0001 through ADR-0004.
- Satisfies PC-001 through PC-010.
- Covers UC-001 through UC-013.
