from tools.pdf_tool import extract_text_from_pdf
from utils.cache import get_hash, load_cache, save_cache
from utils.llm import safe_gemini_call
from utils.safe_json import safe_json_parse
from utils.safe_json import safe_json_parse

def analyze_resume(pdf_path):

    # Extract text from resume
    resume_text = extract_text_from_pdf(pdf_path)

    if not resume_text:
        return {
            "error": "No text extracted from resume."
        }

    # Generate cache key
    key = "resume_" + get_hash(resume_text)

    # Check cache
    cached = load_cache(key)
    if cached:
        return cached

    # Prompt
    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume and return ONLY valid JSON.

Schema:
{{
    "candidate_name": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Resume:
{resume_text}
"""

    # Gemini call
    response = safe_gemini_call(prompt)

    # Parse JSON safely
    result = safe_json_parse(response)

    # Save to cache
    save_cache(key, result)

    return result