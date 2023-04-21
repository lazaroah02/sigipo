DOCKER_COMPOSE := docker-compose -f docker-compose.base.yml
DOCKER_COMPOSE_DEV := $(DOCKER_COMPOSE) -f docker-compose.dev.yml
DOCKER_RUN_WEB := $(DOCKER_COMPOSE_DEV) run --rm web

up-db:
	$(DOCKER_COMPOSE_DEV) up --build db

up:
	$(DOCKER_COMPOSE_DEV) up

up-build:
	$(DOCKER_COMPOSE_DEV) up --build

run-django-command:
	$(DOCKER_RUN_WEB) python manage.py $(ARGS)

run-test:
	$(DOCKER_RUN_WEB) python -m pytest $(ARGS)

run-shell:
	$(DOCKER_RUN_WEB) python manage.py shell

up-production:
	$(DOCKER_COMPOSE) -f docker-compose.prod.yml up --build
