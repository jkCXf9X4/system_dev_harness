# AK-004: Use Review Feedback Loops For Agent Improvement

## Claim

Agent workflows are more robust when they include explicit feedback and review loops instead of relying on single-pass self-assessment.

## Practical Interpretation

Independent reviewers should evaluate implementation evidence against contract, architecture, QA, completeness, and lesson criteria. Blocking findings should route back into a controlled revision loop rather than being silently waived.

## Applies To

- Independent review agents
- Completion gate
- Revision loop
- Improvement workflow

## Evidence

- SRC-006 demonstrates that language agents can improve using verbal feedback derived from external or internal evaluation signals.
- SRC-001 and SRC-003 both treat evaluation as a central challenge for autonomous and multi-agent systems.

## Trace Targets

- review-output protocol
- completion gate
- blocked revision routing

## Limits

Feedback loops need stable findings and evidence. Vague review comments are not enough to support reliable revision.
