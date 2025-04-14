import pytest
from fastapi.testclient import TestClient
from main import app
from services.timesheet_service import TimesheetService
from pydantic import ValidationError

client = TestClient(app)

# Sample data for testing
sample_entry = {
    "id": 1,
    "employee_id": 123,
    "date": "2023-10-01",
    "hours_worked": 8.0,
    "description": "Worked on project X"
}

# Unit tests for TimesheetService
class TestTimesheetService:
    def test_create_timesheet_entry(self):
        entry = TimesheetService.create_timesheet_entry(sample_entry)
        assert entry.id == sample_entry["id"]
        assert entry.employee_id == sample_entry["employee_id"]

    def test_create_timesheet_entry_invalid(self):
        with pytest.raises(ValidationError):
            TimesheetService.create_timesheet_entry({"id": "invalid"})

    def test_read_timesheet_entries(self):
        TimesheetService.create_timesheet_entry(sample_entry)
        entries = TimesheetService.read_timesheet_entries()
        assert len(entries) > 0

    def test_read_timesheet_entry_not_found(self):
        with pytest.raises(ValueError):
            TimesheetService.read_timesheet_entry(999)

    def test_update_timesheet_entry(self):
        TimesheetService.create_timesheet_entry(sample_entry)
        updated_entry = sample_entry.copy()
        updated_entry["hours_worked"] = 9.0
        entry = TimesheetService.update_timesheet_entry(sample_entry["id"], updated_entry)
        assert entry.hours_worked == 9.0

    def test_delete_timesheet_entry(self):
        TimesheetService.create_timesheet_entry(sample_entry)
        TimesheetService.delete_timesheet_entry(sample_entry["id"])
        with pytest.raises(ValueError):
            TimesheetService.read_timesheet_entry(sample_entry["id"])

# Integration tests using TestClient
class TestTimesheetAPI:
    def test_create_timesheet_entry(self):
        response = client.post("/timesheet/", json=sample_entry)
        assert response.status_code == 200
        assert response.json()["id"] == sample_entry["id"]

    def test_read_timesheet_entries(self):
        response = client.get("/timesheet/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_read_timesheet_entry(self):
        response = client.get(f"/timesheet/{sample_entry['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == sample_entry["id"]

    def test_update_timesheet_entry(self):
        updated_entry = sample_entry.copy()
        updated_entry["hours_worked"] = 9.0
        response = client.put(f"/timesheet/{sample_entry['id']}", json=updated_entry)
        assert response.status_code == 200
        assert response.json()["hours_worked"] == 9.0

    def test_delete_timesheet_entry(self):
        response = client.delete(f"/timesheet/{sample_entry['id']}")
        assert response.status_code == 200
        with pytest.raises(ValueError):
            TimesheetService.read_timesheet_entry(sample_entry["id"])