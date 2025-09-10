from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI()
model = joblib.load('model_xgboost.pkl')
label_encoder = joblib.load('label_encoder.pkl')

class ObesityFeatures(BaseModel):
    Age: float
    Gender: str
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O : float
    SCC : str
    FAF : float
    TUE : float
    CALC : str
    MTRANS : str
    

@app.get("/")
def read_root():
       return {"message": "Welcome to the ML Model API"}

@app.post('/predict')

def predict(obesity: ObesityFeatures):
    data_in = obesity.dict()
    features = pd.DataFrame([data_in])
    prediction = model.predict(features)
    label = label_encoder.inverse_transform(prediction) 
    return {'prediction': label[0]}


