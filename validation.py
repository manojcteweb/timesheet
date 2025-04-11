def validate_project_form(form):
    # Check for required fields
    if not form.project_name:
        print("Project name is required.")
        return False
    if not form.start_date or not form.end_date:
        print("Start date and end date are required.")
        return False
    if form.start_date > form.end_date:
        print("Start date cannot be after end date.")
        return False
    # Validate data formats
    if not isinstance(form.budget, (int, float)) or form.budget < 0:
        print("Budget must be a non-negative number.")
        return False
    if not all(isinstance(member, str) for member in form.team_members):
        print("All team members must be valid strings.")
        return False
    return True