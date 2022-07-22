# flake8: noqa
from config.settings.base import *  # unimport:skip

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]
DEBUG = False


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "sigipo", "static"),)
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
