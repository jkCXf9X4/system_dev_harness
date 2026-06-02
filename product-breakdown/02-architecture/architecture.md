# System Architecture

## Architectural Purpose

The current solution acts as a control layer around agentic development. It separates top-level planning, implementation, reviewer-coordinated verification, deterministic completion routing, final reflection, and final reporting while allowing each stage to use directed helper agents.

## Control Flow

This document is the canonical policy for workflow branches, boundaries, and execution ownership.

```text
guarded delivery:
  task intake
    -> OpenCode primary orchestrator (routing only)
    -> planner (request classification, uncertainty resolution, directed planning helpers)
    -> builder (implementation, directed build helpers)
    -> reviewer (verification, independent review helpers, deterministic gate routing)
    -> reflection (memory incorporation triage)
    -> final control report

  continuous improvement:
  improvement intake
    -> read-only discovery
    -> pressure analysis
    -> cleanup, refactoring, and other backlog-ready candidates
    -> persist candidate files under product-breakdown/06-evolution/candidates/
    -> reflection (memory incorporation triage)
    -> final report
```

## Stable Concepts

| Concept | Responsibility |
| --- | --- |
| OpenCode config | Selects the primary agent and loads repository instructions. |
| Orchestrator | Routes stage execution, passes prior outputs forward, and applies gate routing without repository inspection, request classification, or specialist stage work. |
| Intent docs | Define the current solution's vision and use cases. |
| Product commitments | Capture durable promises that should survive implementation changes. |
| Architecture docs | Record control-flow boundaries, permissions, evidence expectations, and design quality goals. |
| Technical decisions | Explain why the current structure exists. |
| Workflow memory | Provide versioned lessons, reusable patterns, decision pointers, and trust metadata under `.opencode/dev_harness_memories/`. |
| Planning work order | Packages contract, guardrails, checks, feedback needs, parallel-safe helper packet evidence, and deferred improvement candidates for implementation. |
| Handoff section | Provides an external or manual coding brief inside the planner work order only when needed. |
| Builder | Applies approved changes and may use directed helpers for build errors, scoped cleanup, documentation updates, information hygiene, and research. |
| Cleanup helper | Performs builder-owned cleanup passes for references, trackers, duplicate or superseded content, orphaned artifacts, links, and traceability inside the approved scope. |
| Reviewer | Coordinates focused checks, independent review helpers, parallel-safe review packets, and the completion gate. |
| Review helpers | Independently review contract completeness, verification adequacy, architecture, code quality, cleanliness, information hygiene, and lessons. |
| Completion gate | Computes approved, blocked, or waiver-required outcomes inside the reviewer stage. |
| Reflection | Reviews the completed run and owns final durable-memory incorporation triage before reporting. |
| Final report | Captures the final state, decision, and remaining gaps. |
| Information hygiene | Reconciles new, changed, moved, and superseded information so the workflow does not leave duplicate, stale, or orphaned artifacts. |
| Improvement workflow | Separately explores cleanup, refactoring, pattern, module responsibility, and tuning opportunities, then persists backlog candidates. |
| Focused improvement evaluator | Evaluates one noteworthy finding raised during normal work and persists it only when evidence, impact, and a scoped future task seed are present. |
| Memory helper | Retrieves task-relevant workflow memory without editing it. |
| Memory curator | Evaluates evidenced repeatable findings and persists only durable workflow memory when invoked by reflection or the focused improvement evaluator. |
| Improvement backlog | Stores proposed or accepted improvement candidates before they become scoped implementation tasks. |
| Dev harness context | Captures cross-project prompts, workflow policy, product-breakdown guidance, and supporting templates under `.opencode/dev_harness/`. |
| Product breakdown guidance | Provides copied, load-on-demand context under `.opencode/dev_harness/product-breakdown/` so target-repo agents can structure layered artifacts without relying on source docs in the package repo. |
| Workflow policy guidance | Provides copied workflow control, information hygiene, and review-output rules under `.opencode/dev_harness/workflow/` so agents reference shared policy instead of duplicating it. |

## Boundaries

- Runtime source of truth lives in `.opencode/`.
- Design and traceability source of truth lives in `product-breakdown/`.
- `opencode.json` selects the primary agent and loads the workflow instructions.
- Pre-implementation discovery is a directed helper owned by `orchestrator-planner`.
- The orchestrator is not a preliminary implementation, discovery, classification, planning, or evaluation layer.
- The primary orchestrator has no file read, search, list, edit, or shell permissions; it may invoke only top-level planner, builder, reviewer, reflection, reporter, and improvement entrypoint agents.
- Planner classifies the request, resolves uncertainty, and decides whether to plan directly or invoke directed planning helpers using adaptive risk triggers. Independent planner helpers should be grouped into parallel-safe packets when their inputs are available and their outputs do not depend on each other.
- Contract, architecture, and lessons prompts are planner-owned helpers and avoid broad rediscovery unless their prompt explicitly allows focused reads.
- Test obligations, product-breakdown placement, traceability, and durable product behavior impact are planner-owned work-order sections rather than separate planning-agent handoffs.
- The builder agent and builder-owned edit helpers are the only agents meant to edit implementation files.
- `orchestrator-cleanup` is a builder-owned edit helper for cleanup caused by the approved change; it may patch references, update status trackers and indexes, reconcile duplicates or superseded content, remove orphaned artifacts, and report cleanup evidence without expanding scope.
- Reviewer selects read-only review helpers using adaptive risk triggers; independent review helpers should be grouped into parallel-safe packets after builder evidence is available. Low-risk tasks may be reviewed directly with an explicit rationale.
- Every top-level stage and directed helper can request user feedback, report out-of-scope improvement candidates, and use the researcher when external source material is needed. Dependency, API, framework, standard, version, or documentation uncertainty requires researcher evidence before approval unless waived.
- The workflow should remain inspectable without a hidden Python runtime.
- Persistent lesson memory lives in versioned markdown, not in ephemeral conversation state.
- Workflow memory is versioned markdown under `.opencode/dev_harness_memories/`; it captures durable lessons, reusable patterns, and decision pointers with trust metadata, not current task state, backlog candidates, or broad run history.
- `orchestrator-memory` is read-only and may be used by planner or reviewer stages for focused recall. `orchestrator-reflection` owns final memory-incorporation triage before reporting. `orchestrator-memory-curator` may be used by reflection or the focused improvement evaluator to persist durable memory candidates.
- Dev harness context lives in versioned markdown under `.opencode/dev_harness/` so it can be copied between projects without losing structure.
- Product breakdown guidance lives under `.opencode/dev_harness/product-breakdown/` because target repositories receive `.opencode/` but not this package's `product-breakdown/` tree.
- Workflow policy guidance lives under `.opencode/dev_harness/workflow/` because target repositories receive `.opencode/` but not this package's `product-breakdown/` tree.
- Every artifact touched by the workflow should have a visible place in the information chain, with no orphaned node left behind after a creation, move, rename, rewrite, or replacement.
- New information must either update an existing artifact, replace a superseded artifact, or declare a clear parent context and downstream destination.
- Completion evidence must cover stale-reference cleanup, status tracker updates, duplicate-content reconciliation, orphaned-artifact handling, and traceability for changed information artifacts.
- Architecture guardrails include modularity, simplicity, readability, and module responsibility fit, not only preservation of the current shape.
- Improvement discovery is separate from contained implementation. It may inspect broadly, but it must not change code.
- Improvement discovery may write only improvement backlog files under `product-breakdown/06-evolution/candidates/`.
- Focused improvement evaluation may be triggered by working agents for one concrete finding; it may write only improvement backlog files and cannot expand the current task.
- Memory curation may be triggered for one evidenced memory candidate; it may write only workflow memory files and cannot expand the current task or replace improvement backlog persistence.
- Improvement candidates must be traceable to current features, requirements, evidence, review findings, or observed module friction.
- Improvement candidates must not be created as dangling artifacts; each one needs an explicit parent context and follow-up destination.
- Improvement candidates become implementation work only after they are accepted into the backlog and turned into a task contract.

## Completion Model

The deterministic completion gate produces `approved`, `blocked`, or `waiver_required`.

The reviewer stage coordinates focused verification and independent reviewer nodes for the risks present in the task: contract satisfaction, acceptance criteria, test adequacy, architecture, code quality, cleanliness, completeness, information hygiene, and known mistakes. Architecture and code-quality checks also cover modularity, simplicity, readability, and module responsibility fit when relevant. The gate aggregates review findings and implementation evidence. Reviewer approval cannot silently override missing contract items, missing cleanup evidence, or missing required researcher evidence. Incomplete items require explicit waivers with reason, risk, owner, and follow-up action.

After approval, accepted waiver, or completed improvement discovery, the reflection stage reviews the run for durable memory candidates before final reporting. Reflection can invoke memory curation for evidenced repeatable lessons or patterns, but it cannot override the gate, expand scope, or store task-local evidence, backlog candidates, or broad run history as memory.

## Workflow Split

The repository supports three related workflow branches:

- Delivery workflow: normalize a bounded task, create a planner-owned work order, implement only the contracted change, review and verify it, and gate completion. Use this when the requested outcome is actual change now.
- Improvement workflow: explore current features, requirements, implementation evidence, reviewer findings, module friction, bug/fix/regression subjects requested as candidate capture, and cleanup opportunities to produce backlog-ready improvement candidates. Use this when the requested outcome is proposal, recommendation, evaluation, discovery, documented candidate, future task seed, or backlog item.
- Focused improvement evaluation: evaluate one concrete finding raised during delivery or improvement work and persist it only when it meets the evidence-plus-impact threshold.

The delivery workflow may report improvement candidates, but it must not absorb exploratory cleanup, refactoring, or pattern changes unless the contract explicitly includes them. This keeps diffs small, verification focused, and review evidence tied to the requested feature or fix.

Route selection is based on requested outcome, not only issue subject. A bug, fix, regression, feature, or documentation subject can route to improvement when the user asks to capture a candidate instead of implementing the change.

## Persistence And Context Mechanisms

The workflow uses different storage mechanisms for different kinds of information. The storage location is part of the architecture, not an implementation detail, because each mechanism has a different lifecycle, owner, and review expectation.

| Mechanism | Stores | Does Not Store | Canonical Location | Owner |
| --- | --- | --- | --- | --- |
| Product-breakdown source | Durable product intent, commitments, architecture, decisions, implementation maps, verification expectations, operation requirements, evolution state, and traceability. | Runnable how-to steps, transient task notes, copied target-repo runtime policy, or raw run history. | `product-breakdown/` | Maintainers through guarded delivery or improvement work. |
| Operator documentation | Install, deploy, usage, verification commands, troubleshooting, and contributor-facing procedures. | Stable product rationale that belongs in product-breakdown source docs. | `docs/` | Maintainers through documentation work. |
| Runtime agent prompts | Agent role definitions, permissions, stage responsibilities, helper-routing rules, and copied workflow behavior. | Product source rationale, repo-local memory, or target-specific task state. | `.opencode/agents/*.md`, `.opencode/instructions.md` | Package maintainers; copied into target repos. |
| Dev harness context | Reusable prompt templates, product-breakdown guidance, workflow policy, information hygiene rules, and review-output protocols. | Repo-local memory, improvement backlog candidates, or package-only product source docs. | `.opencode/dev_harness/` | Package maintainers; copied into target repos. |
| Workflow memory | Durable lessons, reusable procedural patterns, decision pointers, trust metadata, and revalidation cues that should survive future runs in the same repo. | Current task state, broad transcripts, searchable history, unresolved improvement ideas, or facts that cannot be scoped and revalidated. | `.opencode/dev_harness_memories/` | Reflection plus memory curator, with reviewer visibility when memory influences the task. |
| Improvement backlog | Cleanup, refactoring, pattern, module-responsibility, tuning, or future-task candidates that are evidenced but not part of the current delivery contract. | Durable memory lessons, task transcripts, or implementation changes. | `product-breakdown/06-evolution/candidates/`, then selected/done evolution files. | Improvement workflow or focused improvement evaluator. |
| Task-local evidence | The current work order, implementation evidence, verification results, review findings, waivers, and final report for one run. | Durable product rationale unless reconciled into the product breakdown; durable memory unless accepted by reflection and curator. | Stage outputs during the active run; reconciled only into the relevant source artifact when durable. | Current stage owner. |
| Skills and plugins | External Codex capabilities, local procedures, or connector workflows selected by the operator environment. | Primary-agent responsibilities or repo runtime policy. The workflow package does not persist agent `SKILLS` declarations. | Outside the copied payload unless represented as an explicit product decision or runtime prompt change. | Operator environment; package maintainers only document accepted or declined use. |
| External research | Source references, claims, and implementation notes that justify workflow behavior. | Unverified web excerpts, dependency state without retrieval date, or task-local browsing notes. | `knowledge/agent-reasoning/` and cited product-breakdown decisions. | Maintainers through research-backed product work. |

When information could fit more than one mechanism, choose the narrowest durable owner:

- Store stable product rationale in `product-breakdown/`, not in runtime prompts.
- Store executable workflow behavior in `.opencode/`, not only in product-breakdown docs.
- Store repeated, revalidated lessons in workflow memory, not in the improvement backlog.
- Store future work in the improvement backlog, not in memory.
- Store operator procedures in `docs/`, not in product-breakdown source docs.
- Treat skills and plugins as environment capabilities unless the package explicitly adopts or declines them through a decision.

## Trace Links

- Intent docs feed PC-001 through PC-010.
- Product commitments constrain the agent roles and permissions.
- Technical and evolution decisions justify the OpenCode-native workflow and persistent source docs.
- Implementation artifacts realize the workflow in `opencode.json`, `.opencode/agents/*.md`, and `.opencode/dev_harness/**/*.md`, including the repo-local workflow memory schema and memory hygiene guidance.
- Product breakdown guidance supports PC-006 by giving agents copied context for layered decisions and traceability.
- Workflow policy guidance keeps repeated control, information hygiene, and review-output rules centralized for copied agents.
- Persistence and context mechanism boundaries support PC-006 and PC-007 by keeping product rationale, runtime behavior, workflow memory, improvement candidates, skills/plugins, and research in distinct owners.
- IMP-001 through IMP-005 harden the workflow-memory and review/report boundary, while IMP-006 and IMP-007 harden clarification and reflection routing.
