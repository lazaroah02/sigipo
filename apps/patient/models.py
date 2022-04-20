from django.core.validators import MinLengthValidator
from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    ForeignKey,
    IntegerChoices,
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
        return (
            super()
            .get_queryset()
            .select_related("born_municipality", "residence_municipality")
            .filter(is_oncologic=True)
        )

    def only_no_oncologic(self):
        """Fetch only the no oncologic patients."""
        return (
            super()
            .get_queryset()
            .select_related("born_municipality", "residence_municipality")
            .filter(is_oncologic=False)
        )


class PatientRace(IntegerChoices):
    UNDEFINED = 0, "No Definido"
    WHITE = 1, "Blanca"
    BLACK = 2, "Negra"
    HALF_BLOOD = 3, "Mestizo"
    YELLOW = 4, "Amarillo"


class Patient(TimeStampedModel):
    """Model representation of a patient."""

    identity_card = CharField(
        verbose_name="Carnet de Identidad",
        max_length=11,
        validators=[MinLengthValidator(11)],
    )
    first_name = CharField(verbose_name="Nombre", max_length=128)
    last_name = CharField(verbose_name="Apellidos", max_length=255)
    address = TextField(verbose_name="Dirección Actual")
    race = IntegerField(
        verbose_name="Raza", choices=PatientRace.choices, default=PatientRace.UNDEFINED
    )
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
        return f"{self.first_name} {self.last_name} ({self.medical_record})"
