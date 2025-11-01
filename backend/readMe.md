preparation подготовка
	D:\work\fastAPI_shop\backend> 
	python -m venv myvenv
	#source myvenv/bin/activate	# .\venv\Scripts\Activate.ps1
	pip install fastapi uvicorn sqlalchemy pydantic python-dotenv pydantic-settings

backend
	архитектура бэкэнда
	в rest_api есть
		modelies
		repositories
		route
		service
		sheme
		
app			весь бэкэнд хранится тут
		__init__.py	инициализация проекта	#touch __init__.py  #notepad __init__.py

		models	описание моделей 
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
		
git	D:\work\fastAPI_shop> 
	git init	# Initialized empty Git repository in D:/work/fastAPI_shop/.git/
	git add .
	
	в github.com создаем новый репозиторий shop_vue_fastapi
	git remote add origin https://github.com/rootcrop/shop_vue_fastapi.git
	git branch -M main
	git commit -m 'init'
	git push -u origin main



	