from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey 
from sqlalchemy.orm import relationship         # relationship — это функция SQLAlchemy, которая определяет логическую связь между моделями (например, один ко многим, один к одному).
from datetime import datetime
from ..database import Base                     # Импорт базового класса для моделей

class Product (Base):                           # Определение класса модели Product, Создаёт класс Product, который наследуется от Base. Будет соответствовать таблице в базе данных.
    __tablename__="products"                    # объявляет новую сущность данных — "категория", которую можно сохранять и извлекать из БД, __tablename__ то как будет отображаться в б.д.

    id = Column(Integer, primary_key=True, index=True)
    name = Column (String, unique=True, nullable=False, index=True)
    description = Column (Text)
    price=Column (Float, nullable=False)
    category_id=Column(Integer, ForeignKey("categories.id"), nullable=False)    # у продукта всегда должна быть категория, связываем с помощью id ForeignKey
    image_url=Column(String)
    created_at=Column(DateTime, default=datetime.utcnow)

    category = relationship ("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id},name='{self.name}',price='{self.price}')>" 

    
