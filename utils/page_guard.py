import streamlit as st

def require_login():

    if not st.session_state.get("logged_in", False):

        st.warning("Please Login First")

        st.stop()