# Customer Management Feature

The Customer Management feature provides a set of RESTful API endpoints to manage customer data. This includes creating, retrieving, updating, and deleting customer records. Below is a guide on how to use these endpoints.

## Endpoints

### Get a List of Customers
- **URL**: `/customers/`
- **Method**: `GET`
- **Description**: Retrieves a list of all customers.
- **Response**: Returns a JSON object containing a message with the list of customers.

### Create a New Customer
- **URL**: `/customers/`
- **Method**: `POST`
- **Description**: Creates a new customer record.
- **Request Body**: JSON object containing `name`, `email`, `phone`, and `address`.
- **Response**: Returns a JSON object with a message confirming the creation of the customer.

### Update a Customer
- **URL**: `/customers/{customer_id}`
- **Method**: `PUT`
- **Description**: Updates an existing customer record.
- **Request Body**: JSON object containing fields to be updated.
- **Response**: Returns a JSON object with a message confirming the update of the customer.

### Delete a Customer
- **URL**: `/customers/{customer_id}`
- **Method**: `DELETE`
- **Description**: Deletes an existing customer record.
- **Response**: Returns a JSON object with a message confirming the deletion of the customer.

## Authentication

The API uses token-based authentication to secure the endpoints. Ensure that a valid token is provided in the request headers.

## Error Handling

- **Invalid Token**: Returns a 403 status code with a message indicating an invalid or expired token.
- **Validation Errors**: Returns a message with details of the validation errors.
- **Not Found**: Returns a message indicating that the requested entity was not found.

## Testing

Unit tests are provided to ensure the functionality of the customer management endpoints. These tests can be found in the `tests` directory and can be executed using a test runner like `unittest`.