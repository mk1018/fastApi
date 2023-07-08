build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down
freeze:
	docker-compose exec python pip freeze > app/requirements.txt
shel:
	docker-compose exec python bash
start-serve:
	docker-compose exec -d python bash -c "uvicorn main:app --reload --host 0.0.0.0 --port 8080"