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
from utils.page_guard import require_login

require_login()

# existing code
st.title("📅 Appointments")
import streamlit as st
from utils.database import add_appointment

st.title("📅 Book Appointment")

patient = st.text_input(
    "Patient Name"
)

doctor = st.selectbox(
    "Doctor",
    [
        "Dr A",
        "Dr B",
        "Dr C",
        "Dr D"
    ]
)

date = st.date_input(
    "Appointment Date"
)

time = st.selectbox(
    "Time",
    [
        "09:00",
        "10:00",
        "11:00",
        "02:00"
    ]
)

if st.button("Book"):

    add_appointment(
        patient,
        doctor,
        str(date),
        time
    )

    st.success(
        "Appointment Request Sent"
    )