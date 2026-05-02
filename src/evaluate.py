import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = joblib.load("models/model.pkl")
df = pd.read_csv("data/student_data.csv")

X = df.drop("performance", axis=1)
y = df["performance"]

pred = model.predict(X)

print("Accuracy:", accuracy_score(y, pred))
print("\nClassification Report:\n", classification_report(y, pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, pred))