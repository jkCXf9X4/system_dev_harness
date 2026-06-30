# Improvement Backlog Overview

Use this template as the landing area for accepted continuous-improvement candidates.

Generated from candidate-capture mode:

```text
planner -> builder persists backlog candidates -> reviewer gate -> reflection -> final report
```

Each candidate is proposed. None is approved for implementation until it has a scoped task contract.

## Lifecycle

Improvements follow the three-stage lifecycle described in [cross-cutting/06-evolution/README.md](../../../../system_definition/cross-cutting/06-evolution/README.md). Summary: Candidate → Selected → Done.

See `system_definition/cross-cutting/06-evolution/README.md` for the full lifecycle model.

## Usage

Place the overview at the repository's chosen evolution location:

```text
system_definition/cross-cutting/06-evolution/candidates/   — proposed candidates
system_definition/cross-cutting/06-evolution/selected/     — selected for implementation
system_definition/cross-cutting/06-evolution/done/         — completed improvements
system_definition/cross-cutting/06-evolution/evaluations/  — historical rejected or deferred suggestions, when present
```

Each candidate lives in its own file under the appropriate lifecycle folder.
Rejected or deferred suggestions may exist as historical evaluation records, but deliberate candidate capture does not create a placeholder when no backlog-worthy item is found.

## Candidates (Proposed)

| File | ID | Theme | Status | Priority | Blast radius |
| --- | --- | --- | --- | --- | --- |
| `candidates/IMP-NNN.md` | IMP-NNN | <theme> | Proposed | <priority> | <blast radius> |

## Selected (Approved / In Progress)

| File | ID | Theme | Status | Priority | Task Reference |
| --- | --- | --- | --- | --- | --- |
| `selected/IMP-NNN.md` | IMP-NNN | <theme> | Selected | <priority> | <task or PR link> |

## Done (Completed)

| File | ID | Theme | Completed Date | Implementation Reference |
| --- | --- | --- | --- | --- |
| `done/IMP-NNN.md` | IMP-NNN | <theme> | <date> | <changelog or PR link> |

## Evaluations (Rejected / Deferred)

| File | ID | Finding | Disposition | Reason |
| --- | --- | --- | --- | --- |
| `evaluations/EVAL-YYYY-MM-DD-NNN.md` | EVAL-YYYY-MM-DD-NNN | <finding> | Rejected / Needs More Evidence | <reason> |

## Summary

| ID | Theme | Lifecycle Stage | Priority | Prerequisite | Blast radius |
| --- | --- | --- | --- | --- | --- |
| IMP-NNN | <theme> | Candidate / Selected / Done | <priority> | <prerequisite> | <blast radius> |

## Cross-Cutting Constraints

Document architecture constraints, layer-separation rules, invariants, and work that must stay out of unrelated contained feature diffs.
