# Improvement Backlog Overview

Use this template as the landing area for accepted continuous-improvement candidates.

Generated from improvement workflow:

```text
intake -> broad read-only discovery -> architecture/requirement pressure analysis -> backlog candidates -> final report
```

Each candidate is proposed. None is approved for implementation until it has a scoped task contract.

## Usage

Place the overview at the repository's chosen evolution or backlog location, such as:

```text
product-breakdown/06-evolution/backlog/improvement-backlog.md
```

Put each candidate in its own file beside the overview or in a local `candidates/` directory. Move completed implementations to a local `completed/` directory when the repository uses one.

## Individual Candidates

| File | ID | Theme | Status | Priority | Blast radius |
| --- | --- | --- | --- | --- | --- |
| `candidates/IMP-001.md` | IMP-001 | <theme> | Proposed | <priority> | <blast radius> |

## Summary

| ID | Theme | Priority | Prerequisite | Blast radius |
| --- | --- | --- | --- | --- |
| IMP-001 | <theme> | <priority> | <prerequisite> | <blast radius> |

## Cross-Cutting Constraints

Document architecture constraints, layer-separation rules, invariants, and work that must stay out of unrelated contained feature diffs.
