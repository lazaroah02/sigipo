from django.apps import AppConfig


class NuclearMedicineConfig(AppConfig):
    """Define the name of nuclear_medicine app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.nuclear_medicine"
    verbose_name = "Medicina Nuclear"
