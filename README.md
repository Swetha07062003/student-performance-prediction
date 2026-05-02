# 🎓 Student Performance Prediction System

An AI-powered system that predicts student performance using Machine Learning and provides actionable insights through an interactive dashboard and API.

---

## 🚀 Features

* 📊 Predict student performance using ML model
* 📉 Risk detection (At Risk / Average / Good)
* 📈 Interactive dashboard using Streamlit
* ⚡ REST API built with FastAPI
* 💡 Personalized recommendations based on inputs

---

## 🛠 Tech Stack

* Python
* Scikit-learn
* Streamlit
* FastAPI
* Plotly
* Pandas
* Joblib

---

## 📂 Project Structure

```
Student-Performance-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── student_data.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── data_generation.py
│
├── serving/
│   └── app.py
│
└── images/
    ├── api.png
    ├── at_risk.png
    ├── average.png
    └── performing_well.png
```

---

## 🖥️ Application Screenshots

### 🔹 Dashboard Output

![Dashboard](images/performing_well.png)

### 🔹 At Risk Prediction

![At Risk](images/at_risk.png)

### 🔹 Average Performance

![Average](images/average.png)

### 🔹 API Response

![API](images/api.png)

---

## ▶️ Run Streamlit App

```
streamlit run app.py
```

---

## ▶️ Run FastAPI Server

```
uvicorn serving.app:app --reload
```

---

## 📌 Output

* Performance Score (0–100)
* Category (At Risk / Average / Good)
* Visual Gauge Chart
* Personalized Recommendations

---

## 📈 Future Improvements

* Use real-world dataset
* Deploy on cloud (Streamlit Cloud / Render)
* Add user authentication
* Improve model accuracy with advanced algorithms

---

## 👩‍💻 Author

Swetha K

