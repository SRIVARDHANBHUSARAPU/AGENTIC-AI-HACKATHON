import time
time.sleep(2)

from langgraph.graph import StateGraph, END
from graph import RecruitmentState

from agents.supervisor import (
    resume_node,
    jd_node,
    matcher_node,
    salary_node,
    decision_node,
    interview_node,
)

# -----------------------------
# Create Workflow
# -----------------------------
workflow = StateGraph(RecruitmentState)

# -----------------------------
# Add Nodes
# -----------------------------
workflow.add_node("resume", resume_node)
workflow.add_node("jd", jd_node)
workflow.add_node("matcher", matcher_node)
workflow.add_node("salary", salary_node)
workflow.add_node("decision", decision_node)
workflow.add_node("interview", interview_node)

# -----------------------------
# Entry Point
# -----------------------------
workflow.set_entry_point("resume")

# -----------------------------
# Flow
# -----------------------------
workflow.add_edge("resume", "jd")
workflow.add_edge("jd", "matcher")
workflow.add_edge("matcher", "salary")
workflow.add_edge("salary", "decision")


# -----------------------------
# Conditional Routing
# -----------------------------
def route_after_decision(state):

    if (
        state["final_decision"] is not None
        and state["final_decision"]["decision"] == "Proceed to Interview"
    ):
        return "interview"

    return END


workflow.add_conditional_edges(
    "decision",
    route_after_decision,
    {
        "interview": "interview",
        END: END,
    },
)

workflow.add_edge("interview", END)

# -----------------------------
# Compile Graph
# -----------------------------
app = workflow.compile()


# -----------------------------
# Run only when executed directly
# -----------------------------
if __name__ == "__main__":

    initial_state = {
        "resume_path": "database/resumes/resume1.pdf",
        "jd_path": "database/job_descriptions/JD.pdf",

        "resume_analysis": None,
        "jd_analysis": None,
        "match_report": None,
        "salary_report": None,
        "final_decision": None,
        "interview_questions": None,
    }

    result = app.invoke(initial_state)

    print("\n" + "=" * 80)
    print("MATCH REPORT")
    print("=" * 80)
    print(result["match_report"])

    print("\n" + "=" * 80)
    print("SALARY REPORT")
    print("=" * 80)
    print(result["salary_report"])

    print("\n" + "=" * 80)
    print("FINAL DECISION")
    print("=" * 80)
    print(result["final_decision"])

    if result["interview_questions"] is not None:
        print("\n" + "=" * 80)
        print("INTERVIEW QUESTIONS")
        print("=" * 80)
        print(result["interview_questions"])