# Implementation Notes

This artifact records current build details and operational behavior. It is intentionally lower in the documentation chain than vision, product commitments, architecture, and technical decisions.

Implementation details should trace backward to requirements, decisions, and architecture boundaries instead of redefining product intent.

## Traceability

| Implementation Area | Satisfies | Decision | Architecture Boundary |
| --- | --- | --- | --- |
| CLI entrypoint and runner | FR-001, FR-012, FR-020 | ADR-0001 | Task intake, grounded context |
| Graph workflow modules | FR-002, FR-003, FR-004, FR-005, FR-008, FR-013, FR-014, FR-015, FR-018, FR-019 | ADR-0001 | Typed state, independent review, deterministic gate |
| Model access module | FR-009, QR-003 | ADR-0002 | Provider boundary |
| Execution adapter modules | FR-006, FR-007, FR-017, FR-021, FR-022, FR-023 | ADR-0003 | Execution boundary, evidence intake |
| Known-mistake parser and lesson files | FR-005, FR-016, C-006 | ADR-0004 | Mistake memory |

## Current Package Map

| Path | Responsibility |
| --- | --- |
| `devfix/cli.py` | CLI entrypoint, prompt loading, argument parsing, environment setup, and graph invocation. |
| `devfix/runner.py` | Shared runner utilities for context loading, evidence loading, execution adapters, and graph invocation. |
| `devfix/harness/graph.py` | Contract-driven workflow nodes, conditional routing, validation, and graph builders. |
| `devfix/harness/state.py` | Graph state channels and artifact accumulation. |
| `devfix/harness/schemas.py` | Structured contracts, evidence, review, waiver, and completion schemas. |
| `devfix/harness/models.py` | OpenAI-compatible model client configuration. |
| `devfix/harness/prompts.py` | Inspectable role prompts used by workflow nodes. |
| `devfix/harness/rendering.py` | Human-readable artifact rendering. |
| `devfix/harness/lessons.py` | Known-mistake markdown and YAML parsing. |
| `devfix/harness/execution/` | Execution adapter abstractions and implementations. |

## Runtime Configuration

The current implementation reads model and provider configuration from environment variables:

- `OPENROUTER_API_KEY`
- `OPENROUTER_BASE_URL`
- `PLANNER_MODEL`
- `REVIEWER_MODEL`
- `FAST_MODEL`

The default CLI command reads `.agents/devfix/PROMPT.md` when no prompt path is supplied and uses `.agents/devfix/` for local storage.

## Execution Adapters

Current adapters:

- manual: returns paste instructions and no implementation evidence.
- opencode: runs `opencode run --format json` and captures raw output as evidence.

Adapter evidence is fed back into the review graph before the deterministic completion gate runs.
