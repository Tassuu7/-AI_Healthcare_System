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

st.title("👩‍⚕️ Staff Scheduling")

staff=pd.DataFrame({
    "Doctor":[
        "Dr A",
        "Dr B",
        "Dr C",
        "Dr D"
    ],
    "Shift":[
        "Morning",
        "Evening",
        "Night",
        "Morning"
    ],
    "Patients":[45,60,30,55]
})

st.dataframe(
    staff,
    use_container_width=True
)

fig=px.bar(
    staff,
    x="Doctor",
    y="Patients",
    color="Shift",
    title="Doctor Workload"
)

st.plotly_chart(fig,use_container_width=True)

nurses=pd.DataFrame({
    "Nurse":[
        "Nurse1",
        "Nurse2",
        "Nurse3"
    ],
    "Shift":[
        "Morning",
        "Evening",
        "Night"
    ]
})

st.dataframe(
    nurses,
    use_container_width=True
)