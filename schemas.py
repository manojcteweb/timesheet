from pydantic import BaseModel

class Resource(BaseModel):
    id: int
    name: str
    available: bool

class ResourceCreate(BaseModel):
    name: str
    available: bool

class ResourceUpdate(BaseModel):
    name: str = None
    available: bool = None