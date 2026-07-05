from pydantic import BaseModel
from typing import List, Optional


class ResumeData(BaseModel):
    candidate_name: Optional[str] = None
    skills: List[str] = []
    education: List[str] = []
    experience: List[str] = []
    projects: List[str] = []
    certifications: List[str] = []


class JobDescriptionData(BaseModel):
    job_title: Optional[str] = None
    required_skills: List[str] = []
    preferred_skills: List[str] = []
    experience_required: Optional[str] = None
    responsibilities: List[str] = []


class MatchReport(BaseModel):
    match_score: int = 0
    matched_skills: List[str] = []
    missing_skills: List[str] = []
    strengths: List[str] = []
    weaknesses: List[str] = []
    recommendation: str = ""


class SalaryData(BaseModel):
    salary_range: str = ""
    expected_ctc: str = ""
    confidence: str = ""
    reason: str = ""


class FinalRecommendation(BaseModel):
    decision: str = ""
    confidence: str = ""
    reason: str = ""
    pros: List[str] = []
    cons: List[str] = []
    next_step: str = ""


class InterviewQuestions(BaseModel):
    technical: List[dict] = []
    hr: List[dict] = []
    coding_question: dict = {}
    difficulty: str = ""