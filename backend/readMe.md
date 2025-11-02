## preparation подготовка

  D:\work\fastAPI_shop\backend> 
  python -m venv myvenv
  #source myvenv/bin/activate  # .\venv\Scripts\Activate.ps1
  pip install fastapi uvicorn sqlalchemy pydantic python-dotenv pydantic-settings

## backend

  архитектура бэкэнда
  в rest_api есть
    modelies
    repositories
    route
    service
    sheme

## app      весь бэкэнд хранится тут

    __init__.py  инициализация проекта  #touch __init__.py  #notepad __init__.py
    models  описание моделей 
        продукт: название, описание, категория, дата 
        используется для формирования б.д. при миграции
        для создания объекта продукт с названием, описанием ...
    repositories
        работа с б.д. достают из хранилища
    routes
        пути это тоже самое что и urls в джанго - пути
        к пути подвязан сервис который за это путь отвечает и перенаправляет
    schemas
        это сериализаторы для джанго
        описывают формат данных для API
        приводят в нормальный вид json (для фронта)
        валидация данных
    services
        аналог views в джанго
        есть url к нему подвязан сервис
        обрабатывает данные на бэкэнде
        на url пришел запрос
          покажи товар с фильтрацией по категории 
  requirements.txt

## scheme     схема работы

  user
    |
  browser 
    (get product, какие есть товары)
    |
  frontend vue.js
    (нужны product)
    |
  layer routes 
    (нужны product)
    |
  layer service 
    (нужны product)
    |
  layer repository 
    (достань product)
    |
  database sqlite 
    (из б.д. достаются продукты)
    |
  layer service 
    (сервис получил продукты из б.д.)
    (выведи полученные данные продукты)
    |
  layer schemas
    (происходит валидация продуктов)
    |
  frontend vue.js
    |
  browser
    |
  user

## модели

  category.py    сначала пишем категории товара      
          /fastAPI_shop/backend/app/models/category.py
  products.py    потом привяжем по связи

## схемы pydantic для API
  конфигурация API для приема и отсылки данных в нужной нам формате
  под контекст запроса, пример 
  класс - продукт, у него есть поля
  id, name, description, price, category_id, image_url, created_at
  из них id и created_at создаются автоматом и не редактируются




## git

  work\fastAPI_shop> 
  git init  # Initialized empty Git repository in D:/work/fastAPI_shop/.git/
  git add .
  
  в github.com создаем новый репозиторий shop_vue_fastapi
  git remote add origin https://github.com/rootcrop/shop_vue_fastapi.git
  git branch -M main
  git commit -m 'init'
  git push -u origin main
