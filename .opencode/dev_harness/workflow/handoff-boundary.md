# Handoff Boundary

Purpose: Defines constraints for external or manual implementation handoffs.

External or manual handoff is non-executing guidance unless the orchestrator explicitly uses it as builder-stage input.

Any external or manual implementation must produce builder-equivalent evidence and still pass reviewer-coordinated verification, independent reviews, completion gate, and final reporting.

A handoff cannot authorize scope expansion, skipped checks, direct approval, or waived failures.

## File-Based Handoff Methodology

The file-based handoff methodology is the standard for all agent-to-agent handoffs within the guarded workflow.

### Rules

1. **Minimal inline fields**: Only `task_id`, `plan_file_path`, `status`, and `key_evidence` are passed inline between agents.
2. **Full context on disk**: Each stage writes its complete output to a handoff file before returning.
3. **Pre-consumption integrity check**: Every stage must verify file existence and non-emptiness before loading a handoff file.
4. **Schema versioning**: Every handoff file includes `schema_version` for version-aware validation.
5. **Handoff file location**: Files are stored under `.opencode/dev_harness_handoffs/` with the naming convention `<timestamp>-<task_id>-<stage>.md`.

### Exceptions

The initial Router-to-Planner handoff may pass the raw user request inline since there is no prior handoff file to reference. All other handoffs must use the file-based methodology.

