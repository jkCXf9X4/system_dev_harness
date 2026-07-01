# Builder Triggers

Purpose: Defines builder-stage helper triggers for adaptive risk-based helper selection.

- Build, test, type-check, or dependency failures that need isolated diagnosis may use `orchestrator-build-error-resolver`.
- Created, moved, renamed, rewritten, replaced, deleted, or superseded artifacts that require reference patching, tracker/index updates, duplicate reconciliation, orphan cleanup, link checks, or traceability cleanup may use `orchestrator-cleanup`.
- External dependency, API, framework, standard, version, or documentation uncertainty during implementation may use `orchestrator-researcher`.
- Noteworthy cleanup or information-hygiene findings outside the approved scope may be returned as `improvement_candidates` instead of expanding the current task.

