# OpenCode Workflow Package

This repository is a portable OpenCode workflow package. Its active payload is meant to be copied into a development repo so the target repo can run the guarded workflow without a separate orchestration runtime.

The active payload is `opencode.json` plus `.opencode/`. The entrypoint is the `orchestrator` primary agent in `.opencode/agents/orchestrator.md`. It delegates to hidden subagents for planning, discovery, contract writing, architecture guardrails, lessons checks, implementation packaging, implementation, verification, independent reviews, completion gating, final reporting, and continuous-improvement discovery for cleanup, refactoring, and tuning candidates. Small tasks that do not need the guarded chain are handed off to OpenCode's built-in `build` primary agent.

## Layout

- `opencode.json` - copy this into the target development repo root as the OpenCode config
- `.opencode/` - copy this directory into the target development repo root as the workflow payload
- `docs/` - package documentation and source references retained in this repository only
- `.opencode/templates/README.md` - index for the reusable template payload

## Active Payload

- `opencode.json` - selects the primary agent and workflow instructions.
- `.opencode/agents/` - orchestrator and specialist agent prompts.
- `.opencode/known-mistakes.md` - persistent lesson memory.
- `.opencode/templates/prompts/` - reusable prompt templates tied to the use cases.
- `.opencode/templates/others/` - reusable supporting templates such as the improvement backlog template.

## Where To Change Things

| Concern | Change Here |
| --- | --- |
| Package install and copy instructions | `README.md` |
| Runtime agent behavior copied into projects | `.opencode/agents/` |
| Reusable cross-project prompts and supporting templates | `.opencode/templates/` |
| Persistent repeated-failure checks | `.opencode/known-mistakes.md` |
| Product intent, commitments, architecture, and decisions | `docs/` |
| Canonical workflow policy and branch rules | `docs/03-system-architecture/architecture.md` |
| Concrete artifact-to-stage mapping | `docs/05-implementation/implementation.md` |

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

For exploratory cleanup, refactoring, pattern switch, module responsibility, tuning, or backlog-feeding requests, the orchestrator routes to `orchestrator-improvement`.

That workflow is read-only. It produces backlog-ready candidates rather than changing code, so contained feature diffs stay small and verifiable. Use it for exploratory cleanup, refactoring, pattern switches, module responsibility shifts, and tuning.

## Small Task Handoff

For small, low-risk tasks, the orchestrator prepares a compact handoff for OpenCode's built-in `build` primary agent.

That path skips the full contract and architecture chain. The operator switches to `build` to execute the handoff. If the task grows or the risk changes, it escalates back to the delivery workflow before implementation starts.

## Usage

Copy only `opencode.json` and `.opencode/` into the development repo that should use the workflow package.

Do not copy `docs/` or this README. They stay in the package repo as source documentation.

Then run OpenCode from that development repo root:

```bash
opencode
```

For a one-shot run:

```bash
opencode run "your task"
```

Add new agents by creating additional markdown files under `.opencode/agents/` in the package, then copy the updated payload into the development repo.

## Verification Tests

To smoke-test the workflow routing locally, run:

```bash
pytest -q tests/test_opencode_workflow_probes.py
```

The pytest suite copies `tests/fixtures/simple_project/` into a temp worktree, overlays the workflow package payload, and checks three `opencode run` probes:

- contract stage
- build stage
- improvement discovery
