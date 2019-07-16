# import os
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# DEBUG = True
# PORT = 5000
# HOST = "0.0.0.0"
# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1@127.0.0.1/contracts"
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

import os
import logging


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
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1@127.0.0.1/contracts"


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", "dev").strip().lower()
    if env == "prod":
        return ProdConfig

    return DevConfig
