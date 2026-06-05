# Candidate Capture Guidance

Candidate capture uses the normal guarded chain:

```text
planner -> builder -> reviewer -> reflection -> reporter
```

The planner selects `workflow_mode: candidate_capture` when the user asks for a proposal, recommendation, evaluation, discovery, documented candidate, future task seed, or backlog item instead of immediate implementation.

In candidate-capture mode:

- planner uses the normal directed helpers for evidence, requirements, architecture pressure, lessons, memory, and research
- builder persists only improvement backlog artifacts under `product-breakdown/06-evolution/`
- reviewer gates the persisted candidate artifacts as information artifacts
- reflection handles durable memory triage
- reporter summarizes the candidate disposition and next action

Standalone improvement and evaluator agents are not part of the guarded workflow. Candidate persistence has one owner: the builder in `workflow_mode: candidate_capture`.
