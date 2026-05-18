# Architecture Overview

## Current Architecture

```text
CLI input
  -> LangGraph StateGraph
  -> typed contract and evidence state
  -> OpenRouter-backed chat models
  -> deterministic validation and gate routing
  -> final control report
```

## Components

| Component | Responsibility |
| --- | --- |
| `devfix/cli.py` | CLI entrypoint, reads prompt input, gathers default/project context, reads evidence, invokes graph with a thread ID. |
| `devfix/runner.py` | Shared runner utilities for context loading, evidence loading, execution adapters, and graph invocation. |
| `devfix/harness/graph.py` | Defines the contract-driven LangGraph workflow nodes and edges. |
| `devfix/harness/state.py` | Defines graph state channels and artifact accumulation. |
| `devfix/harness/models.py` | Isolates OpenRouter/OpenAI-compatible model configuration. |
| `devfix/harness/prompts.py` | Stores inspectable role prompts. |
| `devfix/harness/execution/` | Contains execution adapter abstractions and implementations for manual and opencode flows. |
| `examples/` | Holds runnable sample backlog inputs. |
| `docs/` | Captures vision, requirements, use cases, traceability, and decisions. |

## Workflow

```text
START
  -> requirement_contract
  -> architecture_context
  -> known_mistake_check
  -> implementation_packet
  -> external_agent_handoff
  -> evidence_intake
  -> requirements_review
  -> architecture_review
  -> qa_review
  -> completeness_review
  -> known_mistake_review
  -> completion_gate
  -> approved: final_control_report
  -> blocked: revise_packet -> final_control_report
  -> waiver_required: human_interrupt -> final_control_report
  -> END
```

## State Model

The graph state stores:

- original backlog item
- stakeholder context
- structured persistent known mistakes
- structured contract, architecture, packet, evidence, review, and gate artifacts
- accumulated artifact list
- final control report

LLM outputs are validated with Pydantic schemas before later nodes can consume them. Artifacts are also rendered as JSON-in-markdown so humans can inspect the same state the graph uses.

## Model Access

The model adapter uses OpenRouter through an OpenAI-compatible client. Model IDs are configured through environment variables:

- `PLANNER_MODEL`
- `REVIEWER_MODEL`
- `FAST_MODEL`

This keeps workflow logic independent from the exact model catalog.

## Grounded Context

The CLI automatically adds repo documentation context from:

- `docs/architecture.md`
- `docs/requirements.md`
- ADRs under `docs/decisions/`

Additional files can be supplied with `--context-file`. This keeps architecture guardrails grounded in versioned project documentation instead of only the task prompt.

## Execution Adapters

Execution adapters are optional. With `--executor none`, the graph runs as a pure control/review pipeline over manually supplied evidence. With `--executor manual` or `--executor opencode`, the harness first generates a handoff packet, executes or prepares an external coding-agent session, then feeds adapter evidence into the review graph.

The current adapters are:

- manual: returns paste instructions and no implementation evidence
- opencode: runs `opencode run --format json` and captures raw output as evidence

## Persistence

The current graph uses LangGraph `InMemorySaver`.

This supports checkpointed execution during a process lifetime and requires a `thread_id`. It does not survive process restarts.

Future durable options:

- SQLite for local development
- Postgres for team/server usage
- Redis for high-throughput or ephemeral workflow state
- LangGraph Platform if deployment moves there

## Boundaries

Current boundaries:

- no repository write access from devfix harness agents
- no issue tracker integration
- no durable state outside process memory
- no retrieval layer over project docs
- no human interrupt/resume flow

These are deliberate first-version boundaries, not final product boundaries.

## Completion Model

The deterministic completion gate produces `approved`, `blocked`, or `waiver_required`.

Independent reviewer nodes evaluate requirements, architecture, QA, completeness, and known mistakes. The deterministic gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

External evidence can include changed files, diff summaries, test output, coding-agent final output, and JSON waiver requests.
