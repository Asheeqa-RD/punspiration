class Config:
    DEBUG = False
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = True

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'
