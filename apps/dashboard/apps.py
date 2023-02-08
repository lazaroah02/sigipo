from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """Defines the name for the dashboard app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.dashboard"
    verbose_name = "Dashboard"
