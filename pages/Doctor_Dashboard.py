import streamlit as st
import pandas as pd
import plotly.express as px
from utils.page_guard import require_login

require_login()

st.markdown("""
<h1 style='color:white;'>
👨‍⚕️ Doctor Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='color:#cbd5e1;'>
Welcome Doctor
</p>
""", unsafe_allow_html=True)

st.divider()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Today's Patients", 38)
c2.metric("Appointments", 24)
c3.metric("Pending Reports", 12)
c4.metric("Critical Cases", 4)

st.divider()

st.subheader("📋 Today's Patients")

patients = pd.DataFrame({
    "Patient ID":[101,102,103,104,105],
    "Name":["John","Rahul","Priya","David","Sara"],
    "Age":[45,30,27,60,40],
    "Disease":["Diabetes","Heart","Kidney","Cancer","Hypertension"]
})

st.dataframe(
    patients,
    width="stretch"
)

st.subheader("📈 Patient Distribution")

df = pd.DataFrame({
    "Disease":["Diabetes","Heart","Kidney","Cancer","Hypertension"],
    "Count":[50,40,30,20,60]
})

fig = px.bar(
    df,
    x="Disease",
    y="Count",
    title="Disease Cases"
)

st.plotly_chart(
    fig,
    width="stretch"
)

col1,col2 = st.columns(2)

with col1:

    recovery = pd.DataFrame({
        "Status":["Recovered","Under Treatment"],
        "Count":[180,70]
    })

    fig2 = px.pie(
        recovery,
        names="Status",
        values="Count",
        title="Recovery Status"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

with col2:

    monthly = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Patients":[100,120,140,160,180,220]
    })

    fig3 = px.line(
        monthly,
        x="Month",
        y="Patients",
        markers=True,
        title="Monthly Patients"
    )

    st.plotly_chart(
        fig3,
        width="stretch"
    )

st.subheader("🩺 Treatment Recommendations")

recommend = pd.DataFrame({
    "Disease":["Diabetes","Heart Disease","Kidney Disease"],
    "Specialist":["Endocrinologist","Cardiologist","Nephrologist"],
    "Priority":["Medium","High","High"]
})

st.dataframe(
    recommend,
    width="stretch"
)

st.success("Doctor Dashboard Loaded Successfully")