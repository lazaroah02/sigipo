from django.apps import AppConfig


class PatientConfig(AppConfig):
    """Defines the name for the patient app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.patient"
    verbose_name = "Paciente"
