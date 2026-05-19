# System Architecture

## Architectural Purpose

The current solution acts as a control layer around agentic development. It separates task definition, architectural grounding, lessons, implementation handoff, execution, independent review, and deterministic completion routing.

## Control Flow

This document is the canonical policy for workflow branches, boundaries, and execution ownership.

```text
guarded delivery:
  task intake
    -> OpenCode primary orchestrator
    -> planner
    -> discovery
    -> contract, architecture, lessons
    -> packet and handoff
    -> builder
    -> verifier
    -> independent reviews
    -> deterministic gate routing
    -> final control report

continuous improvement:
  improvement intake
    -> read-only discovery
    -> pressure analysis
    -> backlog-ready candidates
    -> final report

small task handoff:
  small bounded task
    -> compact build handoff
    -> OpenCode build primary agent
```

## Stable Concepts

| Concept | Responsibility |
| --- | --- |
| OpenCode config | Selects the primary agent and loads repository instructions. |
| Orchestrator | Coordinates the workflow and delegates to specialist agents. |
| Intent docs | Define the current solution's vision and use cases. |
| Product commitments | Capture durable promises that should survive implementation changes. |
| Architecture docs | Record control-flow boundaries, permissions, evidence expectations, and design quality goals. |
| Technical decisions | Explain why the current structure exists. |
| Known mistakes | Provide versioned lesson memory in `.opencode/known-mistakes.md`. |
| Implementation packet | Packages contract, guardrails, and checks for implementation. |
| Builder | Applies approved changes. |
| Verifier | Runs focused checks and summarizes evidence. |
| Review agents | Independently review requirements, architecture, QA, completeness, and lessons. |
| Completion gate | Computes approved, blocked, or waiver-required outcomes. |
| Final report | Captures the final state, decision, and remaining gaps. |
| Small task handoff | Sends small bounded tasks to OpenCode's built-in `build` primary agent instead of the full guardrail loop. |
| Improvement workflow | Separately explores refactoring, pattern, module responsibility, and tuning opportunities. |
| Improvement backlog | Stores accepted improvement candidates before they become scoped implementation tasks. |
| Reusable templates | Capture cross-project prompt and supporting templates under `.opencode/templates/`. |

## Boundaries

- Runtime source of truth lives in `.opencode/`.
- Design and traceability source of truth lives in `docs/`.
- `opencode.json` selects the primary agent and loads the workflow instructions.
- The builder agent is the only agent meant to edit files.
- Review agents are read-only.
- The workflow should remain inspectable without a hidden Python runtime.
- Persistent lesson memory lives in versioned markdown, not in ephemeral conversation state.
- Reusable templates live in versioned markdown under `.opencode/templates/` so they can be copied between projects without losing structure.
- Small-task handoff is for low-risk work where the full contract and review chain would add unnecessary overhead. The orchestrator prepares the brief, then the operator switches to OpenCode's `build` primary agent for execution.
- If a small task grows, it must escalate to the full delivery workflow before implementation starts.
- Architecture guardrails include modularity, simplicity, readability, and module responsibility fit, not only preservation of the current shape.
- Improvement discovery is separate from contained implementation. It may inspect broadly, but it must not change code.
- Improvement candidates must be traceable to current features, requirements, evidence, review findings, or observed module friction.
- Improvement candidates become implementation work only after they are accepted into the backlog and turned into a task contract.

## Completion Model

The deterministic completion gate produces `approved`, `blocked`, or `waiver_required`.

Independent reviewer nodes evaluate requirements, architecture, QA, completeness, and known mistakes. Architecture review also checks modularity, simplicity, readability, and module responsibility fit when relevant. The gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

## Workflow Split

The repository supports three related workflow branches:

- Delivery workflow: normalize a bounded task, create a contract, implement only the contracted change, verify it, review it, and gate completion.
- Small-task handoff: normalize a small bounded task, confirm it stays low-risk, and hand it to OpenCode's built-in `build` primary agent.
- Improvement workflow: explore current features, requirements, implementation evidence, reviewer findings, and module friction to produce backlog-ready improvement candidates.

The delivery workflow may report improvement candidates, but it must not absorb exploratory refactoring or pattern changes unless the contract explicitly includes them. This keeps diffs small, verification focused, and review evidence tied to the requested feature or fix.

## Trace Links

- Intent docs feed PC-001 through PC-010.
- Product commitments constrain the agent roles and permissions.
- Technical decisions justify the OpenCode-native workflow and persistent docs.
- Implementation artifacts realize the workflow in `opencode.json`, `.opencode/agents/*.md`, `.opencode/known-mistakes.md`, and `.opencode/templates/*.md`.
