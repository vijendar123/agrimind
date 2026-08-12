from typing import TypedDict

class FarmState(TypedDict, total=False):
    crop: str
    growth_stage: str
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    temperature: float
    humidity: float
    rainfall: float
    soil_analysis: str
    crop_analysis: str
    fertilizer_recommendation: str
    risk_analysis: str
    final_recommendation: str
