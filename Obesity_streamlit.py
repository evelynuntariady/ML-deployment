import streamlit as st
import joblib
import numpy as np
import pandas as pd
import requests


def main():
    st.title('Obesity Level Prediction')


    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age (years)", min_value=0, max_value=120)
    height = st.number_input("Height (meters)", min_value=0.0, max_value=3.0, step=0.01)
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1)

    family_history = st.radio("Family history with overweight?", ["yes", "no"])
    favc = st.radio("Frequently consumes high-calorie food (FAVC)?", ["yes", "no"])
    fcvc = st.slider("Frequency of vegetable consumption (1=rarely, 3=often)", 1.0, 3.0, step=0.5)
    ncp = st.slider("Number of main meals per day", 1.0, 4.0, step=1.0)
    caec = st.selectbox("Snacking between meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
    smoke = st.radio("Do you smoke?", ["yes", "no"])
    ch2o = st.slider("Daily water intake (CH2O)", 1.0, 3.0, step=0.5)
    scc = st.radio("Do you monitor calorie intake (SCC)?", ["yes", "no"])
    faf = st.slider("Physical activity frequency (FAF)", 0.0, 3.0, step=0.5)
    tue = st.slider("Technology usage time (TUE)", 0.0, 3.0, step=0.5)
    calc = st.selectbox("Alcohol consumption frequency (CALC)", ["no", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("Main mode of transportation (MTRANS)", 
                          ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])
    
    data = {
        "Gender": gender,
        "Age": int(age),
        "Height": float(height),
        "Weight": float(weight),
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }
   
   
    if st.button('Predict Obesity Level'):
        features = data
        result = make_prediction(features)
        if result:
            st.success(f"Predicted Obesity Category: **{result}**")
        else:
            st.error("Prediction failed. Please check if the API is running.")
    

def make_prediction(features):
    response=requests.post("http://127.0.0.1:8000/predict", json=features)
    prediction = response.json()["prediction"]     
    return prediction


if __name__ == '__main__':
    main()

        
