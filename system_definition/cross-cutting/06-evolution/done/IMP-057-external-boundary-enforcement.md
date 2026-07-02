# IMP-057: External Boundary Enforcement — Planner Edit/Write Permission Guard

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Add external enforcement for the planner agent's edit/write permission boundary to prevent accidental implementation edits during planning.

## Evidence

- `.opencode/agents/orchestrator-planner.md` (edit/write permission setting)
- Architecture analysis finding #5 from FRAMEWORK-REVIEW-001: "No external boundary enforcement: Planner has edit/write: allow with only self-enforcement to prevent implementation edits"
- `.opencode/dev_harness/workflow/control-policy.md` (workflow control policy)

## Current Pain Or Risk

The planner agent has `edit/write: allow` permissions, relying solely on self-enforcement (prompt instructions) to prevent implementation edits during the planning stage. This creates:

- **No defense-in-depth**: A single prompt regression or misinterpretation could cause the planner to modify implementation files
- **No audit trail**: If the planner does make an unintended edit, there is no mechanism to detect or revert it
- **Violation of least-privilege principle**: The planner has more permission than it needs for its read-only planning role
- **Risk of silent corruption**: An unintended edit during planning could corrupt implementation files before the builder stage begins

## Proposed Improvement

Implement external boundary enforcement for the planner's edit/write permissions:

1. **Option A (preferred)**: Change planner permissions to `edit/write: deny` and provide a controlled mechanism (e.g., a dedicated plan-file-writer helper or tool) for writing plan files only
2. **Option B**: Add a pre-execution permission check that validates the planner only writes to `dev_harness_plans/` paths
3. **Option C**: Add a post-execution audit step that verifies no files outside `dev_harness_plans/` were modified by the planner

## Expected Benefit

- Defense-in-depth for the planning stage
- Alignment with least-privilege security principle
- Prevention of accidental implementation edits during planning
- Clearer boundary between planning and implementation stages

## Risk And Blast Radius

- Medium blast radius: changing planner permissions could break plan file writing if not carefully implemented
- Option A requires a new helper or tool for plan file writing
- Options B and C are lower risk but provide weaker enforcement
- All downstream agents that depend on plan files must continue to receive them

## Suggested Priority

High (security/process integrity concern)

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

2026-07-02

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

2026-07-02

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

Implemented as part of combined task IMP-055-056-057-060-062-063. See `.opencode/dev_harness_plans/2026-07-02_000000-IMP-055-056-057-060-062-063.md`.

## Task Contract Seed

The smallest scoped task would:
1. Change planner permissions to `edit/write: deny` in `orchestrator-planner.md`
2. Create a `plan-file-writer` helper agent with `edit/write: allow` restricted to `dev_harness_plans/` paths only
3. Update planner prompt to delegate plan file writing to the new helper
4. Update `control-policy.md` to document the new helper and permission boundary
5. Verify plan files are still written correctly

Do NOT implement:
- Changes to builder or reviewer permissions
- Changes to the plan file schema
- Changes to the plan file archive structure

## Out Of Scope

- Changes to builder or reviewer permissions
- Changes to the plan file schema or archive structure
- Changes to the plan approval cycle
- Changes to other agent permissions

## Traceability

- Intent: Add defense-in-depth for planner edit/write boundary
- Product: Evolution layer — agent framework security/process improvement
- Architecture: New helper agent with restricted permissions; planner permission change
- Implementation: Planner agent edit, new helper agent, control-policy update
- Verification: Planner cannot write to non-plan-file paths; plan files are still created correctly

## Notes

This finding originates from FRAMEWORK-REVIEW-001 architecture analysis finding #5. The planner currently has unrestricted edit/write access with only self-enforcement. This violates the least-privilege principle and creates a single-point-of-failure risk for unintended implementation edits.