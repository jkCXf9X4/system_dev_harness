# System Architecture

## Architectural Purpose

The current solution acts as a control layer around agentic development. It separates top-level planning, implementation, reviewer-coordinated verification, deterministic completion routing, and final reporting while allowing each stage to use directed helper agents.

## Control Flow

This document is the canonical policy for workflow branches, boundaries, and execution ownership.

```text
guarded delivery:
  task intake
    -> OpenCode primary orchestrator
    -> planner (request classification, uncertainty resolution, directed planning helpers)
    -> builder (implementation, directed build helpers)
    -> reviewer (verification, independent review helpers, deterministic gate routing)
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
| Known mistakes | Provide versioned lesson memory in `.opencode/dev_harness/workflow/known-mistakes.md`. |
| Planning work order | Packages contract, guardrails, checks, feedback needs, and deferred improvement candidates for implementation. |
| Handoff section | Provides an external or manual coding brief inside the planner work order only when needed. |
| Builder | Applies approved changes and may use directed helpers for build errors, scoped cleanup, documentation updates, and research. |
| Reviewer | Coordinates focused checks, independent review helpers, and the completion gate. |
| Review helpers | Independently review contract completeness, verification adequacy, architecture, code quality, cleanliness, information hygiene, and lessons. |
| Completion gate | Computes approved, blocked, or waiver-required outcomes inside the reviewer stage. |
| Final report | Captures the final state, decision, and remaining gaps. |
| Information hygiene | Reconciles new, changed, moved, and superseded information so the workflow does not leave duplicate, stale, or orphaned artifacts. |
| Improvement workflow | Separately explores cleanup, refactoring, pattern, module responsibility, and tuning opportunities, then persists backlog candidates. |
| Improvement backlog | Stores proposed or accepted improvement candidates before they become scoped implementation tasks. |
| Dev harness context | Captures cross-project prompts, workflow policy, product-breakdown guidance, and supporting templates under `.opencode/dev_harness/`. |
| Product breakdown guidance | Provides copied, load-on-demand context under `.opencode/dev_harness/product-breakdown/` so target-repo agents can structure layered artifacts without relying on source docs in the package repo. |
| Workflow policy guidance | Provides copied workflow control, information hygiene, known-mistakes memory, and review-output rules under `.opencode/dev_harness/workflow/` so agents reference shared policy instead of duplicating it. |

## Boundaries

- Runtime source of truth lives in `.opencode/`.
- Design and traceability source of truth lives in `product-breakdown/`.
- `opencode.json` selects the primary agent and loads the workflow instructions.
- Pre-implementation discovery is a directed helper owned by `orchestrator-planner`.
- The orchestrator is not a preliminary implementation or discovery layer.
- Planner classifies the request, resolves uncertainty, and decides whether to plan directly or invoke directed planning helpers using adaptive risk triggers.
- Contract, architecture, and lessons prompts are planner-owned helpers and avoid broad rediscovery unless their prompt explicitly allows focused reads.
- Test obligations, product-breakdown placement, traceability, and durable product behavior impact are planner-owned work-order sections rather than separate planning-agent handoffs.
- The builder agent and builder-owned edit helpers are the only agents meant to edit implementation files.
- Reviewer selects read-only review helpers using adaptive risk triggers; low-risk tasks may be reviewed directly with an explicit rationale.
- Every top-level stage and directed helper can request user feedback, report out-of-scope improvement candidates, and use the researcher when external source material is needed. Dependency, API, framework, standard, version, or documentation uncertainty requires researcher evidence before approval unless waived.
- The workflow should remain inspectable without a hidden Python runtime.
- Persistent lesson memory lives in versioned markdown, not in ephemeral conversation state.
- Dev harness context lives in versioned markdown under `.opencode/dev_harness/` so it can be copied between projects without losing structure.
- Product breakdown guidance lives under `.opencode/dev_harness/product-breakdown/` because target repositories receive `.opencode/` but not this package's `product-breakdown/` tree.
- Workflow policy guidance lives under `.opencode/dev_harness/workflow/` because target repositories receive `.opencode/` but not this package's `product-breakdown/` tree.
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

The reviewer stage coordinates focused verification and independent reviewer nodes for the risks present in the task: contract satisfaction, acceptance criteria, test adequacy, architecture, code quality, cleanliness, completeness, information hygiene, and known mistakes. Architecture and code-quality checks also cover modularity, simplicity, readability, and module responsibility fit when relevant. The gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items, missing cleanup evidence, or missing required researcher evidence. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

## Workflow Split

The repository supports three related workflow branches:

- Delivery workflow: normalize a bounded task, create a planner-owned work order, implement only the contracted change, review and verify it, and gate completion.
- Improvement workflow: explore current features, requirements, implementation evidence, reviewer findings, module friction, and cleanup opportunities to produce backlog-ready improvement candidates.

The delivery workflow may report improvement candidates, but it must not absorb exploratory cleanup, refactoring, or pattern changes unless the contract explicitly includes them. This keeps diffs small, verification focused, and review evidence tied to the requested feature or fix.

## Trace Links

- Intent docs feed PC-001 through PC-010.
- Product commitments constrain the agent roles and permissions.
- Technical decisions justify the OpenCode-native workflow and persistent source docs.
- Implementation artifacts realize the workflow in `opencode.json`, `.opencode/agents/*.md`, and `.opencode/dev_harness/**/*.md`.
- Product breakdown guidance supports PC-006 by giving agents copied context for layered decisions and traceability.
- Workflow policy guidance keeps repeated control, information hygiene, known-mistakes memory, and review-output rules centralized for copied agents.
