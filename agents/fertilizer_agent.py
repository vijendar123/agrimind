from .state import FarmState

def fertilizer_agent(state: FarmState) -> FarmState:
    recommendations = []

    if state.get("nitrogen", 0) < 40:
        recommendations.append("Consider a nitrogen source based on a soil test and crop requirement.")
    if state.get("phosphorus", 0) < 30:
        recommendations.append("Consider phosphorus supplementation based on a soil test.")
    if state.get("potassium", 0) < 40:
        recommendations.append("Consider potassium supplementation based on a soil test.")

    if not recommendations:
        recommendations.append(
            "No nutrient is flagged as low by the simple screening rules; avoid unnecessary fertilizer."
        )

    state["fertilizer_recommendation"] = " ".join(recommendations)
    return state
