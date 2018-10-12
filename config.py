import os

class BaseConfig(object):
   DEBUG = False
   Testing = False

   SECRET_KEY= os.getenv('SECRET_KEY')
   MYSQL_HOST = os.getenv('MYSQL_HOST')
   MYSQL_USER = os.getenv('MYSQL_USER')
   MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
   MYSQL_DB = os.getenv('MYSQL_DB')
   MYSQL_PORT = int( os.getenv('MYSQL_PORT') )


class DevelopmentConfig(BaseConfig):
    DEBUG= True
    Testing= True

class TestingConfig(BaseConfig):
    DEBUG= False
    Testing= True

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": BaseConfig,
    "default": DevelopmentConfig
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])