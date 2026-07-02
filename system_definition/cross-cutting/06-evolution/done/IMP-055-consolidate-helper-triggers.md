# IMP-055: Consolidate Helper Triggers — Eliminate Overlap Between planner-triggers.md and adaptive-risk-triggers.md

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Consolidate overlapping helper trigger policies to eliminate potential conflicts, duplication, and ambiguity in helper selection logic.

## Evidence

- `.opencode/dev_harness/workflow/planner-triggers.md` (helper selection triggers)
- `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` (risk-based trigger logic)
- Architecture analysis finding #4 from FRAMEWORK-REVIEW-001: "Helper triggers split: planner-triggers.md and adaptive-risk-triggers.md overlap — potential conflict"
- `.opencode/agents/orchestrator-planner.md` (consumes both trigger files)

## Current Pain Or Risk

Two separate files define when and how helpers are triggered:
- `planner-triggers.md` — general helper selection criteria
- `adaptive-risk-triggers.md` — risk-based trigger logic

These files have overlapping scope (both define conditions for invoking helpers) but no clear precedence or conflict-resolution rules. When both files define conditions for the same helper, it is ambiguous which policy takes priority. This creates:
- **Potential silent conflicts**: Two policies may disagree on whether a helper should be invoked
- **Maintenance burden**: Changes must be coordinated across two files
- **Cognitive load**: Readers must cross-reference both files to understand helper selection
- **Inconsistency risk**: One file may be updated without the other, creating drift

## Proposed Improvement

Consolidate the two trigger files into a single authoritative helper-selection policy:

1. Merge `adaptive-risk-triggers.md` content into `planner-triggers.md` (or vice versa, choosing the more descriptive name)
2. Define explicit precedence rules for overlapping conditions
3. Remove the superseded file and update all cross-references
4. Update the planner agent to reference only the consolidated file

## Expected Benefit

- Single source of truth for helper selection logic
- Eliminated ambiguity about which policy applies
- Reduced maintenance burden (one file to update)
- Clearer documentation for new contributors
- Reduced risk of silent conflicts

## Risk And Blast Radius

- Low blast radius: only affects planner helper selection logic
- Risk of losing risk-based trigger nuance during consolidation
- Requires careful merge to preserve all existing trigger conditions
- Cross-references in other files must be updated

## Suggested Priority

Medium

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
1. Read both `planner-triggers.md` and `adaptive-risk-triggers.md` in full
2. Identify all overlapping conditions and document conflict-resolution rules
3. Merge content into `planner-triggers.md` with clear section headers for each trigger category
4. Remove `adaptive-risk-triggers.md`
5. Update `control-policy.md` and planner agent to reference only the consolidated file
6. Verify no cross-references to the removed file remain

Do NOT implement:
- Changes to actual trigger logic or conditions (consolidation only)
- Changes to helper definitions or agent boundaries
- Schema changes to plan files

## Out Of Scope

- Changes to actual trigger logic or conditions
- Changes to helper definitions or agent boundaries
- Schema changes to plan files
- Changes to the planner agent's core routing logic

## Traceability

- Intent: Eliminate duplicate/overlapping policy definitions
- Product: Evolution layer — workflow policy consolidation
- Architecture: File-level consolidation; no structural changes
- Implementation: Merge two files into one, update cross-references
- Verification: All trigger conditions from both files are preserved in the consolidated file

## Notes

This finding originates from FRAMEWORK-REVIEW-001 architecture analysis finding #4. The overlap between `planner-triggers.md` and `adaptive-risk-triggers.md` creates a dual-source-of-truth problem for helper selection. Consolidation aligns with KM-010 (reference, don't duplicate).