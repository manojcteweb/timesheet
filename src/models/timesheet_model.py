from pydantic import BaseModel
from typing import Optional

class TimesheetEntry(BaseModel):
    id: int
    employee_id: int
    date: str
    hours_worked: float
    description: str

class Task(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    project_id: int

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None