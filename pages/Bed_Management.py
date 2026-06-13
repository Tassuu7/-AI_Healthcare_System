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

st.title("🛏 Bed Management System")

col1,col2,col3,col4=st.columns(4)

col1.metric("Total Beds",500)
col2.metric("Occupied Beds",372)
col3.metric("Available Beds",128)
col4.metric("ICU Beds",50)

beds=pd.DataFrame({
    "Ward":["ICU","General","Emergency","Private"],
    "Total Beds":[50,250,100,100],
    "Occupied":[42,180,75,75]
})

st.dataframe(beds,use_container_width=True)

fig=px.bar(
    beds,
    x="Ward",
    y="Occupied",
    title="Ward Occupancy"
)

st.plotly_chart(fig,use_container_width=True)

pie=px.pie(
    names=["Occupied","Available"],
    values=[372,128],
    title="Overall Bed Occupancy"
)

st.plotly_chart(pie,use_container_width=True)