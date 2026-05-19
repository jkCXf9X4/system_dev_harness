from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator


GateStatus = Literal["approved", "blocked", "waiver_required"]
ReviewStatus = Literal["pass", "fail", "needs_waiver"]


class ContractItem(BaseModel):
    id: str = Field(description="Stable short id, for example FR-001.")
    description: str
    verification_method: str


class Waiver(BaseModel):
    item_id: str
    reason: str
    risk: str
    owner: str
    follow_up: str


class TaskContract(BaseModel):
    task_objective: str
    in_scope: list[str]
    out_of_scope: list[str]
    functional_requirements: list[ContractItem]
    architecture_obligations: list[ContractItem]
    quality_obligations: list[ContractItem]
    acceptance_criteria: list[ContractItem]
    completion_checklist: list[ContractItem]
    waiver_rules: list[str]
    open_questions: list[str] = []

    @field_validator("functional_requirements", "acceptance_criteria", "completion_checklist")
    @classmethod
    def require_items(cls, value: list[ContractItem]) -> list[ContractItem]:
        if not value:
            raise ValueError("must contain at least one checklistable item")
        return value


class ArchitectureContext(BaseModel):
    relevant_system_context: list[str]
    architectural_constraints: list[ContractItem]
    integration_boundaries: list[str]
    dependency_and_coupling_risks: list[str]
    required_existing_patterns: list[str]
    forbidden_shortcuts: list[str]
    architecture_review_checklist: list[ContractItem]


class KnownMistake(BaseModel):
    id: str
    title: str
    pattern: str
    prevention_rule: str
    completion_check: str
    severity: Literal["low", "medium", "high"] = "medium"
    tags: list[str] = []


class KnownMistakeCheck(BaseModel):
    relevant_mistakes: list[KnownMistake]
    task_specific_prevention_rules: list[str]
    checks_before_completion: list[ContractItem]
    new_lesson_candidates: list[str] = []


class ImplementationPacket(BaseModel):
    mission: str
    source_material: list[str]
    required_implementation_behavior: list[str]
    execution_steps: list[str]
    architecture_constraints: list[str]
    known_mistakes_to_avoid: list[str]
    required_tests_and_checks: list[str]
    definition_of_done: list[str]
    stop_conditions: list[str]


class ExternalAgentHandoff(BaseModel):
    agent_instruction: str
    non_negotiable_constraints: list[str]
    completion_checklist: list[str]
    required_final_response: list[str]


class BacklogCandidate(BaseModel):
    path: str
    title: str
    status: str = ""
    goal: str = ""
    scope: list[str] = []
    acceptance_criteria: list[str] = []


class TaskResolution(BaseModel):
    resolution_mode: Literal["direct_prompt", "backlog_selection"]
    selected_task_title: str
    selected_task_path: str = ""
    resolved_task_input: str
    selection_rationale: str


class RepoFileContext(BaseModel):
    path: str
    reason: str
    content: str


class RepoDiscoveryPlan(BaseModel):
    search_queries: list[str]
    relevant_files: list[str]
    rationale: str


class RepoContext(BaseModel):
    backlog_overview: list[BacklogCandidate] = []
    relevant_files: list[str]
    search_results: list[str]
    file_contexts: list[RepoFileContext]
    summary: list[str]


class MCPPatch(BaseModel):
    path: str
    patch: str
    rationale: str


class MCPExecutionPlan(BaseModel):
    summary: str
    needs_external_executor: bool = False
    fallback_reason: str = ""
    patches: list[MCPPatch] = []
    verification_commands: list[str] = []


class PatchApplyResult(BaseModel):
    path: str
    status: Literal["applied", "failed", "skipped"]
    detail: str


class MCPExecutionResult(BaseModel):
    status: Literal["applied", "blocked", "fallback_required"]
    summary: str
    applied_patches: list[PatchApplyResult]
    changed_files: list[str]
    fallback_reason: str = ""


class VerificationCommandResult(BaseModel):
    command: str
    exit_code: int
    stdout: str = ""
    stderr: str = ""


class VerificationReport(BaseModel):
    status: Literal["passed", "failed", "not_run"]
    summary: str
    results: list[VerificationCommandResult]


class ToolTraceEntry(BaseModel):
    tool: str
    arguments: dict[str, Any]
    outcome: str
    details: str = ""


class EvidenceBundle(BaseModel):
    has_evidence: bool
    changed_files: list[str] = []
    diff_summary: str = ""
    test_output: str = ""
    agent_output: str = ""
    waiver_requests: list[Waiver] = []


class ReviewFinding(BaseModel):
    item_id: str
    status: ReviewStatus
    finding: str
    required_fix: str = ""
    evidence: str = ""


class ReviewerVerdict(BaseModel):
    reviewer: Literal["requirements", "architecture", "qa", "completeness", "known_mistakes"]
    status: ReviewStatus
    findings: list[ReviewFinding]
    summary: str


class ChecklistStatus(BaseModel):
    item_id: str
    status: ReviewStatus
    evidence: str


class CompletionDecision(BaseModel):
    status: GateStatus
    contract_checklist_status: list[ChecklistStatus]
    reviewer_approval_status: str
    required_waivers: list[Waiver]
    blocking_gaps: list[str]
    next_required_action: str


class RevisionPlan(BaseModel):
    reason: str
    required_packet_changes: list[str]
    required_contract_changes: list[str] = []
    next_step: str


class HumanInterrupt(BaseModel):
    reason: str
    requested_waivers: list[Waiver]
    human_decision_needed: str
    next_step_after_decision: str
