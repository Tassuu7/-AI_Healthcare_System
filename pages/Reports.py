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

st.title("📄 Reports Center")

report=pd.DataFrame({
    "Patient":[
        "Ali",
        "Sara",
        "David"
    ],
    "Disease":[
        "Diabetes",
        "Heart",
        "Kidney"
    ],
    "Cost":[
        15000,
        30000,
        25000
    ]
})

st.dataframe(
    report,
    use_container_width=True
)

csv=report.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "patient_report.csv",
    "text/csv"
)

excel=report.to_csv(index=False)

st.download_button(
    "Download Excel Data",
    excel,
    "patient_report.xls"
)

st.success(
    "Reports Generated Successfully"
)