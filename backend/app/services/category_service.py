from sqlalchemy.orm import Session
from typing import List
from ..repositories.category_repository import CategoryRepository
from ..schemas.category import CategoryResponse, CategoryCreate
from fastapi import HTTPException, status


class CategoryService:  # класс сервиса категорий для работы с репозиторием
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all_categories(self) -> List[CategoryResponse]:
        categories = self.repository.get_all()
        return [CategoryResponse.model_validate(cat) for cat in categories]

    # метод get_category_by_id получаем категорию по id и возвращаем ее
    def get_category_by_id(self, category_id: int) -> CategoryResponse:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found",
            )
        return CategoryResponse.model_validate(category)

    # метод create_category создаем категорию и возвращаем ее
    def create_category(self, category_data: CategoryCreate) -> CategoryResponse:
        category = self.repository.create(category_data)
        return CategoryResponse.model_validate(category) # валидатор - проверка категории, аналог сериализации в джанго
