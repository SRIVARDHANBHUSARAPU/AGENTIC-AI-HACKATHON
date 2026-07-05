from agents.resume_agent import analyze_resume
from agents.jd_agent import analyze_job_description
from agents.matcher_agent import match_resume_with_jd
from agents.salary_agent import predict_salary
from agents.interview_agent import generate_interview_questions


# -----------------------------
# Resume Node
# -----------------------------
def resume_node(state):
    state["resume_analysis"] = analyze_resume(state["resume_path"])
    return state


# -----------------------------
# JD Node
# -----------------------------
def jd_node(state):
    state["jd_analysis"] = analyze_job_description(state["jd_path"])
    return state


# -----------------------------
# Matcher Node
# -----------------------------
def matcher_node(state):
    state["match_report"] = match_resume_with_jd(
        state["resume_analysis"],
        state["jd_analysis"]
    )
    return state


# -----------------------------
# Salary Node
# -----------------------------
def salary_node(state):
    state["salary_report"] = predict_salary(
        state["match_report"]
    )
    return state


# -----------------------------
# Human Decision Node
# -----------------------------
def decision_node(state):
    # Don't ask for terminal input.
    # Just initialize the field.
    state["final_decision"] = None
    return state

    print("\n" + "=" * 80)
    print("SALARY REPORT")
    print("=" * 80)
    print(state["salary_report"])

    print("\n" + "=" * 80)

    while True:
        choice = input(
            "Do you want to continue with Interview? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:
            state["final_decision"] = {
                "decision": "Proceed to Interview"
            }
            break

        elif choice in ["no", "n"]:
            state["final_decision"] = {
                "decision": "Rejected by HR"
            }
            state["interview_questions"] = None
            break

        else:
            print("Please enter yes or no.")

    return state


# -----------------------------
# Interview Node
# -----------------------------
def interview_node(state):

    state["interview_questions"] = generate_interview_questions(
        state["match_report"]
    )

    return state