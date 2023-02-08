from django.apps import AppConfig


class ClassifiersConfig(AppConfig):
    """Defines the name for the classifiers app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.classifiers"
    verbose_name = "Clasificadores"
