# IMP-054: God Planner Anti-Pattern — Decompose Planner Responsibilities

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Decompose the orchestrator-planner agent to eliminate the god-object anti-pattern and improve maintainability, testability, and single-responsibility separation.

## Evidence

- `.opencode/agents/orchestrator-planner.md` (151 lines — 2–3× the length of other agent definitions)
- `.opencode/dev_harness/workflow/plan-summary-schema.md` (planner writes plan files per this schema)
- `.opencode/dev_harness/workflow/planner-triggers.md` (helper selection logic)
- `.opencode/dev_harness/workflow/planner-triggers.md` (risk-based trigger logic)
- `.opencode/dev_harness/workflow/control-policy.md` (clarification gate, draft approval, revision handling)
- Architecture analysis finding #1 from FRAMEWORK-REVIEW-001: "God planner anti-pattern: Planner is 151 lines — 2–3× other agents. Owns routing, helper selection, parallel execution, clarification gate, draft approval, revision handling, interface identification, system-definition placement, and plan file writing"

## Current Pain Or Risk

The planner agent owns at least 8 distinct responsibilities:
1. Request routing and work-order scoping
2. Directed helper selection and parallel execution
3. Clarification gate for ambiguous requests
4. Plan draft approval cycle
5. Revision handling and iteration management
6. Interface identification (`touches_shared_interface`)
7. System-definition layer placement
8. Plan file writing and archive management

This concentration creates:
- **Maintenance burden**: Any change to any of these 8 concerns requires editing the same 151-line file
- **Testing difficulty**: Cannot test routing logic independently from plan-file writing
- **Single point of failure**: A prompt regression in any one concern can break all 8
- **Cognitive load**: New contributors must understand the entire file before modifying any single concern
- **Violation of single-responsibility principle**: The planner is a god object in agent form

## Proposed Improvement

Decompose the planner into focused sub-agents or helper modules, each owning one concern:

1. **orchestrator-planner-router**: Request analysis, work-order scoping, routing decision (build vs. guarded workflow)
2. **orchestrator-planner-helper-selector**: Helper selection and parallel execution orchestration (extract from planner-triggers.md)
3. **orchestrator-planner-contract**: Plan file schema, writing, and archive management
4. **orchestrator-planner-gate**: Clarification gate and draft approval cycle
5. **orchestrator-planner-revision**: Revision handling and iteration management

The main planner becomes a thin coordinator that delegates to these sub-agents.

## Expected Benefit

- Each sub-agent is 30–50 lines with a single responsibility
- Independent testing and modification of each concern
- Reduced blast radius for prompt changes
- Clearer ownership boundaries for future contributors
- Alignment with KM-005 (abstraction separation)

## Risk And Blast Radius

- High blast radius: touches the planner agent, all downstream agents that consume plan files, and the control-policy workflow
- Risk of breaking the routing/execution chain if sub-agent interfaces are not carefully designed
- Requires careful interface contracts between sub-agents to avoid tight coupling
- Migration could introduce regressions in revision handling and draft approval

## Suggested Priority

Medium

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task would:
1. Extract helper selection logic from planner into a new `orchestrator-planner-helper-selector` agent
2. Update `planner-triggers.md` to reference the new agent instead of inline logic
3. Verify that the main planner still produces identical plan files after extraction
4. Update `control-policy.md` to document the new sub-agent

Do NOT implement:
- Full decomposition in a single task (do one extraction per task)
- Changes to plan file schema or downstream consumer interfaces
- Changes to the revision loop or draft approval logic

## Out Of Scope

- Full decomposition in a single task
- Changes to plan file schema or downstream consumer interfaces
- Changes to revision loop, draft approval, or clarification gate logic
- Changes to system-definition layer placement logic

## Traceability

- Intent: Reduce maintenance burden and single-responsibility violation in the planner agent
- Product: Evolution layer — agent framework quality improvement
- Architecture: Additive sub-agent creation; main planner becomes a coordinator
- Implementation: New agent files, updated planner, updated control-policy
- Verification: Planner produces identical plan files before and after each extraction

## Notes

This finding originates from FRAMEWORK-REVIEW-001 architecture analysis finding #1. The planner's 151-line size is 2–3× the length of other agent definitions, confirming the god-object anti-pattern. The proposed decomposition follows KM-005 (abstraction separation) and KM-004 (minimize parallel solutions — each sub-agent has a single entrypoint).