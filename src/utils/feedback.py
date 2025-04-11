def success_message(action: str) -> dict:
    return {"message": f"{action} was successful."}


def error_message(action: str, error: str) -> dict:
    return {"message": f"Failed to {action}. Error: {error}"}


def not_found_message(entity: str) -> dict:
    return {"message": f"{entity} not found."}


def validation_error_message(errors: dict) -> dict:
    return {"message": "Validation error.", "details": errors}