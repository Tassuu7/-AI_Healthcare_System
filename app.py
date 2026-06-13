from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="AI Healthcare Prediction System",
    page_icon="🏥",
    layout="wide"
)

# Load Global CSS
css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# HEADER

st.markdown("""
<h1 style='text-align:center;color:white;'>
🏥 AI Healthcare Prediction & Resource Management System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;color:#cbd5e1;'>
AI Powered Smart Hospital Management Platform
</h4>
""", unsafe_allow_html=True)

st.divider()

# KPI SECTION

c1,c2,c3,c4 = st.columns(4)

c1.metric("👨‍⚕️ Patients","2,450","+12%")
c2.metric("🩺 Doctors","145","+5%")
c3.metric("🛏 Beds","500","420 Occupied")
c4.metric("📅 Appointments","1,280","+18%")

st.divider()

st.subheader("🚀 Healthcare Platform Modules")

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='module-card'>

    <h3>🏥 Clinical Modules</h3>

    ✔ Patient Dashboard <br>
    ✔ Doctor Dashboard <br>
    ✔ Appointment Management <br>
    ✔ Electronic Health Records <br>
    ✔ AI Disease Prediction <br>
    ✔ Treatment Recommendation <br>
    ✔ Medical Report Analysis <br>
    ✔ Emergency Alert System

    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='module-card'>

    <h3>📊 Administration Modules</h3>

    ✔ Admin Dashboard <br>
    ✔ Bed Management <br>
    ✔ Staff Scheduling <br>
    ✔ Resource Allocation <br>
    ✔ Notifications <br>
    ✔ Analytics & Reports <br>
    ✔ Revenue Monitoring <br>
    ✔ AI Chatbot

    </div>
    """,unsafe_allow_html=True)

st.write("")

st.subheader("⭐ Key Features")

f1,f2,f3,f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class='feature-card'>
    <h3>🧠 AI Prediction</h3>
    <p>Disease Risk Analysis</p>
    </div>
    """,unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='feature-card'>
    <h3>📈 Analytics</h3>
    <p>Real-Time Insights</p>
    </div>
    """,unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='feature-card'>
    <h3>🛏 Resources</h3>
    <p>Bed & Equipment Tracking</p>
    </div>
    """,unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class='feature-card'>
    <h3>🤖 AI Assistant</h3>
    <p>Healthcare Chatbot</p>
    </div>
    """,unsafe_allow_html=True)

st.divider()

st.subheader("📋 Project Overview")

st.info("""
The AI-Powered Healthcare Prediction & Resource Management System helps hospitals predict patient outcomes, optimize resources, improve treatment planning, manage appointments, analyze reports, and provide AI-driven recommendations.
""")

st.success("✅ System Loaded Successfully")