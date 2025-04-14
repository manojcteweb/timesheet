from fastapi import FastAPI
from app.routers.dashboard import router as dashboard_router

app = FastAPI()

# Include the dashboard router
app.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Resource Availability Dashboard API"}