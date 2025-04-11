from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from routers import customer, project, linking
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Middleware for logging
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(customer.router, prefix="/customers", tags=["customers"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(linking.router, prefix="/linking", tags=["linking"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}