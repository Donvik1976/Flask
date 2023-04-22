
class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):

    FLASK_DEBUG = True
    DATABASE_URI = 'sqlite:////tmp/blog.db'
    TESTING = True
    SECRET_KEY = 'w3j&!3h0gzwtbf_jvy1byga*u9-*6xtznn0)&y(*a)yg*$k2@='


