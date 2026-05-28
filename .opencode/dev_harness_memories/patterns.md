# Patterns Memory

This file stores reusable workflow patterns that are broader than a single mistake lesson but concrete enough to guide future planning, implementation, or review.

Backlog candidates must not be stored here — see `.opencode/dev_harness/workflow/control-policy.md` "Workflow Memory" section.

## Template

```text
### PAT-000: Short title

Type:
planning | implementation | review | documentation | improvement

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
