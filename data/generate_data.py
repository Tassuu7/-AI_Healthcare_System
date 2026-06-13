import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

np.random.seed(42)

# ---------------- PATIENTS ----------------

patients = pd.DataFrame({
    "PatientID": range(1, 201),
    "Name": [f"Patient_{i}" for i in range(1, 201)],
    "Age": np.random.randint(18, 80, 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "BloodGroup": np.random.choice(
        ["A+", "B+", "AB+", "O+", "A-", "B-"],
        200
    ),
    "Disease": np.random.choice(
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Hypertension",
            "Healthy"
        ],
        200
    ),
    "Phone": [
        f"98{np.random.randint(10000000,99999999)}"
        for _ in range(200)
    ]
})

patients.to_csv("data/patients.csv", index=False)

# ---------------- DOCTORS ----------------

doctors = pd.DataFrame({
    "DoctorID": range(1, 51),
    "DoctorName": [f"Dr_{i}" for i in range(1, 51)],
    "Department": np.random.choice(
        [
            "Cardiology",
            "Neurology",
            "Orthopedic",
            "ICU",
            "General"
        ],
        50
    ),
    "Experience": np.random.randint(1, 25, 50),
    "Availability": np.random.choice(
        [
            "9AM-5PM",
            "10AM-6PM",
            "24 Hours"
        ],
        50
    )
})

doctors.to_csv("data/doctors.csv", index=False)

# ---------------- APPOINTMENTS ----------------

appointments = pd.DataFrame({
    "AppointmentID": range(1, 501),
    "PatientID": np.random.randint(1, 201, 500),
    "DoctorID": np.random.randint(1, 51, 500),
    "Status": np.random.choice(
        ["Pending", "Approved", "Rejected"],
        500
    ),
    "Date": pd.date_range(
        "2026-01-01",
        periods=500
    )
})

appointments.to_csv(
    "data/appointments.csv",
    index=False
)

# ---------------- PAYMENTS ----------------

payments = pd.DataFrame({
    "PaymentID": range(1, 1001),
    "PatientID": np.random.randint(
        1,
        201,
        1000
    ),
    "Amount": np.random.randint(
        500,
        50000,
        1000
    ),
    "Status": np.random.choice(
        ["Paid", "Pending"],
        1000
    )
})

payments.to_csv(
    "data/payments.csv",
    index=False
)

# ---------------- BEDS ----------------

beds = pd.DataFrame({
    "BedID": range(1, 501),
    "Ward": np.random.choice(
        [
            "ICU",
            "General",
            "Emergency",
            "Private"
        ],
        500
    ),
    "Status": np.random.choice(
        [
            "Occupied",
            "Available"
        ],
        500
    )
})

beds.to_csv(
    "data/beds.csv",
    index=False
)

print("All CSV Files Generated Successfully")