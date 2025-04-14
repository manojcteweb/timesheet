from fastapi import APIRouter, HTTPException
from typing import List
from schemas import Resource, ResourceCreate, ResourceUpdate
from fastapi.responses import HTMLResponse

router = APIRouter()

# Simulated in-memory data store
resources = {
    1: {"id": 1, "name": "Resource 1", "available": True},
    2: {"id": 2, "name": "Resource 2", "available": False},
}

@router.get("/resources", response_model=List[Resource])
async def get_resources():
    return list(resources.values())

@router.get("/resources/{resource_id}", response_model=Resource)
async def get_resource(resource_id: int):
    resource = resources.get(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.post("/resources", response_model=Resource)
async def create_resource(resource: ResourceCreate):
    new_id = max(resources.keys()) + 1
    new_resource = {"id": new_id, **resource.dict()}
    resources[new_id] = new_resource
    return new_resource

@router.put("/resources/{resource_id}", response_model=Resource)
async def update_resource(resource_id: int, resource: ResourceUpdate):
    stored_resource = resources.get(resource_id)
    if not stored_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    updated_resource = stored_resource.copy()
    updated_resource.update(resource.dict(exclude_unset=True))
    resources[resource_id] = updated_resource
    return updated_resource

@router.delete("/resources/{resource_id}")
async def delete_resource(resource_id: int):
    if resource_id not in resources:
        raise HTTPException(status_code=404, detail="Resource not found")
    del resources[resource_id]
    return {"detail": "Resource deleted"}

@router.get("/", response_class=HTMLResponse)
async def dashboard_home():
    return """
    <html>
        <head>
            <title>Resource Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
                .container { padding: 20px; }
                .resource { border: 1px solid #ccc; margin-bottom: 10px; padding: 10px; }
                @media (max-width: 600px) {
                    .resource { font-size: 14px; }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Resource Availability Dashboard</h1>
                <div class="resource">
                    <h2>Resource 1</h2>
                    <p>Status: Available</p>
                </div>
                <div class="resource">
                    <h2>Resource 2</h2>
                    <p>Status: Not Available</p>
                </div>
            </div>
        </body>
    </html>
    """