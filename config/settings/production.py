# flake8: noqa
from config.settings.base import *  # unimport:skip

ALLOWED_HOSTS = ["*"]
DEBUG = False


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "sigipo", "static"),)
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
