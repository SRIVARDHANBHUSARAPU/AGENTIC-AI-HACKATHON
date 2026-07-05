import streamlit as st
import tempfile

from app import app
from agents.interview_agent import generate_interview_questions

st.set_page_config(
    page_title="HireGenie AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 HireGenie AI")
st.write("AI Powered Resume Screening System")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.file_uploader(
    "Upload Job Description",
    type=["pdf"]
)

if "result" not in st.session_state:
    st.session_state.result = None

if "interview" not in st.session_state:
    st.session_state.interview = None


if st.button("Analyze Candidate"):

    if resume is None or jd is None:
        st.error("Please upload both Resume and Job Description.")
        st.stop()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(resume.read())
        resume_path = f.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(jd.read())
        jd_path = f.name

    initial_state = {
        "resume_path": resume_path,
        "jd_path": jd_path,

        "resume_analysis": None,
        "jd_analysis": None,
        "match_report": None,
        "salary_report": None,
        "final_decision": None,
        "interview_questions": None,
    }

    with st.spinner("Analyzing Resume..."):
        result = app.invoke(initial_state)

    st.session_state.result = result
    st.session_state.interview = None


if st.session_state.result:

    result = st.session_state.result

    st.success("Analysis Completed")

    st.header("📊 Match Report")
    st.json(result["match_report"])

    st.header("💰 Salary Prediction")
    st.json(result["salary_report"])

    st.header("👨‍💼 HR Decision")

    decision = st.radio(
        "Proceed to Technical Interview?",
        ["Yes", "No"]
    )

    if st.button("Submit Decision"):

        if decision == "Yes":

            with st.spinner("Generating Interview Questions..."):

                interview = generate_interview_questions(
                    result["match_report"]
                )

                st.session_state.interview = interview

        else:

            st.warning("Candidate Rejected by HR")
            st.session_state.interview = None

    if st.session_state.interview is not None:

        st.header("📝 Interview Questions")
        st.json(st.session_state.interview)