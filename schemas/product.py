
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    cost_rate: float
    selling_rate: float
