from tools.pdf_tool import extract_text_from_pdf
from utils.cache import get_hash, load_cache, save_cache
from utils.llm import safe_gemini_call
from utils.safe_json import safe_json_parse
from utils.safe_json import safe_json_parse

def analyze_job_description(pdf_path):

    # Extract text from JD
    jd_text = extract_text_from_pdf(pdf_path)

    if not jd_text:
        return {
            "error": "No text extracted from Job Description."
        }

    # Cache key
    key = "jd_" + get_hash(jd_text)

    # Check cache
    cached = load_cache(key)
    if cached:
        return cached

    # Prompt
    prompt = f"""
You are an expert HR Job Description Analyzer.

Analyze the Job Description and return ONLY valid JSON.

Schema:
{{
    "job_title": "",
    "required_skills": [],
    "preferred_skills": [],
    "experience_required": "",
    "responsibilities": []
}}

Job Description:
{jd_text}
"""

    # Gemini call
    response = safe_gemini_call(prompt)

    # Parse safely
    result = safe_json_parse(response)

    # Save cache
    save_cache(key, result)

    return result