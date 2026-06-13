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

st.title("📈 Patient Outcome Prediction")

age = st.number_input("Age",1,100,50)
severity = st.slider("Severity",1,10,5)

if st.button("Predict Outcome"):

    recovery = max(
        10,
        100 - (severity*8) - (age*0.3)
    )

    icu = severity * 8

    readmission = severity * 5

    st.metric(
        "Recovery Probability",
        f"{round(recovery)}%"
    )

    st.metric(
        "ICU Requirement",
        f"{round(icu)}%"
    )

    st.metric(
        "Readmission Risk",
        f"{round(readmission)}%"
    )

outcome = pd.DataFrame({
    "Category":[
        "Recovered",
        "ICU",
        "Readmitted"
    ],
    "Patients":[150,30,20]
})

fig = px.pie(
    outcome,
    names="Category",
    values="Patients"
)

st.plotly_chart(fig,use_container_width=True)