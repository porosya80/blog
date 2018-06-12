class Configuration(object):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://user:1@localhost/test1"
    SECRET_KEY="something very secret"
    SECURITY_PASSWORD_HASH='bcrypt'
    SECURITY_PASSWORD_SALT="something"
