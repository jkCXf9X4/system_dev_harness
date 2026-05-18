# Requirements

Requirement IDs are stable anchors for traceability. If a requirement changes meaning, create a new ID instead of silently reusing the old one.

## Functional Requirements

| ID | Requirement |
| --- | --- |
| FR-001 | The harness shall accept a rough development task as input. |
| FR-002 | The harness shall produce a checklistable requirement contract. |
| FR-003 | The harness shall define in-scope work, out-of-scope work, acceptance criteria, and completion rules. |
| FR-004 | The harness shall produce architecture and integration guardrails. |
| FR-005 | The harness shall check the task against persistent known mistakes. |
| FR-006 | The harness shall produce an implementation packet for an external coding agent. |
| FR-007 | The harness shall produce a paste-ready external agent handoff. |
| FR-008 | The harness shall run independent reviewer agents across requirements, architecture, QA, completeness, and known mistakes. |
| FR-009 | The harness shall support role-specific model configuration. |
| FR-010 | The harness shall preserve workflow state across graph steps. |
| FR-011 | The harness shall support stable thread IDs for checkpointed execution. |
| FR-012 | The harness shall run from the command line. |
| FR-013 | The harness shall produce a completion decision of approved, blocked, or waiver_required. |
| FR-014 | The harness shall require explicit waivers for incomplete contract items. |
| FR-015 | The harness shall produce a final control report that combines all artifacts. |
| FR-016 | The harness shall accept a versioned known-mistakes file. |
| FR-017 | The harness shall accept external implementation evidence such as changed files, diffs, test output, and agent output. |
| FR-018 | The harness shall validate LLM-generated control artifacts against structured schemas. |
| FR-019 | The harness shall route approved, blocked, and waiver-required outcomes through explicit graph branches. |
| FR-020 | The harness shall ground architecture/context generation in versioned project documentation by default. |

## Quality Requirements

| ID | Requirement |
| --- | --- |
| QR-001 | Design choices shall be traceable to documented goals or use cases. |
| QR-002 | The harness shall avoid direct code modification until external agent handoff is mature. |
| QR-003 | Model provider details shall be isolated from graph workflow logic. |
| QR-004 | Prompts shall be role-specific and inspectable in source control. |
| QR-005 | Documentation shall include decision records for material design choices. |
| QR-006 | The system shall prefer explicit human approval points over hidden autonomy. |
| QR-007 | The first implementation shall remain lightweight enough to run locally. |
| QR-008 | Completion shall be contract-driven rather than based on plausible output. |
| QR-009 | Reviewer approval shall not silently override incomplete contract items. |
| QR-010 | Completion status shall be computed by deterministic gate logic, not only by an LLM prompt. |
| QR-011 | Reviewer agents shall run as independent nodes rather than one simulated council prompt. |

## Constraints

| ID | Constraint |
| --- | --- |
| C-001 | Python is the initial implementation language. |
| C-002 | LangGraph is the initial workflow orchestration framework. |
| C-003 | OpenRouter is the initial model access layer. |
| C-004 | The first graph checkpoint implementation may be in-memory. |
| C-005 | Secrets must be provided through environment variables and must not be committed. |
| C-006 | Persistent mistake memory starts as versioned markdown, with YAML lesson input supported. |

## Open Questions

| ID | Question |
| --- | --- |
| OQ-001 | What project context should be attached first: repository files, architecture docs, issue tracker data, or stakeholder notes? |
| OQ-002 | Should durable persistence use SQLite, Postgres, Redis, or LangGraph Platform later? |
| OQ-003 | Which human approval steps should become hard interrupts rather than generated checklist items? |
| OQ-004 | When should the harness move from external handoff packets to built-in code editing? |
| OQ-005 | Should LiteLLM be introduced later as an owned model gateway, or is direct OpenRouter enough? |
