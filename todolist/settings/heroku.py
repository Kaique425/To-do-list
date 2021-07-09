import environ

from todolist.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env.list("ALLOWED_HOST")

DATABASES = {
    "default": env.db(),
}