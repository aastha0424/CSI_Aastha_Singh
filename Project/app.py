import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("final_student_model.pkl")

st.set_page_config(page_title="🎓 Student Score Predictor", layout="centered")

st.title("🎓 Student Final Score Predictor (G3)")
st.markdown("Enter student details below to predict their final exam score.")

# Input features
G1 = st.slider("Grade Period 1 (G1)", 0, 20, 10)
G2 = st.slider("Grade Period 2 (G2)", 0, 20, 10)
studytime = st.selectbox("Weekly Study Time (1-4)", [1, 2, 3, 4])
failures = st.selectbox("Number of Past Failures", [0, 1, 2, 3])
absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=5)

sex = st.selectbox("Sex", ["F", "M"])
schoolsup = st.selectbox("School Support", ["yes", "no"])
internet = st.selectbox("Internet Access", ["yes", "no"])

Medu = st.selectbox("Mother's Education (0=none, 4=high)", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's Education (0=none, 4=high)", [0, 1, 2, 3, 4])

# Prediction
if st.button("Predict Final Grade (G3)"):
    input_df = pd.DataFrame([{
        'sex': sex,
        'schoolsup': schoolsup,
        'internet': internet,
        'G1': G1,
        'G2': G2,
        'studytime': studytime,
        'failures': failures,
        'absences': absences,
        'Medu': Medu,
        'Fedu': Fedu
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Final Grade (G3): **{prediction:.2f}**")