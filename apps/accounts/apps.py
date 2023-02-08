from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Defines the name for the Accounts app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"
    label = "accounts"
    verbose_name = "Accounts"
