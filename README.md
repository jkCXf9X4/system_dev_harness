# OpenCode Workspace

This repository is now an OpenCode workspace scaffold that recreates the guarded workflow without the Python orchestration stack.

The entrypoint is the `orchestrator` primary agent in `.opencode/agents/orchestrator.md`. It delegates to hidden subagents for planning, discovery, contract writing, architecture guardrails, lessons checks, implementation packaging, implementation, verification, independent reviews, completion gating, final reporting, and continuous-improvement discovery.

## Layout

- `opencode.json` - project-level OpenCode config
- `.opencode/agents/` - orchestrator and specialist agent prompts
- `.opencode/known-mistakes.md` - persistent lesson memory
- `.opencode/templates/prompts/` - reusable prompt templates tied to the use cases
- `.opencode/templates/others/` - reusable supporting templates such as the improvement backlog template

## Delivery Workflow

1. `orchestrator-planner` turns the request into a concrete task and work order.
2. `orchestrator-discovery` finds the smallest relevant file set.
3. `orchestrator-contract`, `orchestrator-architecture`, and `orchestrator-lessons` establish the guardrails.
4. `orchestrator-packet` and `orchestrator-handoff` prepare the implementation brief.
5. `orchestrator-builder` makes the changes.
6. `orchestrator-verifier` runs focused checks and captures evidence.
7. `orchestrator-review-*` agents review the evidence independently.
8. `orchestrator-reviewer` acts as the deterministic completion gate.
9. `orchestrator-reporter` produces the final control report.

## Improvement Workflow

For exploratory refactoring, pattern switch, module responsibility, tuning, or backlog-feeding requests, the orchestrator routes to `orchestrator-improvement`.

That workflow is read-only. It produces backlog-ready candidates rather than changing code, so contained feature diffs stay small and verifiable.

## Usage

Install OpenCode, then run it from the repository root:

```bash
opencode
```

For a one-shot run:

```bash
opencode run "your task"
```

Add new agents by creating additional markdown files under `.opencode/agents/`.
