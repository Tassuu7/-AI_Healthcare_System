import hashlib
import streamlit as st

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()

def verify_password(
    password,
    hashed
):

    return hash_password(
        password
    ) == hashed

def login_user(username,role):

    st.session_state["logged_in"]=True
    st.session_state["username"]=username
    st.session_state["role"]=role

def logout():

    st.session_state.clear()

def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )