import pytest
from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    """Test the health check endpoint"""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "message": "Server is running"
    }

def test_health_check_content_type(client: TestClient):
    """Test the health check endpoint returns JSON"""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"