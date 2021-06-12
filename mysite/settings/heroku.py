from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")cs-%s3ednl%7cw2$12&g-h(%*c8lv+!zcw2$jj$^*t7wm+^$%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# The file storage engine to use when collecting static files with the collectstatic management command.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

