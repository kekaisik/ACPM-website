import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'acpm',
        'USER': 'postgres',
        'PASSWORD': '504142',
        'HOST': 'localhost',
        'PORT': '6000',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'
