setup-dev:
	pip install -r config/local.txt

code-convention:
	black . --line-length=119
	flake8

migrate:
	python production_center_core/manage.py makemigrations
	python production_center_core/manage.py migrate

all: setup-dev migrate code-convention
