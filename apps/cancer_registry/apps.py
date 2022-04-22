from django.apps import AppConfig


class CancerRegistryConfig(AppConfig):
    """Defines the name for the cancer_registry app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cancer_registry"
    verbose_name = "Registro de cancer"
