import os

from .settings import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db.sqlite3"),
    }
}
