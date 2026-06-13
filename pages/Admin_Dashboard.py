import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Admin Dashboard", layout="wide")

# ---------------- LOGIN GUARD ----------------
from utils.page_guard import require_login
require_login()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🏥 Hospital System")

    st.write(f"👤 {st.session_state.get('username','User')}")
    st.write(f"🔑 {st.session_state.get('role','Admin')}")

    st.divider()

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# ---------------- MAIN TITLE (ONLY ONCE) ----------------
st.title("🏥 Admin Dashboard")

st.markdown("### Overview of Hospital Performance")

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", "200")
col2.metric("Doctors", "50")
col3.metric("Revenue", "₹12,50,000")
col4.metric("Beds Occupied", "372")

st.divider()

# ---------------- HOSPITAL STATS TABLE ----------------
st.subheader("📊 Hospital Statistics")

stats = pd.DataFrame({
    "Metric": ["Patients", "Doctors", "Beds", "Appointments"],
    "Count": [200, 50, 500, 1200]
})

st.dataframe(stats, use_container_width=True)

# ---------------- REVENUE CHART ----------------
st.subheader("💰 Monthly Revenue")

revenue = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Revenue": [200000,250000,180000,300000,400000,500000]
})

fig = px.line(revenue, x="Month", y="Revenue", markers=True)
st.plotly_chart(fig, use_container_width=True)

# ---------------- DISEASE PIE ----------------
st.subheader("🦠 Disease Distribution")

disease = pd.DataFrame({
    "Disease": ["Diabetes","Heart","Kidney","Cancer","Hypertension"],
    "Patients": [60,40,30,20,50]
})

fig2 = px.pie(disease, names="Disease", values="Patients")
st.plotly_chart(fig2, use_container_width=True)

# ---------------- DEPARTMENT BAR ----------------
st.subheader("🏥 Department Performance")

dept = pd.DataFrame({
    "Department": ["Cardiology","Neurology","Orthopedic","ICU"],
    "Patients": [150,120,100,80]
})

fig3 = px.bar(dept, x="Department", y="Patients")
st.plotly_chart(fig3, use_container_width=True)

# ---------------- STAFF TABLE ----------------
st.subheader("👨‍⚕️ Staff Performance")

staff = pd.DataFrame({
    "Doctor": ["Dr A","Dr B","Dr C","Dr D"],
    "Patients Handled": [80,120,100,150]
})

st.dataframe(staff, use_container_width=True)

# ---------------- BED OCCUPANCY ----------------
st.subheader("🛏 Bed Occupancy")

beds = pd.DataFrame({
    "Status": ["Occupied","Available"],
    "Beds": [372,128]
})

fig4 = px.pie(beds, names="Status", values="Beds")
st.plotly_chart(fig4, use_container_width=True)

# ---------------- FOOTER ----------------
st.success("✅ Admin Dashboard Loaded Successfully")