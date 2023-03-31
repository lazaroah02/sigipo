from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model
    """

    class Meta:
        ordering = ["username"]
        permissions = (
            (
                "download_cancer_report",
                "Puede descargar reportes del registro de cáncer",
            ),
        )

    def __str__(self) -> str:
        """Define the str representation for the user."""
        return self.get_full_name() or self.username
