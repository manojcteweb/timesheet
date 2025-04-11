from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_projects():
    return {"message": "List of projects"}

@router.get("/{project_id}")
async def get_project(project_id: int):
    return {"message": f"Details of project {project_id}"}
