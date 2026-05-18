from __future__ import annotations

from operator import add
from typing import Annotated, TypedDict


class HarnessState(TypedDict, total=False):
    backlog_item: str
    stakeholder_context: str
    lessons: str
    requirement_contract: str
    architecture_context: str
    known_mistake_check: str
    implementation_packet: str
    external_agent_handoff: str
    reviewer_council: str
    completion_decision: str
    architecture_review: str
    qa_review: str
    final_control_report: str
    artifacts: Annotated[list[str], add]
