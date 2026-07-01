# Common Policies

**Directives for all agents:**

1. If there is an obvious better or more correct answer than what was requested, flag this to the user before proceeding. Do not silently substitute your own judgment for the user's intent.
2. Apply `agent-boundaries.md` for read/write boundaries and scope containment.
3. Apply `stage-output-schema.md` for common output fields.
4. Apply `subagent-lifecycle.md` before sending follow-up work to an existing helper.
5. For system-definition work, apply `product-breakdown-work.md`.
6. For lessons/memory, apply `memory-and-lessons.md`.
7. Read-only agents: do not modify files using Edit or Write. Return blocking gaps, required follow-up, or `improvement_candidates` instead.
8. When the work order includes `workflow_mode: candidate_capture`, load `.opencode/dev_harness/workflow/candidate-capture.md`.