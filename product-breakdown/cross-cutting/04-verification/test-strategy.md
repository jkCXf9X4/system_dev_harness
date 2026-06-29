# Test Strategy

## Verification Approach

Verification is distributed across multiple workflow stages:

1. **Reviewer-coordinated verifier helper** (`orchestrator-verifier`): Runs focused checks against the planner work order and implementation evidence. Shell-capable, edit-incapable. Verifies file content, permission integrity, and information hygiene.

2. **Independent review helpers** (`orchestrator-review-*`): Reviewers independently evaluate the domains triggered by task risk: contract satisfaction, acceptance criteria, test adequacy, architecture, code quality, cleanliness, completeness, information hygiene, and lessons. Read-only. Structured findings with stable item IDs. Independent helpers should run as parallel-safe packets when their inputs are available and they do not depend on each other's results.

3. **Completion gate** (`orchestrator-reviewer`): Aggregates all review findings with verifier evidence. Produces `approved`, `blocked`, or `waiver_required`. The revision loop routes `blocked` back to planner.

4. **Smoke tests** (`tests/test_opencode_workflow_probes.py`): Run against a fixture project to verify agent routing, template references, and control-policy enforcement. Run manually via `pytest`.

## Types of Verification

- **Structural verification**: agent prompt content, permission blocks, template references
- **Workflow verification**: route correctness, gate behavior, revision loop routing
- **Parallel helper verification**: planner and reviewer prompts include parallel helper packets, dependencies, expected outputs, `parallel_safe`, and `file_write_set`
- **Information hygiene**: stale references, status trackers, duplicate content, orphaned artifacts, unresolved links, and traceability cleanup
- **Traceability**: decision records, layer placement, cross-layer links
