import streamlit as st
import pickle
import joblib
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

st.title("Health Risk Assessment")

# Upload model files
st.sidebar.header("Upload Model Files")
random_forest_file = st.sidebar.file_uploader("Upload Random Forest Model", type=["pkl"])
scaler_file = st.sidebar.file_uploader("Upload Scaler Model", type=["pkl"])
xgboost_file = st.sidebar.file_uploader("Upload XGBoost Model", type=["pkl"])
neural_network_file = st.sidebar.file_uploader("Upload Neural Network Model", type=["h5"])

# Model selection
model_choice = st.sidebar.selectbox("Select a Model", ["Random Forest", "Scaler", "XGBoost", "Neural Network"])

# Load selected model
def load_model_file(uploaded_file, model_type):
    if uploaded_file is not None:
        try:
            if model_type == "Neural Network":
                return load_model(uploaded_file)
            else:
                return joblib.load(uploaded_file)
        except Exception as e:
            st.error(f"Error loading {model_type} model: {e}")
    return None

model = None
if model_choice == "Random Forest":
    model = load_model_file(random_forest_file, "Random Forest")
elif model_choice == "Scaler":
    model = load_model_file(scaler_file, "Scaler")
elif model_choice == "XGBoost":
    model = load_model_file(xgboost_file, "XGBoost")
elif model_choice == "Neural Network":
    model = load_model_file(neural_network_file, "Neural Network")

if model:
    st.success(f"{model_choice} model loaded successfully!")

# Input fields
bmi = st.number_input("BMI", min_value=0.0, step=0.1, format="%.1f")
heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, step=1)
blood_pressure = st.text_input("Blood Pressure (e.g., 120/80)")
oxygen_saturation = st.slider("Oxygen Saturation (%)", min_value=80, max_value=100, value=98)
respiratory_rate = st.number_input("Respiratory Rate (breaths per minute)", min_value=0, step=1)
blood_sugar = st.number_input("Blood Sugar Level (mg/dL)", min_value=0, step=1)
cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=0, step=1)

# Categorical inputs
exercises = st.radio("Do you exercise regularly?", ["Yes", "No"])
follows_diet = st.radio("Do you follow a healthy diet?", ["Yes", "No"])
sleep_quality = st.selectbox("Sleep Quality", ["Poor", "Average", "Good"])

# Convert categorical inputs to numerical values
exercise_map = {"Yes": 1, "No": 0}
diet_map = {"Yes": 1, "No": 0}
sleep_map = {"Poor": 0, "Average": 1, "Good": 2}

exercise_val = exercise_map[exercises]
diet_val = diet_map[follows_diet]
sleep_val = sleep_map[sleep_quality]

# Process Blood Pressure (convert to two values: systolic and diastolic)
try:
    systolic, diastolic = map(int, blood_pressure.split("/"))
except:
    systolic, diastolic = 0, 0  # Default values if input is invalid

# Submit Button
if st.button("Submit"):
    st.success("Data Submitted Successfully!")
    st.write("### Entered Health Data:")
    st.write(f"- **BMI:** {bmi}")
    st.write(f"- **Heart Rate:** {heart_rate} bpm")
    st.write(f"- **Blood Pressure:** {blood_pressure}")
    st.write(f"- **Oxygen Saturation:** {oxygen_saturation}%")
    st.write(f"- **Respiratory Rate:** {respiratory_rate} breaths/min")
    st.write(f"- **Blood Sugar Level:** {blood_sugar} mg/dL")
    st.write(f"- **Cholesterol Level:** {cholesterol} mg/dL")
    st.write(f"- **Exercises Regularly:** {exercises}")
    st.write(f"- **Follows Diet:** {follows_diet}")
    st.write(f"- **Sleep Quality:** {sleep_quality}")

# Risk Level Prediction Button
if st.button("Calculate Risk Level"):
    if model:  # Ensure the model is loaded
        input_data = np.array([[bmi, heart_rate, systolic, diastolic, oxygen_saturation, 
                                respiratory_rate, blood_sugar, cholesterol, 
                                exercise_val, diet_val, sleep_val]])
        try:
            if model_choice == "Neural Network":
                risk_prediction = model.predict(input_data)[0][0]
            else:
                risk_prediction = model.predict(input_data)[0]
            st.write(f"### Predicted Risk Level: **{risk_prediction}**")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.error("Model not loaded. Please upload and select a model.")
