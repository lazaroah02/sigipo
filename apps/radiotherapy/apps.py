from django.apps import AppConfig


class RadiotherapyConfig(AppConfig):
    """Defines the name for the Radiotherapy app."""

    verbose_name = "Radioterapia"
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.radiotherapy"