import datetime

from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
)
from django.db.models.manager import Manager

from apps.core.models import TimeStampedModel
from apps.employee.models import Doctor
from apps.patient.models import Patient
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_mama_cdis import MamaCDISBiopsyDiagnostic

# Create your models here.

class HospitalChoice(IntegerChoices):
    """Defines the Hospital in Holguin"""

    lenin_h = 1, "Hospital Lenin"
    clinic_h = 2, "Hospital Clinico"
    pediatric_h = 3, "hospital Pediatrico"
    military_h = 4, "Hosptal Militar"


class BiopsyTypeChoice(IntegerChoices):
    """Defines the type of biopsy"""

    head_biopsy = 1, "Biopsia de Cabeza"
    neck_biopsy = 2, "Biopsia de Cuello"
    digestive_biopsy = 3, "Biopsia Digestivo"
    ginecologic_biopsy = 4, "Biopsia de Ginecologia"
    lymphoma_biopsy = 5, "Biopsia de Linfoma"
    breast_biopsy_cdi = 6, "Biopsia de Mama CDI"
    breast_biopsy_cdis = 7, "Biopsia de Mama CDIS"


class BiopsyOrderQuerysetManager(Manager):
    """Manager to handle related models."""

    def get_queryset(self):
        """Fetch the related models."""
        return (
            super()
            .get_queryset()
            .select_related(
                "patient",
                "medic_that_report",
            )
        )


class BiopsyRequest(TimeStampedModel):
    biopsy_id = CharField(
        max_length=100, verbose_name="No Biopsia", null=True, editable=False
    )
    hospital = IntegerField(
        verbose_name="Hospital", choices=HospitalChoice.choices, blank=True, null=True
    )
    sample_date = DateField(verbose_name="Fecha de la muestra", blank=True, null=True)
    health_area = CharField(
        max_length=255, verbose_name="Area de Salud", blank=True, null=True
    )
    especialty = CharField(
        max_length=255, verbose_name="Especialidad", blank=True, null=True
    )
    patient = ForeignKey(Patient, on_delete=CASCADE, verbose_name="Paciente")
    biopsy_type = IntegerField(
        verbose_name="Tipo de Biopsia",
        choices=BiopsyTypeChoice.choices,
        blank=True,
        null=True,
    )
    sample_biopsy = CharField(max_length=255, verbose_name="Tipo de Muestra")
    clinic_data = CharField(max_length=255, verbose_name="Datos Clinicos")
    clinic_diagnostic = CharField(max_length=255, verbose_name="Diagnostico Clinico")
    verificated = BooleanField(verbose_name="Biopsia Verificada", default=False)
    medic_that_report = ForeignKey(
        Doctor,
        verbose_name="Médico que reporta",
        on_delete=CASCADE,
        blank=True,
        null=True,
    )
    objects = BiopsyOrderQuerysetManager()

    class Meta:
        verbose_name = "Solicitud de Biopsia"
        verbose_name_plural = "Solicitudes de Biopsias"
        ordering = ["pk"]

    def __str__(self):
        return f"{self.biopsy_id} {self.get_biopsy_type_display()}"

    def save(self, *args, **kwargs):
        if not self.biopsy_id:
            year = datetime.date.today().year
            super().save(*args, **kwargs)
            self.biopsy_id = f"{year}-B-{self.pk}"
            super().save(update_fields=["biopsy_id"])
        else:
            super().save(*args, **kwargs)
