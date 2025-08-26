from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/div")
def div(numbers: Numbers):
    if numbers.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": numbers.a / numbers.b}
