from fpdf import FPDF
import pandas as pd

def generate_pdf():

    pdf=FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        200,
        10,
        txt="Healthcare Report",
        ln=True
    )

    pdf.output(
        "healthcare_report.pdf"
    )

    return "healthcare_report.pdf"

def export_excel(df):

    file="healthcare_report.xlsx"

    df.to_excel(
        file,
        index=False
    )

    return file