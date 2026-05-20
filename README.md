# OpenCode Workflow Package

This repository contains a portable OpenCode workflow package plus the source documentation that explains how it works.

The active payload is `opencode.json` plus `.opencode/`. The entrypoint is the `orchestrator` primary agent in `.opencode/agents/orchestrator.md`. It delegates to hidden subagents for planning, discovery, contract writing, architecture guardrails, lessons checks, implementation packaging, implementation, verification, independent reviews, completion gating, final reporting, and continuous-improvement discovery for cleanup, refactoring, and tuning candidates. OpenCode's built-in `build` primary agent remains available for direct operator use, but the orchestrator does not route to it as a shortcut path.

The guarded workflow treats new or changed information as part of the deliverable. Agents are expected to reconcile stale references, duplicates, superseded artifacts, and orphaned information nodes before completion.

## Quick Start

1. Clone or open this repository.
2. Make sure `opencode` is available on your `PATH`.
3. Make sure you can run `pytest` locally.
4. Run the probe suite from the repository root:

```bash
pytest -q tests/test_opencode_workflow_probes.py
```

## How This Repo Is Organized

- `opencode.json` - OpenCode config that selects the default primary agent.
- `.opencode/` - workflow payload copied into the target development repo.
- `product-breakdown/` - source documentation and traceability for the workflow package.
- `tests/` - smoke tests and test guidance for the copied workflow payload.

## Active Payload

- `opencode.json` - selects the primary agent and workflow instructions.
- `.opencode/agents/` - orchestrator and specialist agent prompts.
- `.opencode/known-mistakes.md` - persistent lesson memory.
- `.opencode/templates/prompts/` - reusable prompt templates tied to the use cases.
- `.opencode/templates/product-breakdown/` - copied, load-on-demand guidance for layered product breakdown artifacts, decisions, and traceability.
- `.opencode/templates/workflow/` - copied workflow control, information hygiene, and review-output policies referenced by agents.

## Where To Change Things

| Concern | Change Here |
| --- | --- |
| Package usage and contributor guidance | `README.md` |
| Runtime agent behavior copied into projects | `.opencode/agents/` |
| Reusable cross-project prompts and supporting templates | `.opencode/templates/` |
| Persistent repeated-failure checks | `.opencode/known-mistakes.md` |
| Product intent, commitments, architecture, decisions, and traceability | `product-breakdown/` |
| Canonical workflow policy and branch rules | `product-breakdown/02-architecture/architecture.md` |
| Concrete artifact-to-stage mapping | `product-breakdown/03-implementation/implementation.md` |
| Smoke tests and prompt-probe guidance | `tests/README.md` |

## Delivery Workflow

1. `orchestrator-planner` turns the request into a concrete task and work order.
2. `orchestrator-discovery` finds the smallest relevant file set.
3. `orchestrator-contract`, `orchestrator-architecture`, and `orchestrator-lessons` establish the guardrails.
4. `orchestrator-packet` prepares the implementation brief; `orchestrator-handoff` adds an external/manual handoff only when needed.
5. `orchestrator-builder` makes the changes.
6. `orchestrator-verifier` runs focused checks and captures evidence.
7. `orchestrator-review-*` agents review the evidence independently.
8. `orchestrator-reviewer` acts as the deterministic completion gate.
9. `orchestrator-reporter` produces the final control report.

## Improvement Workflow

For exploratory cleanup, refactoring, pattern switch, module responsibility, tuning, or backlog-feeding requests, the orchestrator routes to `orchestrator-improvement`.

That workflow is read-only. It produces backlog-ready candidates rather than changing code, so contained feature diffs stay small and verifiable. Use it for exploratory cleanup, refactoring, pattern switches, module responsibility shifts, and tuning.

## Developing This Repo

When you change the workflow package, keep the source docs and the copied runtime payload in sync:

- Update `product-breakdown/` when the intent, workflow model, decisions, traceability, or implementation mapping changes.
- Update `.opencode/` when the runtime prompts, control policy, or agent behavior changes.
- Keep references in agents pointed at the canonical files rather than duplicating policy text.
- Use the tests to confirm that the prompts still reference the intended source files and that stale paths do not reappear.

To use the package in another repository, copy only `opencode.json` and `.opencode/` into the target repo root.

Do not copy `product-breakdown/` or this README. They stay in this repository as source documentation.

Then run OpenCode from the target repository root:

```bash
opencode
```

For a one-shot run:

```bash
opencode run "your task"
```

Add new agents by creating additional markdown files under `.opencode/agents/` in the package, then copy the updated payload into the development repo.

## Testing

Run the smoke tests from the repository root:

```bash
pytest -q tests/test_opencode_workflow_probes.py
```

The suite copies `tests/fixtures/simple_project/` into a temp worktree, overlays `opencode.json` and `.opencode/`, and checks three `opencode run` probes:

- contract stage
- build stage
- improvement discovery

If you are changing prompts or template references, also read `tests/README.md` before adding exact string assertions.
