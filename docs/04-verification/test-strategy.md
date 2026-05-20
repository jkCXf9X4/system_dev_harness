# Test Strategy

## Verification Approach

Verification is distributed across multiple workflow stages:

1. **Verifier stage** (`orchestrator-verifier`): Runs focused checks against the implementation packet and captures evidence. Shell-capable, edit-incapable. Verifies file content, permission integrity, and information hygiene.

2. **Independent review stages** (`orchestrator-review-*`): Five reviewers independently evaluate requirements, architecture, completeness, lessons, and QA. Read-only. Structured findings with stable item IDs.

3. **Completion gate** (`orchestrator-reviewer`): Aggregates all review findings with verifier evidence. Produces `approved`, `blocked`, or `waiver_required`. The revision loop routes `blocked` back to planner.

4. **Smoke tests** (`tests/test_opencode_workflow_probes.py`): Run against a fixture project to verify agent routing, template references, and control-policy enforcement. Run manually via `pytest`.

## Types of Verification

- **Structural verification**: agent prompt content, permission blocks, template references
- **Workflow verification**: route correctness, gate behavior, revision loop routing
- **Information hygiene**: stale references, duplicate content, orphaned artifacts
- **Traceability**: decision records, layer placement, cross-layer links