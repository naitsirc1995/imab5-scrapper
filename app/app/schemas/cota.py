from pydantic import BaseModel
from typing import List

class Cota(BaseModel):
    quote: float
    date: str



