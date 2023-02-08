from django.db.models import CASCADE, CharField, ForeignKey, Model
from django.db.models.manager import Manager


# Create your models here.
class Group(Model):
    name = CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupo"
        ordering = ["pk"]
        default_permissions = ()


class DoctorQuerysetManager(Manager):
    """Manager to handle group."""

    def get_queryset(self):
        """Select related group."""
        return super().get_queryset().select_related("group")


class Doctor(Model):
    first_name = CharField(verbose_name="Nombre", max_length=255)
    last_name = CharField(
        verbose_name="Apellidos", max_length=255, blank=True, null=True
    )
    personal_record_number = CharField(
        verbose_name="Número de registro", max_length=255, primary_key=True
    )
    group = ForeignKey(Group, verbose_name="Grupo de trabajo", on_delete=CASCADE)
    objects = DoctorQuerysetManager()

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctor"
        ordering = ["personal_record_number"]
        default_permissions = ()

    def __str__(self):
        """Returns the name of the patient."""
        return f"{self.first_name} {self.last_name} ({self.personal_record_number})"
