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
import pickle
import numpy as np

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Disease Prediction System")

# ==========================
# LOAD MODEL
# ==========================

try:
    model = pickle.load(
        open(
            "models/disease_model.pkl",
            "rb"
        )
    )

    model_loaded = True

except:

    model_loaded = False

    st.error(
        "Disease Model Not Found. Run disease_model.py first."
    )

# ==========================
# PATIENT DETAILS
# ==========================

st.subheader("Patient Information")

col1,col2 = st.columns(2)

with col1:

    patient_name = st.text_input(
        "Patient Name"
    )

    age = st.number_input(
        "Age",
        1,
        100,
        30
    )

    bp = st.number_input(
        "Blood Pressure",
        50,
        250,
        120
    )

with col2:

    sugar = st.number_input(
        "Sugar Level",
        50,
        500,
        100
    )

    cholesterol = st.number_input(
        "Cholesterol",
        50,
        500,
        180
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        24.0
    )

# ==========================
# PREDICT BUTTON
# ==========================

if st.button("Predict Disease"):

    if model_loaded:

        data = np.array(
            [
                [
                    age,
                    bp,
                    sugar,
                    cholesterol
                ]
            ]
        )

        prediction = model.predict(data)[0]

        risk_score = round(
            (
                bp * 0.20 +
                sugar * 0.30 +
                cholesterol * 0.20 +
                bmi * 2
            ),
            2
        )

        if prediction == 1:

            disease = "High Risk Disease"

        else:

            disease = "Low Risk Disease"

        st.success(
            f"Prediction Result : {disease}"
        )

        st.warning(
            f"Risk Score : {risk_score}"
        )

        if risk_score > 200:

            severity = "Critical"

        elif risk_score > 150:

            severity = "Moderate"

        else:

            severity = "Low"

        st.info(
            f"Severity Level : {severity}"
        )

# ==========================
# KPI CARDS
# ==========================

st.divider()

st.subheader("Disease Statistics")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Diabetes Cases",
    120
)

c2.metric(
    "Heart Disease",
    85
)

c3.metric(
    "Kidney Disease",
    42
)

c4.metric(
    "Cancer Risk",
    18
)

# ==========================
# DISEASE DISTRIBUTION
# ==========================

disease_df = pd.DataFrame({

    "Disease":[
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Cancer"
    ],

    "Patients":[
        120,
        85,
        42,
        18
    ]

})

fig1 = px.bar(
    disease_df,
    x="Disease",
    y="Patients",
    title="Disease Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================
# RISK ANALYSIS
# ==========================

risk_df = pd.DataFrame({

    "Category":[
        "Low Risk",
        "Moderate Risk",
        "High Risk"
    ],

    "Patients":[
        100,
        60,
        40
    ]

})

fig2 = px.pie(
    risk_df,
    names="Category",
    values="Patients",
    title="Risk Analysis"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================
# MONTHLY TREND
# ==========================

trend_df = pd.DataFrame({

    "Month":[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],

    "Cases":[
        20,
        35,
        40,
        55,
        70,
        85
    ]

})

fig3 = px.line(
    trend_df,
    x="Month",
    y="Cases",
    markers=True,
    title="Monthly Disease Trend"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================
# PATIENT HISTORY
# ==========================

st.subheader(
    "Recent Disease Predictions"
)

history = pd.DataFrame({

    "Patient":[
        "Ali",
        "Sara",
        "David",
        "Ravi"
    ],

    "Disease":[
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Low Risk"
    ],

    "Risk Score":[
        220,
        190,
        170,
        110
    ],

    "Severity":[
        "Critical",
        "Moderate",
        "Moderate",
        "Low"
    ]

})

st.dataframe(
    history,
    use_container_width=True
)

# ==========================
# DOWNLOAD REPORT
# ==========================

csv = history.to_csv(
    index=False
)

st.download_button(
    "Download Prediction Report",
    csv,
    file_name="Disease_Report.csv",
    mime="text/csv"
)

st.success(
    "Disease Prediction Module Loaded Successfully"
)