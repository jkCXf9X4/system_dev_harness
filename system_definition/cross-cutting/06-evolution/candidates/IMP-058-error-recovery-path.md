# IMP-058: Error Recovery Path — Defined Recovery for Stage Failures

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Define a formal error recovery path for when any guarded workflow stage fails mid-task.

## Evidence

- `.opencode/dev_harness/workflow/control-policy.md` (entire file: no error recovery section)
- `.opencode/dev_harness/workflow/stage-output-schema.md` (no error/exception fields)
- `.opencode/agents/orchestrator-planner.md` (no error recovery logic)
- `.opencode/agents/orchestrator-builder.md` (no error recovery logic)
- `.opencode/agents/orchestrator-reviewer.md` (no error recovery logic)
- Systems engineering finding #1 from FRAMEWORK-REVIEW-001: "No error recovery path: If any stage fails mid-task, no defined recovery"
- Systems engineering finding #6 from FRAMEWORK-REVIEW-001: "No rollback mechanism for approved changes"

## Current Pain Or Risk

The guarded workflow has no defined error recovery path. If any stage fails mid-task:
- Planner fails: No plan file, no downstream stages can start — but no recovery procedure is defined
- Builder fails mid-edit: Partial implementation with no rollback mechanism
- Reviewer fails: No gate result, but no defined escalation path
- Reporter fails: Task completes but no final summary is produced

The only implicit recovery is the revision loop (planner→builder→reviewer→planner), but this assumes the planner can always produce a valid revision. If the planner itself fails, there is no recovery.

Additionally, there is no rollback mechanism for approved changes that fail verification. Once a builder edit is approved by the reviewer, there is no defined way to revert if post-approval verification fails.

## Proposed Improvement

Add a formal error recovery framework to the guarded workflow:

1. **Stage failure detection**: Add error/exception fields to `stage-output-schema.md` for each stage
2. **Recovery escalation path**: Define a three-tier recovery:
   - Tier 1 (local retry): Stage retries with modified parameters
   - Tier 2 (stage skip): Task continues without the failed stage's output
   - Tier 3 (task abort): Task is aborted with a clear error summary
3. **Rollback mechanism**: Define a rollback procedure for builder edits that fail post-approval verification
4. **Error reporting**: Reporter stage includes error summary in its output when recovery was invoked

## Expected Benefit

- Defined behavior when things go wrong (instead of silent failure or infinite loops)
- Reduced risk of partial/corrupt state after stage failure
- Clear escalation path for operators
- Alignment with ISO 15288 risk management and contingency planning
- Improved workflow robustness

## Risk And Blast Radius

- Medium blast radius: touches control-policy.md, stage-output-schema.md, and potentially all stage agents
- Risk of over-engineering if recovery paths are too complex
- Risk of masking real failures if retry logic is too aggressive
- Requires careful design to avoid introducing new failure modes

## Suggested Priority

High (process integrity concern)

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task would:
1. Add `error` and `recovery` sections to `control-policy.md` defining the three-tier recovery model
2. Add optional `stage_error` and `recovery_action` fields to `stage-output-schema.md`
3. Update planner agent to include recovery routing logic
4. Update reporter agent to include error summary in output

Do NOT implement:
- Full rollback mechanism (separate candidate)
- Changes to stage agent prompts beyond error handling
- Automated retry logic (define the framework only)

## Out Of Scope

- Full rollback mechanism for builder edits (separate candidate IMP-062 covers related stale-artifact cleanup)
- Automated retry logic implementation
- Changes to stage agent prompts beyond error handling
- Integration with external monitoring or alerting

## Traceability

- Intent: ISO 15288 risk management — contingency planning for process failures
- Product: Evolution layer — workflow process robustness
- Architecture: Additive error-handling layer; no structural changes to existing stages
- Implementation: control-policy.md, stage-output-schema.md, planner, reporter updates
- Verification: Error recovery paths are documented and referenced by all stages

## Notes

This finding originates from FRAMEWORK-REVIEW-001 systems engineering findings #1 and #6. The workflow currently has zero error recovery or rollback mechanisms. This is a critical process integrity gap for a production workflow.