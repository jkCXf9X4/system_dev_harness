# Improvement Backlog Overview

Theme: Align the package `docs/` tree with the product-breakdown template structure that the same package prescribes for target repos.

The template at `.opencode/templates/product-breakdown/` defines the canonical layered structure, naming conventions, decision placement rules, and per-layer artifact expectations. The package's own `docs/` tree uses a different numbering scheme, a flat decisions directory, and leaves two layers entirely implicit. The gap creates a self-inconsistency: the package instructs target repos to use a structure it does not follow itself.

Generated from improvement workflow: `intake -> broad read-only discovery -> architecture/requirement pressure analysis -> backlog candidates -> final report`

Each candidate is proposed. None is approved for implementation until it has a scoped task contract.

## Individual Candidates

| File | ID | Theme | Status | Priority | Blast radius |
| --- | --- | --- | --- | --- | --- |
| `candidates/IMP-001.md` | IMP-001 | Renumber and rename layer directories to match template numbering | Proposed | High | docs/ tree only; 20+ cross-reference updates needed |
| `candidates/IMP-002.md` | IMP-002 | Distribute decisions into per-layer decisions/ directories with prefixed IDs | Proposed | High | 5 ADR files moved; cross-references in 4+ docs files |
| `candidates/IMP-003.md` | IMP-003 | Create missing verification layer (04-verification/) | Proposed | Medium | New directory; no existing files moved |
| `candidates/IMP-004.md` | IMP-004 | Create missing operation layer (05-operation/) | Proposed | Medium | New directory; no existing files moved |
| `candidates/IMP-005.md` | IMP-005 | Add missing per-layer artifacts to existing layers | Proposed | Low | New files only; risk of content drift with template |
| `candidates/IMP-006.md` | IMP-006 | Add root-level traceability-map.md | Proposed | Medium | New single file; needs reliable cross-reference audit |
| `candidates/IMP-007.md` | IMP-007 | Establish improvement backlog infrastructure under 06-evolution/backlog/ | Proposed | Low | New directory and template content; no move risk |
| `candidates/IMP-008.md` | IMP-008 | Persist improvement candidates to disk automatically | Proposed | High | Two agent prompts updated (orchestrator.md, orchestrator-improvement.md) |
| `candidates/IMP-009.md` | IMP-009 | Route gate `blocked` to planner for automatic revision loop | Proposed | High | 3-5 agent prompts updated (orchestrator.md primary, planner + contract + architecture + lessons adjacencies) |

## Summary

| ID | Theme | Priority | Prerequisite | Blast radius |
| --- | --- | --- | --- | --- |
| IMP-006 | Add root traceability-map.md | Medium | IMP-001 | One new file |
| IMP-007 | Establish improvement backlog infrastructure | Low | IMP-001 | New files and directories |
| IMP-008 | Persist improvement candidates to disk automatically | High | None | Two agent prompts updated |
| IMP-009 | Route gate `blocked` to planner for automatic revision loop | High | IMP-008 (recommended) | 3-5 agent prompts updated; core flow change |

## Recommended Execution Order

1. **IMP-008** — meta: add automatic persistence so all future improvement output survives. No prerequisites, highest leverage.
2. **IMP-009** — meta: add revision loop so reviewer feedback is actionable. Depends on IMP-008 for robust iteration artifact persistence.
3. **IMP-001** — foundation: rename directories.
4. **IMP-002** — critical: move decisions out of the 04- slot so verification can exist.
5. **IMP-003** + **IMP-004** — parallel: create missing layers.
6. **IMP-006** — traceability consolidation (can start after IMP-001).
7. **IMP-007** — backlog infrastructure (can start after IMP-001, richer after IMP-008).
8. **IMP-005** — lowest urgency; incremental per layer.

## Cross-Cutting Constraints

1. **Package-only scope.** The `docs/` tree stays in this repository. No change copies into target repos. The `.opencode/templates/product-breakdown/` runtime payload is separate and already follows the template structure. These candidates affect only the source-of-truth docs for this package.
2. **No agent payload change.** `.opencode/templates/product-breakdown/` must not be modified by these candidates. It is the canonical template; these candidates align the package docs to it, not the other way around.
3. **Synchronization risk.** After migration, anything described in `docs/` about the product breakdown structure must match `.opencode/templates/product-breakdown/`. Changes to the template must be reflected in the package docs, and vice versa.
4. **Decision history must be preserved.** Moving ADR files must not lose their git history, review context, or cross-references. Use `git mv` for each file, and update every `# ADR-XXXX:` title to the new prefix-style ID.
5. **No feature-diff bundling.** These restructuring tasks must not be bundled into unrelated feature or bugfix diffs. Each candidate requires a separate task contract before implementation.