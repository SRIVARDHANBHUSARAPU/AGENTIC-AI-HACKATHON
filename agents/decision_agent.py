from utils.llm import safe_gemini_call
from utils.safe_json import safe_json_parse
import json
from utils.safe_json import safe_json_parse

def hiring_decision(match_report):

    prompt = f"""
You are a Senior HR Manager.

Analyze the candidate's match report and decide whether the candidate should be hired.

Return ONLY valid JSON.

Schema:
{{
    "decision": "",
    "confidence": "",
    "reason": "",
    "pros": [],
    "cons": [],
    "next_step": ""
}}

Candidate Match Report:
{json.dumps(match_report, indent=2)}
"""

    # Gemini call
    response = safe_gemini_call(prompt)

    # Parse JSON safely
    result = safe_json_parse(response)

    return result