import os

class Config:
    SECRET_KEY='ercfgvbniojnngfdfgssdfghjsdfghdfg'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://johnny:john@localhost/quotes'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'inspire':DevConfig,
'production':ProdConfig

}