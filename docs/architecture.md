# Architecture Overview

## Current Architecture

```text
CLI input
  -> LangGraph StateGraph
  -> contract-driven role nodes
  -> OpenRouter-backed chat models
  -> markdown artifacts in graph state
  -> final control report
```

## Components

| Component | Responsibility |
| --- | --- |
| `app.py` | CLI entrypoint, reads backlog input, invokes graph with a thread ID. |
| `harness/graph.py` | Defines the contract-driven LangGraph workflow nodes and edges. |
| `harness/state.py` | Defines graph state channels and artifact accumulation. |
| `harness/models.py` | Isolates OpenRouter/OpenAI-compatible model configuration. |
| `harness/prompts.py` | Stores inspectable role prompts. |
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
  -> reviewer_council
  -> completion_decision
  -> final_control_report
  -> END
```

## State Model

The graph state stores:

- original backlog item
- stakeholder context
- persistent known mistakes
- per-role control artifacts
- accumulated artifact list
- final control report

Artifacts are accumulated with a reducer so every node can append its output without replacing earlier artifacts.

## Model Access

The model adapter uses OpenRouter through an OpenAI-compatible client. Model IDs are configured through environment variables:

- `PLANNER_MODEL`
- `REVIEWER_MODEL`
- `FAST_MODEL`

This keeps workflow logic independent from the exact model catalog.

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

- no repository write access from harness agents
- no issue tracker integration
- no durable state outside process memory
- no retrieval layer over project docs
- no human interrupt/resume flow

These are deliberate first-version boundaries, not final product boundaries.

## Completion Model

The harness produces `approved`, `blocked`, or `waiver_required`.

Reviewer approval is required, but it cannot silently override missing contract items. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.
