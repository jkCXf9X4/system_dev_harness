from __future__ import annotations

import json
import re
from pathlib import Path
from typing import TypeVar

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, ValidationError

from devfix.harness.execution import FilesystemMCPClient, MCPPolicy
from devfix.harness.models import openrouter_model
from devfix.harness.prompts import (
    ARCHITECTURE_CONTEXT_PROMPT,
    ARCHITECTURE_REVIEW_PROMPT,
    COMPLETENESS_REVIEW_PROMPT,
    EXTERNAL_AGENT_HANDOFF_PROMPT,
    FINAL_CONTROL_REPORT_PROMPT,
    IMPLEMENTATION_PACKET_PROMPT,
    KNOWN_MISTAKE_CHECK_PROMPT,
    KNOWN_MISTAKE_REVIEW_PROMPT,
    MCP_EXECUTION_PROMPT,
    QA_REVIEW_PROMPT,
    REPO_DISCOVERY_PROMPT,
    REQUIREMENT_CONTRACT_PROMPT,
    REQUIREMENTS_REVIEW_PROMPT,
    TASK_SELECTION_PROMPT,
)
from devfix.harness.rendering import render_model, render_text
from devfix.harness.schemas import (
    ArchitectureContext,
    BacklogCandidate,
    ChecklistStatus,
    CompletionDecision,
    EvidenceBundle,
    ExternalAgentHandoff,
    HumanInterrupt,
    ImplementationPacket,
    KnownMistakeCheck,
    MCPExecutionPlan,
    MCPExecutionResult,
    PatchApplyResult,
    RepoContext,
    RepoDiscoveryPlan,
    ReviewerVerdict,
    RevisionPlan,
    TaskContract,
    TaskResolution,
    ToolTraceEntry,
    Waiver,
    VerificationCommandResult,
    VerificationReport,
)
from devfix.harness.state import HarnessState
from devfix.harness.tasking import build_task_prompt, looks_like_backlog_meta_prompt, parse_backlog_candidate

SchemaT = TypeVar("SchemaT", bound=BaseModel)


def _invoke_text(prompt: str, user_content: str, model_env: str, *, temperature: float = 0.2) -> str:
    model = openrouter_model(model_env, temperature=temperature)
    response = model.invoke([SystemMessage(content=prompt), HumanMessage(content=user_content)])
    return str(response.content)


def _invoke_schema(
    prompt: str,
    user_content: str,
    schema: type[SchemaT],
    model_env: str,
    *,
    temperature: float = 0.1,
) -> SchemaT:
    schema_prompt = f"""{prompt}

JSON schema:
{json.dumps(schema.model_json_schema(), indent=2)}
"""
    raw = _invoke_text(schema_prompt, user_content, model_env, temperature=temperature)
    try:
        return schema.model_validate(_extract_json(raw))
    except (json.JSONDecodeError, ValidationError) as exc:
        raise RuntimeError(f"{schema.__name__} validation failed: {exc}") from exc


def _extract_json(raw: str) -> object:
    stripped = raw.strip()
    fenced = re.search(r"```(?:json)?\s*(.*?)```", stripped, re.S)
    if fenced:
        stripped = fenced.group(1).strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        start = min([index for index in [stripped.find("{"), stripped.find("[")] if index >= 0], default=-1)
        if start < 0:
            raise
        decoder = json.JSONDecoder()
        value, _ = decoder.raw_decode(stripped[start:])
        return value


def _policy(state: HarnessState) -> MCPPolicy:
    return MCPPolicy.model_validate(state.get("mcp_policy") or {"allowed_roots": ["plans", "docs", "src", ".agents"]})


def _client(state: HarnessState) -> FilesystemMCPClient:
    return FilesystemMCPClient(workdir=Path.cwd(), policy=_policy(state))


def _resolved_task_text(state: HarnessState) -> str:
    resolution = state.get("task_resolution")
    if resolution:
        return TaskResolution.model_validate(resolution).resolved_task_input
    return state["backlog_item"]


def task_resolution(state: HarnessState) -> HarnessState:
    prompt = state["backlog_item"].strip()
    client = _client(state)
    traces: list[dict] = []
    if not looks_like_backlog_meta_prompt(prompt):
        resolution = TaskResolution(
            resolution_mode="direct_prompt",
            selected_task_title=prompt.splitlines()[0][:120] or "Task Input",
            resolved_task_input=prompt,
            selection_rationale="Input already appears to be a concrete task.",
        )
        return {"task_resolution": resolution.model_dump(), "artifacts": [render_model("Task Resolution", resolution)]}

    listing = client.list_files(["plans/backlog"])
    traces.append(listing.trace.model_dump())
    candidates: list[BacklogCandidate] = []
    candidate_content: dict[str, str] = {}
    for path in listing.payload:
        if "/completed/" in path or path.endswith("/README.md") or not path.endswith(".md"):
            continue
        file_result = client.read_file(path)
        traces.append(file_result.trace.model_dump())
        candidate = parse_backlog_candidate(path, file_result.payload)
        candidates.append(candidate)
        candidate_content[path] = file_result.payload

    selection_request = f"""Task input:
{prompt}

Backlog candidates:
{json.dumps([candidate.model_dump() for candidate in candidates], indent=2)}
"""
    resolution = _invoke_schema(TASK_SELECTION_PROMPT, selection_request, TaskResolution, "PLANNER_MODEL", temperature=0.1)
    if resolution.selected_task_path and resolution.selected_task_path in candidate_content:
        selected_candidate = next((item for item in candidates if item.path == resolution.selected_task_path), None)
        if selected_candidate is not None:
            resolution.resolved_task_input = build_task_prompt(selected_candidate, candidate_content[resolution.selected_task_path])
    overview = RepoContext(
        backlog_overview=candidates,
        relevant_files=[],
        search_results=[],
        file_contexts=[],
        summary=["Backlog candidate inventory for task selection."],
    )
    return {
        "task_resolution": resolution.model_dump(),
        "tool_trace": traces,
        "artifacts": [render_model("Task Resolution", resolution), render_model("Backlog Candidates", overview)],
    }


def repo_discovery(state: HarnessState) -> HarnessState:
    client = _client(state)
    traces: list[dict] = []
    listing = client.list_files(["docs", "src", "plans", ".agents"])
    traces.append(listing.trace.model_dump())
    discovery_request = f"""Resolved task input:
{_resolved_task_text(state)}

File inventory:
{json.dumps(listing.payload, indent=2)}
"""
    plan = _invoke_schema(REPO_DISCOVERY_PROMPT, discovery_request, RepoDiscoveryPlan, "PLANNER_MODEL", temperature=0.1)
    search_results: list[str] = []
    for query in plan.search_queries:
        result = client.search_text(query, ["docs", "src", "plans"])
        traces.append(result.trace.model_dump())
        search_results.extend(result.payload)

    relevant_files: list[str] = []
    file_contexts = []
    for path in plan.relevant_files[: _policy(state).max_discovery_files]:
        result = client.read_file(path)
        traces.append(result.trace.model_dump())
        relevant_files.append(path)
        file_contexts.append({"path": path, "reason": plan.rationale, "content": result.payload})

    context = RepoContext(
        relevant_files=relevant_files,
        search_results=search_results[: _policy(state).max_search_results],
        file_contexts=file_contexts,
        summary=[
            plan.rationale,
            f"Loaded {len(relevant_files)} file(s) through governed MCP access.",
            f"Collected {len(search_results[: _policy(state).max_search_results])} search hit(s).",
        ],
    )
    return {
        "repo_discovery": plan.model_dump(),
        "repo_context": context.model_dump(),
        "tool_trace": traces,
        "artifacts": [render_model("Repository Discovery Plan", plan), render_model("Repository Context", context)],
    }


def requirement_contract(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{_resolved_task_text(state)}

Stakeholder or project context:
{state.get("stakeholder_context", "")}

Repository context:
{json.dumps(state.get("repo_context", {}), indent=2)}
"""
    contract = _invoke_schema(REQUIREMENT_CONTRACT_PROMPT, content, TaskContract, "REVIEWER_MODEL", temperature=0.1)
    return {"requirement_contract": contract.model_dump(), "artifacts": [render_model("Requirement Contract", contract)]}


def architecture_context(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{_resolved_task_text(state)}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Stakeholder or project context:
{state.get("stakeholder_context", "")}

Repository context:
{json.dumps(state.get("repo_context", {}), indent=2)}
"""
    architecture = _invoke_schema(
        ARCHITECTURE_CONTEXT_PROMPT,
        content,
        ArchitectureContext,
        "REVIEWER_MODEL",
        temperature=0.1,
    )
    return {"architecture_context": architecture.model_dump(), "artifacts": [render_model("Architecture Context", architecture)]}


def known_mistake_check(state: HarnessState) -> HarnessState:
    content = f"""Persistent known mistakes:
{json.dumps(state.get("lessons", []), indent=2)}

Task input:
{_resolved_task_text(state)}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}
"""
    check = _invoke_schema(KNOWN_MISTAKE_CHECK_PROMPT, content, KnownMistakeCheck, "FAST_MODEL", temperature=0.1)
    return {"known_mistake_check": check.model_dump(), "artifacts": [render_model("Known Mistake Check", check)]}


def implementation_packet(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{_resolved_task_text(state)}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}

Known mistake check:
{json.dumps(state["known_mistake_check"], indent=2)}

Repository context:
{json.dumps(state.get("repo_context", {}), indent=2)}
"""
    packet = _invoke_schema(IMPLEMENTATION_PACKET_PROMPT, content, ImplementationPacket, "PLANNER_MODEL", temperature=0.1)
    return {"implementation_packet": packet.model_dump(), "artifacts": [render_model("Implementation Packet", packet)]}


def external_agent_handoff(state: HarnessState) -> HarnessState:
    content = f"""Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}

Known mistake check:
{json.dumps(state["known_mistake_check"], indent=2)}

Implementation packet:
{json.dumps(state["implementation_packet"], indent=2)}
"""
    handoff = _invoke_schema(EXTERNAL_AGENT_HANDOFF_PROMPT, content, ExternalAgentHandoff, "PLANNER_MODEL", temperature=0.1)
    return {"external_agent_handoff": handoff.model_dump(), "artifacts": [render_model("External Agent Handoff", handoff)]}


def mcp_execution(state: HarnessState) -> HarnessState:
    client = _client(state)
    traces: list[dict] = []
    content = f"""Resolved task:
{_resolved_task_text(state)}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}

Known mistake check:
{json.dumps(state["known_mistake_check"], indent=2)}

Implementation packet:
{json.dumps(state["implementation_packet"], indent=2)}

Repository context:
{json.dumps(state.get("repo_context", {}), indent=2)}
"""
    plan = _invoke_schema(MCP_EXECUTION_PROMPT, content, MCPExecutionPlan, "PLANNER_MODEL", temperature=0.1)
    if plan.needs_external_executor:
        execution = MCPExecutionResult(
            status="fallback_required",
            summary=plan.summary,
            applied_patches=[],
            changed_files=[],
            fallback_reason=plan.fallback_reason or "Planner requested fallback.",
        )
        return {
            "mcp_execution_plan": plan.model_dump(),
            "mcp_execution_result": execution.model_dump(),
            "artifacts": [render_model("MCP Execution Plan", plan), render_model("MCP Execution Result", execution)],
        }

    results: list[PatchApplyResult] = []
    changed_files: list[str] = []
    for patch in plan.patches:
        result = client.apply_patch(patch.patch)
        traces.append(result.trace.model_dump())
        status = "applied" if result.payload.get("applied") else "failed"
        results.append(PatchApplyResult(path=patch.path, status=status, detail=result.trace.details))
        if status == "applied":
            changed_files.append(patch.path)
    execution = MCPExecutionResult(
        status="applied" if results and all(item.status == "applied" for item in results) else "blocked",
        summary=plan.summary,
        applied_patches=results,
        changed_files=changed_files,
        fallback_reason=plan.fallback_reason,
    )
    return {
        "mcp_execution_plan": plan.model_dump(),
        "mcp_execution_result": execution.model_dump(),
        "changed_files": changed_files,
        "tool_trace": traces,
        "artifacts": [render_model("MCP Execution Plan", plan), render_model("MCP Execution Result", execution)],
    }


def verification(state: HarnessState) -> HarnessState:
    client = _client(state)
    traces: list[dict] = []
    plan = MCPExecutionPlan.model_validate(state.get("mcp_execution_plan", {}))
    if not plan.verification_commands:
        report = VerificationReport(status="not_run", summary="No verification commands were planned.", results=[])
        return {"verification_report": report.model_dump(), "artifacts": [render_model("Verification Report", report)]}

    results: list[VerificationCommandResult] = []
    for command in plan.verification_commands:
        result = client.run_test(command)
        traces.append(result.trace.model_dump())
        results.append(VerificationCommandResult.model_validate(result.payload))
    passed = all(item.exit_code == 0 for item in results)
    report = VerificationReport(
        status="passed" if passed else "failed",
        summary="All verification commands passed." if passed else "One or more verification commands failed.",
        results=results,
    )
    test_output = "\n\n".join(
        [
            f"$ {item.command}\nexit={item.exit_code}\n{item.stdout}".strip()
            + (f"\nSTDERR:\n{item.stderr}" if item.stderr else "")
            for item in results
        ]
    )
    return {
        "verification_report": report.model_dump(),
        "test_output": test_output,
        "tool_trace": traces,
        "artifacts": [render_model("Verification Report", report)],
    }


def evidence_intake(state: HarnessState) -> HarnessState:
    tool_trace = [ToolTraceEntry.model_validate(item) for item in state.get("tool_trace", [])]
    agent_output = state.get("agent_output", "")
    if not agent_output:
        agent_output = json.dumps(
            {
                "mcp_execution_result": state.get("mcp_execution_result", {}),
                "verification_report": state.get("verification_report", {}),
                "tool_trace": [entry.model_dump() for entry in tool_trace],
            },
            indent=2,
        )
    evidence = EvidenceBundle(
        has_evidence=bool(
            state.get("changed_files")
            or state.get("diff_summary")
            or state.get("test_output")
            or agent_output
            or state.get("waiver_requests")
        ),
        changed_files=state.get("changed_files", []),
        diff_summary=state.get("diff_summary", ""),
        test_output=state.get("test_output", ""),
        agent_output=agent_output,
        waiver_requests=[Waiver.model_validate(item) for item in state.get("waiver_requests", [])],
    )
    return {"evidence": evidence.model_dump(), "artifacts": [render_model("Evidence Intake", evidence)]}


def requirements_review(state: HarnessState) -> HarnessState:
    verdict = _review("requirements", REQUIREMENTS_REVIEW_PROMPT, state, "REVIEWER_MODEL")
    return {"requirements_review": verdict.model_dump(), "artifacts": [render_model("Requirements Review", verdict)]}


def architecture_review(state: HarnessState) -> HarnessState:
    verdict = _review("architecture", ARCHITECTURE_REVIEW_PROMPT, state, "REVIEWER_MODEL")
    return {"architecture_review": verdict.model_dump(), "artifacts": [render_model("Architecture Review", verdict)]}


def qa_review(state: HarnessState) -> HarnessState:
    verdict = _review("qa", QA_REVIEW_PROMPT, state, "FAST_MODEL")
    return {"qa_review": verdict.model_dump(), "artifacts": [render_model("QA Review", verdict)]}


def completeness_review(state: HarnessState) -> HarnessState:
    verdict = _review("completeness", COMPLETENESS_REVIEW_PROMPT, state, "REVIEWER_MODEL")
    return {"completeness_review": verdict.model_dump(), "artifacts": [render_model("Completeness Review", verdict)]}


def known_mistake_review(state: HarnessState) -> HarnessState:
    verdict = _review("known_mistakes", KNOWN_MISTAKE_REVIEW_PROMPT, state, "FAST_MODEL")
    return {"known_mistake_review": verdict.model_dump(), "artifacts": [render_model("Known Mistake Review", verdict)]}


def _review(role: str, prompt: str, state: HarnessState, model_env: str) -> ReviewerVerdict:
    content = f"""Reviewer role:
{role}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}

Known mistake check:
{json.dumps(state["known_mistake_check"], indent=2)}

Implementation packet:
{json.dumps(state["implementation_packet"], indent=2)}

External agent handoff:
{json.dumps(state["external_agent_handoff"], indent=2)}

Implementation evidence:
{json.dumps(state["evidence"], indent=2)}
"""
    return _invoke_schema(prompt, content, ReviewerVerdict, model_env, temperature=0.0)


def completion_gate(state: HarnessState) -> HarnessState:
    evidence = EvidenceBundle.model_validate(state["evidence"])
    reviews = [
        ReviewerVerdict.model_validate(state["requirements_review"]),
        ReviewerVerdict.model_validate(state["architecture_review"]),
        ReviewerVerdict.model_validate(state["qa_review"]),
        ReviewerVerdict.model_validate(state["completeness_review"]),
        ReviewerVerdict.model_validate(state["known_mistake_review"]),
    ]
    waivers = evidence.waiver_requests
    blocking_gaps: list[str] = []
    required_waivers: list[Waiver] = []
    checklist_status = []

    fallback = state.get("mcp_execution_result", {})
    if fallback and fallback.get("status") == "fallback_required":
        blocking_gaps.append(f"MCP fallback required: {fallback.get('fallback_reason', 'unspecified')}")

    if not evidence.has_evidence:
        blocking_gaps.append("No implementation evidence was provided; generated packet is ready for handoff but cannot be approved.")

    for review in reviews:
        for finding in review.findings:
            checklist_status.append(
                ChecklistStatus(item_id=finding.item_id, status=finding.status, evidence=finding.evidence or finding.finding)
            )
            if finding.status == "fail":
                blocking_gaps.append(f"{review.reviewer}: {finding.item_id}: {finding.finding}")
            elif finding.status == "needs_waiver":
                matching = [waiver for waiver in waivers if waiver.item_id == finding.item_id]
                if matching:
                    required_waivers.extend(matching)
                else:
                    blocking_gaps.append(f"{review.reviewer}: {finding.item_id} needs waiver but none was provided.")

    failing_reviews = [review.reviewer for review in reviews if review.status == "fail"]
    waiver_reviews = [review.reviewer for review in reviews if review.status == "needs_waiver"]
    if blocking_gaps:
        status = "blocked"
        next_action = "Revise the MCP execution plan or rerun with an external executor fallback and updated evidence."
    elif waiver_reviews or required_waivers:
        status = "waiver_required"
        next_action = "Human review must approve or reject requested waivers."
    else:
        status = "approved"
        next_action = "Proceed with completion; all reviewers passed against available evidence."

    decision = CompletionDecision(
        status=status,
        contract_checklist_status=checklist_status,
        reviewer_approval_status=f"failed={failing_reviews}; needs_waiver={waiver_reviews}",
        required_waivers=required_waivers,
        blocking_gaps=blocking_gaps,
        next_required_action=next_action,
    )
    return {"completion_decision": decision.model_dump(), "artifacts": [render_model("Completion Decision", decision)]}


def route_after_gate(state: HarnessState) -> str:
    decision = CompletionDecision.model_validate(state["completion_decision"])
    if decision.status == "approved":
        return "final_control_report"
    if decision.status == "waiver_required":
        return "human_interrupt"
    return "revise_packet"


def revise_packet(state: HarnessState) -> HarnessState:
    decision = CompletionDecision.model_validate(state["completion_decision"])
    plan = RevisionPlan(
        reason="Deterministic completion gate blocked approval.",
        required_packet_changes=decision.blocking_gaps,
        next_step="Revise the contract, MCP execution plan, or fallback external-agent run, then rerun the harness with updated evidence.",
    )
    return {"revision_plan": plan.model_dump(), "artifacts": [render_model("Revision Plan", plan)]}


def human_interrupt(state: HarnessState) -> HarnessState:
    decision = CompletionDecision.model_validate(state["completion_decision"])
    interrupt = HumanInterrupt(
        reason="Completion requires human waiver approval.",
        requested_waivers=decision.required_waivers,
        human_decision_needed="Approve, reject, or revise the requested waivers before completion.",
        next_step_after_decision="If waivers are approved, rerun with waiver evidence; otherwise revise implementation.",
    )
    return {"human_interrupt": interrupt.model_dump(), "artifacts": [render_model("Human Interrupt", interrupt)]}


def final_control_report(state: HarnessState) -> HarnessState:
    decision = CompletionDecision.model_validate(state["completion_decision"])
    content = "\n\n".join(state["artifacts"])
    prompt = f"""Deterministic status: {decision.status}

Structured artifacts:
{content}
"""
    output = _invoke_text(FINAL_CONTROL_REPORT_PROMPT, prompt, "PLANNER_MODEL", temperature=0.1)
    return {"final_control_report": output, "artifacts": [render_text("Final Control Report", output)]}


def build_packet_graph():
    workflow = StateGraph(HarnessState)
    workflow.add_node("task_resolution", task_resolution)
    workflow.add_node("repo_discovery", repo_discovery)
    workflow.add_node("requirement_contract", requirement_contract)
    workflow.add_node("architecture_context", architecture_context)
    workflow.add_node("known_mistake_check", known_mistake_check)
    workflow.add_node("implementation_packet", implementation_packet)
    workflow.add_node("external_agent_handoff", external_agent_handoff)

    workflow.add_edge(START, "task_resolution")
    workflow.add_edge("task_resolution", "repo_discovery")
    workflow.add_edge("repo_discovery", "requirement_contract")
    workflow.add_edge("requirement_contract", "architecture_context")
    workflow.add_edge("architecture_context", "known_mistake_check")
    workflow.add_edge("known_mistake_check", "implementation_packet")
    workflow.add_edge("implementation_packet", "external_agent_handoff")
    workflow.add_edge("external_agent_handoff", END)
    return workflow.compile(checkpointer=InMemorySaver())


def build_review_graph():
    workflow = StateGraph(HarnessState)
    workflow.add_node("evidence_intake", evidence_intake)
    workflow.add_node("requirements_review", requirements_review)
    workflow.add_node("architecture_review", architecture_review)
    workflow.add_node("qa_review", qa_review)
    workflow.add_node("completeness_review", completeness_review)
    workflow.add_node("known_mistake_review", known_mistake_review)
    workflow.add_node("completion_gate", completion_gate)
    workflow.add_node("revise_packet", revise_packet)
    workflow.add_node("human_interrupt", human_interrupt)
    workflow.add_node("final_control_report", final_control_report)

    workflow.add_edge(START, "evidence_intake")
    workflow.add_edge("evidence_intake", "requirements_review")
    workflow.add_edge("requirements_review", "architecture_review")
    workflow.add_edge("architecture_review", "qa_review")
    workflow.add_edge("qa_review", "completeness_review")
    workflow.add_edge("completeness_review", "known_mistake_review")
    workflow.add_edge("known_mistake_review", "completion_gate")
    workflow.add_conditional_edges(
        "completion_gate",
        route_after_gate,
        {
            "final_control_report": "final_control_report",
            "revise_packet": "revise_packet",
            "human_interrupt": "human_interrupt",
        },
    )
    workflow.add_edge("revise_packet", "final_control_report")
    workflow.add_edge("human_interrupt", "final_control_report")
    workflow.add_edge("final_control_report", END)
    return workflow.compile(checkpointer=InMemorySaver())


def build_graph():
    workflow = StateGraph(HarnessState)
    workflow.add_node("task_resolution", task_resolution)
    workflow.add_node("repo_discovery", repo_discovery)
    workflow.add_node("requirement_contract", requirement_contract)
    workflow.add_node("architecture_context", architecture_context)
    workflow.add_node("known_mistake_check", known_mistake_check)
    workflow.add_node("implementation_packet", implementation_packet)
    workflow.add_node("external_agent_handoff", external_agent_handoff)
    workflow.add_node("mcp_execution", mcp_execution)
    workflow.add_node("verification", verification)
    workflow.add_node("evidence_intake", evidence_intake)
    workflow.add_node("requirements_review", requirements_review)
    workflow.add_node("architecture_review", architecture_review)
    workflow.add_node("qa_review", qa_review)
    workflow.add_node("completeness_review", completeness_review)
    workflow.add_node("known_mistake_review", known_mistake_review)
    workflow.add_node("completion_gate", completion_gate)
    workflow.add_node("revise_packet", revise_packet)
    workflow.add_node("human_interrupt", human_interrupt)
    workflow.add_node("final_control_report", final_control_report)

    workflow.add_edge(START, "task_resolution")
    workflow.add_edge("task_resolution", "repo_discovery")
    workflow.add_edge("repo_discovery", "requirement_contract")
    workflow.add_edge("requirement_contract", "architecture_context")
    workflow.add_edge("architecture_context", "known_mistake_check")
    workflow.add_edge("known_mistake_check", "implementation_packet")
    workflow.add_edge("implementation_packet", "external_agent_handoff")
    workflow.add_edge("external_agent_handoff", "mcp_execution")
    workflow.add_edge("mcp_execution", "verification")
    workflow.add_edge("verification", "evidence_intake")
    workflow.add_edge("evidence_intake", "requirements_review")
    workflow.add_edge("requirements_review", "architecture_review")
    workflow.add_edge("architecture_review", "qa_review")
    workflow.add_edge("qa_review", "completeness_review")
    workflow.add_edge("completeness_review", "known_mistake_review")
    workflow.add_edge("known_mistake_review", "completion_gate")
    workflow.add_conditional_edges(
        "completion_gate",
        route_after_gate,
        {
            "final_control_report": "final_control_report",
            "revise_packet": "revise_packet",
            "human_interrupt": "human_interrupt",
        },
    )
    workflow.add_edge("revise_packet", "final_control_report")
    workflow.add_edge("human_interrupt", "final_control_report")
    workflow.add_edge("final_control_report", END)
    return workflow.compile(checkpointer=InMemorySaver())
