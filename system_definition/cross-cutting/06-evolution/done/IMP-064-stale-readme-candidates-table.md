# IMP-064: Stale README Candidates Table — Update Lifecycle State References

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Done

## Status

Completed

## Layer

Evolution

## Theme

Update the `system_definition/cross-cutting/06-evolution/README.md` candidates table to reflect the actual lifecycle state of all candidates, removing entries that have been moved to `done/` or `discarded/`.

## Evidence

- `system_definition/cross-cutting/06-evolution/README.md` — Candidates table (lines 41–53) lists 11 candidates as "Proposed" that no longer reside in `candidates/`:
  - IMP-028 and IMP-030 are in `discarded/` (not `candidates/`)
  - IMP-034, IMP-037, IMP-049, IMP-050, IMP-051, IMP-053 are in `done/` (not `candidates/`)
  - IMP-052 is in `discarded/` (not `candidates/`)
- `system_definition/cross-cutting/06-evolution/candidates/` — Contains only IMP-027, IMP-054, IMP-058, IMP-059, IMP-064 (5 files, not 11)
- `system_definition/cross-cutting/06-evolution/done/` — Contains 46 completed IMP files including IMP-034, IMP-037, IMP-049, IMP-050, IMP-051, IMP-053
- `system_definition/cross-cutting/06-evolution/discarded/` — Contains 9 discarded IMP files including IMP-028, IMP-030, IMP-035, IMP-052
- KM-007 (stale references) — The README table is a stale reference that will mislead agents and operators about candidate lifecycle state

## Current Pain Or Risk

The README candidates table is the authoritative index for the improvement backlog. It currently lists 11 candidates as "Proposed" that have already been moved to `done/` or `discarded/`. This creates:

- **Misleading backlog state**: Agents and operators see 11 proposed candidates that don't actually exist in `candidates/`
- **Confused lifecycle tracking**: A new contributor or agent cannot determine the true state of these candidates from the README alone
- **Duplicate risk**: Future candidate-capture runs may create duplicate candidates because the README suggests these items are still proposed
- **Information hygiene violation**: Per KM-007, stale references must be checked and fixed; this is a confirmed stale reference

## Proposed Improvement

Update the `system_definition/cross-cutting/06-evolution/README.md` candidates table to:

1. Remove entries that have been moved to `done/` (IMP-034, IMP-037, IMP-049, IMP-050, IMP-051, IMP-053)
2. Remove entries that have been moved to `discarded/` (IMP-028, IMP-030, IMP-052)
3. Add the current active candidates (IMP-027, IMP-054, IMP-058, IMP-059) with correct status and date
4. Verify the Selected and Done tables are also current

## Expected Benefit

- Accurate backlog state visible from the README
- Reduced risk of duplicate candidate creation
- Clear lifecycle tracking for all IMP items
- KM-007 compliance for the evolution layer index

## Risk And Blast Radius

- Low blast radius: changes are confined to a single README file
- No functional impact on workflow or agents
- Risk of introducing new stale entries if the update is incomplete — mitigated by verifying against actual directory contents

## Suggested Priority

Medium

## Selected Date

2026-07-03

## Completed Date

2026-07-03

## Implementation Reference

`.opencode/dev_harness_plans/2026-07-03_000000-IMP-064.md`

## Task Contract Seed

The smallest scoped task would:
1. Read `system_definition/cross-cutting/06-evolution/README.md` candidates table
2. Cross-reference each listed candidate against `candidates/`, `done/`, `discarded/`, and `selected/` directories
3. Remove entries that no longer reside in `candidates/`
4. Add any active candidates missing from the table
5. Verify the Selected and Done tables are also current
6. Update the table date column to reflect the update timestamp

Do NOT implement:
- Changes to candidate file content or lifecycle
- Changes to the lifecycle model or folder structure
- Automated README synchronization (separate candidate)

## Out Of Scope

- Changes to candidate file content or lifecycle state
- Changes to the lifecycle model or folder structure
- Automated README synchronization or CI checks
- Cleanup of other stale references outside the README candidates table

## Traceability

- Intent: Fix stale reference in evolution layer index (KM-007)
- Product: Evolution layer — backlog index accuracy
- Architecture: Single-file update; no structural changes
- Implementation: Update `system_definition/cross-cutting/06-evolution/README.md` candidates table
- Verification: README candidates table matches actual `candidates/` directory contents

## Notes

This finding was identified during the comprehensive project review (2026-07-02). The README candidates table has not been updated since the last lifecycle transitions moved multiple candidates to `done/` and `discarded/`. The current active candidates (IMP-027, IMP-054, IMP-058, IMP-059) are correctly placed in `candidates/` but are not listed in the README table.