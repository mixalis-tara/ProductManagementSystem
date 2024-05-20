from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class StockPayLoad(Product):
    action: str
    quantity: int