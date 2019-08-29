# Production Center Core
This is a core project to manage the Entities for the Operational Production Center.

## Requirements

- Python 3.6.x
- Django 2.x
- Django Rest Framework 3.x
- ElasticSearch 7.x
- PostgreSql
- Docker - https://lmgtfy.com/?q=how+to+install+docker

## Install (This README is for Linux OS)

### Installing PIP, Pyenv, VirtualEnv, Python
```
# Pip

$ sudo apt update
$ sudo apt install python3-pip

# Pyenv

$ curl https://pyenv.run | bash
$ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
$ exec "$SHELL"

# Python

$ pyenv install 3.6.9

# Virtualenv
$ pyenv virtualenv 3.6.9 production-center-core

```
### Installing all Dependencies, Running Migrate SQLite, Tests and code convention

```
$ make all
```

### Installing and configuring postgres and creating tables
```
# UP Docker Container

$ mkdir ~/postgresql-data
$ docker pull postgres
$ docker network create --driver bridge postgres-network
$ docker run --name production-core-postgres --network=postgres-network -e "POSTGRES_PASSWORD=PCP" -p 5432:5432 -v ~/postgresql-data:/var/lib/postgresql/data -d postgres

# Setting Environment Variables

$ echo 'APP_DB_ENGINE=django.db.backends.postgresql_psycopg2' >> ~/.bashrc
$ echo 'DB_NAME=postgres' >> ~/.bashrc
$ echo 'DB_USER=postgres' >> ~/.bashrc
$ echo 'DB_PASSWORD=PCP' >> ~/.bashrc
$ echo 'DB_HOST=localhost' >> ~/.bashrc
$ echo 'DB_PORT=5432' >> ~/.bashrc

# Restarting Shell
$ exec "$SHELL"

or

$ exec bash

# Creating tables

$ make migrate
```

### Start Container ElasticSearch and Creating Indexes
```
$ docker pull docker.elastic.co/elasticsearch/elasticsearch:7.3.1
$ sudo docker network create elasticnetwork
$ sudo docker run --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.3.1

# Creating indexes

$ make build-indexes
```

### Running Server

```
$ python manage.py runserver
```

### Docs and OpenAPI Usage
- Docs: http://localhost:8000/redoc
- OpenApi to make Requests: http://localhost:8000/swagger

# Known Issues
1) Post and put "final-products" end-point documentation have a wrong data body example:
```
Today is:
{
  "name": "string",
  "employee": 0,
  "raw_materials": [
    0
  ],
  "employee_related": {
    "name": "string",
    "work_hours": 4
  },
  "raw_materials_related": [
    {
      "name": "string",
      "quantity_in_stock": 0
    }
  ]
}

MUST BE:
{
  "name": "string",
  "employee": 0,
  "raw_materials": [
    0
  ]
}

```
 
2) Improve the code in method "partial_update" in final_product.services module.
3) Use gunicorn for serve the project.