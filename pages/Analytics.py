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

st.title("📈 Healthcare Analytics")

revenue=pd.DataFrame({
    "Month":[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Revenue":[
        2,
        3,
        4,
        5,
        6,
        8
    ]
})

fig=px.line(
    revenue,
    x="Month",
    y="Revenue",
    markers=True
)

st.plotly_chart(fig,use_container_width=True)

disease=pd.DataFrame({
    "Disease":[
        "Diabetes",
        "Heart",
        "Kidney"
    ],
    "Cases":[
        120,
        80,
        40
    ]
})

fig2=px.pie(
    disease,
    names="Disease",
    values="Cases"
)

st.plotly_chart(fig2,use_container_width=True)