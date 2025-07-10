import os

# Ganti basedir pakai os.getcwd() biar aman di Railway
basedir = os.path.abspath(os.getcwd())

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'devpeople-secret')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app', 'squadmaster.db')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app', 'squadmaster.db')

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}