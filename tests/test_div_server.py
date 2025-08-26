from fastapi.testclient import TestClient
from src.div_server import app

client = TestClient(app)

def test_div_positive_numbers():
    res = client.post("/div", json={"a":8, "b":2})
    assert res.status_code == 200
    assert res.json() == {"result": 4.0}

def test_div_negative_numbers():
    res = client.post("/div", json={"a":-9, "b":3})
    assert res.status_code == 200
    assert res.json() == {"result": -3.0}

def test_div_by_zero():
    res = client.post("/div", json={"a":5, "b":0})
    assert res.status_code == 400
    assert "detail" in res.json()
    assert res.json()["detail"] == "Division by zero"
