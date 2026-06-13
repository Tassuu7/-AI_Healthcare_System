import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Patient Dashboard", layout="wide")

# ---------------- THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #e5e7eb;
}

h1, h2, h3 {
    color: #38bdf8;
}

.card {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #1f2937;
}
</style>
""", unsafe_allow_html=True)

# ---------------- USE SESSION DATA ----------------
username = st.session_state.get("username", "Patient")

st.title(f"🧑‍⚕️ Welcome {username}")

st.subheader("Patient Health Overview")

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Age", "34")
col2.metric("Weight", "70 kg")
col3.metric("Risk Level", "Medium")

st.divider()

# ---------------- DATA ----------------
df = pd.DataFrame({
    "Condition": ["Diabetes", "Heart", "BP", "Obesity"],
    "Risk": [60, 80, 50, 40]
})

fig = px.bar(df, x="Condition", y="Risk", color="Risk")
st.plotly_chart(fig, use_container_width=True)

# ---------------- APPOINTMENTS ----------------
st.subheader("📅 Appointments")

appt = pd.DataFrame({
    "Doctor": ["Dr Rao", "Dr Mehta"],
    "Date": ["2026-06-15", "2026-06-20"],
    "Status": ["Confirmed", "Pending"]
})

st.dataframe(appt, use_container_width=True)

# ---------------- REPORTS ----------------
st.subheader("🧪 Reports")

rep = pd.DataFrame({
    "Test": ["Blood", "ECG", "X-Ray"],
    "Result": ["Normal", "Alert", "Normal"]
})

st.dataframe(rep, use_container_width=True)

st.success("Dashboard Loaded Successfully")