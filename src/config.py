from decouple import config


class Config:
    SECRET_KEY= config('SECRET_KEY')

class DevelepmentConfig(Config):
    DEBUG=True

config = {
    'development': DevelepmentConfig
}