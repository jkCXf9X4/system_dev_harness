# System Architecture

## Architectural Purpose

The current solution acts as a control layer around agentic development. It separates task definition, architectural grounding, lessons, implementation packaging, optional external handoff, execution, independent review, and deterministic completion routing.

## Control Flow

This document is the canonical policy for workflow branches, boundaries, and execution ownership.

```text
guarded delivery:
  task intake
    -> OpenCode primary orchestrator
    -> planner (request classification)
    -> discovery (broad repository search and context bundle)
    -> contract, architecture, lessons (upstream context consumers)
    -> packet (implementation synthesis)
    -> optional handoff when external or manual implementation is requested
    -> builder
    -> verifier
    -> independent reviews
    -> deterministic gate routing
    -> final control report

  continuous improvement:
  improvement intake
    -> read-only discovery
    -> pressure analysis
    -> cleanup, refactoring, and other backlog-ready candidates
    -> persist candidate files under product-breakdown/06-evolution/backlog/
    -> final report
```

## Stable Concepts

| Concept | Responsibility |
| --- | --- |
| OpenCode config | Selects the primary agent and loads repository instructions. |
| Orchestrator | Routes stage execution, passes prior outputs forward, and applies gate routing without doing specialist stage work directly. |
| Intent docs | Define the current solution's vision and use cases. |
| Product commitments | Capture durable promises that should survive implementation changes. |
| Architecture docs | Record control-flow boundaries, permissions, evidence expectations, and design quality goals. |
| Technical decisions | Explain why the current structure exists. |
| Known mistakes | Provide versioned lesson memory in `.opencode/known-mistakes.md`. |
| Implementation packet | Packages contract, guardrails, and checks for implementation. |
| Handoff | Provides an external or manual coding brief only when needed. |
| Builder | Applies approved changes. |
| Verifier | Runs focused checks and summarizes evidence. |
| Review agents | Independently review requirements, architecture, QA, completeness, and lessons. |
| Completion gate | Computes approved, blocked, or waiver-required outcomes. |
| Final report | Captures the final state, decision, and remaining gaps. |
| Information hygiene | Reconciles new, changed, moved, and superseded information so the workflow does not leave duplicate, stale, or orphaned artifacts. |
| Improvement workflow | Separately explores cleanup, refactoring, pattern, module responsibility, and tuning opportunities, then persists backlog candidates. |
| Improvement backlog | Stores proposed or accepted improvement candidates before they become scoped implementation tasks. |
| Reusable templates | Capture cross-project prompt and supporting templates under `.opencode/templates/`. |
| Product breakdown guidance | Provides copied, load-on-demand context under `.opencode/templates/product-breakdown/` so target-repo agents can structure layered artifacts without relying on source docs in the package repo. |
| Workflow policy guidance | Provides copied workflow control, information hygiene, and review-output rules under `.opencode/templates/workflow/` so agents reference shared policy instead of duplicating it. |

## Boundaries

- Runtime source of truth lives in `.opencode/`.
- Design and traceability source of truth lives in `product-breakdown/`.
- `opencode.json` selects the primary agent and loads the workflow instructions.
- Pre-implementation discovery has a single owner: `orchestrator-discovery`.
- The orchestrator is not a preliminary implementation or discovery layer.
- Planner classifies the request without repository inspection.
- Contract, architecture, packet, and handoff consume upstream context and avoid broad rediscovery.
- The builder agent is the only agent meant to edit files.
- Review agents are read-only.
- The workflow should remain inspectable without a hidden Python runtime.
- Persistent lesson memory lives in versioned markdown, not in ephemeral conversation state.
- Reusable templates live in versioned markdown under `.opencode/templates/` so they can be copied between projects without losing structure.
- Product breakdown guidance lives under `.opencode/templates/product-breakdown/` because target repositories receive `.opencode/` but not this package's `product-breakdown/` tree.
- Workflow policy guidance lives under `.opencode/templates/workflow/` because target repositories receive `.opencode/` but not this package's `product-breakdown/` tree.
- Every artifact touched by the workflow should have a visible place in the information chain, with no orphaned node left behind after a creation, move, rename, rewrite, or replacement.
- New information must either update an existing artifact, replace a superseded artifact, or declare a clear parent context and downstream destination.
- Completion evidence must cover stale-reference cleanup, duplicate-content reconciliation, and traceability for changed information artifacts.
- Architecture guardrails include modularity, simplicity, readability, and module responsibility fit, not only preservation of the current shape.
- Improvement discovery is separate from contained implementation. It may inspect broadly, but it must not change code.
- Improvement discovery may write only improvement backlog files under `product-breakdown/06-evolution/backlog/`.
- Improvement candidates must be traceable to current features, requirements, evidence, review findings, or observed module friction.
- Improvement candidates must not be created as dangling artifacts; each one needs an explicit parent context and follow-up destination.
- Improvement candidates become implementation work only after they are accepted into the backlog and turned into a task contract.

## Completion Model

The deterministic completion gate produces `approved`, `blocked`, or `waiver_required`.

Independent reviewer nodes evaluate requirements, architecture, QA, completeness, information hygiene, and known mistakes. Architecture review also checks modularity, simplicity, readability, and module responsibility fit when relevant. The gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items or missing cleanup evidence. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

## Workflow Split

The repository supports three related workflow branches:

- Delivery workflow: normalize a bounded task, create a contract, implement only the contracted change, verify it, review it, and gate completion.
- Improvement workflow: explore current features, requirements, implementation evidence, reviewer findings, module friction, and cleanup opportunities to produce backlog-ready improvement candidates.

The delivery workflow may report improvement candidates, but it must not absorb exploratory cleanup, refactoring, or pattern changes unless the contract explicitly includes them. This keeps diffs small, verification focused, and review evidence tied to the requested feature or fix.

## Trace Links

- Intent docs feed PC-001 through PC-010.
- Product commitments constrain the agent roles and permissions.
- Technical decisions justify the OpenCode-native workflow and persistent source docs.
- Implementation artifacts realize the workflow in `opencode.json`, `.opencode/agents/*.md`, `.opencode/known-mistakes.md`, and `.opencode/templates/*.md`.
- Product breakdown guidance supports PC-006 by giving agents copied context for layered decisions and traceability.
- Workflow policy guidance keeps repeated control, information hygiene, and review-output rules centralized for copied agents.
