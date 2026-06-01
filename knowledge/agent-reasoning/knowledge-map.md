# Knowledge Map

This map connects research-backed claims to the current workflow concepts. It is descriptive only; it does not modify runtime behavior.

| Workflow concept | Relevant claims | Why it matters |
| --- | --- | --- |
| Orchestrator as dispatcher | AK-001, AK-007 | Keeps role boundaries explicit and preserves handoff discipline. |
| Planner stage | AK-001, AK-002, AK-005, AK-009 | Separates request normalization from repository inspection and later implementation while treating memory-derived assumptions as reviewable inputs. |
| Discovery stage | AK-002, AK-003, AK-006 | Grounds downstream reasoning in inspected repository evidence. |
| Contract stage | AK-002, AK-008 | Converts context into criteria that can be reviewed and verified. |
| Architecture stage | AK-001, AK-002, AK-008 | Applies design constraints before implementation choices are made. |
| Lessons stage | AK-005, AK-006, AK-009 | Applies persistent feedback without relying on ephemeral conversation memory, while checking whether retrieved lessons still apply. |
| Memory helper and curator | AK-005, AK-009 | Retrieve and persist durable workflow memory only when it is scoped, useful, and reviewable. |
| Packet and handoff stages | AK-003, AK-007 | Preserve constraints and required checks across execution boundaries. |
| Builder stage | AK-003, AK-006 | Uses the code-facing interface to make scoped changes and collect evidence. |
| Verifier stage | AK-006, AK-008 | Checks concrete results rather than relying on implementation self-report. |
| Independent review stages | AK-004, AK-008, AK-009 | Provide feedback and catch missing evidence, drift, stale memory, or incomplete work. |
| Completion gate | AK-004, AK-008 | Aggregates evidence and review findings into a deterministic outcome. |
| Improvement workflow | AK-004, AK-005, AK-008, AK-009 | Turns recurring pressure into backlog candidates without expanding delivery scope and keeps improvement candidates separate from durable memory. |

## Trace Use

Future product decisions or prompt changes can cite this map plus the relevant claim files. Runtime files should not depend on this directory unless a later decision explicitly moves selected knowledge into copied agent context.
