from __future__ import annotations

import json
import re
from typing import TypeVar

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, ValidationError

from harness.models import openrouter_model
from harness.prompts import (
    ARCHITECTURE_CONTEXT_PROMPT,
    ARCHITECTURE_REVIEW_PROMPT,
    COMPLETENESS_REVIEW_PROMPT,
    EXTERNAL_AGENT_HANDOFF_PROMPT,
    FINAL_CONTROL_REPORT_PROMPT,
    IMPLEMENTATION_PACKET_PROMPT,
    KNOWN_MISTAKE_CHECK_PROMPT,
    KNOWN_MISTAKE_REVIEW_PROMPT,
    QA_REVIEW_PROMPT,
    REQUIREMENT_CONTRACT_PROMPT,
    REQUIREMENTS_REVIEW_PROMPT,
)
from harness.rendering import render_model, render_text
from harness.schemas import (
    ArchitectureContext,
    ChecklistStatus,
    CompletionDecision,
    ContractItem,
    EvidenceBundle,
    ExternalAgentHandoff,
    HumanInterrupt,
    ImplementationPacket,
    KnownMistakeCheck,
    ReviewFinding,
    ReviewerVerdict,
    RevisionPlan,
    TaskContract,
    Waiver,
)
from harness.state import HarnessState

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


def requirement_contract(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{state["backlog_item"]}

Stakeholder or project context:
{state.get("stakeholder_context", "")}
"""
    contract = _invoke_schema(REQUIREMENT_CONTRACT_PROMPT, content, TaskContract, "REVIEWER_MODEL", temperature=0.1)
    return {
        "requirement_contract": contract.model_dump(),
        "artifacts": [render_model("Requirement Contract", contract)],
    }


def architecture_context(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{state["backlog_item"]}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Stakeholder or project context:
{state.get("stakeholder_context", "")}
"""
    architecture = _invoke_schema(
        ARCHITECTURE_CONTEXT_PROMPT,
        content,
        ArchitectureContext,
        "REVIEWER_MODEL",
        temperature=0.1,
    )
    return {
        "architecture_context": architecture.model_dump(),
        "artifacts": [render_model("Architecture Context", architecture)],
    }


def known_mistake_check(state: HarnessState) -> HarnessState:
    content = f"""Persistent known mistakes:
{json.dumps(state.get("lessons", []), indent=2)}

Task input:
{state["backlog_item"]}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}
"""
    check = _invoke_schema(KNOWN_MISTAKE_CHECK_PROMPT, content, KnownMistakeCheck, "FAST_MODEL", temperature=0.1)
    return {
        "known_mistake_check": check.model_dump(),
        "artifacts": [render_model("Known Mistake Check", check)],
    }


def implementation_packet(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{state["backlog_item"]}

Requirement contract:
{json.dumps(state["requirement_contract"], indent=2)}

Architecture context:
{json.dumps(state["architecture_context"], indent=2)}

Known mistake check:
{json.dumps(state["known_mistake_check"], indent=2)}
"""
    packet = _invoke_schema(
        IMPLEMENTATION_PACKET_PROMPT,
        content,
        ImplementationPacket,
        "PLANNER_MODEL",
        temperature=0.1,
    )
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
    handoff = _invoke_schema(
        EXTERNAL_AGENT_HANDOFF_PROMPT,
        content,
        ExternalAgentHandoff,
        "PLANNER_MODEL",
        temperature=0.1,
    )
    return {"external_agent_handoff": handoff.model_dump(), "artifacts": [render_model("External Agent Handoff", handoff)]}


def evidence_intake(state: HarnessState) -> HarnessState:
    evidence = EvidenceBundle(
        has_evidence=bool(
            state.get("changed_files")
            or state.get("diff_summary")
            or state.get("test_output")
            or state.get("agent_output")
            or state.get("waiver_requests")
        ),
        changed_files=state.get("changed_files", []),
        diff_summary=state.get("diff_summary", ""),
        test_output=state.get("test_output", ""),
        agent_output=state.get("agent_output", ""),
        waiver_requests=[Waiver.model_validate(item) for item in state.get("waiver_requests", [])],
    )
    return {"evidence": evidence.model_dump(), "artifacts": [render_model("Evidence Intake", evidence)]}


def requirements_review(state: HarnessState) -> HarnessState:
    verdict = _review(
        "requirements",
        REQUIREMENTS_REVIEW_PROMPT,
        state,
        "REVIEWER_MODEL",
    )
    return {"requirements_review": verdict.model_dump(), "artifacts": [render_model("Requirements Review", verdict)]}


def architecture_review(state: HarnessState) -> HarnessState:
    verdict = _review(
        "architecture",
        ARCHITECTURE_REVIEW_PROMPT,
        state,
        "REVIEWER_MODEL",
    )
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
    checklist_status: list[ChecklistStatus] = []

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
        next_action = "Revise the implementation packet or provide missing implementation evidence before approval."
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
        next_step="Revise the contract, implementation packet, or external-agent output, then run the harness again with evidence.",
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
    workflow.add_node("requirement_contract", requirement_contract)
    workflow.add_node("architecture_context", architecture_context)
    workflow.add_node("known_mistake_check", known_mistake_check)
    workflow.add_node("implementation_packet", implementation_packet)
    workflow.add_node("external_agent_handoff", external_agent_handoff)

    workflow.add_edge(START, "requirement_contract")
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
    workflow.add_node("requirement_contract", requirement_contract)
    workflow.add_node("architecture_context", architecture_context)
    workflow.add_node("known_mistake_check", known_mistake_check)
    workflow.add_node("implementation_packet", implementation_packet)
    workflow.add_node("external_agent_handoff", external_agent_handoff)
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

    workflow.add_edge(START, "requirement_contract")
    workflow.add_edge("requirement_contract", "architecture_context")
    workflow.add_edge("architecture_context", "known_mistake_check")
    workflow.add_edge("known_mistake_check", "implementation_packet")
    workflow.add_edge("implementation_packet", "external_agent_handoff")
    workflow.add_edge("external_agent_handoff", "evidence_intake")
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
