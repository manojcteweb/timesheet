from fastapi import APIRouter

router = APIRouter()

# Endpoint to link a customer to a project
@router.post("/link")
async def link_customer_to_project(customer_id: int, project_id: int):
    # Logic to link customer to project would go here
    return {"message": f"Customer {customer_id} linked to project {project_id}"}

# Endpoint to unlink a customer from a project
@router.post("/unlink")
async def unlink_customer_from_project(customer_id: int, project_id: int):
    # Logic to unlink customer from project would go here
    return {"message": f"Customer {customer_id} unlinked from project {project_id}"}