import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    # Arrange & Act
    response = client.get("/")
    # Assert
    assert response.status_code == 200
