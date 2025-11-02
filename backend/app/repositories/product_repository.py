# работа с sqlAlchemy
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from ..models.product import Product  # достаем модели продуктов
from ..schemas.product import ProductCreate  # достаем схемы создания продуктов


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    # метод get_all получаем все продукты через список
    def get_all(self) -> List[Product]:
        return self.db.query(Product).options(joinedload(Product.category)).all()

    # метод get_by_id получаем продукт по id
    def get_by_id(self, product_id: int) -> Optional[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id == product_id)
            .first()
        )

    def get_by_category(self, category_id: int) -> List[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.category_id == category_id)
            .all()
        )

    def create(self, product_data: ProductCreate) -> Product:   # метод create создаем продукт из схемы 
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_multiple_by_ids(self, product_ids: List[int]) -> List[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id.in_(product_ids))
            .all()
        )
