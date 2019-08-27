setup-dev:
	pip install -r requirements/local.txt

code-convention:
	black . --line-length=119
	flake8

test:
	pytest --cov=production_center_core

migrate:
	python manage.py makemigrations
	python manage.py migrate

build-indexes:
	python manage.py search_index --rebuild

all: setup-dev migrate test code-convention
