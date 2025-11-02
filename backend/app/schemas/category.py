# схема для категорий, точнее схема для фильтрации входящих_исходящих данных для категорий
from pydantic import BaseModel, Field


# CategoryBase это общие поля для остальных схем, описываем поля для валидации создаваемых категорий
class CategoryBase(BaseModel):
    name: str = Field(..., min_length=4, max_length=30, description="Category name")
    slug: str = Field(
        ..., min_length=4, max_length=30, description="URL-friendly category name"
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):  # id нужно для вывода детальной инфы
    id: int = Field(..., description="Unique catyegory identifier")

    class Config:
        form_attributes = True  # можно создавать схему напрямую из модели
