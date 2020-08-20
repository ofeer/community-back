import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Basic configurations relevant for all environments (dev and prod).
    """
    # os.getenv tries to get the environment variable SECRET_KEY, if doesn't exist returns
    # as default value - bigsecret
    SECRET_KEY = os.getenv('SECRET_KEY', 'bigsecret')
    SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH', 'bcrypt')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Configurations for the development environment - local environment
    """
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:fooder@localhost/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Configurations for the production environment - heruko environment
    """
    DEBUG = False
    # TODO: understand how to connect to heroku
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:fooder@localhost/')


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)
key = Config.SECRET_KEY
