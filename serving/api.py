from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("../models/model.pkl")

# ✅ Define schema
class StudentInput(BaseModel):
    study_hours: int
    attendance: int
    marks: int
    assignments: int
    sleep_hours: int
    internet_usage: int

@app.get("/")
def home():
    return {"message": "Student Performance Prediction API is running"}

@app.post("/predict")
def predict(data: StudentInput):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "prediction": int(pred),
        "status": "PASS" if pred == 1 else "FAIL",
        "probability": round(proba, 2)
    }