from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    Index,
    IntegerChoices,
    IntegerField,
    UniqueConstraint,
)
from django.db.models.manager import Manager

from apps.core.models import TimeStampedModel
from apps.geographic_location.models import Municipality
from apps.patient.validators import IdentityCardValidator, only_numbers_validator


class PatientQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related municipality."""
        return (
            super()
            .get_queryset()
            .select_related(
                "born_municipality",
                "born_municipality__province",
                "residence_municipality",
                "residence_municipality__province",
            )
        )

    def only_oncologic(self):
        """Fetch only the oncologic patients."""
        return self.get_queryset().filter(is_oncologic=True)

    def only_no_oncologic(self):
        """Fetch only the no oncologic patients."""
        return self.get_queryset().filter(is_oncologic=False)


class PatientRace(IntegerChoices):
    """Defines the patient race."""

    UNDEFINED = 0, "No Definido"
    WHITE = 1, "Blanca"
    BLACK = 2, "Negra"
    HALF_BLOOD = 3, "Mestizo"
    YELLOW = 4, "Amarillo"


class SexChoices(IntegerChoices):
    """Defines the patients sex."""

    UNDEFINED = 0, "No definido"
    MALE = 1, "Masculino"
    FEMALE = 2, "Femenino"


class Patient(TimeStampedModel):
    """Model representation of a patient."""

    identity_card = CharField(
        verbose_name="Carnet de Identidad",
        max_length=11,
        validators=[IdentityCardValidator(6, 11), only_numbers_validator],
    )
    first_name = CharField(verbose_name="Nombre", max_length=128)
    last_name = CharField(verbose_name="Apellidos", max_length=255)
    street = CharField(verbose_name="Calle", max_length=255, blank=True, null=True)
    number = CharField(verbose_name="Número", max_length=255, blank=True, null=True)
    building = CharField(verbose_name="Edificio", max_length=255, blank=True, null=True)
    apartment = CharField(
        verbose_name="Apartamento", max_length=255, blank=True, null=True
    )
    sex = IntegerField(
        verbose_name="Sexo",
        choices=SexChoices.choices,
        blank=True,
        null=True,
    )
    date_of_birth = DateField(
        verbose_name="Fecha de nacimiento",
        blank=True,
        null=True,
    )
    between_streets = CharField(
        verbose_name="Entre calles", max_length=255, blank=True, null=True
    )
    division = CharField(verbose_name="Reparto", max_length=255, blank=True, null=True)
    race = IntegerField(
        verbose_name="Raza", choices=PatientRace.choices, default=PatientRace.UNDEFINED
    )
    medical_record = CharField(
        verbose_name="No. Historia Clínica", max_length=32, blank=True, null=True
    )
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
    is_oncologic = BooleanField(default=False)
    objects = PatientQuerysetManager()

    class Meta:
        """Meta definition for Patient."""

        verbose_name = "Paciente"
        verbose_name_plural = "pacientes"
        ordering = ["updated_at"]
        permissions = (
            (
                "add_oncologic",
                "Puede añadir pacientes al registro de cáncer",
            ),
            (
                "view_oncologic",
                "Puede añadir pacientes al registro de cáncer",
            ),
            (
                "change_oncologic",
                "Puede añadir pacientes al registro de cáncer",
            ),
            (
                "delete_oncologic",
                "Puede añadir pacientes al registro de cáncer",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["identity_card"],
                name="patient_identity_card_constraints",
            )
        ]
        indexes = [
            Index(fields=["last_name", "first_name"]),
            Index(fields=["first_name"]),
            Index(fields=["last_name"]),
            Index(fields=["identity_card"]),
            Index(fields=["medical_record"]),
        ]

    def __str__(self):
        """Returns the name of the patient."""
        return f"{self.first_name} {self.last_name} ({self.identity_card})"
