import streamlit as st
from utils.page_guard import require_login

require_login()

with st.sidebar:

    st.write(
        f"👤 {st.session_state.get('username','User')}"
    )

    st.write(
        f"🔑 {st.session_state.get('role','User')}"
    )

    st.divider()

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.stop()


import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📋 Electronic Health Records")

st.subheader("Patient Medical Records")

ehr = pd.DataFrame({
    "Patient ID":[101,102,103,104],
    "Patient":["Ali","Sara","David","Ravi"],
    "Disease":["Diabetes","Heart Disease","Kidney Disease","Hypertension"],
    "Doctor":["Dr A","Dr B","Dr C","Dr D"],
    "Status":["Under Treatment","Recovered","Critical","Stable"]
})

st.dataframe(ehr,use_container_width=True)

st.subheader("Prescription History")

prescriptions = pd.DataFrame({
    "Patient":["Ali","Sara","David"],
    "Medicine":["Metformin","Aspirin","Dialysis Support"],
    "Duration":["30 Days","15 Days","60 Days"]
})

st.dataframe(prescriptions,use_container_width=True)

st.subheader("Vaccination Records")

vaccines = pd.DataFrame({
    "Patient":["Ali","Sara","David"],
    "Vaccine":["COVID","Hepatitis","Flu"],
    "Date":["2026-01-01","2026-02-01","2026-03-01"]
})

st.dataframe(vaccines,use_container_width=True)

fig = px.pie(
    ehr,
    names="Status",
    title="Patient Status Distribution"
)

st.plotly_chart(fig,use_container_width=True)