from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proyecto_ong',
        'USER': 'postgres',
        'PASSWORD': 'Postgresqlpassword5466289',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}
