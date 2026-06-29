# Patterns Memory

This file stores reusable workflow patterns that are broader than a single mistake lesson but concrete enough to guide future planning, implementation, or review.

Backlog candidates must not be stored here — see `.opencode/dev_harness/workflow/control-policy.md` "Workflow Memory" section.

## Template

```text
### PAT-000: Short title

Type:
planning | implementation | review | documentation | improvement

Metadata:
Scope:
Source:
Last verified:
Confidence:
Revalidation trigger:
Environment notes:

Decision pointer:

Source evidence:
Where did this pattern come from?

Trigger conditions:
When should future agents apply this pattern?

Guidance:
What should future agents do?

Verification check:
How should reviewers confirm the pattern was applied correctly?
```

## Current Patterns

### PAT-001: Surgical Goal-Driven Changes

Metadata:
Scope: planning, implementation, review, and documentation
Source: repeated workflow tuning and revision loops
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a task can drift into speculative scope, related cleanup, or hidden assumptions
Environment notes: applies to bounded change requests in any repository

Decision pointer: Separate assumptions, issue kind, requested outcome, and success criteria before editing.

Type:
planning | implementation | review

Source evidence:
Repeated workflow tuning showed agents can overcomplicate small tasks, silently choose among ambiguous interpretations, or clean unrelated mess while trying to be helpful.

Trigger conditions:
Apply when planning, implementing, cleaning up, or reviewing any bounded change request.

Guidance:
Separate assumptions, issue kind, requested outcome, and success criteria before editing. Prefer the smallest change that satisfies the request. Do not add speculative abstractions, unrelated cleanup, or convenience behavior. Builders clean up only stale artifacts caused by their own change; unrelated cleanup becomes an improvement candidate.

Verification check:
Reviewers confirm that every changed line traces to the work order, ambiguity was surfaced before implementation, success criteria were verified, and unrelated cleanup or speculative flexibility was not included.

### PAT-002: Decomposition Boundary Decision Pattern

Metadata:
Scope: decomposition boundary decisions in planning, review, documentation, and implementation follow-through
Source: IMP-023 evaluation (cross-cutting FBS/PBS/WBS decomposition analysis), IMP-024 evaluation (PBS merger evaluation), and multiple prior KM entries (KM-004, KM-006, KM-007, KM-008)
Last verified: 2026-06-29
Confidence: high
Revalidation trigger: when a future decomposition restructure proposal reopens the boundary question, or when architecture guardrails change
Environment notes: designed for the product-breakdown hierarchy used by this repo's orchestrator workflow; assumes INCOSE MECE decomposition dimensions (functional, physical, work-breakdown, cross-cutting)

Decision pointer: Classify the artifact first, then compare all plausible destinations, then weigh guardrails and change cost before choosing retain, move, add a new dimension, or defer.

Type:
planning | review | documentation | implementation

Source evidence:
IMP-023 systematically resolved whether cross-cutting layers should be redistributed into FBS, PBS, or WBS per INCOSE MECE principles. IMP-024 evaluated a specific PBS merger for 05-operation and refined the method by showing that (1) destination enumeration must happen up front to avoid sequential try-and-reject loops, (2) cross-candidate dependencies should be documented explicitly, and (3) recent restructure churn is a real cost factor. The method also draws on KM-004, KM-006, KM-007, and KM-008 for navigation, traceability, and stale-reference risk.

Trigger conditions:
Apply whenever a proposal would move content between decomposition dimensions, collapse a grouping, split a layer, or introduce a new top-level category.

Guidance:
When evaluating a decomposition boundary question:
0. **Enumerate all plausible destinations.** List every decomposition home the artifact could reasonably occupy before choosing one. Consider the local canonical homes plus any new dimension the content might justify.
1. **Classify the content first.** Judge the artifact by what it says, not where it currently lives. Use functional / physical / work / cross-cutting classification as the first pass.
2. **Apply guardrails as hard constraints.** If a destination would violate architecture rules, reject it regardless of MECE elegance or convenience.
3. **Assess fit quality for each destination.** Distinguish between a natural fit, a forced fit, and an outright mismatch. Prefer the natural fit when one exists.
4. **Estimate change cost.** Count the blast radius in files and references, then factor in recent restructure churn and stale-reference risk. Treat a move as high cost when it would revisit the same content repeatedly or exceed the local precedent by a wide margin.
5. **Estimate residual cross-cutting.** If a meaningful share of the content would still span multiple dimensions after the move, document that residual explicitly rather than pretending the split is complete. Use a qualitative estimate unless a clear counting rule exists.
6. **Check navigation impact.** Prefer the structure that is easiest to scan and easiest for future contributors to locate without backtracking.
7. **Choose the least harmful complete outcome.** Available outcomes are: retain in place and strengthen documentation, move to a new canonical home, create a new dimension/category, or defer until sequencing reduces the cost. Do not default to retention unless retention is genuinely the least harmful option.
8. **Document dependencies and sequencing.** If the outcome affects another active candidate, state the dependency, the preferred order, and the fallback if sequencing cannot be coordinated.

Verification check:
Reviewers confirm that content classification was performed before location reasoning, all plausible destinations were enumerated upfront, guardrails were checked, destination fit was compared, blast radius and churn were estimated, residual cross-cutting was acknowledged, navigation impact was considered, and any dependency or sequencing issue was named explicitly.
