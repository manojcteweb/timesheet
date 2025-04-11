def validate_project_form(form):
    # Basic validation logic
    if not form.project_name:
        print("Project name is required.")
        return False
    if not form.start_date or not form.end_date:
        print("Start date and end date are required.")
        return False
    if form.start_date > form.end_date:
        print("Start date cannot be after end date.")
        return False
    return True