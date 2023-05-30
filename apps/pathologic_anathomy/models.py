from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
)

from django.db.models.manager import Manager

from apps.core.models import TimeStampedModel
from apps.employee.models import Doctor
from apps.patient.models import (
    Patient,
    SexChoices as PatientSexChoices,
    PatientRace as PatientRaceChoice,
    )




# Create your models here.


class HospitalChoice(IntegerChoices):
    """Defines the Hospital in Holguin"""
    lenin_h = 1, "Hospital Lenin"
    clinic_h = 2, "Hospital Clinico"
    pediatric_h = 3, "hospital Pediatrico"
    military_h = 4, "Hosptal Militar"
    
    def __str__(self):
        return self.name

class BiopsyTypeChoice(IntegerChoices):
    """Defines the type of biopsy"""

    breast_biopsy = 1, "Biopsia de mama"
    neck_biopsy = 2, "Biopsia de Cuello"
    digestive_biopsy = 3, "Siopsia Digestivo"
    lymphoma_biopsy = 4, "Biopsia de Linfoma"
    ginecologic_biopsy = 5, "Biopsia de Ginecologia"
    head_biopsy = 6, "Biopsia de Cabeza"
    
    def __str__(self):
        return self.name


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
    biopsy_id = CharField(max_length=100, verbose_name="No Biopsia",null=True)
    hospital = IntegerField(verbose_name="Hospital", choices=HospitalChoice.choices, blank=True, null=True)
    sample_date = DateField(verbose_name="Fecha de la muestra",blank=True, null=True)
    health_area = CharField(max_length=250, verbose_name="Area de Salud", blank=True, null=True)
    especiality = CharField(max_length=250, verbose_name="Especialidad", blank=True, null=True)
    patient = ForeignKey(Patient, on_delete=CASCADE, verbose_name="Paciente")
    age = IntegerField(verbose_name="Edad", blank=True, null=True)
    sex = IntegerField(verbose_name="Sexo", choices=PatientSexChoices.choices, default=PatientSexChoices.UNDEFINED)
    race = IntegerField(verbose_name="Raza", choices=PatientRaceChoice.choices, default=PatientRaceChoice.UNDEFINED)
    address = CharField(max_length=255, verbose_name="Direeción Particular", blank=True, null=True)
    biopsy_type = IntegerField(verbose_name="Tipo de Biopsia", choices=BiopsyTypeChoice.choices, blank=True, null=True)
    sample_biopsy = CharField(max_length=250, verbose_name="Tipo de Muestra")
    clinic_data = CharField(max_length=255, verbose_name="Datos Clinicos")
    clinic_diagnostic = CharField(max_length=255, verbose_name="Diagnostico Clinico")
    medic_that_report = ForeignKey(Doctor, verbose_name="Médico que reporta", on_delete=CASCADE, blank=True, null=True)
    objects = BiopsyOrderQuerysetManager()

    class Meta:
        verbose_name = "Solicitud de Biopsia"
        verbose_name_plural = "Solicitudes de Biopsias"
        ordering = ["pk"]
        
    
    def __str__(self):
        return f"{self.biopsy_id}"
    
