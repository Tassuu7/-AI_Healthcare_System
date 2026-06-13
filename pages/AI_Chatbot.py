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
from datetime import datetime

st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Healthcare Assistant")

st.markdown("""
### Ask about:
- Symptoms
- Diseases
- Treatments
- Emergency situations
- Appointments
- Medical tests
- Diet recommendations
- Hospital services
""")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input(
    "Enter your question"
)

def healthcare_response(text):

    text = text.lower()

    # Diabetes
    if "diabetes" in text:
        return """
### Diabetes Analysis

**Possible Symptoms**
- Frequent urination
- Excessive thirst
- Fatigue
- Weight loss

**Recommended Tests**
- HbA1c
- Fasting Blood Sugar
- Random Blood Sugar

**Recommended Specialist**
- Endocrinologist

**Lifestyle Suggestions**
- Avoid sugary drinks
- Daily walking
- Weight management

**Risk Level**
🟡 Moderate Risk
"""

    # Heart Disease
    elif "heart" in text or "chest pain" in text:
        return """
### Heart Disease Assessment

**Symptoms**
- Chest pain
- Shortness of breath
- Dizziness

**Recommended Tests**
- ECG
- Echo
- Lipid Profile

**Specialist**
- Cardiologist

**Emergency Warning**
🔴 Seek emergency care if chest pain is severe.
"""

    # Kidney
    elif "kidney" in text:
        return """
### Kidney Health Assessment

**Possible Indicators**
- Swelling
- Fatigue
- Reduced urine output

**Recommended Tests**
- Creatinine
- GFR
- Urine Analysis

**Specialist**
- Nephrologist
"""

    # Fever
    elif "fever" in text:
        return """
### Fever Analysis

**Possible Causes**
- Viral Infection
- Flu
- Bacterial Infection

**Suggestions**
- Stay hydrated
- Take rest
- Monitor temperature

**Consult Doctor If**
- Fever > 103°F
- Lasts more than 3 days
"""

    # BP
    elif "blood pressure" in text or "bp" in text:
        return """
### Blood Pressure Guidance

**Normal**
120/80

**High BP**
140/90+

**Recommendations**
- Reduce salt intake
- Daily exercise
- Stress management

**Specialist**
Cardiologist
"""

    # Appointment
    elif "appointment" in text:
        return """
### Appointment Assistance

1. Open Appointment Module
2. Select Doctor
3. Choose Available Slot
4. Submit Request
5. Wait for Doctor Approval

Status can be checked in Patient Dashboard.
"""

    # Ambulance
    elif "ambulance" in text or "emergency" in text:
        return """
### Emergency Contacts

🚑 Ambulance : 108

🏥 Hospital Emergency :
+91-9876543210

👨‍⚕️ Duty Doctor :
+91-9123456789

Call immediately for critical conditions.
"""

    # Diet
    elif "diet" in text:
        return """
### General Healthy Diet Plan

Breakfast
- Oats
- Fruits

Lunch
- Rice
- Vegetables
- Protein

Dinner
- Light meal

Avoid
- Excess sugar
- Junk food
- Soft drinks
"""

    else:
        return """
### AI Health Assistant

Please ask about:

- Diabetes
- Heart Disease
- Kidney Disease
- Fever
- Blood Pressure
- Diet
- Appointments
- Emergency Services

For serious symptoms please consult a doctor immediately.
"""

if st.button("Ask AI"):

    if question:

        answer = healthcare_response(question)

        st.session_state.chat_history.append(
            {
                "Question": question,
                "Answer": answer,
                "Time": datetime.now().strftime("%H:%M:%S")
            }
        )

for item in reversed(st.session_state.chat_history):

    st.markdown("---")

    st.markdown(
        f"### 👤 {item['Question']}"
    )

    st.markdown(
        item["Answer"]
    )

    st.caption(
        f"Time: {item['Time']}"
    )

st.divider()

st.subheader("Common Questions")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.info("What are diabetes symptoms?")

with col2:
    st.info("How to control BP?")

with col3:
    st.info("Emergency ambulance number")

with col4:
    st.info("How to book appointment?")