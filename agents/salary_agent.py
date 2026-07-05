from utils.llm import safe_gemini_call
from utils.safe_json import safe_json_parse
import json
from utils.safe_json import safe_json_parse

def predict_salary(match_report):

    prompt = f"""
You are an HR Salary Expert.

Based on the candidate's match report, estimate a realistic salary.

Return ONLY valid JSON.

Schema:
{{
    "salary_range": "",
    "expected_ctc": "",
    "confidence": "",
    "reason": ""
}}

Candidate Match Report:
{json.dumps(match_report, indent=2)}
"""

    # Gemini Call
    response = safe_gemini_call(prompt)

    # Parse JSON safely
    result = safe_json_parse(response)

    return result