from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    DateField,
    CharField,
    PositiveIntegerField,
)
from apps.employee.models import Doctor

from apps.patient.models import Patient

# Create your models here.

# Evaluate the posibility of moving Physicist to employee.models

class Physicist(Model):
    """
    Model representation of a Physicist (Only Name field for now)
    """

    name = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Nombre",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Físico"
        verbose_name_plural = "Físicos"
        ordering = ["pk"]

class Dosimetrist(Model):
    """
    Model representation of a Dosimetrist (Only Name field for now)
    """

    name = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Nombre",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Dosimetrista"
        verbose_name_plural = "Dosimetristas"
        ordering = ["pk"]

class TACRequest(Model):
    """
    Model representation of a TAC request for planning
    """

    id_code = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="ID",
    )

    patient = ForeignKey(
        Patient,
        on_delete=CASCADE,
        verbose_name="Paciente",
    )

    date_of_request = DateField(
        verbose_name="Fecha de solicitud",
        blank=True,
        null=True,
    )

    bb_position = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Pocición del BB",
    )

    location = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Localización",
    )

    upper_limit = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Límite Superior",
    )

    lower_limit = CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Límite Inferior",
    )

    distance_betwen_cuts = PositiveIntegerField(
        blank=True, 
        null=True, 
        verbose_name="Distancia entre Cortes (mm)",
    )

    medic_that_requests = ForeignKey(
        Doctor,
        verbose_name="Médico",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )

    physicist = ForeignKey(
        Physicist,
        on_delete=CASCADE,
        verbose_name="Físico",
    )

    dosimetrist = ForeignKey(
        Dosimetrist,
        on_delete=CASCADE,
        verbose_name="Dosimetrista",
    )

    def __str__(self) -> str:
        return f'{self.id_code} - {self.patient}'

    class Meta:
        verbose_name = "Solicitud de TAC"
        verbose_name_plural = "Solicitudes de TAC"
        ordering = ["pk"]