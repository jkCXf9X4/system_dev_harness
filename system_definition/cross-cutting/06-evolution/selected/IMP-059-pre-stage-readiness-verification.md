# IMP-059: Pre-Stage Readiness Verification — Stage Gate Readiness Checks

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Add pre-stage readiness verification so that each workflow stage only starts when its prerequisites are confirmed satisfied.

## Evidence

- `.opencode/dev_harness/workflow/control-policy.md` (entire file: no readiness check section)
- `.opencode/dev_harness/workflow/plan-summary-schema.md` (defines plan file content but no readiness criteria)
- `.opencode/agents/orchestrator-planner.md` (routes to stages based on work order, not readiness)
- `.opencode/agents/orchestrator-builder.md` (starts based on routing, not readiness check)
- `.opencode/agents/orchestrator-reviewer.md` (starts based on routing, not readiness check)
- Systems engineering finding #2 from FRAMEWORK-REVIEW-001: "No pre-stage readiness verification: Stages start based on routing, not readiness checks"

## Current Pain Or Risk

Stages in the guarded workflow start based on routing decisions from the planner, not on readiness verification. This means:

- **Builder starts without verifying**: Plan file exists, is valid, and contains all required fields
- **Reviewer starts without verifying**: Builder output exists, is complete, and is internally consistent
- **Reporter starts without verifying**: All stage outputs are present and consistent
- **No prerequisite validation**: If a plan file write fails silently, the builder starts with no work order
- **No input validation**: Stage inputs are assumed valid without verification

This creates a fragile chain where a failure in one stage propagates silently to the next.

## Proposed Improvement

Add a lightweight pre-stage readiness verification step before each stage begins:

1. **Define readiness criteria per stage**:
   - Planner readiness: Request is unambiguous, work order is scoped
   - Builder readiness: Plan file exists, is valid per schema, contains assigned files
   - Reviewer readiness: Builder output exists, plan file is still valid
   - Reporter readiness: All stage outputs are present
2. **Add readiness check step**: Before each stage starts, verify its readiness criteria
3. **Failure handling**: If readiness check fails, escalate per error recovery path (see IMP-058)
4. **Document criteria**: Add readiness criteria to `control-policy.md` and/or `plan-summary-schema.md`

## Expected Benefit

- Early detection of missing or invalid prerequisites
- Reduced silent failure propagation
- Clearer failure diagnosis (which prerequisite was missing)
- More robust workflow execution
- Better debugging information when things go wrong

## Risk And Blast Radius

- Low blast radius: additive checks that don't change stage logic
- Risk of false positives if readiness criteria are too strict
- Minimal performance impact (checks are file-existence and schema-validation)
- Requires coordination with error recovery path (IMP-058)

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
1. Define readiness criteria for builder stage (plan file exists, valid per schema)
2. Add readiness check step to builder agent prompt
3. Add readiness criteria section to `control-policy.md`
4. Verify builder correctly reports readiness failure instead of starting with invalid input

Do NOT implement:
- Readiness checks for all stages in one task (start with builder)
- Changes to stage routing logic
- Integration with error recovery path (IMP-058) — keep checks independent

## Out Of Scope

- Readiness checks for all stages in a single task
- Changes to stage routing logic
- Integration with error recovery path
- Automated recovery from readiness failure

## Traceability

- Intent: Add prerequisite validation before stage execution
- Product: Evolution layer — workflow process robustness
- Architecture: Additive readiness check step; no structural changes
- Implementation: control-policy.md, builder agent, plan-summary-schema.md updates
- Verification: Builder correctly rejects invalid/missing plan files

## Notes

This finding originates from FRAMEWORK-REVIEW-001 systems engineering finding #2. The workflow currently has no readiness verification — stages start based solely on routing. This is a process robustness gap that compounds the error recovery gap (IMP-058).