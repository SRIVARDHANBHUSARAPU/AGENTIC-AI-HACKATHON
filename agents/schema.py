from pydantic import BaseModel
from typing import List, Optional


class ResumeAnalysis(BaseModel):
    name: Optional[str]
    skills: List[str]
    education: List[str]
    experience: List[str]
    projects: List[str]
    certifications: List[str]


class JDAnalysis(BaseModel):
    role: str
    required_skills: List[str]
    preferred_skills: List[str]
    experience_required: str


class MatchReport(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    strengths: List[str]
    weaknesses: List[str]
    recommendation: str


class InterviewQuestions(BaseModel):
    technical: List[str]
    hr: List[str]
    coding_question: str
    difficulty: str