import os

class BaseConfig(object):
   DEBUG = False
   Testing = False


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