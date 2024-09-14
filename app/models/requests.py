import enum
import os

from dotenv import load_dotenv
from fastapi import Query
from pydantic import BaseModel


class Colour(enum.Enum):
    RED = "red"
    BLUE = "blue"


# Load environment variables from .env file
load_dotenv()
ENV_VAR_1 = float(os.getenv("ENV_VAR_1"))


class RequestModel(BaseModel):
    n: int = Query(..., gt=0)                  # assert that this must be > 0
    env_param: float = Query(ENV_VAR_1, ge=0)  # assert that this must be >= 0
    colour: Colour = Query(
        Colour("red"), description="Colour must be RED or BLUE"
    )



class ResponseModel(BaseModel):
    output: str
