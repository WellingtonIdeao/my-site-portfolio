from .base import *
import json


# Extract Keys From the Json file
def get_key(path):
    with open(path) as f:
        return json.load(f)


keys = get_key(BASE_DIR / 'secrets.json')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = keys['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = keys['DEBUG']

ALLOWED_HOSTS = keys['ALLOWED_HOSTS']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# HSTS is an HTTP header that informs a browser that all future connections to a particular site should always use HTTPS
SECURE_HSTS_SECONDS = keys['SECURE_HSTS_SECONDS']
SECURE_HSTS_PRELOAD = keys['SECURE_HSTS_PRELOAD']
SECURE_HSTS_INCLUDE_SUBDOMAINS = keys['SECURE_HSTS_INCLUDE_SUBDOMAINS']

# Requests over HTTP are redirected to HTTPS.
SECURE_SSL_REDIRECT = keys['SECURE_SSL_REDIRECT']

# Secure cookies
SESSION_COOKIE_SECURE = keys['SESSION_COOKIE_SECURE']
CSRF_COOKIE_SECURE = keys['CSRF_COOKIE_SECURE']


# The file storage engine to use when collecting static files with the collectstatic management command.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

