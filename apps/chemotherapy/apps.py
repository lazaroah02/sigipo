from django.apps import AppConfig


class ChemotherapyConfig(AppConfig):
    """Defines the name for the chemotherapy app."""

    verbose_name = "Quimioterapia"
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.chemotherapy"
