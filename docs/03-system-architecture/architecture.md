# System Architecture

## Architectural Purpose

The system acts as a control layer around agentic development. It separates task definition, architectural grounding, external execution, evidence collection, independent review, and deterministic completion routing.

## Control Flow

```text
task intake
  -> typed contract state
  -> grounded architecture context
  -> known-mistake guardrails
  -> external execution handoff
  -> evidence intake
  -> independent review
  -> deterministic gate routing
  -> final control report
```

## Stable Concepts

| Concept | Responsibility |
| --- | --- |
| Task intake | Accepts a rough development task and any supplied project context. |
| Requirement contract | Converts task input into checklistable obligations, acceptance criteria, and completion rules. |
| Architecture context | Grounds the task in stable system boundaries, constraints, and integration expectations. |
| Mistake memory | Applies persistent lessons to reduce repeated correction loops. |
| Implementation handoff | Packages contract, constraints, and checks for an external coding agent. |
| Execution boundary | Keeps coding-tool mechanics outside the control workflow. |
| Evidence intake | Normalizes implementation output, test output, waivers, and session references for review. |
| Independent review | Separates requirements, architecture, QA, completeness, and mistake-review responsibilities. |
| Deterministic gate | Computes approved, blocked, or waiver-required outcomes from structured evidence and reviews. |
| Control report | Captures the final state, decision, and remaining gaps for human inspection. |

## Workflow

```text
start
  -> establish contract
  -> establish architecture context
  -> apply known-mistake guardrails
  -> prepare external implementation handoff
  -> collect implementation evidence
  -> run independent reviews
  -> compute completion outcome
  -> approve, revise, or require waiver
  -> emit control report
  -> end
```

## State Model

The graph state stores:

- original backlog item
- stakeholder context
- structured persistent known mistakes
- structured contract, architecture, packet, evidence, review, and gate artifacts
- accumulated artifact list
- final control report

Generated control artifacts are validated against typed schemas before later steps can consume them. Artifacts are also rendered for human inspection so the same state can be audited outside the running workflow.

## Model Access

Model access is isolated behind a provider boundary. Workflow logic depends on role-level model capabilities rather than direct provider calls or hard-coded model IDs.

## Grounded Context

Architecture guardrails should be grounded in versioned project documentation and explicit task context. This prevents the architecture context from depending only on the immediate task prompt.

## Execution Adapters

Execution adapters are optional integration boundaries. They prepare or run external coding-agent sessions and return evidence to the control workflow. Adapter-specific commands and session mechanics remain outside the architecture layer.

## Persistence

Workflow state should be checkpointable by thread or run identity. The initial implementation may use process-local persistence, but the architecture requires persistence concerns to remain separable from task, review, and gate logic.

## Boundaries

Current boundaries:

- no repository write access from harness-controlled agents
- no issue tracker integration
- no durable state outside process memory
- no retrieval layer over project docs
- no human interrupt/resume flow

These are deliberate first-version boundaries, not final product boundaries.

## Completion Model

The deterministic completion gate produces `approved`, `blocked`, or `waiver_required`.

Independent reviewer nodes evaluate requirements, architecture, QA, completeness, and known mistakes. The deterministic gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

External evidence can include changed files, diff summaries, test output, coding-agent final output, and JSON waiver requests.
