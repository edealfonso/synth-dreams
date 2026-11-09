# Docker Compose shortcuts
.PHONY: up down build-images logs migrate makemigrations superuser shell manage build

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

superuser:
	docker compose exec web python manage.py createsuperuser

shell:
	docker compose exec web python manage.py shell

# Usage: make manage cmd="showmigrations"
manage:
	docker compose exec web python manage.py $(cmd)

# webpack production build
build:
	docker compose run --rm assets sh -c "npm install && npm run build"
