# IMP-031: Create orchestrator-systems-engineering Subagent

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Selected

## Status

In Progress

## Layer

Evolution

## Theme

Create a new `orchestrator-systems-engineering` subagent that embodies ISO 15288 staged pipeline concepts and adapted SysML text-artifact modeling for the dev-harness workflow.

## Evidence

- All 19 existing agent files under `.opencode/agents/` — consistent `orchestrator-<role>.md` naming, YAML frontmatter pattern, color assignment
- `.opencode/dev_harness/workflow/agent-boundaries.md` — read-only / limited-write / editing classification
- `.opencode/dev_harness/workflow/planner-triggers.md` — planner/builder/reviewer trigger tables
- `.opencode/agents/orchestrator.md` — orchestrator task permission allow-list
- Color audit — all standard colors taken except `danger`
- `.opencode/dev_harness/workflow/subagent-lifecycle.md` — helper reuse policy
- `.opencode/dev_harness/workflow/parallel-helper-execution.md` — parallel-safe helper grouping
- `.opencode/agents/orchestrator-architecture.md` — closest existing read-only planner helper pattern
- ISO/IEC/IEEE 15288 — 4 process groups, 30 processes, 6 lifecycle stages
- OMG SysML — 9 diagram types, allocation tables, MBSE modeling domains
- INCOSE SE Handbook — technical processes, technical management processes

## Current Pain Or Risk

Complex systems-engineering concerns (cross-system interface analysis, multi-module dependency tracing, workflow-stage integration assessment, requirements-to-component traceability matrices, verification/validation gap identification) currently have no dedicated analytical agent. These concerns are either handled ad-hoc by the planner or forced into `orchestrator-architecture` (which focuses on software structure, not systems-level process integration). The gap creates risk of missed interface contracts, unverified cross-stage handoffs, and incomplete verification chains.

## Proposed Improvement

Create `orchestrator-systems-engineering.md` as a read-only planner-directed helper subagent with the following characteristics:

- **Agent role and knowledge:**
  - ISO 15288 staged pipeline: Concept→Requirements→Architecture→Design→Build→Integrate→Verify→Validate→Deploy→Maintain — used as an analytical framework for assessing task completeness and stage readiness
  - SysML text adaptations: BDD→component hierarchy tables, IBD→interface specification tables, Requirements Diagram→traceability matrices, Activity Diagram→workflow step lists, Sequence Diagram→interaction sequences, State Machine→state/transition tables, Parametric Diagram→constraint blocks
  - MBSE four modeling domains: Requirements (what must the system do), Behavior (how does it respond), Structure (components and relationships), Verification (how is correctness proven)
  - Core SE principles: requirements-first, architecture-before-detail, verification-gate, traceability-thread, risk-aware, single-truth-model, separation-of-concerns, iterative-refinement
  - Output artifacts: requirements specifications, component hierarchies, interface contracts, verification matrices, risk lists, integration analysis

- **YAML frontmatter specification:**
```yaml
description: "Provides cross-system analysis, interface contracts, and systems-level constraints following ISO 15288 and SysML."
mode: subagent
model: openrouter/deepseek/deepseek-v4-flash
hidden: true
color: danger
temperature: 0.1
permission:
  read: allow
  glob: allow
  grep: allow
  list: allow
  edit: deny
  write: deny
  bash: allow
  external_directory: deny
  task:
    "*": deny
    "orchestrator-researcher": allow
```

- **Integration touch-points (files needing modification during implementation):**
  1. `.opencode/agents/orchestrator-systems-engineering.md` — new file (agent definition with YAML frontmatter + role prompt)
  2. `.opencode/dev_harness/workflow/agent-boundaries.md` — add `orchestrator-systems-engineering` to Read-Only Agents list
  3. `.opencode/dev_harness/workflow/planner-triggers.md` — add trigger: "Cross-system, multi-module, interface, workflow-stage, or systems-architecture-level analysis requires `orchestrator-systems-engineering`" under Planner Triggers
  4. `.opencode/agents/orchestrator-planner.md` — add to Directed Helpers section and parallel-safe list
  5. `.opencode/dev_harness/workflow/parallel-helper-execution.md` — add to typical parallel-safe planner helpers list
  6. `.opencode/agents/orchestrator.md` — add `"orchestrator-systems-engineering": allow` to task permission block

## Expected Benefit

A dedicated systems-engineering analytical lens that catches cross-stage integration risks, incomplete traceability chains, unverified interfaces, and systems-level constraint violations before implementation begins. Reduces rework cycles by identifying architectural and integration issues during planning rather than during review.

## Risk And Blast Radius

Low — the new agent is read-only, additive, and does not modify any existing artifact. Implementation touches 6 existing control files (additions only) plus creates 1 new agent definition file. No existing agent behavior changes. No routing changes to the top-level guarded chain (planner→builder→reviewer→reflection→reporter). Color `danger` is confirmed unused.

## Suggested Priority

Medium — systems-engineering analysis is valuable for complex multi-module tasks but not a blocking gap for routine contained work.

## Selected Date

N/A

## Completed Date

N/A

## Implementation Reference

N/A

## Task Contract Seed

1. Create `.opencode/agents/orchestrator-systems-engineering.md` with YAML frontmatter (color: danger, read-only permissions, researcher subagent access only) and role prompt incorporating ISO 15288 pipeline + SysML text patterns + MBSE domains + core SE principles.
2. Add `orchestrator-systems-engineering` to Read-Only Agents list in `agent-boundaries.md`.
3. Add systems-engineering trigger entry under Planner Triggers in `planner-triggers.md`.
4. Add `orchestrator-systems-engineering` to Directed Helpers and parallel-safe list in `orchestrator-planner.md`.
5. Add to typical parallel-safe planner helpers in `parallel-helper-execution.md`.
6. Add `"orchestrator-systems-engineering": allow` to `orchestrator.md` task permission block.
7. Verify agent is callable via orchestrator→planner→systems-engineering delegation path.

## Out Of Scope

- Modifying builder, reviewer, or reporter agent definitions
- Changing the top-level guarded chain routing
- Adding the agent as a required top-level stage
- Creating SKILLS files (per AD-004)
- Modifying plan-summary-schema.md or stage-output-schema.md
- Implementing any systems-engineering process for existing tasks
- Creating system-definition decision records

## Traceability

- Intent: ISO/IEC/IEEE 15288 systems engineering lifecycle processes, OMG SysML modeling patterns, INCOSE SE Handbook
- Product: Evolution layer improvement backlog (06-evolution)
- Architecture: New additive subagent file following established read-only planner helper pattern
- Implementation: 6-file task contract seed
- Verification: Agent callable by orchestrator; produces structured systems-engineering analysis; reviewer confirms no overlap with existing architecture agent

## Notes

KM-004 (minimize parallel solutions) requires explicit non-overlap justification with `orchestrator-architecture`: architecture focuses on *software* structure (module boundaries, coupling, design quality, code-level patterns); systems-engineering focuses on *system/process* structure (cross-agent handoffs, interface contracts, stage-readiness gates, requirements-to-component traceability chains). They are complementary, not parallel, just as `orchestrator-contract` (requirements) and `orchestrator-architecture` (design) are distinct but complementary planning helpers.