from .base import *
import json

# Application definition

INSTALLED_APPS += ['psycopg2', ]


# Extract Keys From the Json file
def get_key(path):
    with open(path) as f:
        return json.load(f)


keys = get_key(BASE_DIR / 'secrets.json')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = keys['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = keys['DEBUG']

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': keys['DB_NAME'],
        'USER': keys['DB_USER'],
        'PASSWORD': keys['DB_PASSWORD'],
        'HOST': keys['DB_HOST'],
        'PORT': keys['DB_PORT'],
    }
}


