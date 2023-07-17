APP_CONTAINER_NAME=python
DB_CONTAINER_NAME=mysql

# container
build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down

# app
shel:
	docker-compose exec $(APP_CONTAINER_NAME) bash
freeze:
	docker-compose exec $(APP_CONTAINER_NAME) pip freeze > src/requirements.txt
start-serve:
	docker-compose exec $(APP_CONTAINER_NAME) bash -c "uvicorn app.main:app --reload --host 0.0.0.0 --port 8080"
migrate:
	docker-compose exec $(APP_CONTAINER_NAME) python -m migrations
test:
	docker-compose exec $(APP_CONTAINER_NAME) pytest -v --disable-warnings

# db
db-shel:
	docker-compose exec $(DB_CONTAINER_NAME) mysql -umy_user -p sample