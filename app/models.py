from typing import List, Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    in_stock: bool


class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None
