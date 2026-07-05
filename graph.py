from typing import TypedDict, Optional


class RecruitmentState(TypedDict):
    # -----------------------------
    # Input Files
    # -----------------------------
    resume_path: str
    jd_path: str

    # -----------------------------
    # Agent Outputs
    # -----------------------------
    resume_analysis: Optional[dict]
    jd_analysis: Optional[dict]
    match_report: Optional[dict]
    salary_report: Optional[dict]
    final_decision: Optional[dict]
    interview_questions: Optional[dict]