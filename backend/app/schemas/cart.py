from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, lt=10, description="Quantity > 0")


class CartItemCreate(CartItemBase):  # выносим работу с сессиями во фронтэнд vue.js
    pass

class CartItem (BaseModel):
    product_id: int=Field(..., description="producr name")
    name: str=Field(..., description="product name")
    price: float=Field(..., description="product price")
    quantity: int=Field(..., description="product quantity")
    subtotal: float=Field(..., description="total price")
    image_url: Optional[str] = Field(None, description="img url")

class CartResponse(BaseModel):
    items: list[CartItem]=Field(..., description="list of items in cart")
    total: float=Field(..., description="total cart price")
    items_count: int=Field(..., decimal_places="total number of items in cart")
