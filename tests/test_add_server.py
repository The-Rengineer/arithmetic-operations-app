from fastapi.testclient import TestClient
from src.add_server import app  # src 配下からインポート

client = TestClient(app)

def test_add_positive_numbers():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_add_negative_numbers():
    response = client.post("/add", json={"a": -1, "b": -4})
    assert response.status_code == 200
    assert response.json() == {"result": -5.0}

def test_add_zero():
    response = client.post("/add", json={"a": 0, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 7.0}
