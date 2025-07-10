import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'devpeople-secret')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.getenv('mysql+pymysql://username:password@host:port/dbname')  # ← tambahkan ini

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}