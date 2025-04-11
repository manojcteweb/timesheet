from budget_estimation import estimate_budget, submit_budget
from validation import validate_project_form
from user_assignment import assign_users_to_project
from project_rate_assignment import assign_project_rate
from integration import integrate_with_financial_system

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
        self.project_rate = 0.0

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
        print("Project Rate:", self.project_rate)

    def submit_form(self):
        if validate_project_form(self):
            # Logic to handle form submission
            print("Form submitted successfully.")
            integrate_with_financial_system(self)
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
        self.project_rate = 0.0
        print("Form has been reset.")

    def estimate_budget_for_project(self):
        self.budget = estimate_budget(self)
        print(f"Estimated budget: {self.budget}")

    def submit_budget_for_project(self):
        if submit_budget(self):
            print("Budget submitted successfully.")
        else:
            print("Budget submission failed.")

    def assign_users(self, users):
        self.team_members = assign_users_to_project(self.project_id, users)
        print(f"Assigned users: {', '.join(self.team_members)}")

    def assign_rate(self):
        self.project_rate = assign_project_rate(self.project_id)
        print(f"Assigned project rate: {self.project_rate}")