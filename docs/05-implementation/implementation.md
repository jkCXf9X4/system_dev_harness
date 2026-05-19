# Implementation

The current solution is implemented as repository-local OpenCode configuration and agent prompts.

## Implemented Artifacts

- `opencode.json` - selects the primary agent and loads the traceability docs and lessons.
- `.opencode/agents/orchestrator.md` - primary workflow coordinator.
- `.opencode/agents/orchestrator-*.md` - stage agents for planning, discovery, contract, architecture, lessons, packet, handoff, builder, verifier, review, gate, reporter, and research.
- `.opencode/known-mistakes.md` - persistent lesson memory.
- `.opencode/01-intent/vision.md` - current solution vision.
- `.opencode/01-intent/use-cases.md` - current solution use cases.
- `.opencode/02-product-commitments/product-commitments.md` - durable product commitments.
- `.opencode/03-system-architecture/architecture.md` - control-flow architecture and boundaries.
- `.opencode/04-technical-decisions/*.md` - decision records that justify the current shape.
- `.opencode/traceability.md` - end-to-end trace map.
- `README.md` - human entrypoint and layout summary.

## Execution Roles

- `orchestrator-builder` is the only edit-capable stage.
- `orchestrator-verifier` is shell-capable for focused checks.
- review agents are read-only and exist to keep approval separate from implementation.

## Trace Links

- Implements ADR-0001 through ADR-0004.
- Satisfies PC-001 through PC-007.
- Covers UC-001 through UC-010.
