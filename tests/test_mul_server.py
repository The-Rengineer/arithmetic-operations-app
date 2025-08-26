from fastapi.testclient import TestClient
from src.mul_server import app

client = TestClient(app)

def test_mul_positive_numbers():
    res = client.post("/mul", json={"a":4, "b":3})
    assert res.status_code == 200
    assert res.json() == {"result": 12.0}

def test_mul_negative_numbers():
    res = client.post("/mul", json={"a":-2, "b":5})
    assert res.status_code == 200
    assert res.json() == {"result": -10.0}

def test_mul_zero():
    res = client.post("/mul", json={"a":0, "b":9})
    assert res.status_code == 200
    assert res.json() == {"result": 0.0}
