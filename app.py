import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Smart City AQI Monitor",
    page_icon="🌍",
    layout="centered"
)

# ---------- LOAD MODELS ----------
pipeline = pickle.load(open("aqi_pipeline.pkl","rb"))
columns = pickle.load(open("columns.pkl","rb"))
early_model = pickle.load(open("early_model.pkl","rb"))
early_cols = pickle.load(open("early_columns.pkl","rb"))

# ---------- AQI CATEGORY ----------
def aqi_category(aqi):
    if aqi <= 50: return "Good", "#2ecc71"
    elif aqi <= 100: return "Satisfactory", "#9acd32"
    elif aqi <= 200: return "Moderate", "#f39c12"
    elif aqi <= 300: return "Poor", "#e67e22"
    elif aqi <= 400: return "Very Poor", "#e74c3c"
    else: return "Severe", "#8e44ad"

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;'>🌍 Smart City AQI Monitoring System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>AI-powered Early Warning + AQI Prediction</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------- INPUTS ----------
st.subheader("📊 Enter Sensor Readings")

col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5 (µg/m³)",0.0,1000.0,80.0)
    pm10 = st.number_input("PM10 (µg/m³)",0.0,1000.0,120.0)
    no2 = st.number_input("NO₂ (ppb)",0.0,500.0,40.0)
    so2 = st.number_input("SO₂ (ppb)",0.0,500.0,15.0)

with col2:
    co = st.number_input("CO (ppm)",0.0,50.0,1.5)
    o3 = st.number_input("O₃ (ppb)",0.0,500.0,35.0)
    temp = st.number_input("Temperature (°C)",-10.0,55.0,28.0)
    humidity = st.number_input("Humidity (%)",0.0,100.0,65.0)

city_type = st.selectbox(
    "City Type",
    ["coastal","desert","industrial","metropolitan","mixed","plains","IT_hub"]
)

st.markdown("---")

# ---------- PREDICT ----------
if st.button("🔍 Run Smart AQI Analysis"):

    features = pd.DataFrame([{
        'PM2.5': pm25,
        'PM10': pm10,
        'NO2': no2,
        'SO2': so2,
        'CO': co,
        'O3': o3,
        'Temperature': temp,
        'Humidity': humidity,
        'City_Type': city_type
    }])

    # encode categorical
    features = pd.get_dummies(features, columns=['City_Type'])

    # ---------- ML EARLY WARNING ----------
    early_features = features.reindex(columns=early_cols, fill_value=0)
    risk_prob = early_model.predict_proba(early_features)[0][1]

    st.markdown("### 🤖 Early Air Quality Risk Advisory")

    # probability bar
    st.progress(float(risk_prob))
    st.write(f"**Predicted Risk Probability:** `{risk_prob:.2f}`")

    if risk_prob >= 0.75:
        st.error("🚨 **High Risk (0.75–1.00)**")
        st.write("Air pollution is likely to worsen soon.")
        st.write("**Recommended actions:**")
        st.write("• Avoid outdoor exposure")
        st.write("• Children & elderly stay indoors")
        st.write("• Use masks or air purifiers")

    elif risk_prob >= 0.45:
        st.warning("⚠ **Moderate Risk (0.45–0.74)**")
        st.write("Pollution trends suggest air quality may deteriorate later today.")
        st.write("**Recommended actions:**")
        st.write("• Limit outdoor activity")
        st.write("• Monitor updates")
        st.write("• Avoid peak traffic hours")

    else:
        st.success("✅ **Low Risk (0.00–0.44)**")
        st.write("Air conditions appear stable.")
        st.write("Normal outdoor activities are safe.")

    st.markdown("---")

    # ---------- FINAL AQI PREDICTION ----------
    features = features.reindex(columns=columns, fill_value=0)
    predicted_aqi = pipeline.predict(features)[0]
    category, color = aqi_category(predicted_aqi)

    st.markdown("### 🌫 Final AQI Prediction")

    st.markdown(
        f"""
        <div style="padding:25px;background:{color};
                    color:white;border-radius:12px;
                    text-align:center;font-size:28px;
                    font-weight:600;">
            AQI Value: {predicted_aqi:.2f} <br>
            Category: {category}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("Smart City Environmental Intelligence Dashboard")