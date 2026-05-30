# AK-003: Connect Reasoning With Tool And Environment Actions

## Claim

Agents perform better on interactive tasks when reasoning and actions inform each other, rather than treating tool use as an unrelated final step.

## Practical Interpretation

Prompts should require agents to state what evidence they inspected, what actions they performed, and how those actions affect the plan or verification result. Action-capable stages should stay scoped to their assigned role.

## Applies To

- Discovery
- Builder
- Verifier
- Researcher

## Evidence

- SRC-004 introduces a pattern where reasoning traces and task-specific actions are interleaved so actions can gather external information and reasoning can update plans.
- SRC-007 shows that software agents benefit from interfaces that make repository navigation, editing, and testing explicit.

## Trace Targets

- bash-capable agent prompts
- evidence reporting requirements
- verifier command output summaries

## Limits

This claim supports evidence-aware tool use. It does not justify unrestricted search, shell access, or scope expansion.
