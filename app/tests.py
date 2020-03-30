"""
    Bishop API tests
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_path():
    """
        Root api path should return basic service information.
    """
    response = client.get("/")
    expected_data = {"service": "Bishop: API Metadata Service", "version":0.1}

    assert response.status_code == 200
    assert response.json() == expected_data
