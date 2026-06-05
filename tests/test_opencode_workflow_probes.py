from __future__ import annotations

import json
import subprocess
from pathlib import Path


# Keep prompt assertions behavior-oriented. See tests/README.md before adding
# exact string checks against agent prompts.


def as_text(value: str | bytes | None) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    return value or ""


def run_opencode(
    project: Path,
    env: dict[str, str],
    *,
    agent: str,
    title: str,
    prompt: str,
    timeout: int = 30,
) -> tuple[int, str]:
    cmd = [
        "opencode",
        "run",
        "--format",
        "default",
        "--print-logs",
        "--pure",
        "--title",
        title,
        "--agent",
        agent,
        prompt,
    ]

    try:
        completed = subprocess.run(
            cmd,
            cwd=project,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        output = as_text(completed.stdout) + as_text(completed.stderr)
        return completed.returncode, output
    except subprocess.TimeoutExpired as exc:
        output = as_text(exc.stdout) + as_text(exc.stderr)
        return 124, output


def assert_output_contains(output: str, needle: str) -> None:
    assert needle in output, f"missing {needle!r}\n\nlast output:\n{output[-2000:]}"


def read_prompt(project: Path, relative_path: str) -> str:
    return (project / relative_path).read_text(encoding="utf-8")


def test_contract_stage_smoke(simple_project: Path, opencode_env: dict[str, str]) -> None:
    status, output = run_opencode(
        simple_project,
        opencode_env,
        agent="orchestrator-contract",
        title="contract_stage",
        prompt="Create a requirement contract for adding a verification probes section to the repository.",
        timeout=30,
    )

    assert status in {0, 124}
    assert_output_contains(output, "Falling back to default agent")
    prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-contract.md")
    assert "requirements contract stage" in prompt.lower()
    assert "verifiable contract" in prompt.lower()


def test_build_stage_smoke(simple_project: Path, opencode_env: dict[str, str]) -> None:
    status, output = run_opencode(
        simple_project,
        opencode_env,
        agent="build",
        title="build_stage",
        prompt="Fix a tiny typo in README.",
        timeout=20,
    )

    assert status in {0, 124}
    assert_output_contains(output, "agent=build mode=primary")


def test_direct_build_agent_does_not_inherit_orchestrator_prompt(simple_project: Path) -> None:
    config = json.loads(read_prompt(simple_project, "opencode.json"))
    instructions = config.get("instructions", [])
    package_instructions = read_prompt(simple_project, ".opencode/instructions.md").lower()

    assert config["default_agent"] == "orchestrator"
    assert ".opencode/instructions.md" in instructions
    assert ".opencode/agents/orchestrator.md" not in instructions
    assert "currently selected agent" in package_instructions
    assert "normal `build` agent" in package_instructions
    assert "outside the guarded orchestrator path" in package_instructions
    assert "do not invoke planner, builder, reviewer, reporter" in package_instructions


def test_candidate_capture_uses_full_guarded_chain(simple_project: Path) -> None:
    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    reflection_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reflection.md").lower()
    reporter_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reporter.md").lower()
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()
    candidate_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/candidate-capture.md").lower()

    assert '"orchestrator-improvement": allow' not in orchestrator_prompt
    assert "workflow_mode: candidate_capture" in orchestrator_prompt
    assert "same builder, reviewer, reflection, and reporter chain" in orchestrator_prompt

    assert "`workflow_mode`: `candidate_capture`" in planner_prompt
    assert "`route`: `guarded_chain`" in planner_prompt
    assert "candidate-capture.md" in planner_prompt

    assert "for `workflow_mode: candidate_capture`" in builder_prompt
    assert "persist improvement backlog artifacts instead of implementation changes" in builder_prompt
    assert "candidate-capture.md" in builder_prompt
    assert "candidate-capture disposition" in builder_prompt

    assert "for `workflow_mode: candidate_capture`" in reviewer_prompt
    assert "same completion gate" in reviewer_prompt
    assert "candidate-capture.md" in reviewer_prompt

    assert "workflow_mode: candidate_capture" in reflection_prompt
    assert "candidate-capture.md" in reporter_prompt
    assert "both workflow modes use the same guarded chain" in control_policy
    assert "builder is the only workflow stage that persists improvement backlog artifacts" in candidate_policy
    assert "should write backlog-worthy candidates to file before returning" in candidate_policy
    assert "do not create a placeholder file" in candidate_policy


def test_candidate_capture_has_single_persistence_owner(simple_project: Path) -> None:
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    reporter_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reporter.md").lower()
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()
    candidate_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/candidate-capture.md").lower()

    assert not (simple_project / ".opencode/agents/orchestrator-improvement.md").exists()
    assert not (simple_project / ".opencode/agents/orchestrator-improvement-evaluator.md").exists()
    assert "candidate-capture.md" in control_policy
    assert "builder is the only workflow stage that persists improvement backlog artifacts" in candidate_policy
    assert "persist improvement backlog artifacts instead of implementation changes" in builder_prompt
    assert "save every backlog-worthy candidate to disk before returning" in builder_prompt
    assert "request a follow-up `workflow_mode: candidate_capture` run" in reporter_prompt
    assert "evaluator" not in reporter_prompt


def test_decision_templates_are_generic_and_referenced(simple_project: Path) -> None:
    architecture_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-architecture.md")
    review_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-architecture.md")
    architecture_guidance = read_prompt(simple_project, ".opencode/dev_harness/workflow/architecture-guidance.md").lower()
    decision_placement = read_prompt(
        simple_project,
        ".opencode/dev_harness/product-breakdown/decision-placement.md",
    )
    decision_template = read_prompt(
        simple_project,
        ".opencode/dev_harness/product-breakdown/templates/decision-template.md",
    )
    decision_log_entry = read_prompt(
        simple_project,
        ".opencode/dev_harness/product-breakdown/templates/decision-log-entry-template.md",
    )

    assert "decision-template.md" in architecture_guidance
    assert "decision-log-entry-template.md" in architecture_guidance
    assert "architecture-guidance.md" in architecture_prompt.lower()
    assert "architecture-guidance.md" in review_prompt.lower()
    assert "treat unknown architecture as risk" in architecture_guidance
    assert "context expectations" in architecture_guidance
    assert "caller-provided implementation evidence" in review_prompt.lower()
    assert "product-breakdown/" in architecture_guidance
    assert "where its consequences are most directly felt" in decision_placement.lower()
    assert "durable product breakdown decisions" in decision_template.lower()
    assert "decision log entry template" in decision_log_entry.lower()
    assert "ssp_references" not in decision_template
    assert "ssp_references" not in decision_log_entry
    assert "product-breakdown/adr/README.md" not in decision_template
    assert "product-breakdown/adr/README.md" not in decision_log_entry


def test_product_breakdown_usage_is_embedded_in_agent_workflow(simple_project: Path) -> None:
    agents = [
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-discovery.md",
        ".opencode/agents/orchestrator-contract.md",
        ".opencode/agents/orchestrator-architecture.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-completeness.md",
        ".opencode/agents/orchestrator-reviewer.md",
    ]

    for agent_path in agents:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "product breakdown" in prompt or "product-breakdown" in prompt

    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    verifier_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-verifier.md").lower()
    completeness_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-completeness.md").lower()
    gate_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    product_breakdown_readme = read_prompt(
        simple_project,
        ".opencode/dev_harness/product-breakdown/README.md",
    ).lower()

    assert "intent, product behavior, architecture, implementation, verification, operation, and evolution" in product_breakdown_readme
    assert "primary layer" in planner_prompt
    assert "planner work order" in verifier_prompt
    assert "product-breakdown-work.md" in verifier_prompt
    assert "product-breakdown-work.md" in completeness_prompt
    assert "product breakdown evidence" in gate_prompt


def test_docs_and_product_breakdown_boundaries_are_explicit(simple_project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    docs_readme = read_prompt(repo_root, "docs/README.md").lower()
    docs_product_breakdown = read_prompt(repo_root, "docs/product-breakdown.md").lower()
    product_breakdown_readme = read_prompt(repo_root, "product-breakdown/README.md").lower()
    operation_requirements = read_prompt(repo_root, "product-breakdown/05-operation/runbook.md").lower()
    deployment_requirements = read_prompt(repo_root, "product-breakdown/05-operation/deployment-process.md").lower()
    copied_guidance = read_prompt(
        simple_project,
        ".opencode/dev_harness/product-breakdown/README.md",
    ).lower()

    assert "runnable guidance" in docs_readme
    assert "command examples" in docs_readme
    assert "link to them for product context" in docs_readme

    assert "product facts" in docs_product_breakdown
    assert "runnable instructions" in docs_product_breakdown
    assert "link to these product-breakdown pages" in docs_product_breakdown

    assert "product source information" in product_breakdown_readme
    assert "use `docs/` for runnable" in product_breakdown_readme
    assert "do not duplicate" in product_breakdown_readme

    assert "use `docs/` for runnable guidance" in copied_guidance
    assert "usage guides" in copied_guidance

    for product_doc in (operation_requirements, deployment_requirements):
        assert "runnable" in product_doc
        assert "requirements" in product_doc
        assert "```" not in product_doc
        assert "opencode run" not in product_doc


def test_orchestrator_does_not_route_shortcut_build(simple_project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md")
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md")
    architecture_doc = read_prompt(repo_root, "product-breakdown/02-architecture/architecture.md")

    for content in (orchestrator_prompt, planner_prompt, architecture_doc):
        lowered = content.lower()
        assert "small-task handoff" not in lowered
        assert "compact handoff" not in lowered
        assert "shortcut path" not in lowered


def test_information_hygiene_is_workflow_gated(simple_project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    contract_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-contract.md")
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md")
    verifier_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-verifier.md")
    completeness_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-completeness.md")
    gate_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md")
    architecture_doc = read_prompt(repo_root, "product-breakdown/02-architecture/architecture.md")
    commitments_doc = read_prompt(repo_root, "product-breakdown/01-product/product-commitments.md")
    information_hygiene_policy = read_prompt(
        simple_project,
        ".opencode/dev_harness/workflow/information-hygiene.md",
    )

    for content in (
        contract_prompt,
        builder_prompt,
        verifier_prompt,
        completeness_prompt,
        gate_prompt,
        information_hygiene_policy,
        architecture_doc,
        commitments_doc,
    ):
        lowered = content.lower()
        assert "information hygiene" in lowered or "information-hygiene" in lowered

    policy = information_hygiene_policy.lower()
    assert "traceability" in policy
    assert "stale references" in policy
    assert "duplicate content" in policy
    assert "orphaned artifacts" in policy


def test_agent_control_policy_closes_escape_hatches(simple_project: Path) -> None:
    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    contract_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-contract.md").lower()
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    verifier_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-verifier.md").lower()
    gate_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()

    assert "control-policy.md" not in orchestrator_prompt
    assert "temperature: 0.0" in orchestrator_prompt
    assert '"*": deny' in orchestrator_prompt
    for denied_permission in (
        "read: deny",
        "glob: deny",
        "grep: deny",
        "list: deny",
        "edit: deny",
        "bash: deny",
    ):
        assert denied_permission in orchestrator_prompt

    assert "do not inspect repository files" in orchestrator_prompt
    assert "do not classify the request" in orchestrator_prompt
    assert "planner decides workflow type" in orchestrator_prompt
    assert "do not evaluate implementation evidence" in orchestrator_prompt
    assert "do not invoke directed helpers" in orchestrator_prompt
    assert "use only prior stage outputs, reviewer gate labels, and user decisions" in orchestrator_prompt
    assert "workflow_mode: candidate_capture" in orchestrator_prompt
    assert "orchestrator-builder" in orchestrator_prompt
    assert "workflow_type: improvement" not in orchestrator_prompt
    assert "route: improvement" not in orchestrator_prompt
    assert "call `orchestrator-planner` again with the corrected outcome" in orchestrator_prompt

    assert "every listed top-level guarded workflow stage must run" in control_policy
    assert "not_applicable" in control_policy
    assert "waivers are not approvals" in control_policy

    for prompt in (planner_prompt, contract_prompt):
        assert "touches_information_artifacts" in prompt
        assert "touches_product_breakdown" in prompt
        assert "requires_decision_record" in prompt

    assert "handoff_required" in planner_prompt
    assert "builder-equivalent evidence" in control_policy
    assert "cannot authorize scope expansion" in control_policy

    assert "revised through the guarded workflow" in builder_prompt
    assert "control-policy.md" in verifier_prompt
    assert "control-policy.md" in gate_prompt
    assert "explicit user approval" in control_policy
    assert "not `approved`" in control_policy


def test_planner_routes_candidate_capture_by_requested_outcome(simple_project: Path) -> None:
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()

    assert "separate the subject from the requested outcome" in planner_prompt
    assert "`issue_kind`: bug, fix, regression" in planner_prompt
    assert "`requested_outcome`: `implement_now`" in planner_prompt
    assert "`requested_outcome`: `capture_candidate`" in planner_prompt
    assert "`workflow_mode`: `delivery`" in planner_prompt
    assert "`workflow_mode`: `candidate_capture`" in planner_prompt
    assert "`route`: `guarded_chain`" in planner_prompt
    assert "a bug, fix, regression, feature, or documentation subject can still use `workflow_mode: candidate_capture`" in planner_prompt
    assert "do not classify a candidate/backlog request as delivery only because the subject is a bug or fix" in planner_prompt


def test_top_level_flow_and_directed_helpers_are_explicit(simple_project: Path) -> None:
    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    implementation_doc = read_prompt(
        simple_project,
        ".opencode/dev_harness/workflow/control-policy.md",
    ).lower()

    for top_level_stage in (
        "orchestrator-planner",
        "orchestrator-builder",
        "orchestrator-reviewer",
        "orchestrator-reporter",
    ):
        assert f'"{top_level_stage}": allow' in orchestrator_prompt

    assert '"orchestrator-improvement": allow' not in orchestrator_prompt

    for directed_helper in (
        "orchestrator-discovery",
        "orchestrator-contract",
        "orchestrator-architecture",
        "orchestrator-lessons",
        "orchestrator-memory",
        "orchestrator-memory-curator",
        "orchestrator-build-error-resolver",
        "orchestrator-cleanup",
        "orchestrator-verifier",
        "orchestrator-review-architecture",
        "orchestrator-review-completeness",
        "orchestrator-review-lessons",
        "orchestrator-researcher",
    ):
        assert f'"{directed_helper}": allow' not in orchestrator_prompt

    for helper in (
        "orchestrator-architecture",
        "orchestrator-memory",
        "test planning",
        "product-breakdown placement",
        "workflow_mode",
    ):
        assert helper in planner_prompt

    for helper in (
        "orchestrator-build-error-resolver",
        "orchestrator-cleanup",
        "orchestrator-researcher",
    ):
        assert helper in builder_prompt

    for helper in (
        "acceptance criteria",
        "orchestrator-memory",
        "orchestrator-review-architecture",
        "orchestrator-review-completeness",
    ):
        assert helper in reviewer_prompt

    for removed_helper in (
        "orchestrator-plan-test-architect",
        "orchestrator-plan-product-architect",
        "orchestrator-review-qa",
        "orchestrator-review-requirements",
    ):
        assert removed_helper not in planner_prompt
        assert removed_helper not in reviewer_prompt
        assert not (simple_project / ".opencode" / "agents" / f"{removed_helper}.md").exists()

    assert "planner-owned" in implementation_doc
    assert "reviewer-coordinated verification" in implementation_doc


def test_builder_cleanup_helper_is_scoped_and_wired(simple_project: Path) -> None:
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    cleanup_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-cleanup.md").lower()
    information_hygiene = read_prompt(
        simple_project,
        ".opencode/dev_harness/workflow/information-hygiene.md",
    ).lower()
    architecture_doc = read_prompt(
        Path(__file__).resolve().parents[1],
        "product-breakdown/02-architecture/architecture.md",
    ).lower()
    implementation_doc = read_prompt(
        Path(__file__).resolve().parents[1],
        "product-breakdown/03-implementation/implementation.md",
    ).lower()

    assert '"orchestrator-cleanup": allow' in builder_prompt
    assert "focused cleanup after implementation" in builder_prompt
    assert "cleanup helper result" in builder_prompt

    assert "cleanup helper for the builder stage" in cleanup_prompt
    assert "approved builder work order" in cleanup_prompt
    assert "status trackers" in cleanup_prompt
    assert "duplicate, superseded, contradictory, or orphaned information" in cleanup_prompt
    assert "product-breakdown-work.md" in cleanup_prompt
    assert "improvement_candidates" in cleanup_prompt
    assert "stage-output-schema.md" in cleanup_prompt
    assert "agent-boundaries.md" in cleanup_prompt

    assert "orchestrator-cleanup" in information_hygiene
    assert "status tracker updates" in information_hygiene
    assert "traceability cleanup" in information_hygiene
    assert "cleanup helper" in architecture_doc
    assert "orchestrator-cleanup.md" in implementation_doc


def test_builder_can_run_review_helper_passes_without_becoming_the_gate(simple_project: Path) -> None:
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    implementation_doc = read_prompt(
        Path(__file__).resolve().parents[1],
        "product-breakdown/03-implementation/implementation.md",
    ).lower()

    for helper in (
        "orchestrator-verifier",
        "orchestrator-review-completeness",
        "orchestrator-review-architecture",
        "orchestrator-review-lessons",
        "orchestrator-memory",
    ):
        assert f'"{helper}": allow' in builder_prompt

    assert "builder-owned review pass" in builder_prompt
    assert "review-helper routing" in implementation_doc
    assert "builder-owned review pass" in implementation_doc
    assert "review coordinator and completion gate" in reviewer_prompt
    assert "return one of:" in reviewer_prompt
    assert "approved" in reviewer_prompt
    assert "blocked" in reviewer_prompt
    assert "waiver_required" in reviewer_prompt


def test_structured_feedback_protocol_is_shared(simple_project: Path) -> None:
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()
    stage_schema = read_prompt(simple_project, ".opencode/dev_harness/workflow/stage-output-schema.md").lower()
    agent_paths = [
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-discovery.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-reviewer.md",
        ".opencode/agents/orchestrator-reporter.md",
        ".opencode/agents/orchestrator-researcher.md",
        ".opencode/agents/orchestrator-memory.md",
        ".opencode/agents/orchestrator-memory-curator.md",
        ".opencode/agents/orchestrator-build-error-resolver.md",
        ".opencode/agents/orchestrator-cleanup.md",
        ".opencode/agents/orchestrator-review-architecture.md",
    ]

    for field in (
        "user_feedback_required",
        "user_feedback_request",
        "improvement_candidates",
        "research_requests",
    ):
        assert field in stage_schema

    assert "stage-output-schema.md" in control_policy
    assert "not_applicable" in stage_schema
    assert "clarification_status" in stage_schema

    for agent_path in agent_paths:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "stage-output-schema.md" in prompt


def test_shared_boundary_and_product_breakdown_policy_are_extracted(simple_project: Path) -> None:
    agent_boundaries = read_prompt(simple_project, ".opencode/dev_harness/workflow/agent-boundaries.md").lower()
    product_breakdown_work = read_prompt(simple_project, ".opencode/dev_harness/workflow/product-breakdown-work.md").lower()
    implementation_doc = read_prompt(
        Path(__file__).resolve().parents[1],
        "product-breakdown/03-implementation/implementation.md",
    ).lower()

    for phrase in (
        "read-only agents",
        "editing agents",
        "do not broaden scope",
        "candidate_capture",
    ):
        assert phrase in agent_boundaries

    for phrase in (
        "loading rules",
        "placement rules",
        "required evidence",
        "traceability updates",
        "decision-record update",
    ):
        assert phrase in product_breakdown_work

    for agent_path in (
        ".opencode/agents/orchestrator.md",
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-cleanup.md",
        ".opencode/agents/orchestrator-contract.md",
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-completeness.md",
    ):
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "agent-boundaries.md" in prompt

    for agent_path in (
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-cleanup.md",
        ".opencode/agents/orchestrator-contract.md",
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-completeness.md",
    ):
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "product-breakdown-work.md" in prompt

    assert "stage-output-schema.md" in implementation_doc
    assert "agent-boundaries.md" in implementation_doc
    assert "product-breakdown-work.md" in implementation_doc


def test_directed_agents_can_use_researcher(simple_project: Path) -> None:
    agent_paths = [
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-reviewer.md",
        ".opencode/agents/orchestrator-discovery.md",
        ".opencode/agents/orchestrator-contract.md",
        ".opencode/agents/orchestrator-architecture.md",
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-completeness.md",
        ".opencode/agents/orchestrator-cleanup.md",
    ]

    for agent_path in agent_paths:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "orchestrator-researcher" in prompt


def test_working_agents_surface_incidental_improvement_candidates_without_writer_duplication(simple_project: Path) -> None:
    agent_paths = [
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-reviewer.md",
        ".opencode/agents/orchestrator-reporter.md",
        ".opencode/agents/orchestrator-researcher.md",
        ".opencode/agents/orchestrator-discovery.md",
        ".opencode/agents/orchestrator-contract.md",
        ".opencode/agents/orchestrator-architecture.md",
        ".opencode/agents/orchestrator-lessons.md",
        ".opencode/agents/orchestrator-build-error-resolver.md",
        ".opencode/agents/orchestrator-cleanup.md",
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-architecture.md",
        ".opencode/agents/orchestrator-review-completeness.md",
        ".opencode/agents/orchestrator-review-lessons.md",
        ".opencode/agents/orchestrator-memory.md",
        ".opencode/agents/orchestrator-memory-curator.md",
    ]

    for agent_path in agent_paths:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "stage-output-schema.md" in prompt or "improvement_candidates" in prompt

    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md")
    assert "orchestrator-improvement" not in orchestrator_prompt
    assert not (simple_project / ".opencode/agents/orchestrator-improvement.md").exists()
    assert not (simple_project / ".opencode/agents/orchestrator-improvement-evaluator.md").exists()


def test_workflow_memory_layer_is_versioned_and_scoped(simple_project: Path) -> None:
    lessons = read_prompt(simple_project, ".opencode/dev_harness_memories/lessons.md").lower()
    patterns = read_prompt(simple_project, ".opencode/dev_harness_memories/patterns.md").lower()
    memory_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-memory.md").lower()
    curator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-memory-curator.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    reflection_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reflection.md").lower()
    reporter_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reporter.md").lower()
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()
    workflow_memory = read_prompt(simple_project, ".opencode/dev_harness/workflow/workflow-memory.md").lower()
    review_output = read_prompt(simple_project, ".opencode/dev_harness/workflow/review-output.md").lower()
    memories_readme = read_prompt(simple_project, ".opencode/dev_harness_memories/README.md").lower()

    assert "repo-local workflow memory" in lessons
    assert "km-001" in lessons
    assert "metadata:" in lessons
    assert "revalidation trigger:" in lessons
    assert "pat-000" in patterns
    assert "pat-001: surgical goal-driven changes" in patterns
    assert "metadata:" in patterns
    assert "decision pointer:" in patterns
    assert "every changed line traces to the work order" in patterns
    assert "unrelated cleanup becomes an improvement candidate" in patterns

    for metadata_field in (
        "`scope`",
        "`source`",
        "`last_verified`",
        "`confidence`",
        "`revalidation_trigger`",
        "`environment_notes`",
    ):
        assert metadata_field in memories_readme

    assert "edit: deny" in memory_prompt
    assert "dev_harness_memories/lessons.md" in memory_prompt
    assert "dev_harness_memories/patterns.md" in memory_prompt
    assert "memory candidates" in memory_prompt
    assert "treat retrieved memory as a hypothesis" in memory_prompt

    assert "edit: allow" in curator_prompt
    assert "dev_harness_memories/lessons.md" in curator_prompt
    assert "dev_harness_memories/patterns.md" in curator_prompt
    assert "current task state" in curator_prompt
    assert "backlog candidates" in curator_prompt
    assert "accepted: durable lesson" in curator_prompt
    assert "rejected: duplicate" in curator_prompt
    assert "rejected: belongs in improvement backlog" in curator_prompt
    assert not (simple_project / ".opencode/dev_harness/workflow/memory/lessons.md").exists()
    assert not (simple_project / ".opencode/dev_harness/workflow/memory/patterns.md").exists()
    assert not (simple_project / ".opencode/dev_harness/workflow/memory/decisions-index.md").exists()

    assert '"orchestrator-memory": allow' in planner_prompt
    assert '"orchestrator-memory": allow' in reviewer_prompt
    assert '"orchestrator-memory-curator": allow' not in reviewer_prompt
    assert '"orchestrator-memory-curator": allow' in reflection_prompt
    assert '"orchestrator-memory-curator": allow' not in reporter_prompt
    assert "memory candidates identified for reflection" in reviewer_prompt
    assert "memory hygiene input evidence" in reviewer_prompt
    assert "memory hygiene input evidence" in review_output
    assert "durable memory incorporation triage" in reflection_prompt
    assert "memory hygiene summary" in reflection_prompt
    assert "owner of final memory incorporation and memory hygiene synthesis" in reporter_prompt
    assert "reflection-owned memory hygiene summary" in reporter_prompt
    assert "workflow-memory.md" in control_policy
    assert "workflow-memory.md" in reflection_prompt
    assert "workflow-memory.md" in reporter_prompt
    assert "current task state" in workflow_memory
    assert "reflection owns final memory-incorporation triage" in workflow_memory
    assert "reporter relays the reflection-owned memory hygiene summary" in workflow_memory


def test_workflow_roles_use_runtime_memory_guidance_without_prompt_design_comments(simple_project: Path) -> None:
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md").lower()
    cleanup_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-cleanup.md").lower()
    completeness_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-completeness.md").lower()
    architecture_review_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-architecture.md").lower()
    memory_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-memory.md").lower()
    lessons_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-lessons.md").lower()
    lessons_guidance = read_prompt(simple_project, ".opencode/dev_harness/workflow/lessons-guidance.md").lower()

    for prompt in (
        planner_prompt,
        builder_prompt,
        cleanup_prompt,
        completeness_prompt,
        architecture_review_prompt,
    ):
        assert "pat-001" not in prompt
        assert "do not embed concrete memory entries" not in prompt
        assert "memory guidance" in prompt or "memory helper output" in prompt

    assert "dev_harness_memories/patterns.md" in memory_prompt
    assert "relevant lessons, patterns, and decision pointers" in memory_prompt
    assert "lessons-guidance.md" in lessons_prompt
    assert "lessons-guidance.md" in read_prompt(simple_project, ".opencode/agents/orchestrator-review-lessons.md").lower()
    assert "identify only the lessons that matter" in lessons_guidance
    assert "caller-provided task context" in lessons_guidance
    assert "lessons" in lessons_prompt


def test_adaptive_risk_triggers_drive_helper_selection(simple_project: Path) -> None:
    risk_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/adaptive-risk-triggers.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()

    for content in (planner_prompt, reviewer_prompt):
        assert "adaptive-risk-triggers.md" in content
        assert "helper_not_used" in content

    for content in (risk_policy,):
        assert "adaptive" in content
        assert "triggers" in content
        assert "code changes require" in content
        assert "behavior changes require" in content
        assert "product-breakdown" in content
        assert "external dependency, api, framework, standard, version, or documentation uncertainty requires" in content
        assert "low-risk documentation, formatting, wording, or metadata-only tasks" in content
        assert "helper_not_used" in content
        assert "workflow memory" in content

    assert "orchestrator-discovery" in planner_prompt
    assert "orchestrator-contract" in planner_prompt
    assert "orchestrator-memory" in planner_prompt
    assert "test obligations" in risk_policy
    assert "product-breakdown placement" in planner_prompt
    assert "requires_external_research: true" in risk_policy

    assert "orchestrator-verifier" in reviewer_prompt
    assert "orchestrator-review-completeness" in reviewer_prompt
    assert "memory candidates identified for reflection" in reviewer_prompt
    assert "acceptance criteria" in reviewer_prompt
    assert "may not approve external claims without cited researcher evidence or a waiver" in risk_policy


def test_planner_and_reviewer_support_parallel_helper_packets(simple_project: Path) -> None:
    parallel_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/parallel-helper-execution.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()

    assert "parallel helper execution" in parallel_policy
    assert "parallel_helper_plan" in parallel_policy
    assert "parallel_safe: true|false" in parallel_policy
    assert "file_write_set" in parallel_policy
    assert "do not parallelize helper work" in parallel_policy
    assert "external research must decide" in parallel_policy

    assert "parallel-helper-execution.md" in planner_prompt
    assert "orchestrator-discovery" in planner_prompt
    assert "orchestrator-contract" in planner_prompt
    assert "orchestrator-architecture" in planner_prompt
    assert "parallel_helper_plan" in planner_prompt
    assert "file_write_set" in planner_prompt

    assert "parallel-helper-execution.md" in reviewer_prompt
    assert "orchestrator-verifier" in reviewer_prompt
    assert "orchestrator-review-completeness" in reviewer_prompt
    assert "orchestrator-review-architecture" in reviewer_prompt
    assert "parallel_helper_plan" in reviewer_prompt
    assert "file_write_set" in reviewer_prompt


def test_shared_review_output_policy_is_referenced(simple_project: Path) -> None:
    review_output_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/review-output.md").lower()
    lessons_memory = read_prompt(simple_project, ".opencode/dev_harness_memories/lessons.md").lower()
    lessons_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-lessons.md").lower()
    review_agents = [
        ".opencode/agents/orchestrator-review-architecture.md",
        ".opencode/agents/orchestrator-review-completeness.md",
        ".opencode/agents/orchestrator-review-lessons.md",
    ]

    assert "pass" in review_output_policy
    assert "fail" in review_output_policy
    assert "needs_waiver" in review_output_policy
    assert "repo-local workflow memory" in lessons_memory
    assert "dev_harness_memories/lessons.md" in lessons_prompt

    for agent_path in review_agents:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "review-output.md" in prompt
