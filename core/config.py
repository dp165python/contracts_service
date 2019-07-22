import logging
import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from core.constants import APP_ENV_DEV, APP_ENV_PROD, APP_ENV_TEST

db = SQLAlchemy()
migrate = Migrate()


class Config:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '1')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'contracts')
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


class TestConfig(Config):
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '1')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'test_contracts')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DEFAULT_DB}'
    DEBUG = True


def runtime_config():
    env = os.environ.get('APP_ENV', APP_ENV_TEST).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig
    elif env == APP_ENV_TEST:
        return TestConfig
    return DevConfig
