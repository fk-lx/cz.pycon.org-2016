from .settings import *

DEBUG = True
SECRET_KEY = 42

INTERNAL_IPS = ['127.0.0.1']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
