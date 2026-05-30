# Knowledge Map

This map connects research-backed claims to the current workflow concepts. It is descriptive only; it does not modify runtime behavior.

| Workflow concept | Relevant claims | Why it matters |
| --- | --- | --- |
| Orchestrator as dispatcher | AK-001, AK-007 | Keeps role boundaries explicit and preserves handoff discipline. |
| Planner stage | AK-001, AK-002, AK-005 | Separates request normalization from repository inspection and later implementation. |
| Discovery stage | AK-002, AK-003, AK-006 | Grounds downstream reasoning in inspected repository evidence. |
| Contract stage | AK-002, AK-008 | Converts context into criteria that can be reviewed and verified. |
| Architecture stage | AK-001, AK-002, AK-008 | Applies design constraints before implementation choices are made. |
| Lessons stage | AK-005, AK-006 | Applies persistent feedback without relying on ephemeral conversation memory. |
| Packet and handoff stages | AK-003, AK-007 | Preserve constraints and required checks across execution boundaries. |
| Builder stage | AK-003, AK-006 | Uses the code-facing interface to make scoped changes and collect evidence. |
| Verifier stage | AK-006, AK-008 | Checks concrete results rather than relying on implementation self-report. |
| Independent review stages | AK-004, AK-008 | Provide feedback and catch missing evidence, drift, or incomplete work. |
| Completion gate | AK-004, AK-008 | Aggregates evidence and review findings into a deterministic outcome. |
| Improvement workflow | AK-004, AK-005, AK-008 | Turns recurring pressure into backlog candidates without expanding delivery scope. |

## Trace Use

Future product decisions or prompt changes can cite this map plus the relevant claim files. Runtime files should not depend on this directory unless a later decision explicitly moves selected knowledge into copied agent context.
