from __future__ import annotations

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


def test_improvement_stage_smoke(simple_project: Path, opencode_env: dict[str, str]) -> None:
    status, output = run_opencode(
        simple_project,
        opencode_env,
        agent="orchestrator-improvement",
        title="improvement_stage",
        prompt="Find and persist backlog-ready improvement candidates in this workflow package.",
        timeout=60,
    )

    assert status in {0, 124}
    assert "orchestrator-improvement" in output.lower()
    prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-improvement.md")
    assert "continuous improvement discovery stage" in prompt.lower()
    assert "backlog-worthy improvement work" in prompt.lower()
    assert "product-breakdown/06-evolution/backlog/" in prompt
    assert "edit: allow" in prompt
    assert "may edit only improvement backlog artifacts" in prompt.lower()
    assert "plans/backlog" not in prompt


def test_focused_improvement_evaluator_is_scoped(simple_project: Path) -> None:
    prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-improvement-evaluator.md").lower()
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()

    assert "focused improvement evaluator" in prompt
    assert "one specific improvement finding" in prompt
    assert "product-breakdown/06-evolution/backlog/" in prompt
    assert "improvement-backlog-overview-template.md" in prompt
    assert "improvement-candidate-template.md" in prompt
    assert "edit: allow" in prompt
    assert "do not edit implementation files" in prompt
    assert "persisted" in prompt
    assert "rejected" in prompt
    assert "needs_more_evidence" in prompt
    assert "evidence, impact, and scoped future task seed" in prompt
    assert '"orchestrator-memory-curator": allow' in prompt
    assert "focused improvement evaluation" in control_policy
    assert "backlog capture only" in control_policy


def test_decision_templates_are_generic_and_referenced(simple_project: Path) -> None:
    architecture_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-architecture.md")
    review_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-architecture.md")
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

    assert "decision-template.md" in architecture_prompt.lower()
    assert "decision-log-entry-template.md" in architecture_prompt.lower()
    assert "durable choice" in review_prompt.lower()
    assert "product-breakdown/" in review_prompt.lower()
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
    assert "product-breakdown/" in verifier_prompt
    assert "product-breakdown/" in completeness_prompt
    assert "product breakdown evidence" in gate_prompt


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
    assert "call `orchestrator-improvement` only when planner output explicitly declares `workflow_type: improvement`" in orchestrator_prompt

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
        "orchestrator-improvement",
    ):
        assert f'"{top_level_stage}": allow' in orchestrator_prompt

    for directed_helper in (
        "orchestrator-discovery",
        "orchestrator-contract",
        "orchestrator-architecture",
        "orchestrator-lessons",
        "orchestrator-memory",
        "orchestrator-memory-curator",
        "orchestrator-build-error-resolver",
        "orchestrator-verifier",
        "orchestrator-review-architecture",
        "orchestrator-review-completeness",
        "orchestrator-review-lessons",
        "orchestrator-researcher",
        "orchestrator-improvement-evaluator",
    ):
        assert f'"{directed_helper}": allow' not in orchestrator_prompt

    for helper in (
        "orchestrator-architecture",
        "orchestrator-memory",
        "test planning",
        "product-breakdown placement",
    ):
        assert helper in planner_prompt

    for helper in (
        "orchestrator-build-error-resolver",
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


def test_structured_feedback_protocol_is_shared(simple_project: Path) -> None:
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()
    agent_paths = [
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-reviewer.md",
        ".opencode/agents/orchestrator-reporter.md",
        ".opencode/agents/orchestrator-researcher.md",
        ".opencode/agents/orchestrator-memory.md",
        ".opencode/agents/orchestrator-memory-curator.md",
        ".opencode/agents/orchestrator-build-error-resolver.md",
        ".opencode/agents/orchestrator-review-architecture.md",
    ]

    for field in (
        "user_feedback_required",
        "user_feedback_request",
        "improvement_candidates",
        "research_requests",
    ):
        assert field in control_policy

    for agent_path in agent_paths:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "structured feedback fields" in prompt
        assert "control-policy.md" in prompt


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
    ]

    for agent_path in agent_paths:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "orchestrator-researcher" in prompt


def test_working_agents_can_trigger_focused_improvement_evaluation(simple_project: Path) -> None:
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
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-architecture.md",
        ".opencode/agents/orchestrator-review-completeness.md",
        ".opencode/agents/orchestrator-review-lessons.md",
        ".opencode/agents/orchestrator-memory.md",
        ".opencode/agents/orchestrator-memory-curator.md",
        ".opencode/agents/orchestrator-improvement.md",
    ]

    for agent_path in agent_paths:
        prompt = read_prompt(simple_project, agent_path)
        assert '"orchestrator-improvement-evaluator": allow' in prompt

    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md")
    evaluator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-improvement-evaluator.md")
    assert '"orchestrator-improvement-evaluator": allow' not in orchestrator_prompt
    assert '"orchestrator-researcher": allow' in evaluator_prompt
    assert '"orchestrator-memory-curator": allow' in evaluator_prompt


def test_workflow_memory_layer_is_versioned_and_scoped(simple_project: Path) -> None:
    lessons = read_prompt(simple_project, ".opencode/dev_harness_memories/lessons.md").lower()
    patterns = read_prompt(simple_project, ".opencode/dev_harness_memories/patterns.md").lower()
    decisions = read_prompt(simple_project, ".opencode/dev_harness_memories/decisions-index.md").lower()
    memory_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-memory.md").lower()
    curator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-memory-curator.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()
    reporter_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reporter.md").lower()
    evaluator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-improvement-evaluator.md").lower()
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()

    assert "repo-local workflow memory" in lessons
    assert "km-001" in lessons
    assert "pat-000" in patterns
    assert "decision pointers" in decisions

    assert "edit: deny" in memory_prompt
    assert "dev_harness_memories/lessons.md" in memory_prompt
    assert "dev_harness_memories/patterns.md" in memory_prompt
    assert "dev_harness_memories/decisions-index.md" in memory_prompt
    assert "memory candidates" in memory_prompt

    assert "edit: allow" in curator_prompt
    assert "dev_harness_memories/lessons.md" in curator_prompt
    assert "dev_harness_memories/patterns.md" in curator_prompt
    assert "dev_harness_memories/decisions-index.md" in curator_prompt
    assert "current task state" in curator_prompt
    assert "backlog candidates" in curator_prompt
    assert not (simple_project / ".opencode/dev_harness/workflow/memory/lessons.md").exists()
    assert not (simple_project / ".opencode/dev_harness/workflow/memory/patterns.md").exists()
    assert not (simple_project / ".opencode/dev_harness/workflow/memory/decisions-index.md").exists()

    assert '"orchestrator-memory": allow' in planner_prompt
    assert '"orchestrator-memory": allow' in reviewer_prompt
    assert '"orchestrator-memory-curator": allow' in reviewer_prompt
    assert '"orchestrator-memory-curator": allow' in reporter_prompt
    assert '"orchestrator-memory-curator": allow' in evaluator_prompt
    assert "workflow memory" in control_policy
    assert "current task state" in control_policy


def test_adaptive_risk_triggers_drive_helper_selection(simple_project: Path) -> None:
    control_policy = read_prompt(simple_project, ".opencode/dev_harness/workflow/control-policy.md").lower()
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    reviewer_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md").lower()

    for content in (planner_prompt, reviewer_prompt):
        assert "adaptive risk triggers" in content
        assert "control-policy.md" in content
        assert "helper_not_used" in content

    for content in (control_policy,):
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
    assert "test obligations" in control_policy
    assert "product-breakdown placement" in planner_prompt
    assert "requires_external_research: true" in control_policy

    assert "orchestrator-verifier" in reviewer_prompt
    assert "orchestrator-review-completeness" in reviewer_prompt
    assert "orchestrator-memory-curator" in reviewer_prompt
    assert "acceptance criteria" in reviewer_prompt
    assert "may not approve external claims without cited researcher evidence or a waiver" in control_policy


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
