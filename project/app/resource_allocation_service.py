from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.resource import Resource, ResourceCreate, ResourceUpdate
from sqlalchemy.future import select
from sqlalchemy import update, delete

async def get_all_resources():
    async with get_db() as session:
        result = await session.execute(select(Resource))
        return result.scalars().all()

async def get_single_resource(resource_id: int):
    async with get_db() as session:
        result = await session.execute(select(Resource).where(Resource.id == resource_id))
        return result.scalar_one_or_none()

async def create_new_resource(resource: ResourceCreate):
    async with get_db() as session:
        new_resource = Resource(**resource.dict())
        session.add(new_resource)
        await session.commit()
        await session.refresh(new_resource)
        return new_resource

async def update_existing_resource(resource_id: int, resource: ResourceUpdate):
    async with get_db() as session:
        stmt = update(Resource).where(Resource.id == resource_id).values(**resource.dict(exclude_unset=True))
        await session.execute(stmt)
        await session.commit()
        return await get_single_resource(resource_id)

async def delete_existing_resource(resource_id: int):
    async with get_db() as session:
        stmt = delete(Resource).where(Resource.id == resource_id)
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount > 0
