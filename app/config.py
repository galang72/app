import os

basedir = os.path.abspath(os.path.dirname(_file_))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'devpeople-secret')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'squadmaster.db')

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'squadmaster.db')

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}