RESUME_PROMPT = """
You are an expert HR Resume Analyzer.

Extract:

Name

Email

Phone

Skills

Education

Experience

Projects

Certifications

Return structured JSON only.
"""



JD_PROMPT = """
You are a Job Description Analyzer.

Extract

Job Title

Required Skills

Education

Experience

Return JSON only.
"""



INTERVIEW_PROMPT = """
Generate

5 Technical Questions

5 HR Questions

based on the resume and job description.
"""



DECISION_PROMPT = """
Compare resume with job description.

Calculate match score.

Return

Strengths

Weaknesses

Recommendation

Return JSON only.
"""