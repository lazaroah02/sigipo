from django.core.validators import MinLengthValidator
from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    ForeignKey,
    IntegerField,
    PositiveSmallIntegerField,
    TextField,
    UniqueConstraint,
)
from django.db.models.manager import Manager

from apps.core.models import TimeStampedModel
from apps.geographic_location.models import Municipality


class PatientQuerysetManager(Manager):
    """Manager to handle patient."""

    def only_oncologic(self):
        """Fetch only the oncologic patients."""
        return super().get_queryset().filter(is_oncologic=True)

    def only_no_oncologic(self):
        """Fetch only the no oncologic patients."""
        return super().get_queryset().filter(is_oncologic=False)


class Patient(TimeStampedModel):
    """Model representation of a patient."""

    RACE = (
        (0, "No Definido"),
        (1, "Blanca"),
        (2, "Negra"),
        (3, "Mestizo"),
        (4, "Amarillo"),
    )
    identity_card = CharField(
        verbose_name="Carné de Identidad",
        max_length=11,
        validators=[MinLengthValidator(11)],
    )
    first_name = CharField(verbose_name="Nombre", max_length=128)
    last_name = CharField(verbose_name="Apellidos", max_length=255)
    address = TextField(verbose_name="Dirección Actual")
    race = IntegerField(verbose_name="Raza", choices=RACE, default=0)
    medical_record = CharField(verbose_name="No. Historia Clínica", max_length=32)
    residence_municipality = ForeignKey(
        Municipality,
        verbose_name="Municipio de residencia",
        related_name="residence_municipality",
        null=True,
        on_delete=SET_NULL,
    )
    born_municipality = ForeignKey(
        Municipality,
        verbose_name="Municipio natal",
        related_name="born_municipality",
        null=True,
        on_delete=SET_NULL,
    )
    age_at_diagnosis = PositiveSmallIntegerField(
        verbose_name="Edad al momento del diagnóstico", blank=True, null=True
    )
    is_oncologic = BooleanField(default=False)
    objects = PatientQuerysetManager()

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "pacientes"
        ordering = ["updated_at"]
        constraints = [
            UniqueConstraint(
                fields=["identity_card", "medical_record"],
                name="patient_medical_record_identity_card_constraints",
            )
        ]

    def __str__(self):
        """Returns the name of the patient."""
        return f"{self.first_name} {self.last_name}"
