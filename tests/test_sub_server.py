from fastapi.testclient import TestClient
from src.sub_server import app

client = TestClient(app)

def test_sub_positive_numbers():
    res = client.post("/sub", json={"a":5, "b":3})
    assert res.status_code == 200
    assert res.json() == {"result": 2.0}

def test_sub_negative_numbers():
    res = client.post("/sub", json={"a":-1, "b":-4})
    assert res.status_code == 200
    assert res.json() == {"result": 3.0}

def test_sub_zero():
    res = client.post("/sub", json={"a":0, "b":7})
    assert res.status_code == 200
    assert res.json() == {"result": -7.0}
