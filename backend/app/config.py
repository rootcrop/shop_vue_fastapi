from pydantic_settings import BaseSettings  # настраиваем конфигурацию pydantic_settings


class Settings(BaseSettings):
    app_name: str = "FastAPI shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origin: list = [  # пути от котрых бэкэнд принимает запросы
        "http://localhost:5173",  # Vite (5173) порт фронтэнда, проверить если нет связи
        "http://localhost:3000",  # Create React App (3000)
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5173",
    ]

    static_dir: str = "static"
    images_dir: str = "static/images"


class Config:  # значения настроек можно переопределить из файла .env в корне проекта
    env_file = ".env"


settings = Settings()  # инициализируем_создаем экземпляр,
# чтобы эти настройки можно было подтянуть позже, пример:
""" 
from app.config import settings
print(settings.app_name)
if settings.debug:
    print("Debug mode is on")
"""

#
# Поддержка .env — легко менять настройки под разные окружения (dev, test, prod).
# Типизация и валидация — Pydantic проверит, что debug — это bool, cors_origin — список и т.д.
# Добавить .env в .gitignore, чтобы не заливать секреты в репозиторий

# Для продакшена:
# env
# DEBUG=False
# DATABASE_URL=postgresql://...
