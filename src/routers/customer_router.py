from fastapi import APIRouter
from services.customer_service import CustomerService

router = APIRouter()
customer_service = CustomerService()

# Example endpoint to get a list of customers
@router.get("/", summary="Get a list of customers")
def get_customers():
    return customer_service.get_customers()

# Example endpoint to create a new customer
@router.post("/", summary="Create a new customer")
def create_customer():
    return customer_service.create_customer()

# Example endpoint to update a customer
@router.put("/{customer_id}", summary="Update a customer")
def update_customer(customer_id: int):
    return customer_service.update_customer(customer_id)

# Example endpoint to delete a customer
@router.delete("/{customer_id}", summary="Delete a customer")
def delete_customer(customer_id: int):
    return customer_service.delete_customer(customer_id)
