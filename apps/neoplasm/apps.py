from django.apps import AppConfig


class NeoplasmConfig(AppConfig):
    """Defines the name for the neoplasm app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.neoplasm"
    verbose_name = "Neoplasma"
