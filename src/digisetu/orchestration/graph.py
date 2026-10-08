from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class DigiSetuState(TypedDict, total=False):
    business: dict[str, object]
    audit: dict[str, object]
    digital_need_score: int
    qualification: dict[str, object]
    contact: dict[str, object]
    message: str
    approved: bool
    intent: str
    lead_status: str


def discovery_node(state: DigiSetuState) -> DigiSetuState:
    print("Discovery Agent running...")

    return {
        **state,
        "business": {
            "name": "ABC Dental Clinic",
            "business_type": "Dental Clinic",
            "location": "Nagpur",
        },
    }


def audit_node(state: DigiSetuState) -> DigiSetuState:
    print("Website Audit running...")

    return {
        **state,
        "audit": {
            "website_exists": True,
            "https": True,
            "accessible": True,
            "booking": False,
            "payment": False,
            "mobile_friendly": True,
        },
    }


def scoring_node(state: DigiSetuState) -> DigiSetuState:
    print("Scoring running...")

    return {
        **state,
        "digital_need_score": 35,
    }


def qualification_node(state: DigiSetuState) -> DigiSetuState:
    print("Qualification Agent running...")

    return {
        **state,
        "qualification": {
            "qualified": False,
            "digital_gaps": [
                "booking",
                "payment",
            ],
        },
    }


def build_graph():
    workflow = StateGraph(DigiSetuState)

    workflow.add_node("discovery", discovery_node)
    workflow.add_node("audit", audit_node)
    workflow.add_node("scoring", scoring_node)
    workflow.add_node("qualification", qualification_node)

    workflow.add_edge(START, "discovery")
    workflow.add_edge("discovery", "audit")
    workflow.add_edge("audit", "scoring")
    workflow.add_edge("scoring", "qualification")
    workflow.add_edge("qualification", END)

    return workflow.compile()