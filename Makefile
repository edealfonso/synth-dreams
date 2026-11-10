# Docker Compose shortcuts
.PHONY: up down build-images logs migrate makemigrations superuser shell manage build export

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

# Static export for GitHub Pages into dist/ (prefixed build + export, then the dev build again).
# Usage: make export (or make export prefix=/other-path)
prefix ?= /synth-dreams
export:
	docker compose stop assets
	docker compose run --rm -e SITE_PREFIX=$(prefix) assets npm run build
	docker compose exec -e SITE_PREFIX=$(prefix) web python manage.py export_static
	docker compose start assets
