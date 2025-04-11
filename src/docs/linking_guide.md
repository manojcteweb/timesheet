# Linking Feature Guide

## Overview
The linking feature allows you to associate customers with projects. This is useful for tracking which customers are involved in which projects and managing these associations efficiently.

## Endpoints

### Link Customer to Project
- **URL**: `/linking/link`
- **Method**: `POST`
- **Description**: Links a customer to a project.
- **Request Body**:
  ```json
  {
    "customer_id": int,
    "project_id": int
  }
  ```
- **Response**:
  - **Success**: Returns a message confirming the link.
    ```json
    {
      "message": "Customer {customer_id} linked to project {project_id}"
    }
    ```

### Unlink Customer from Project
- **URL**: `/linking/unlink`
- **Method**: `POST`
- **Description**: Unlinks a customer from a project.
- **Request Body**:
  ```json
  {
    "customer_id": int,
    "project_id": int
  }
  ```
- **Response**:
  - **Success**: Returns a message confirming the unlink.
    ```json
    {
      "message": "Customer {customer_id} unlinked from project {project_id}"
    }
    ```
  - **Failure**: Returns a message if the customer was not linked to the project.
    ```json
    {
      "message": "Customer {customer_id} was not linked to project {project_id}"
    }
    ```

## Usage
To use the linking feature, send a POST request to the appropriate endpoint with the required JSON body. Ensure that the `customer_id` and `project_id` are valid integers representing existing records in your system.

## Error Handling
- If a customer is already linked to a project, the system will still return a success message when attempting to link them again.
- If a customer is not linked to a project and an unlink request is made, the system will return a message indicating that the customer was not linked.

## Logging
All linking actions are logged for auditing purposes. This includes both successful and failed attempts to link or unlink customers and projects.