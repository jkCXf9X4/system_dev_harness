# System Architecture

## Architectural Purpose

The current solution acts as a control layer around agentic development. It separates task definition, architectural grounding, lessons, implementation handoff, execution, independent review, and deterministic completion routing.

## Control Flow

```text
task intake
  -> OpenCode primary orchestrator
  -> specialist agents
  -> implementation evidence
  -> independent review
  -> deterministic gate routing
  -> final control report
```

## Stable Concepts

| Concept | Responsibility |
| --- | --- |
| OpenCode config | Selects the primary agent and loads repository instructions. |
| Orchestrator | Coordinates the workflow and delegates to specialist agents. |
| Intent docs | Define the current solution's vision and use cases. |
| Product commitments | Capture durable promises that should survive implementation changes. |
| Architecture docs | Record control-flow boundaries, permissions, and evidence expectations. |
| Technical decisions | Explain why the current structure exists. |
| Known mistakes | Provide versioned lesson memory in `.opencode/known-mistakes.md`. |
| Implementation packet | Packages contract, guardrails, and checks for implementation. |
| Builder | Applies approved changes. |
| Verifier | Runs focused checks and summarizes evidence. |
| Review agents | Independently review requirements, architecture, QA, completeness, and lessons. |
| Completion gate | Computes approved, blocked, or waiver-required outcomes. |
| Final report | Captures the final state, decision, and remaining gaps. |

## Boundaries

- The source of truth lives in `.opencode/`.
- `opencode.json` loads the traceability docs and persistent lessons.
- The builder agent is the only agent meant to edit files.
- Review agents are read-only.
- The workflow should remain inspectable without a hidden Python runtime.
- Persistent lesson memory lives in versioned markdown, not in ephemeral conversation state.

## Completion Model

The deterministic completion gate produces `approved`, `blocked`, or `waiver_required`.

Independent reviewer nodes evaluate requirements, architecture, QA, completeness, and known mistakes. The gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

## Trace Links

- Intent docs feed PC-001 through PC-007.
- Product commitments constrain the agent roles and permissions.
- Technical decisions justify the OpenCode-native workflow and persistent docs.
- Implementation artifacts realize the workflow in `opencode.json` and `.opencode/agents/*.md`.
