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

st.title("📦 Resource Allocation")

resources=pd.DataFrame({
    "Resource":[
        "Ventilators",
        "Oxygen Units",
        "Wheel Chairs",
        "Monitors"
    ],
    "Available":[
        25,
        100,
        40,
        60
    ]
})

st.dataframe(
    resources,
    use_container_width=True
)

fig=px.bar(
    resources,
    x="Resource",
    y="Available",
    title="Resource Availability"
)

st.plotly_chart(fig,use_container_width=True)

forecast=pd.DataFrame({
    "Month":[
        "Jul",
        "Aug",
        "Sep",
        "Oct"
    ],
    "Demand":[
        120,
        140,
        170,
        200
    ]
})

fig2=px.line(
    forecast,
    x="Month",
    y="Demand",
    markers=True
)

st.plotly_chart(fig2,use_container_width=True)