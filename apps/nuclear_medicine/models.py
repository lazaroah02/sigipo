from django.db.models import (
    CASCADE,
    AutoField,
    FloatField,
    ForeignKey,
    OneToOneField,
    TextChoices,
)
from django.db.models.manager import Manager
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


class OncologicStudyQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


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
    objects = OncologicStudyQuerysetManager()

    class Meta:
        verbose_name = "Estudio oncológico RIA-IRMA"
        verbose_name_plural = "Estudios oncológicos RIA-IRMA"
        ordering = ["created_at"]

    def __str__(self):
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"


class HormonalStudyChoices(TextChoices):
    TSG = "TSH", "TSH"
    T3 = "T3", "T3"
    T4 = "T4", "T4"
    T3F = "T3F", "T3F"
    T4F = "T4F", "T4F"
    TRL = "PRL", "PRL"
    FSH = "FSH", "FSH"
    LH = "LH", "LH"
    PRG = "PRG", "PRG"
    E2 = "E2", "E2"
    CORT = "CORT", "CORT"
    INS = "INS", "INS"
    TEST = "TEST", "TEST"
    TGH = "GH", "GH"


class HormonalStudyQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class PatientHormonalStudy(TimeStampedModel):
    """Model representation of hormonal study."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    sample_number = AutoField(primary_key=True)
    tests = MultiSelectField(
        choices=HormonalStudyChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )
    objects = HormonalStudyQuerysetManager()

    class Meta:
        verbose_name = "Estudio hormonal RIA-IRMA"
        verbose_name_plural = "Estudios hormonales RIA-IRMA"
        ordering = ["created_at"]

    def __str__(self):
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"


class HormonalResultQuerysetManager(Manager):
    """Manager to handle hormonal_study."""

    def get_queryset(self):
        """Fetch the related hormonal_study."""
        return super().get_queryset().select_related("hormonal_study")


class HormonalResult(TimeStampedModel):
    hormonal_study = OneToOneField(
        PatientHormonalStudy, blank=False, null=False, on_delete=CASCADE
    )
    tsh = FloatField(blank=True, null=True)
    t3 = FloatField(blank=True, null=True)
    t4 = FloatField(blank=True, null=True)
    t3f = FloatField(blank=True, null=True)
    t4f = FloatField(blank=True, null=True)
    prl = FloatField(blank=True, null=True)
    fsh = FloatField(blank=True, null=True)
    lh = FloatField(blank=True, null=True)
    prg = FloatField(blank=True, null=True)
    e2 = FloatField(blank=True, null=True)
    cort = FloatField(blank=True, null=True)
    ins = FloatField(blank=True, null=True)
    test = FloatField(blank=True, null=True)
    gh = FloatField(blank=True, null=True)
    objects = HormonalResultQuerysetManager()

    class Meta:
        verbose_name = "Resultado hormonal RIA-IRMA"
        verbose_name_plural = "Resultados hormonales RIA-IRMA"
        ordering = ["pk"]

    def __str__(self):
        return f"Resultado de {str(self.hormonal_study)}"


class OncologicResultQuerysetManager(Manager):
    """Manager to handle oncologic_study."""

    def get_queryset(self):
        """Fetch the related oncologic_study."""
        return super().get_queryset().select_related("oncologic_study")


class OncologicResult(TimeStampedModel):
    oncologic_study = OneToOneField(
        PatientOncologicStudy, blank=False, null=False, on_delete=CASCADE
    )
    tsh = FloatField(blank=True, null=True)
    t3 = FloatField(blank=True, null=True)
    t4 = FloatField(blank=True, null=True)
    tg = FloatField(blank=True, null=True)
    anti_tg = FloatField(blank=True, null=True)
    anti_tipo = FloatField(blank=True, null=True)
    calcit = FloatField(blank=True, null=True)
    ca19_9 = FloatField(blank=True, null=True)
    ca15_3 = FloatField(blank=True, null=True)
    ca125 = FloatField(blank=True, null=True)
    cea = FloatField(blank=True, null=True)
    alf = FloatField(blank=True, null=True)
    psa = FloatField(blank=True, null=True)
    psafree = FloatField(blank=True, null=True)
    objects = OncologicResultQuerysetManager()

    class Meta:
        verbose_name = "Resultado oncología RIA-IRMA"
        verbose_name_plural = "Resultados oncología RIA-IRMA"
        ordering = ["pk"]

    def __str__(self):
        return f"Resultado de {str(self.oncologic_study)}"


class IodineDetectionQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class IodineDetection(TimeStampedModel):
    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    two_hours = FloatField(blank=True, null=True)
    twenty_four_hours = FloatField(blank=True, null=True)
    objects = IodineDetectionQuerysetManager()

    class Meta:
        verbose_name = "Detección de yodo"
        verbose_name_plural = "Detección de yodo"
        ordering = ["pk"]

    def __str__(self):
        return f"Detección de yodo de {str(self.patient)}"


class SerialIodineDetection(TimeStampedModel):
    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    two_hours = FloatField(blank=True, null=True)
    four_hours = FloatField(blank=True, null=True)
    eight_hours = FloatField(blank=True, null=True)
    twenty_four_hours = FloatField(blank=True, null=True)
    forty_eight_hours = FloatField(blank=True, null=True)
    seventy_two_hours = FloatField(blank=True, null=True)
    ninety_six_hours = FloatField(blank=True, null=True)
    objects = IodineDetectionQuerysetManager()

    class Meta:
        verbose_name = "Detección de yodo seriada"
        verbose_name_plural = "Detección de yodo seriada"
        ordering = ["pk"]

    def __str__(self):
        return f"Detección de yodo seriada de {str(self.patient)}"
