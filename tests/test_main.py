import pytest
from fastapi.testclient import TestClient

from app.main import app

def test_app_exists():
    """Test that the FastAPI app is created"""
    assert app is not None
    assert app.title == "Minimal FastAPI Server"
    assert app.version == "1.0.0"

def test_app_has_health_route():
    """Test that the app includes the health route"""
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200