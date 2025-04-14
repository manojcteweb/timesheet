import mysql.connector
from typing import List, Optional
from pydantic import BaseModel

# Pydantic model for timesheet entry
class TimesheetEntry(BaseModel):
    id: int
    employee_id: int
    date: str
    hours_worked: float
    description: str

class TimesheetRepository:
    def __init__(self, db_config):
        self.db_config = db_config

    def _get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def query_tasks(self, employee_id: Optional[int] = None, date: Optional[str] = None) -> List[TimesheetEntry]:
        connection = self._get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM timesheet_entries WHERE 1=1"
        params = []
        if employee_id is not None:
            query += " AND employee_id = %s"
            params.append(employee_id)
        if date is not None:
            query += " AND date = %s"
            params.append(date)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return [TimesheetEntry(**result) for result in results]

    def query_projects(self) -> List[dict]:
        connection = self._get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM projects"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

    def update_timesheet_entry(self, entry_id: int, updated_entry: TimesheetEntry) -> TimesheetEntry:
        connection = self._get_connection()
        cursor = connection.cursor()
        update_query = """
        UPDATE timesheet_entries
        SET employee_id = %s, date = %s, hours_worked = %s, description = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (
            updated_entry.employee_id,
            updated_entry.date,
            updated_entry.hours_worked,
            updated_entry.description,
            entry_id
        ))
        connection.commit()
        cursor.close()
        connection.close()
        return updated_entry

    def delete_timesheet_entry(self, entry_id: int) -> None:
        connection = self._get_connection()
        cursor = connection.cursor()
        delete_query = "DELETE FROM timesheet_entries WHERE id = %s"
        cursor.execute(delete_query, (entry_id,))
        connection.commit()
        cursor.close()
        connection.close()