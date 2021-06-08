from .base import *
import json


# Extract Keys From the Json file
def get_key(path):
    with open(path) as f:
        return json.load(f)


# SECURITY WARNING: keep the secret key used in production secret!
keys = get_key(BASE_DIR / 'secrets.json')

SECRET_KEY = keys['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


