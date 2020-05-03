import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = config("DEBUG", default=False, cast=bool)
APP_DEFAULT_PORT = config("APP_DEFAULT_PORT", cast=int)
APP_DEFAULT_HOST = config("APP_DEFAULT_HOST")
BASE_PATH = config("BASE_PATH")


class DatabaseSettings:
    DATABASE_URI = config('DATABASE_URI')
    REPLICA_DATABASE_URI = config('DATABASE_URI')
