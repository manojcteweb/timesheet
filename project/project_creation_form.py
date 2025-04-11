from validation import validate_project_form

class ProjectCreationForm:
    def __init__(self):
        self.project_id = ""
        self.project_name = ""
        self.description = ""
        self.objectives = ""
        self.start_date = None
        self.end_date = None
        self.budget = 0.0
        self.team_members = []

    def render_form(self):
        # Logic to render the form with all fields
        print("Rendering form with the following fields:")
        print("Project ID:", self.project_id)
        print("Project Name:", self.project_name)
        print("Description:", self.description)
        print("Objectives:", self.objectives)
        print("Start Date:", self.start_date)
        print("End Date:", self.end_date)
        print("Budget:", self.budget)
        print("Team Members:", ", ".join(self.team_members))

    def submit_form(self):
        if validate_project_form(self):
            # Logic to handle form submission
            print("Form submitted successfully.")
        else:
            print("Form validation failed.")

    def reset_form(self):
        self.project_id = ""
        self.project_name = ""
        self.description = ""
        self.objectives = ""
        self.start_date = None
        self.end_date = None
        self.budget = 0.0
        self.team_members = []
        print("Form has been reset.")