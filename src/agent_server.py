from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import re

app = FastAPI()

# サーバURL
ADD_URL = "http://localhost:8001/add"
SUB_URL = "http://localhost:8002/sub"
MUL_URL = "http://localhost:8003/mul"
DIV_URL = "http://localhost:8004/div"

class ExprPayload(BaseModel):
    expr: str

@app.post("/calculate")
def calculate(payload: ExprPayload):
    """
    ユーザ入力例: POST /calculate {"expr":"4+4"}
    """
    expr = payload.expr
    match = re.match(r"(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)", expr.replace(" ", ""))
    if not match:
        raise HTTPException(status_code=400, detail="Invalid expression")

    a, op, b = match.groups()
    a, b = float(a), float(b)

    try:
        if op == "+":
            res = requests.post(ADD_URL, json={"a": a, "b": b}).json()
        elif op == "-":
            res = requests.post(SUB_URL, json={"a": a, "b": b}).json()
        elif op == "*":
            res = requests.post(MUL_URL, json={"a": a, "b": b}).json()
        elif op == "/":
            res = requests.post(DIV_URL, json={"a": a, "b": b}).json()
        else:
            raise HTTPException(status_code=400, detail="Unsupported operator")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    return res
