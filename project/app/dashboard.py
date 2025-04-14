from fastapi import APIRouter, HTTPException
from typing import List
from schemas.resource import Resource, ResourceCreate, ResourceUpdate
from fastapi.responses import HTMLResponse
from app.resource_allocation_service import (
    get_all_resources,
    get_single_resource,
    create_new_resource,
    update_existing_resource,
    delete_existing_resource
)

router = APIRouter()

@router.get("/resources", response_model=List[Resource])
async def get_resources():
    return await get_all_resources()

@router.get("/resources/{resource_id}", response_model=Resource)
async def get_resource(resource_id: int):
    resource = await get_single_resource(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.post("/resources", response_model=Resource)
async def create_resource(resource: ResourceCreate):
    return await create_new_resource(resource)

@router.put("/resources/{resource_id}", response_model=Resource)
async def update_resource(resource_id: int, resource: ResourceUpdate):
    updated_resource = await update_existing_resource(resource_id, resource)
    if not updated_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return updated_resource

@router.delete("/resources/{resource_id}")
async def delete_resource(resource_id: int):
    if not await delete_existing_resource(resource_id):
        raise HTTPException(status_code=404, detail="Resource not found")
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
