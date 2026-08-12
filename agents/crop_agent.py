from .state import FarmState

def crop_agent(state: FarmState) -> FarmState:
    crop = state.get("crop", "Unknown")
    stage = state.get("growth_stage", "Unknown")

    state["crop_analysis"] = (
        f"Crop: {crop}. Growth stage: {stage}. "
        "Recommendations should be adjusted using the crop stage and measured farm conditions."
    )
    return state
