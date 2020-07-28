import os

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = '5@#$60a9515-0201-4606-8e42-86#$RR#R$d7e35aef2e1'
    WTF_CSRF_SECRET_KEY = 'c*($^#@8c42784-7735-4595-9563-jaj$^$(599934e701ef'
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6Ld2PbcZAAAAAM_48s2z7lNkdO2qQwsCuNrHFBC0'
    RECAPTCHA_PRIVATE_KEY = '6Ld2PbcZAAAAAJyucCuts5o_FE4XFCjOeICojtgb'
    RECAPTCHA_OPTIONS = {'theme': 'white'}

class TestingConfig(Config):
    TESTING = True
