import streamlit as st

st.set_page_config(
    page_title="Logout",
    page_icon="🚪",
    layout="centered"
)

st.title("🚪 Logout")

st.write("Click below to logout from the Healthcare System.")

if st.button("Logout"):

    st.session_state.clear()

    st.success("Logged Out Successfully")

    st.info("Please refresh the page and login again.")

    st.stop()