# Improvement Backlog Overview

Use this template as the landing area for accepted continuous-improvement candidates.

Generated from improvement workflow:

```text
intake -> broad read-only discovery -> architecture/requirement pressure analysis -> backlog candidates -> final report
```

Each candidate is proposed. None is approved for implementation until it has a scoped task contract.

## Lifecycle

Improvements follow a three-stage lifecycle:

1. **Candidate** (`candidates/`): Proposed improvements not yet selected for development.
2. **Selected** (`selected/`): Improvements approved and waiting or being implemented.
3. **Done** (`done/`): Completed improvements tracked for historical reference.

See `product-breakdown/06-evolution/README.md` for the full lifecycle model.

## Usage

Place the overview at the repository's chosen evolution location:

```text
product-breakdown/06-evolution/candidates/   — proposed candidates
product-breakdown/06-evolution/selected/     — selected for implementation
product-breakdown/06-evolution/done/         — completed improvements
```

Each candidate lives in its own file under the appropriate lifecycle folder.

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

## Summary

| ID | Theme | Lifecycle Stage | Priority | Prerequisite | Blast radius |
| --- | --- | --- | --- | --- | --- |
| IMP-NNN | <theme> | Candidate / Selected / Done | <priority> | <prerequisite> | <blast radius> |

## Cross-Cutting Constraints

Document architecture constraints, layer-separation rules, invariants, and work that must stay out of unrelated contained feature diffs.
