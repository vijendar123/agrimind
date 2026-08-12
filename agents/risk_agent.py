from .state import FarmState

def risk_agent(state: FarmState) -> FarmState:
    risks = []

    temperature = state.get("temperature", 0)
    humidity = state.get("humidity", 0)
    rainfall = state.get("rainfall", 0)

    if temperature >= 35:
        risks.append("High-temperature stress may be a concern.")
    if humidity >= 85:
        risks.append("High humidity may increase disease risk.")
    if rainfall >= 50:
        risks.append("Heavy rainfall may increase waterlogging or nutrient-loss risk.")

    if not risks:
        risks.append("No major environmental risk is flagged by the simple screening rules.")

    state["risk_analysis"] = " ".join(risks)
    return state
