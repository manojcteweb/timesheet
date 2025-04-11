from typing import Optional

class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_customer_data(self) -> dict:
        """
        Retrieves the customer data as a dictionary.

        :return: A dictionary containing customer data.
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    def validate_customer_data(self) -> Optional[str]:
        """
        Validates the customer data.

        :return: None if data is valid, otherwise an error message.
        """
        if not self.name:
            return "Customer name is required."
        if not self.email or "@" not in self.email:
            return "A valid email is required."
        return None
