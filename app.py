import streamlit as st
from agents.orchestrator import agri_graph

st.set_page_config(page_title="AgriMind", page_icon="🌱", layout="wide")

st.title("🌱 AgriMind")
st.caption("Multi-agent agriculture advisory system")

with st.sidebar:
    st.header("Farm Inputs")
    crop = st.text_input("Crop", "Tomato")
    growth_stage = st.text_input("Growth stage", "Flowering")
    nitrogen = st.number_input("Nitrogen (N)", value=30.0)
    phosphorus = st.number_input("Phosphorus (P)", value=35.0)
    potassium = st.number_input("Potassium (K)", value=50.0)
    ph = st.number_input("Soil pH", value=6.5)
    temperature = st.number_input("Temperature (°C)", value=28.0)
    humidity = st.number_input("Humidity (%)", value=70.0)
    rainfall = st.number_input("Rainfall (mm)", value=10.0)

if st.button("Analyze Farm", type="primary"):
    farm_data = {
        "crop": crop,
        "growth_stage": growth_stage,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "ph": ph,
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall,
    }

    try:
        result = agri_graph.invoke(farm_data)

        st.subheader("🌾 Final Recommendation")
        st.write(result.get("final_recommendation", "No final recommendation generated."))

        with st.expander("Soil Analysis"):
            st.write(result.get("soil_analysis", ""))

        with st.expander("Crop Analysis"):
            st.write(result.get("crop_analysis", ""))

        with st.expander("Fertilizer Recommendation"):
            st.write(result.get("fertilizer_recommendation", ""))

        with st.expander("Risk Analysis"):
            st.write(result.get("risk_analysis", ""))

    except Exception as e:
        st.error(f"Agent execution failed: {e}")
