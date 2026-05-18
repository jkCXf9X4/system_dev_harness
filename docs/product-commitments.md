# Product Commitments

Product commitments translate the product vision into durable promises the harness should preserve across implementation changes.

They are more stable than implementation plans and more concrete than vision statements. They should not describe package names, function names, model prompts, or execution details.

## Commitments

| ID | Commitment |
| --- | --- |
| PC-001 | The harness shall keep development work anchored to an explicit task contract. |
| PC-002 | The harness shall make architecture and requirement drift visible before work is considered complete. |
| PC-003 | The harness shall use persistent mistake memory to reduce repeated correction loops. |
| PC-004 | The harness shall separate execution from approval so coding output is reviewed against evidence. |
| PC-005 | The harness shall require incomplete work to be blocked or explicitly waived rather than silently accepted. |
| PC-006 | The harness shall keep design rationale traceable without coupling product intent to implementation details. |

## Trace Links

| Commitment | Satisfies |
| --- | --- |
| PC-001 | Vision: governed contract loop |
| PC-002 | Vision: architecture preservation over locally convenient implementation |
| PC-003 | Vision: persistent mistake memory over repeating the same correction loop |
| PC-004 | Vision: reviewer approval over self-assessed completion |
| PC-005 | Vision: explicit waivers over silent requirement loss |
| PC-006 | Vision: configurable, inspectable control system |
