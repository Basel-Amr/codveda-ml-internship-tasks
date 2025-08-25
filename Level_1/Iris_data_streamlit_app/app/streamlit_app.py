import streamlit as st
import pandas as pd
import numpy as np
from utils.model_utils import load_model, save_prediction, get_prediction_history
from utils.preprocessing import load_scaler
from streamlit.components.v1 import html

# -------------------- #
# Streamlit Config
# -------------------- #
st.set_page_config(page_title="Iris Classifier 🌸", page_icon="🌸", layout="wide")

# -------------------- #
# Show Custom HTML Home Page
# -------------------- #
with open("app/templates/home.html", "r", encoding="utf-8") as f:
    home_html = f.read()
html(home_html, height=250)

# -------------------- #
# Load Model + Scaler
# -------------------- #
model = load_model("models/KNN_best_Iris.pkl")
scaler, num_cols = load_scaler("models/scaler.pkl")
if model is None or scaler is None:
    st.error("❌ Failed to load model or scaler. Please check paths.")
    st.stop()

# -------------------- #
# Sidebar Input Features
# -------------------- #
st.sidebar.header("🔧 Input Features")
sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.8)
sepal_width  = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 4.3)
petal_width  = st.sidebar.slider("Petal Width", 0.1, 2.5, 1.3)

input_raw = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=num_cols)
input_scaled = input_raw.copy()
input_scaled[num_cols] = scaler.transform(input_scaled[num_cols])


# -------------------- #
# Predict Button
# -------------------- #
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #f8b500;
        color: #1e1e1e;
        font-size: 20px;
        height: 50px;
        width: 100%;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ffaa00;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

if st.button("Predict 🌸"):
    # -------------------- #
    # Prediction
    # -------------------- #
    prediction = model.predict(input_scaled)[0]
    class_map = { "setosa": "Setosa 🌱", "versicolor": "Versicolor 🌿", "virginica": "Virginica 🌺" }
    predicted_label = class_map.get(prediction, prediction)

    st.subheader("🔮 Prediction Result")
    st.success(f"The model predicts: **{predicted_label}**")

    # -------------------- #
    # Save to database
    # -------------------- #
    save_prediction(sepal_length, sepal_width, petal_length, petal_width, predicted_label)

    # -------------------- #
    # Probability Visualization
    # -------------------- #
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_scaled)[0]
        prob_df = pd.DataFrame({
            "Class": list(class_map.values()),
            "Probability": probs
        })
        st.subheader("📈 Prediction Confidence")
        for i, row in prob_df.iterrows():
            st.write(f"**{row['Class']}**")
            st.progress(int(row['Probability']*100))
    else:
        st.info("ℹ️ This model does not support probability outputs (predict_proba).")

    # -------------------- #
    # Prediction History
    # -------------------- #
    st.subheader("📜 Prediction History (Latest 50)")
    history_df = get_prediction_history(limit=50)
    if not history_df.empty:
        st.dataframe(history_df, height=300)
    else:
        st.info("No prediction history found yet.")

# -------------------- #
# Personal Info Footer (Dark Theme)
# -------------------- #
st.markdown("---")
footer_html = """
<div style="
    text-align: center;
    background-color: #1e1e1e;
    color: #f8b500;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
">
    <strong style="font-size: 1.2em;">Developed by Basel Amr Barakat</strong><br>
    <a href='https://www.linkedin.com/in/baselamrbarakat/' target='_blank' style='color:#f8b500; text-decoration:none; margin:0 10px;'>🔗 LinkedIn</a> |
    <a href='https://github.com/Basel-Amr' target='_blank' style='color:#f8b500; text-decoration:none; margin:0 10px;'>🐱 GitHub</a> |
    <a href='mailto:baselamr52@gmail.com' style='color:#f8b500; text-decoration:none; margin:0 10px;'>✉️ Email</a> |
    <span style='margin:0 10px;'>📞 01000907482</span>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
