import sqlite3

DB_NAME = "healthcare.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        doctor_name TEXT,
        appointment_date TEXT,
        appointment_time TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_appointment(
    patient,
    doctor,
    date,
    time
):

    conn = get_connection()

    conn.execute(
    """
    INSERT INTO appointments(
    patient_name,
    doctor_name,
    appointment_date,
    appointment_time,
    status
    )
    VALUES(?,?,?,?,?)
    """,
    (
        patient,
        doctor,
        date,
        time,
        "Pending"
    )
    )

    conn.commit()
    conn.close()

def get_appointments():

    conn = get_connection()

    data = conn.execute(
        "SELECT * FROM appointments"
    ).fetchall()

    conn.close()

    return data

def update_appointment(
    app_id,
    status
):

    conn = get_connection()

    conn.execute(
    """
    UPDATE appointments
    SET status=?
    WHERE id=?
    """,
    (
        status,
        app_id
    )
    )

    conn.commit()
    conn.close()