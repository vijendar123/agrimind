from .state import FarmState

def soil_agent(state: FarmState) -> FarmState:
    n = state.get("nitrogen", 0)
    p = state.get("phosphorus", 0)
    k = state.get("potassium", 0)
    ph = state.get("ph", 7)

    observations = []

    if n < 40:
        observations.append("Nitrogen is relatively low.")
    elif n > 100:
        observations.append("Nitrogen is relatively high.")
    else:
        observations.append("Nitrogen is in a moderate range.")

    if p < 30:
        observations.append("Phosphorus is relatively low.")
    else:
        observations.append("Phosphorus is not flagged as low.")

    if k < 40:
        observations.append("Potassium is relatively low.")
    else:
        observations.append("Potassium is not flagged as low.")

    if ph < 5.5:
        observations.append("Soil is acidic.")
    elif ph > 7.5:
        observations.append("Soil is alkaline.")
    else:
        observations.append("Soil pH is in a broadly suitable range.")

    state["soil_analysis"] = " ".join(observations)
    return state
