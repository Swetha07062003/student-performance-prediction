import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000  # increased data size

data = pd.DataFrame({
    "study_hours": np.random.randint(1, 10, n),
    "attendance": np.random.randint(40, 100, n),
    "marks": np.random.randint(30, 100, n),
    "assignments": np.random.randint(30, 100, n),
    "sleep_hours": np.random.randint(4, 9, n),
    "internet_usage": np.random.randint(1, 6, n)
})

# Add noise
noise = np.random.normal(0, 15, n)

# More complex scoring
score = (
    data["study_hours"] * 2 +
    data["attendance"] * 0.25 +
    data["marks"] * 0.35 +
    data["assignments"] * 0.25 +
    data["sleep_hours"] * 1.5 -
    data["internet_usage"] * 2 +
    noise
)

# Convert to classification
threshold = np.percentile(score, 60)  # creates imbalance
data["performance"] = (score > threshold).astype(int)

data.to_csv("data/student_data.csv", index=False)

print("Dataset recreated successfully!")
print(data.head())