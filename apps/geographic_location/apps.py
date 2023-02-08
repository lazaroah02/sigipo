from django.apps import AppConfig


class GeographicLocationConfig(AppConfig):
    """Defines the name for the geographic_location app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.geographic_location"
    verbose_name = "Ubicación geográfica"
