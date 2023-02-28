from django.db.models import (
    SET_NULL,
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    IntegerField,
    DateTimeField,
    OneToOneField,
    Model)

from apps.geographic_location.models import Municipality
from apps.patient.validators import IdentityCardValidator, only_numbers_validator
from apps.patient.models import SexChoices,PatientQuerysetManager,PatientRace
from apps.pathological_anatomy.models import Pathology

class DeathCertificate(Model):
    """Model representation of a death_certificate."""

    death_cause = CharField(verbose_name="Causa de Muerte", max_length=1000)

    authopsy_number = OneToOneField(Pathology, to_field="authopsy_number", null=False, blank=False, on_delete=CASCADE, primary_key=True)

    time_of_death = DateTimeField(
        verbose_name="Fecha de defunción",
        blank=True,
        null=True,
        auto_now_add=True,
    )
    
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
        related_name="residence_municipality_death",
        null=True,
        on_delete=SET_NULL,
    )
    born_municipality = ForeignKey(
        Municipality,
        verbose_name="Municipio natal",
        related_name="born_municipality_death",
        null=True,
        on_delete=SET_NULL,
    )
    is_oncologic = BooleanField(default=False)
    objects = PatientQuerysetManager()


    class Meta:
        verbose_name = "Certificado de Defunción"
        verbose_name_plural = "Certificados de Defunción"
        ordering = ["pk"]
        default_permissions = ()

    def __str__(self):
        """String representation of death_certificate."""
        return f"{self.name}"
