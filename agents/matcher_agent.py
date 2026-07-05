from utils.llm import safe_gemini_call
from utils.safe_json import safe_json_parse
import json
from utils.safe_json import safe_json_parse

def match_resume_with_jd(resume_analysis, jd_analysis):

    prompt = f"""
You are an expert ATS Resume Matcher.

Compare the Resume with the Job Description.

Return ONLY valid JSON.

Schema:
{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "recommendation": ""
}}

Resume Analysis:
{json.dumps(resume_analysis, indent=2)}

Job Description Analysis:
{json.dumps(jd_analysis, indent=2)}
"""

    # Gemini Call
    response = safe_gemini_call(prompt)

    # Parse JSON safely
    result = safe_json_parse(response)

    return result