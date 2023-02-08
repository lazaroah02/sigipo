from django.apps import AppConfig


class DeathCertificateConfig(AppConfig):
    """Defines the name for the death_certificate app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.death_certificate"
    verbose_name = "Certificado de Defunción"
