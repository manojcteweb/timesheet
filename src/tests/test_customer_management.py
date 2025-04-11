import unittest
from fastapi.testclient import TestClient
from main import app

class TestCustomerManagement(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_customers(self):
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_create_customer(self):
        response = self.client.post("/customers/", json={"name": "John Doe", "email": "john@example.com", "phone": "1234567890", "address": "123 Elm Street"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_update_customer(self):
        customer_id = 1  # Assuming a customer with ID 1 exists
        response = self.client.put(f"/customers/{customer_id}", json={"name": "Jane Doe"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_delete_customer(self):
        customer_id = 1  # Assuming a customer with ID 1 exists
        response = self.client.delete(f"/customers/{customer_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

if __name__ == "__main__":
    unittest.main()