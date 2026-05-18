from __future__ import annotations

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from harness.models import openrouter_model
from harness.prompts import (
    ARCHITECTURE_CONTEXT_PROMPT,
    COMPLETION_DECISION_PROMPT,
    EXTERNAL_AGENT_HANDOFF_PROMPT,
    FINAL_CONTROL_REPORT_PROMPT,
    IMPLEMENTATION_PACKET_PROMPT,
    KNOWN_MISTAKE_CHECK_PROMPT,
    REQUIREMENT_CONTRACT_PROMPT,
    REVIEWER_COUNCIL_PROMPT,
)
from harness.state import HarnessState


def _invoke_role(prompt: str, user_content: str, model_env: str, *, temperature: float = 0.2) -> str:
    model = openrouter_model(model_env, temperature=temperature)
    response = model.invoke(
        [
            SystemMessage(content=prompt),
            HumanMessage(content=user_content),
        ]
    )
    return str(response.content)


def requirement_contract(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{state["backlog_item"]}

Stakeholder or project context:
{state.get("stakeholder_context", "")}
"""
    output = _invoke_role(REQUIREMENT_CONTRACT_PROMPT, content, "REVIEWER_MODEL", temperature=0.1)
    return {"requirement_contract": output, "artifacts": [f"## Requirement Contract\n\n{output}"]}


def architecture_context(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{state["backlog_item"]}

Requirement contract:
{state["requirement_contract"]}

Stakeholder or project context:
{state.get("stakeholder_context", "")}
"""
    output = _invoke_role(ARCHITECTURE_CONTEXT_PROMPT, content, "REVIEWER_MODEL", temperature=0.1)
    return {"architecture_context": output, "artifacts": [f"## Architecture Context\n\n{output}"]}


def known_mistake_check(state: HarnessState) -> HarnessState:
    content = f"""Persistent known mistakes:
{state.get("lessons", "")}

Task input:
{state["backlog_item"]}

Requirement contract:
{state["requirement_contract"]}

Architecture context:
{state["architecture_context"]}
"""
    output = _invoke_role(KNOWN_MISTAKE_CHECK_PROMPT, content, "FAST_MODEL", temperature=0.1)
    return {"known_mistake_check": output, "artifacts": [f"## Known Mistake Check\n\n{output}"]}


def implementation_packet(state: HarnessState) -> HarnessState:
    content = f"""Task input:
{state["backlog_item"]}

Requirement contract:
{state["requirement_contract"]}

Architecture context:
{state["architecture_context"]}

Known mistake check:
{state["known_mistake_check"]}
"""
    output = _invoke_role(IMPLEMENTATION_PACKET_PROMPT, content, "PLANNER_MODEL", temperature=0.1)
    return {"implementation_packet": output, "artifacts": [f"## Implementation Packet\n\n{output}"]}


def external_agent_handoff(state: HarnessState) -> HarnessState:
    content = f"""Requirement contract:
{state["requirement_contract"]}

Architecture context:
{state["architecture_context"]}

Known mistake check:
{state["known_mistake_check"]}

Implementation packet:
{state["implementation_packet"]}
"""
    output = _invoke_role(EXTERNAL_AGENT_HANDOFF_PROMPT, content, "PLANNER_MODEL", temperature=0.1)
    return {"external_agent_handoff": output, "artifacts": [f"## External Agent Handoff\n\n{output}"]}


def reviewer_council(state: HarnessState) -> HarnessState:
    content = f"""Requirement contract:
{state["requirement_contract"]}

Architecture context:
{state["architecture_context"]}

Known mistake check:
{state["known_mistake_check"]}

Implementation packet:
{state["implementation_packet"]}

External agent handoff:
{state["external_agent_handoff"]}
"""
    output = _invoke_role(REVIEWER_COUNCIL_PROMPT, content, "REVIEWER_MODEL", temperature=0.1)
    return {
        "reviewer_council": output,
        "architecture_review": output,
        "qa_review": output,
        "artifacts": [f"## Reviewer Council\n\n{output}"],
    }


def completion_decision(state: HarnessState) -> HarnessState:
    content = f"""Requirement contract:
{state["requirement_contract"]}

Reviewer council:
{state["reviewer_council"]}

Implementation packet:
{state["implementation_packet"]}

Known mistake check:
{state["known_mistake_check"]}
"""
    output = _invoke_role(COMPLETION_DECISION_PROMPT, content, "REVIEWER_MODEL", temperature=0.0)
    return {"completion_decision": output, "artifacts": [f"## Completion Decision\n\n{output}"]}


def final_control_report(state: HarnessState) -> HarnessState:
    content = "\n\n".join(state["artifacts"])
    output = _invoke_role(FINAL_CONTROL_REPORT_PROMPT, content, "PLANNER_MODEL", temperature=0.1)
    return {"final_control_report": output, "artifacts": [f"## Final Control Report\n\n{output}"]}


def build_graph():
    workflow = StateGraph(HarnessState)
    workflow.add_node("requirement_contract", requirement_contract)
    workflow.add_node("architecture_context", architecture_context)
    workflow.add_node("known_mistake_check", known_mistake_check)
    workflow.add_node("implementation_packet", implementation_packet)
    workflow.add_node("external_agent_handoff", external_agent_handoff)
    workflow.add_node("reviewer_council", reviewer_council)
    workflow.add_node("completion_decision", completion_decision)
    workflow.add_node("final_control_report", final_control_report)

    workflow.add_edge(START, "requirement_contract")
    workflow.add_edge("requirement_contract", "architecture_context")
    workflow.add_edge("architecture_context", "known_mistake_check")
    workflow.add_edge("known_mistake_check", "implementation_packet")
    workflow.add_edge("implementation_packet", "external_agent_handoff")
    workflow.add_edge("external_agent_handoff", "reviewer_council")
    workflow.add_edge("reviewer_council", "completion_decision")
    workflow.add_edge("completion_decision", "final_control_report")
    workflow.add_edge("final_control_report", END)

    return workflow.compile(checkpointer=InMemorySaver())
