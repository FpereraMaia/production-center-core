setup-dev:
	pip install -r env/local.txt

code-convention:
	black . --line-length=119
	flake8

migrate:
	python manage.py makemigrations
	python manage.py migrate

all: setup-dev migrate code-convention
