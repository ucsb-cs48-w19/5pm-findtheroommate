import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = #Placeholder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3 #post per page configuration

    #SECURITY_EMAIL_SENDER = 'valid_email@my_domain.com'

    MAIL_SERVER = #os.environ.get('MAIL_SERVER')
    MAIL_PORT = #int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = #os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = #os.environ.get('MAIL_PASSWORD')
    ADMINS = #placeholder
