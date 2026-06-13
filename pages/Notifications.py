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

st.title("🔔 Notifications")

notifications=pd.DataFrame({
    "Type":[
        "Appointment",
        "Lab Report",
        "Medicine Reminder",
        "Emergency"
    ],
    "Message":[
        "Appointment Approved",
        "Report Available",
        "Take Medication",
        "Emergency Alert"
    ]
})

st.dataframe(
    notifications,
    use_container_width=True
)

st.success(
    "All notifications loaded"
)