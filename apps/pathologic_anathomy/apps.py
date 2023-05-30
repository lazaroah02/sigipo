from django.apps import AppConfig


class PathologicAnathomyConfig(AppConfig):
    """Defines the name for the cancer_registry app."""
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.pathologic_anathomy"
    verbose_name = "Anatomia Patologica"
