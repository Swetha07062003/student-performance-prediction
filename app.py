import streamlit as st
import plotly.graph_objects as go
import joblib

# Load model
model = joblib.load("models/model.pkl")

st.set_page_config(layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #020617);
    color: white;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 5px;
    background: linear-gradient(to right, #00f5a0, #00d9f5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 25px;
}
.kpi {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-weight: 600;
}
.k1 {background: linear-gradient(135deg,#10b981,#059669);}
.k2 {background: linear-gradient(135deg,#06b6d4,#0284c7);}
.k3 {background: linear-gradient(135deg,#8b5cf6,#6d28d9);}
.k4 {background: linear-gradient(135deg,#f59e0b,#d97706);}
.section {
    font-size: 20px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 12px;
}
.stButton > button {
    background: linear-gradient(135deg, #00f5a0, #00d9f5);
    color: black;
    font-weight: bold;
    border-radius: 8px;
}
.good {
    background: linear-gradient(90deg,#065f46,#064e3b);
    padding: 12px;
    border-radius: 8px;
}
.warn {
    background: linear-gradient(90deg,#7c2d12,#7f1d1d);
    padding: 12px;
    border-radius: 8px;
}
.avg {
    background: linear-gradient(90deg,#713f12,#854d0e);
    padding: 12px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">Student Performance Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered Academic Risk Analyzer</div>', unsafe_allow_html=True)

# ---------- KPI ----------
c1, c2, c3, c4 = st.columns(4)
c1.markdown('<div class="kpi k1">Smart Prediction<br><small>ML Powered</small></div>', unsafe_allow_html=True)
c2.markdown('<div class="kpi k2">Risk Detection<br><small>Early Identification</small></div>', unsafe_allow_html=True)
c3.markdown('<div class="kpi k3">Better Decisions<br><small>Insights</small></div>', unsafe_allow_html=True)
c4.markdown('<div class="kpi k4">Improve Performance<br><small>Guidance</small></div>', unsafe_allow_html=True)

# ---------- LAYOUT ----------
left, right = st.columns([1,1])

# ---------- INPUT ----------
with left:
    st.markdown('<div class="section">Enter Student Details</div>', unsafe_allow_html=True)

    study = st.slider("Study Hours", 1, 10, 5)
    attendance = st.slider("Attendance (%)", 40, 100, 75)
    marks = st.slider("Marks (%)", 30, 100, 60)
    assignments = st.slider("Assignments (%)", 30, 100, 65)
    sleep = st.slider("Sleep Hours", 4, 9, 6)
    internet = st.slider("Internet Usage", 1, 6, 3)

    btn = st.button("Predict Performance")

# ---------- RESULT ----------
with right:
    st.markdown('<div class="section">Prediction Result</div>', unsafe_allow_html=True)

    if btn:
        input_data = [[study, attendance, marks, assignments, sleep, internet]]

        # ML Prediction
        prediction = model.predict(input_data)[0]

        # ✅ SMART SCORE (FIXED)
        score = (
            study * 5 +
            attendance * 0.3 +
            marks * 0.3 +
            assignments * 0.2 +
            sleep * 2 -
            internet * 2
        )

        score = max(0, min(100, int(score)))

        # ---------- GAUGE ----------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            number={'font': {'size': 42, 'color': 'white'}},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "rgba(0,0,0,0)"},
                'steps': [
                    {'range': [0, score], 'color': "#06b6d4"},
                    {'range': [score, 100], 'color': "#1e293b"}
                ],
                'bgcolor': "#020617"
            }
        ))

        fig.update_layout(paper_bgcolor="#020617", font={'color': "white"})
        st.plotly_chart(fig, use_container_width=True)

        # ---------- STATUS ----------
        if score < 40:
            st.markdown('<div class="warn">⚠️ AT RISK - Needs Improvement</div>', unsafe_allow_html=True)
        elif score < 70:
            st.markdown('<div class="avg">⚡ AVERAGE - Can Improve</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="good">✅ GOOD - Performing Well</div>', unsafe_allow_html=True)

        # ---------- RECOMMENDATIONS ----------
        st.markdown('<div class="section">Recommendations</div>', unsafe_allow_html=True)

        rec = []

        if study < 5:
            rec.append("Increase study hours")
        if attendance < 75:
            rec.append("Improve attendance")
        if marks < 60:
            rec.append("Focus on academics")
        if assignments < 60:
            rec.append("Submit assignments on time")
        if sleep < 6:
            rec.append("Improve sleep cycle")
        if internet > 4:
            rec.append("Reduce internet usage")

        if len(rec) == 0:
            st.markdown('<div class="good">Everything looks good 👍</div>', unsafe_allow_html=True)
        else:
            for r in rec:
                st.write("•", r)