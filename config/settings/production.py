# flake8: noqa
from config.settings.base import *  # unimport:skip

ALLOWED_HOSTS = ["*"]
DEBUG = False

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "sigipo", "static"),)
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'