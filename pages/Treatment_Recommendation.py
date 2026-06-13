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

st.title("💊 Treatment Recommendation Engine")

disease = st.selectbox(
    "Select Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Hypertension"
    ]
)

recommendations = {
    "Diabetes":[
        "Low Sugar Diet",
        "Metformin",
        "Exercise Daily"
    ],
    "Heart Disease":[
        "Cardiology Consultation",
        "Blood Pressure Monitoring",
        "Aspirin Therapy"
    ],
    "Kidney Disease":[
        "Dialysis Evaluation",
        "Protein Restriction",
        "Kidney Function Tests"
    ],
    "Hypertension":[
        "Salt Restriction",
        "Exercise",
        "BP Monitoring"
    ]
}

if st.button("Generate Recommendation"):

    recs = recommendations[disease]

    st.success("Recommended Treatment")

    for r in recs:
        st.write("✅",r)

df = pd.DataFrame({
    "Disease":list(recommendations.keys()),
    "Specialist":[
        "Endocrinologist",
        "Cardiologist",
        "Nephrologist",
        "General Physician"
    ]
})

st.dataframe(df,use_container_width=True)