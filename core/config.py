import os
import logging
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from core.constants import APP_ENV_DEV, APP_ENV_PROD

db = SQLAlchemy()
migrate = Migrate()


class Config:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '1')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'contracts')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DEFAULT_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig

    return DevConfig