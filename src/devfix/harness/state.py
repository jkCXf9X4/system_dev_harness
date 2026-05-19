from __future__ import annotations

from operator import add
from typing import Annotated, Any, TypedDict


class HarnessState(TypedDict, total=False):
    backlog_item: str
    execution_backend: str
    mcp_policy: dict[str, Any]
    stakeholder_context: str
    lessons: list[dict[str, Any]]
    changed_files: list[str]
    diff_summary: str
    test_output: str
    agent_output: str
    waiver_requests: list[dict[str, Any]]
    task_resolution: dict[str, Any]
    repo_discovery: dict[str, Any]
    repo_context: dict[str, Any]
    requirement_contract: dict[str, Any]
    architecture_context: dict[str, Any]
    known_mistake_check: dict[str, Any]
    implementation_packet: dict[str, Any]
    external_agent_handoff: dict[str, Any]
    mcp_execution_plan: dict[str, Any]
    mcp_execution_result: dict[str, Any]
    verification_report: dict[str, Any]
    evidence: dict[str, Any]
    requirements_review: dict[str, Any]
    architecture_review: dict[str, Any]
    qa_review: dict[str, Any]
    completeness_review: dict[str, Any]
    known_mistake_review: dict[str, Any]
    completion_decision: dict[str, Any]
    revision_plan: dict[str, Any]
    human_interrupt: dict[str, Any]
    final_control_report: str
    tool_trace: Annotated[list[dict[str, Any]], add]
    artifacts: Annotated[list[str], add]
