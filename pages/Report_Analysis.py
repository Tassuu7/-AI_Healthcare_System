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

st.title("📊 Medical Report Analysis")

reports=pd.DataFrame({
    "Patient":[
        "Ali",
        "Sara",
        "David",
        "Ravi"
    ],
    "Hemoglobin":[
        11,
        13,
        9,
        12
    ],
    "Sugar":[
        180,
        120,
        90,
        150
    ]
})

st.dataframe(
    reports,
    use_container_width=True
)

fig=px.scatter(
    reports,
    x="Hemoglobin",
    y="Sugar",
    color="Patient"
)

st.plotly_chart(fig,use_container_width=True)

st.warning(
    "Ali has high sugar level"
)