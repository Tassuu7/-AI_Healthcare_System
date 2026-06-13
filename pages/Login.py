import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 AI Healthcare System Login")

role = st.selectbox(
    "Login As",
    ["Patient", "Doctor", "Admin"]
)

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username and password:

        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["role"] = role

        st.success("Login Successful")

        st.switch_page("app.py")

    else:

        st.error("Enter Username & Password")