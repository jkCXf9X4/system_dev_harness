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


def test_adr_templates_are_generic_and_referenced(simple_project: Path) -> None:
    architecture_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-architecture.md")
    packet_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-packet.md")
    review_prompt = read_prompt(simple_project, ".opencode/agents/orchestrator-review-architecture.md")
    adr_template = read_prompt(simple_project, ".opencode/templates/others/adr-template.md")
    adr_record = read_prompt(simple_project, ".opencode/templates/others/adr_record.md")

    assert "adr-template.md" in architecture_prompt.lower()
    assert "adr_record.md" in architecture_prompt.lower()
    assert "adr-template.md" in packet_prompt.lower()
    assert "adr_record.md" in packet_prompt.lower()
    assert "adr-template.md" in review_prompt.lower()
    assert "adr_record.md" in review_prompt.lower()
    assert "architecture decision record" in adr_template.lower()
    assert "adr record template" in adr_record.lower()
    assert "ssp_references" not in adr_template
    assert "ssp_references" not in adr_record
    assert "docs/adr/README.md" not in adr_template
    assert "docs/adr/README.md" not in adr_record


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
