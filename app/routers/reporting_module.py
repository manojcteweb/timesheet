from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.report import Report, ReportCreate
from app.services.reporting_service import (
    generate_report,
    get_report_by_id,
    get_all_reports
)

router = APIRouter()

@router.post("/reports", response_model=Report)
async def create_report(report: ReportCreate):
    return await generate_report(report)

@router.get("/reports/{report_id}", response_model=Report)
async def get_report(report_id: int):
    report = await get_report_by_id(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.get("/reports", response_model=List[Report])
async def get_reports():
    return await get_all_reports()