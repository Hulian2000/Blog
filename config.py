import os

class Config:
    SECRET_KEY='ercfgvbniojnngfdfgssdfghjsdfghdfg'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://johnny:john@localhost/pitches'


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}