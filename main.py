from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Math API",
    description="A simple API that performs math operations.",
    version="1.0.0",
)

class SumRequest(BaseModel):
    a: float
    b: float

class SumResponse(BaseModel):
    result: float

@app.post("/sum", response_model=SumResponse, summary="Sum two numbers")
def sum_numbers(payload: SumRequest):
    """
    Takes two numbers and returns their sum.
    """
    return SumResponse(result=payload.a + payload.b)
