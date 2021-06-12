from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")cs-%s3ednl%7cw2$12&g-h(%*c8lv+!zcw2$jj$^*t7wm+^$%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "https://wi-portfolio.herokuapp.com/",
    ".herokuapp.com"
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "darde7b71sag6t",
        'USER': "xsdyaptsklaroz",
        'PASSWORD': "d3d74b6616053c4bf48a3d4ed25ab785313b3f07cce9ecfbfd0ba58192120fe1",
        'HOST': "ec2-3-233-7-12.compute-1.amazonaws.com",
        'PORT': 5432,
    }
}

# The file storage engine to use when collecting static files with the collectstatic management command.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

