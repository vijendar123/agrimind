from .state import FarmState

def final_agent(state: FarmState) -> FarmState:
    state["final_recommendation"] = (
        f"### AgriMind Summary\n\n"
        f"**Crop:** {state.get('crop', 'Unknown')}\n\n"
        f"**Soil:** {state.get('soil_analysis', '')}\n\n"
        f"**Crop assessment:** {state.get('crop_analysis', '')}\n\n"
        f"**Fertilizer guidance:** {state.get('fertilizer_recommendation', '')}\n\n"
        f"**Risk assessment:** {state.get('risk_analysis', '')}\n\n"
        "These are screening recommendations, not a substitute for a local agronomist or laboratory soil test."
    )
    return state
