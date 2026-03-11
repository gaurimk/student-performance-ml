import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

# Page title
st.title("🎓 Student Performance Predictor")

st.write("Enter student details to predict the final grade (G3).")

st.divider()

# Input fields
studytime = st.slider("Study Time (1 = low, 4 = high)", 1, 4, 2)
failures = st.slider("Number of Past Failures", 0, 3, 0)
absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=5)
G1 = st.number_input("First Period Grade (G1)", min_value=0, max_value=20, value=10)
G2 = st.number_input("Second Period Grade (G2)", min_value=0, max_value=20, value=10)

st.divider()

# Prediction button
if st.button("Predict Final Grade"):

    features = np.array([[studytime, failures, absences, G1, G2]])

    prediction = model.predict(features)

    st.success(f"📊 Predicted Final Grade (G3): {prediction[0]:.2f}")

    if prediction >= 10:
        st.info("✅ The student is likely to PASS.")
    else:
        st.error("⚠️ The student is likely to FAIL.")