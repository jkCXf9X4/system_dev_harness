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
