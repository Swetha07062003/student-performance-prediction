import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

sample = pd.DataFrame([{
    "study_hours": 6,
    "attendance": 85,
    "marks": 75,
    "assignments": 80,
    "sleep_hours": 7,
    "internet_usage": 2
}])

pred = model.predict(sample)
proba = model.predict_proba(sample)[0][1]

print(f"Prediction: {'PASS' if pred[0]==1 else 'FAIL'}")
print(f"Probability of PASS: {proba:.2f}")