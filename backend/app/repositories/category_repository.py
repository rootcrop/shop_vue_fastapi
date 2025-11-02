# работа с sqlAlchemy
from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.category import Category          # достаем модели категории
from ..schemas.category import CategoryCreate   # достаем схемы создания категории

class CategoryRepository:
    def __init__(self, db: Session):
        self.db=db                              # провели инициализацию связи

    def get_all(self) -> List[Category]:        # метод get_all получаем все категории через список
        return self.db.query(Category).all()    # обращаемся к базе данных и возвращаем список всех категорий
    
    def get_by_id(self, category_id: int) -> Optional[Category]:                    # метод get_by_id получаем категорию по id
        return self.db.query(Category).filter(Category.id == category_id).first()   # обращаемся к базе данных и возвращаем категорию по id   

    def get_by_slug (self, slug: str) -> Optional[Category]:                        # метод get_by_id получаем категорию по slug
        return self.db.query(Category).filter(Category.slug == slug).first()        # обращаемся к базе данных и возвращаем категорию по slug   
    
    def create(self, category_data:CategoryCreate) -> Category:                     # метод create создаем категорию из схемы
        db_category = Category(**category_data.model_dump())                        # берем все данные из схемы и создаем категорию
        self.db.add(db_category)                                                    # добавляем категорию в базу данных
        self.db.commit()                                                            # подтверждаем изменения
        self.db.refresh(db_category)                                                # обновляем категорию
        return db_category
    