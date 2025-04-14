from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.report import Report, ReportCreate
from sqlalchemy.future import select
import pandas as pd
from fpdf import FPDF

# Function to generate a report based on task breakdown
async def generate_report_by_task(session: Session, task_id: int):
    # Logic to generate report by task
    result = await session.execute(select(Report).where(Report.task_id == task_id))
    return result.scalars().all()

# Function to generate a report based on project phase
async def generate_report_by_project_phase(session: Session, phase: str):
    # Logic to generate report by project phase
    result = await session.execute(select(Report).where(Report.project_phase == phase))
    return result.scalars().all()

# Function to generate a report based on category
async def generate_report_by_category(session: Session, category: str):
    # Logic to generate report by category
    result = await session.execute(select(Report).where(Report.category == category))
    return result.scalars().all()

# Function to export report to PDF
async def export_report_to_pdf(report_data, file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in report_data:
        pdf.cell(200, 10, txt=str(line), ln=True)
    pdf.output(file_path)

# Function to export report to Excel
async def export_report_to_excel(report_data, file_path):
    df = pd.DataFrame(report_data)
    df.to_excel(file_path, index=False)
