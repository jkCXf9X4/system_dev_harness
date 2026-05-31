# AK-008: Evaluate Agent Output Against Evidence

## Claim

Agent outputs should be judged against task criteria, environment evidence, and failure modes rather than the agent's confidence or plausibility.

## Practical Interpretation

Prompts should require verifiable acceptance criteria, command output, changed-file evidence, review findings, and explicit blocked or waiver-required outcomes when evidence is incomplete.

## Applies To

- Contract
- Verifier
- Review agents
- Completion gate
- Reporter

## Evidence

- SRC-001 surveys evaluation strategies for LLM-based autonomous agents and identifies evaluation as a key part of the field.
- SRC-003 summarizes benchmarks and challenges for LLM-based multi-agent systems.
- SRC-006 supports feedback-driven correction based on evaluation signals.

## Trace Targets

- requirement contract checklist
- verifier evidence
- review-output protocol
- deterministic completion gate

## Limits

Evidence quality depends on the checks selected. Passing a weak check is not proof that the task is complete.
