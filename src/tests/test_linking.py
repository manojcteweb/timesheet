import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_link_customer_to_project():
    response = client.post("/linking/link", json={"customer_id": 1, "project_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Customer 1 linked to project 1"}


def test_unlink_customer_from_project():
    response = client.post("/linking/unlink", json={"customer_id": 1, "project_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Customer 1 unlinked from project 1"}


def test_link_customer_to_project_already_linked():
    # First link the customer to the project
    client.post("/linking/link", json={"customer_id": 1, "project_id": 1})
    # Try linking again
    response = client.post("/linking/link", json={"customer_id": 1, "project_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Customer 1 linked to project 1"}


def test_unlink_customer_from_project_not_linked():
    response = client.post("/linking/unlink", json={"customer_id": 2, "project_id": 2})
    assert response.status_code == 200
    assert response.json() == {"message": "Customer 2 was not linked to project 2"}