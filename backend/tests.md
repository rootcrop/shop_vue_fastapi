# тестированию API в Postman

## Запуск бэкенда

Установка зависимостей
cd backend
pip install -r requirements.txt
source venv/bin/activate #linux
\venv\Scripts\Activate.ps1 #windows

## Заполнение базы данных тестовыми данными

python seed_data.py

## Запуск сервера

cd work\fastAPI_shop\backend\
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload  
или python run.py

## postman

Скачиваем, запускаем агента postman
{{base_url}} http://localhost:8000/health
{{category_id}} 1

## Тестирование эндпоинтов postman

### Health Check

Проверка работоспособности сервера
    GET  http://localhost:8000/health
в body корректный ответ:
    {    "status": "healthy" }

в postman scripts добавляем
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Status is healthy", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.status).to.eql("healthy");
});

корректный ответ postman tab / test result:
    passed, Status code is 200
    passed, Status is healthy

### Категории (Categories)

#### Получить все категории

GET http://localhost:8000/api/categories

корректный ответ в body  (200 OK):
[
    {
        "name": "Electronics",
        "slug": "electronics",
        "id": 1 },
    {
        "name": "Clothing",
        "slug": "clothing",
        "id": 2  },
    {
        "name": "Books",
        "slug": "books",
        "id": 3  },
    {
        "name": "Home & Garden",
        "slug": "home-garden",
        "id": 4 }  
]

тесты (postman / scripts tab):
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);  });

pm.test("Response is array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');  });

pm.test("Categories have required fields", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0]).to.have.property('id');
    pm.expect(jsonData[0]).to.have.property('name');
    pm.expect(jsonData[0]).to.have.property('slug'); });

if (pm.response.json().length > 0) {
    pm.environment.set("category_id", pm.response.json()[0].id); }

корректный ответ postman tab / test result:
passed Status code is 200
passed Response is array
passed Categories have required fields

#### Получить категорию по ID

GET {{base_url}}/api/categories/{{category_id}}
GET http://localhost:8000/api/categories/1

Корректный ответ (200 OK):
{   "name": "Electronics",
    "slug": "electronics",
    "id": 1 }

тесты (postman / scripts tab):
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Category has correct structure", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData).to.have.property('name');
    pm.expect(jsonData).to.have.property('slug'); });

корректный ответ postman tab / test result:
passed Status code is 200
passed Category has correct structure

#### Получить несуществующую категорию
GET http://localhost:8000/api/categories/11

Корректный ответ (200 OK):
... "detail": "Category with id 11 not found"

### 3. Товары (Products)

#### Получить все товары
GET http://localhost:8000/api/products

Корректный ответ (200 OK):
  ...
  "id": 13,
            "name": "Garden Tool Kit",
            "description": "Complete garden tool kit with 10 essential tools. Durable stainless steel construction. Includes carrying bag for easy storage.",
            "price": 79.99,
            "category_id": 4,
            "image_url": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=400",
            "created_at": "2025-11-03T08:13:33.747730",
            "category": {
                "name": "Home & Garden",
                "slug": "home-garden",
                "id": 4
            }
        }
    ],
    "total": 13

#### Получить товар по ID
GET http://localhost:8000/api/products/{{product_id}}

#### Получить товары по категории
GET http://localhost:8000/api/products/category/{{category_id}}

#### Получить товары несуществующей категории
GET http://localhost:8000/api/products/category/99

### Корзина (Cart)

#### Добавить товар в корзину

POST http://localhost:8000/api/cart/add
Content-Type: application/json

{ "product_id": 1,
  "quantity": 2,
  "cart": {} }

корректный ответ (200 OK):
{ "cart": {
    "1": 2  } }


#### Добавить ещё один товар

POST http://localhost:8000/api/cart/add

Content-Type: application/json
{ "product_id": 2,
  "quantity": 1,
  "cart": {{cart}} }

Pre-request Script:
// Загружаем корзину из переменной окружения
var cart = pm.environment.get("cart");
if (cart) { pm.variables.set("cart", cart);} 
else { pm.variables.set("cart", "{}"); }

Получить детали корзины
POST http://localhost:8000/api/cart
Content-Type: application/json
{ "1": 2,
  "2": 1 }

Корректный ответ (200 OK):
...
  "items": [ {
      "product_id": 1,
      "name": "Wireless Headphones",
      "price": 299.99,
      "quantity": 2,
      "subtotal": 600.0,
      "image_url": "https://images.unsplash.com/..." },
    { "product_id": 2,
      "name": "Smart Watch Pro",
      "price": 399.99,
      "quantity": 1,
      "subtotal": 400.0,
      "image_url": "https://images.unsplash.com/..." } ],
  "total": 1000.0,
  "items_count": 3

#### Удалить товар из корзины

DELETE http://localhost:8000/api/cart/remove/1
Content-Type: application/json

{ "cart": {
    "1": 5,
    "2": 1 } }

Ожидаемый ответ (200 OK):
{ "cart": {
    "2": 1 } }

#### Добавить несуществующий товар

POST http://localhost:8000/api/cart/add
Content-Type: application/json

{ "product_id": 9999,
  "quantity": 1,
  "cart": {} }

Корректный ответ (404 Not Found):
{ "detail": "Product with id 9999 not found" }

### Pre-request Script для всей коллекции
// Устанавливаем базовые переменные, если их нет
if (!pm.environment.get("base_url")) {
    pm.environment.set("base_url", "http://localhost:8000"); }

// Добавляем timestamp для уникальных запросов
pm.variables.set("timestamp", Date.now());
Tests для всей коллекции
// Проверка времени ответа
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500); });

// Проверка наличия Content-Type
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type"); });
