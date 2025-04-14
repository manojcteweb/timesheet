from typing import List, Optional
from pydantic import BaseModel, ValidationError

# Pydantic models for request and response
class TimesheetEntry(BaseModel):
    id: int
    employee_id: int
    date: str
    hours_worked: float
    description: str

# In-memory storage for timesheet entries
fake_timesheet_db = []

class TimesheetService:
    @staticmethod
    def create_timesheet_entry(entry: TimesheetEntry) -> TimesheetEntry:
        # Validate entry
        try:
            entry = TimesheetEntry(**entry.dict())
        except ValidationError as e:
            raise ValueError(f"Invalid entry: {e}")
        fake_timesheet_db.append(entry)
        return entry

    @staticmethod
    def read_timesheet_entries(employee_id: Optional[int] = None, date: Optional[str] = None) -> List[TimesheetEntry]:
        results = fake_timesheet_db
        if employee_id is not None:
            results = [entry for entry in results if entry.employee_id == employee_id]
        if date is not None:
            results = [entry for entry in results if entry.date == date]
        return results

    @staticmethod
    def read_timesheet_entry(entry_id: int) -> TimesheetEntry:
        for entry in fake_timesheet_db:
            if entry.id == entry_id:
                return entry
        raise ValueError("Timesheet entry not found")

    @staticmethod
    def update_timesheet_entry(entry_id: int, updated_entry: TimesheetEntry) -> TimesheetEntry:
        # Validate updated entry
        try:
            updated_entry = TimesheetEntry(**updated_entry.dict())
        except ValidationError as e:
            raise ValueError(f"Invalid entry: {e}")
        for index, entry in enumerate(fake_timesheet_db):
            if entry.id == entry_id:
                fake_timesheet_db[index] = updated_entry
                return updated_entry
        raise ValueError("Timesheet entry not found")

    @staticmethod
    def delete_timesheet_entry(entry_id: int) -> TimesheetEntry:
        for index, entry in enumerate(fake_timesheet_db):
            if entry.id == entry_id:
                return fake_timesheet_db.pop(index)
        raise ValueError("Timesheet entry not found")
