from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_customers():
    return {"message": "List of customers"}

@router.get("/{customer_id}")
async def get_customer(customer_id: int):
    return {"message": f"Details of customer {customer_id}"}
