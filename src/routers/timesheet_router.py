from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.timesheet_service import TimesheetService

router = APIRouter()

# Pydantic models for request and response
class TimesheetEntry(BaseModel):
    id: int
    employee_id: int
    date: str
    hours_worked: float
    description: str

@router.post("/timesheet/", response_model=TimesheetEntry)
async def create_timesheet_entry(entry: TimesheetEntry):
    return TimesheetService.create_timesheet_entry(entry)

@router.get("/timesheet/", response_model=List[TimesheetEntry])
async def read_timesheet_entries(employee_id: Optional[int] = None, date: Optional[str] = None):
    return TimesheetService.read_timesheet_entries(employee_id, date)

@router.get("/timesheet/{entry_id}", response_model=TimesheetEntry)
async def read_timesheet_entry(entry_id: int):
    try:
        return TimesheetService.read_timesheet_entry(entry_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Timesheet entry not found")

@router.put("/timesheet/{entry_id}", response_model=TimesheetEntry)
async def update_timesheet_entry(entry_id: int, updated_entry: TimesheetEntry):
    try:
        return TimesheetService.update_timesheet_entry(entry_id, updated_entry)
    except ValueError:
        raise HTTPException(status_code=404, detail="Timesheet entry not found")

@router.delete("/timesheet/{entry_id}", response_model=TimesheetEntry)
async def delete_timesheet_entry(entry_id: int):
    try:
        return TimesheetService.delete_timesheet_entry(entry_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Timesheet entry not found")
