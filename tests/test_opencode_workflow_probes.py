from __future__ import annotations

import subprocess
from pathlib import Path


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
        prompt="Find backlog-ready improvement candidates in this workflow package. Do not edit files.",
        timeout=60,
    )

    assert status in {0, 124}
    assert "orchestrator-improvement" in output.lower()
    prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-improvement.md")
    assert "continuous improvement discovery stage" in prompt.lower()
    assert "backlog-worthy improvement work" in prompt.lower()


def test_decision_templates_are_generic_and_referenced(simple_project: Path) -> None:
    architecture_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-architecture.md")
    packet_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-packet.md")
    review_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-architecture.md")
    decision_template = read_prompt(
        simple_project,
        ".opencode/templates/product-breakdown/templates/decision-template.md",
    )
    decision_log_entry = read_prompt(
        simple_project,
        ".opencode/templates/product-breakdown/templates/decision-log-entry-template.md",
    )

    assert "decision-template.md" in architecture_prompt.lower()
    assert "decision-log-entry-template.md" in architecture_prompt.lower()
    assert "decision-template.md" in packet_prompt.lower()
    assert "decision-log-entry-template.md" in packet_prompt.lower()
    assert "decision-template.md" in review_prompt.lower()
    assert "decision-log-entry-template.md" in review_prompt.lower()
    assert "durable product breakdown decisions" in decision_template.lower()
    assert "decision log entry template" in decision_log_entry.lower()
    assert "ssp_references" not in decision_template
    assert "ssp_references" not in decision_log_entry
    assert "docs/adr/README.md" not in decision_template
    assert "docs/adr/README.md" not in decision_log_entry


def test_product_breakdown_usage_is_embedded_in_agent_workflow(simple_project: Path) -> None:
    agents = [
        ".opencode/agents/orchestrator-planner.md",
        ".opencode/agents/orchestrator-discovery.md",
        ".opencode/agents/orchestrator-contract.md",
        ".opencode/agents/orchestrator-architecture.md",
        ".opencode/agents/orchestrator-packet.md",
        ".opencode/agents/orchestrator-builder.md",
        ".opencode/agents/orchestrator-verifier.md",
        ".opencode/agents/orchestrator-review-completeness.md",
        ".opencode/agents/orchestrator-reviewer.md",
    ]

    for agent_path in agents:
        prompt = read_prompt(simple_project, agent_path).lower()
        assert "product breakdown" in prompt or "product-breakdown" in prompt
        assert "layer" in prompt

    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md").lower()
    packet_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-packet.md").lower()
    verifier_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-verifier.md").lower()

    assert "intent, product behavior, architecture, implementation, verification, operation, and evolution" in planner_prompt
    assert "guidance files" in packet_prompt
    assert "decision-placement.md" in verifier_prompt
    assert "traceability.md" in verifier_prompt


def test_orchestrator_does_not_route_shortcut_build(simple_project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    orchestrator_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator.md")
    planner_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-planner.md")
    architecture_doc = read_prompt(repo_root, "docs/03-system-architecture/architecture.md")

    for content in (orchestrator_prompt, planner_prompt, architecture_doc):
        lowered = content.lower()
        assert "small-task handoff" not in lowered
        assert "compact handoff" not in lowered
        assert "shortcut path" not in lowered


def test_information_hygiene_is_workflow_gated(simple_project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    contract_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-contract.md")
    packet_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-packet.md")
    builder_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-builder.md")
    verifier_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-verifier.md")
    completeness_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-completeness.md")
    gate_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-reviewer.md")
    architecture_doc = read_prompt(repo_root, "docs/03-system-architecture/architecture.md")
    commitments_doc = read_prompt(repo_root, "docs/02-product-commitments/product-commitments.md")

    for content in (
        contract_prompt,
        packet_prompt,
        builder_prompt,
        verifier_prompt,
        completeness_prompt,
        gate_prompt,
        architecture_doc,
        commitments_doc,
    ):
        lowered = content.lower()
        assert "information hygiene" in lowered
        assert "stale" in lowered
        assert "duplicate" in lowered
        assert "traceability" in lowered
