from django.db.models import CASCADE, AutoField, ForeignKey, TextChoices
from multiselectfield import MultiSelectField

from apps.core.models import TimeStampedModel
from apps.patient.models import Patient


class OncologicStudyChoices(TextChoices):
    TSH = "TSH", "TSH"
    T3 = "T3", "T3"
    T4 = "T4", "T4"
    TG = "TG", "TG"
    ANTI_TG = "ANTI-TG", "ANTI-TG"
    ANTI_TIPO = "ANTI-TIPO", "ANTI-TIPO"
    CALCIT = "CALCIT", "CALCIT"
    CA_10_9 = "CA 19-9", "CA 19-9"
    CA_15_3 = "CA 15-3", "CA 15-3"
    CA_125 = "CA 125", "CA 125"
    PSA = "PSA", "PSA"
    PSA_FREE = "PSA Free", "PSA Free"
    CEA = "CEA", "CEA"
    ALF = "ALF", "ALF"


class PatientOncologicStudy(TimeStampedModel):
    """Model representation of oncologic study."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    sample_number = AutoField(primary_key=True)
    tests = MultiSelectField(
        choices=OncologicStudyChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )

    class Meta:
        verbose_name = "Estudio oncológico RIA-IRMA"
        verbose_name_plural = "Estudios oncológicos RIA-IRMA"
        ordering = ["pk"]

    def __str__(self):
        return "Muestra " + str(self.sample_number) + " " + str(self.tests)
