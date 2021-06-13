"""
Production Settings for Heroku
"""
from .production import *
import environ

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!git
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

# HSTS is an HTTP header that informs a browser that all future connections to a particular site should always use HTTPS
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Requests over HTTP are redirected to HTTPS.
SECURE_SSL_REDIRECT = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# The file storage engine to use when collecting static files with the collectstatic management command.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

