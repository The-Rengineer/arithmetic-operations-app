from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/sub")
def sub(numbers: Numbers):
    return {"result": numbers.a - numbers.b}
