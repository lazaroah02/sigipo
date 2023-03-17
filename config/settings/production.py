# flake8: noqa
from config.settings.base import *  # unimport:skip

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["https://sigipo.azurewebsites.net"]

DEBUG = False

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [str(BASE_DIR / "sigipo" / "static" )]

STATIC_ROOT = BASE_DIR / "staticfiles"

