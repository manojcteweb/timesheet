from fastapi import APIRouter

router = APIRouter()

# Example endpoint to get a list of customers
@router.get("/", summary="Get a list of customers")
def get_customers():
    return {"message": "List of customers"}

# Example endpoint to create a new customer
@router.post("/", summary="Create a new customer")
def create_customer():
    return {"message": "Customer created"}

# Example endpoint to update a customer
@router.put("/{customer_id}", summary="Update a customer")
def update_customer(customer_id: int):
    return {"message": f"Customer {customer_id} updated"}

# Example endpoint to delete a customer
@router.delete("/{customer_id}", summary="Delete a customer")
def delete_customer(customer_id: int):
    return {"message": f"Customer {customer_id} deleted"}