import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Saved Model aur Scaler ko load karte hain
@st.cache_resource
def load_assets():
    model = joblib.load('crypto_volatility_model.pkl')
    scaler = joblib.load('crypto_scaler.pkl')
    return model, scaler

try:
    model, scaler = load_assets()
    assets_loaded = True
    feature_names = model.feature_names_in_
except:
    assets_loaded = False

# 2. Web App ka UI Design
st.set_page_config(page_title="Crypto Volatility Predictor", page_icon="🪙", layout="centered")
st.title("🪙 Cryptocurrency Volatility Predictor")
st.write("Enter the required technical features below to forecast market volatility level.")

if not assets_loaded:
    st.error("⚠️ Error: 'crypto_volatility_model.pkl' or 'crypto_scaler.pkl' not found! Please keep them in the same folder.")
else:
    st.subheader("📊 Input Features (Scaled/Engineered Values)")
    input_data = {}
    col1, col2 = st.columns(2)
 
    for i, feature in enumerate(feature_names):
        with col1 if i % 2 == 0 else col2:
            input_data[feature] = st.number_input(f"Enter {feature}", value=0.0, format="%.6f")
 
    # 3. Prediction Button
    st.markdown("---")
    if st.button("🔮 Predict Volatility", type="primary"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
 
        st.success(f"### 📈 Predicted Volatility Score: **{prediction:.6f}**")
 
        if prediction < 0.005:
            st.info("💡 Market State: **Low Volatility** (Stable/Consolidation)")
        elif prediction < 0.015:
            st.warning("⚡ Market State: **Moderate Volatility** (Normal Trading)")
        else:
            st.error("🚨 Market State: **High Volatility** (Extreme Action/High Risk)")