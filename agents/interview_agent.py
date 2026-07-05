from utils.llm import safe_gemini_call
from utils.safe_json import safe_json_parse
import json
from utils.safe_json import safe_json_parse

def generate_interview_questions(match_report):

    # Convert to dict if Gemini returned string
    if isinstance(match_report, str):
        try:
            match_report = json.loads(match_report)
        except Exception:
            match_report = {}

    strengths = match_report.get("strengths", [])
    missing_skills = match_report.get("missing_skills", [])
    weaknesses = match_report.get("weaknesses", [])

    prompt = f"""
You are a Senior Technical Interviewer.

Generate interview questions ONLY.
DO NOT analyze the candidate again.
DO NOT repeat the match report.

Return ONLY valid JSON.

Schema:
{{
    "technical": [
        {{
            "question": "",
            "answer": ""
        }}
    ],
    "hr": [
        {{
            "question": "",
            "answer": ""
        }}
    ],
    "coding_question": {{
        "question": "",
        "answer": ""
    }},
    "difficulty": ""
}}

Rules:
- Generate exactly 10 technical interview questions with answers.
- Generate exactly 5 HR interview questions with answers.
- Generate 1 Python coding question with solution.
- Focus mainly on the candidate's missing skills.
- Do NOT return strengths, weaknesses, recommendation, or match score.

Candidate Strengths:
{json.dumps(strengths, indent=2)}

Missing Skills:
{json.dumps(missing_skills, indent=2)}

Weaknesses:
{json.dumps(weaknesses, indent=2)}
"""

    response = safe_gemini_call(prompt)

    return safe_json_parse(response)