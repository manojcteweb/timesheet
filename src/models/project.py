from typing import Optional

class Project:
    def __init__(self, project_id: int, title: str, description: str):
        self.project_id = project_id
        self.title = title
        self.description = description

    def get_project_data(self) -> dict:
        """
        Retrieves the project data as a dictionary.

        :return: A dictionary containing project data.
        """
        return {
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description
        }

    def validate_project_data(self) -> Optional[str]:
        """
        Validates the project data.

        :return: None if data is valid, otherwise an error message.
        """
        if not self.title:
            return "Project title is required."
        if not self.description:
            return "Project description is required."
        return None
