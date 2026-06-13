import plotly.express as px
import pandas as pd

def revenue_chart():

    df=pd.DataFrame({
        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],
        "Revenue":[
            2,
            3,
            5,
            4,
            7,
            8
        ]
    })

    fig=px.line(
        df,
        x="Month",
        y="Revenue",
        markers=True
    )

    return fig

def patient_chart():

    df=pd.DataFrame({
        "Department":[
            "Cardiology",
            "Neurology",
            "Orthopedic",
            "ICU"
        ],
        "Patients":[
            150,
            120,
            100,
            80
        ]
    })

    fig=px.bar(
        df,
        x="Department",
        y="Patients"
    )

    return fig

def bed_chart():

    fig=px.pie(
        names=[
            "Occupied",
            "Available"
        ],
        values=[
            372,
            128
        ]
    )

    return fig