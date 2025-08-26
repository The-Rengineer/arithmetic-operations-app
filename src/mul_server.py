from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/mul")
def mul(numbers: Numbers):
    return {"result": numbers.a * numbers.b}
