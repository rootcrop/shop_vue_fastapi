# схемы для продуктов
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse


class ProductBase(BaseModel):  # описываем поля для валидации создаваемых продуктов
    name: str = Field(
        ..., min_length=4, max_length=20, description="Product name"
    )  # ...           это обязательное поле
    description: Optional[str] = Field(
        None, description="Product description"
    )  # Field(None, ) не обязательное поле
    price: float = Field(..., gt=0, description="Product price > 0 ")
    category_id: int = Field(..., description="Category ID")
    image_url: Optional[str] = Field(None, description="img url")


class ProductCreate(ProductBase):
    pass


# класс вывода продуктов для админки
class ProductResponse(BaseModel):
    id: int = Field(..., description="unique product ID")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")
    # CategoryResponse взяли из from .category import CategoryResponse

    class Config:
        from_attributes = True  # можно создавать схему напрямую из модели


class ProductListResponse(BaseModel):  # класс вывода продуктов
    products: list[ProductResponse]
    total: int = Field(..., description="Total numbers of products")
