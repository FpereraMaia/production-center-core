setup-dev:
	pip install -r config/local.txt

code-convention:
	black . --line-length=119
	flake8

all: setup-dev code-convention
