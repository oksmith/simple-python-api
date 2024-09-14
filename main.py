from fastapi import FastAPI

from app.internal import calculate
from app.models.requests import RequestModel, ResponseModel

app = FastAPI()


@app.post("/calculate")
def calculate_output(request: RequestModel) -> ResponseModel:
    output = calculate.calculate(request.n, request.env_param, request.colour)
    return {"output": output}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
