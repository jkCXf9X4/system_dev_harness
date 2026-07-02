# IMP-062: Stale Artifacts Cleanup — Typo Files, Stale Tracked Files, Empty Directories, Dual Source-of-Truth

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Clean up stale artifacts in the repository: typo-named files, stale tracked files, empty directories, naming convention inconsistencies, and dual source-of-truth for acceptance criteria.

## Evidence

- Discovery findings #1–5 from FRAMEWORK-REVIEW-001:
  - Finding #1: Typo files in `pre_written/`: `arch_traceabillity.md` and `code_quallity.md` have spelling errors
  - Finding #2: Stale `opencode.json.tmp` tracked in git at repo root
  - Finding #3: `pre_written/` directory uses underscore; all other `.opencode/` dirs use hyphens
  - Finding #4: `.opencode/dev_harness/systems_engineering/architecture/` is empty (contains only a README stating runtime copies were removed)
  - Finding #5: Dual source-of-truth for acceptance criteria: `system_definition/cross-cutting/04-verification/acceptance-criteria.md` (canonical) vs `.opencode/dev_harness/systems_engineering/verification/acceptance-criteria.md` (runtime copy)

## Current Pain Or Risk

Five distinct stale-artifact issues degrade repository hygiene:

1. **Typo file names**: `arch_traceabillity.md` and `code_quallity.md` have spelling errors that make the files harder to discover and suggest lack of quality control
2. **Stale tracked file**: `opencode.json.tmp` is a temporary file tracked in git at the repo root — it should not be version-controlled
3. **Naming convention inconsistency**: `pre_written/` uses underscore while all other `.opencode/` directories use hyphens — creates cognitive friction and inconsistent patterns
4. **Empty directory**: `.opencode/dev_harness/systems_engineering/architecture/` is empty (runtime copies were removed but the directory remains) — creates confusion about whether content is missing
5. **Dual source-of-truth**: Acceptance criteria exist in two locations — the canonical version in `system_definition/cross-cutting/04-verification/acceptance-criteria.md` and a runtime copy in `.opencode/dev_harness/systems_engineering/verification/acceptance-criteria.md` — risk of drift and inconsistency

## Proposed Improvement

Clean up each stale artifact:

1. **Typo files**: Rename `arch_traceabillity.md` → `arch_traceability.md` and `code_quallity.md` → `code_quality.md` (or remove if unused)
2. **Stale tracked file**: Remove `opencode.json.tmp` from git tracking and add to `.gitignore`
3. **Naming convention**: Rename `pre_written/` → `pre-written/` to match the hyphen convention used by all other `.opencode/` directories
4. **Empty directory**: Remove the empty `architecture/` directory (or add a `.gitkeep` with a clear explanation if the directory serves a structural purpose)
5. **Dual source-of-truth**: Remove the runtime copy and update the canonical reference to point to the single source, or add a synchronization mechanism

## Expected Benefit

- Improved repository hygiene and professionalism
- Reduced cognitive friction from inconsistent naming
- Eliminated drift risk from dual source-of-truth
- Cleaner git history (no tracked temp files)
- Clearer directory structure (no empty directories)

## Risk And Blast Radius

- Low blast radius: file renames and removals only
- Risk of breaking cross-references if typo files are referenced elsewhere
- Risk of breaking git history for contributors who have local branches referencing the old paths
- Dual source-of-truth fix requires updating all references to the runtime copy

## Suggested Priority

Low (cosmetic/hygiene improvements; no functional impact)

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
1. Check if typo files (`arch_traceabillity.md`, `code_quallity.md`) are referenced anywhere in the codebase
2. If unreferenced, remove them; if referenced, rename and update references
3. Remove `opencode.json.tmp` from git tracking and add to `.gitignore`
4. Verify no cross-references break

Do NOT implement:
- All five fixes in one task (start with typo files and stale tracked file)
- Naming convention change (separate task due to broader impact)
- Dual source-of-truth resolution (separate task due to verification implications)

## Out Of Scope

- Naming convention change for `pre_written/` (separate task)
- Dual source-of-truth resolution (separate task)
- Changes to acceptance criteria content
- Changes to directory structure beyond the specific stale artifacts listed

## Traceability

- Intent: Improve repository hygiene and eliminate stale artifacts
- Product: Evolution layer — repository quality improvement
- Architecture: File-level cleanup; no structural changes
- Implementation: File renames, removals, .gitignore update
- Verification: No stale files remain; no cross-references are broken

## Notes

This finding originates from FRAMEWORK-REVIEW-001 discovery findings #1–5. These are low-priority hygiene issues but collectively degrade repository quality and professionalism. Each fix is independent and can be implemented in separate tasks.