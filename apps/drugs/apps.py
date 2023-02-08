from django.apps import AppConfig


class DrugsConfig(AppConfig):
    """Define the name of drugs app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.drugs"
    verbose_name = "Fármacos"
