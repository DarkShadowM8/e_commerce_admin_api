
from pydantic import BaseModel

class Sale(BaseModel):
    product_id: int
    units_sold: int
