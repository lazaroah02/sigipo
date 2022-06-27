from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model
    """

    class Meta:
        ordering = ["username"]
        default_permissions = ()
        permissions = (
            (
                "patient_manage",
                "Puede Crear/Modificar/Eliminar datos de pacientes no oncologicos",
            ),
            (
                "cancer_registry_view",
                "Puede visualizar datos del registro de cáncer",
            ),
            (
                "cancer_registry_manage",
                "Puede Crear/Modificar/Eliminar datos del registro de cáncer",
            ),
            (
                "download_cancer_report",
                "Puede descargar reportes del registro de cáncer",
            ),
            (
                "nuclear_medicine_view",
                "Puede visualizar datos de medicina nuclear.",
            ),
            (
                "nuclear_medicine_manage",
                "Puede Crear/Modificar/Eliminar datos de medicina nuclear",
            ),
            (
                "drug_view",
                "Puede visualizar fármacos.",
            ),
            (
                "drug_manage",
                "Puede Crear/Modificar/Eliminar datos de fármacos",
            ),
            (
                "employee_view",
                "Puede visualizar fármacos.",
            ),
            (
                "employee_manage",
                "Puede Crear/Modificar/Eliminar datos de grupos de trabajo/médicos",
            ),
        )

    def __str__(self) -> str:
        """Define the str representation for the user."""
        return self.get_full_name() or self.username
