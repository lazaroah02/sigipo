from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
    Model,
    SmallIntegerField,
)
from django.db.models.manager import Manager

from apps.classifiers.models import Morphology, Topography
from apps.patient.models import Patient


class NeoplasmLateralityChoices(IntegerChoices):
    NO = 1, "No"
    RIGHT = 2, "Derecho"
    LEFT = 3, "Izquierdo"


class NeoplasmDiagnosticConfirmationChoices(IntegerChoices):
    CLINIC = 1, "Clínica"
    CLINIC_RESEARCH = 2, "Investigación Clínica"
    TUMOR_MARKERS = 4, "Marcadores Tumorales"
    CYTOLOGY = 5, "Citología"
    HISTOLOGY_OF_A_METASTASIS = 6, "Histología de una metástasis"
    PRIMARY_TUMOR_HISTOLOGY = 7, "Histología del tumor primario"
    UNKNOWN = 9, "Desconocido"


class NeoplasmDifferentiationGradesChoices(IntegerChoices):
    Differentiated = 1, "Diferenciado"
    MODERATELY_DIFFERENTIATED = 2, "Moderadamente diferenciado"
    POORLY_DIFFERENTIATED = 3, "Poco diferenciado"
    UNDIFFERENTIATED = 4, "Indiferenciado"
    T_CELLS = 5, "Células T"
    B_CELLS = 6, "Células B"
    NULL_CELLS = 7, "Células nulas"
    NK_CELLS = 8, "Células NK"
    UNDETERMINED = 9, "No determinado"


class NeoplasmClinicalExtensionsChoices(IntegerChoices):
    IN_SITU = 1, "In situ"
    LOCATED = 2, "Localizada"
    DIRECT_EXTENSION = 3, "Extesión Directa"
    REGIONAL_LYMPHATIC = 4, "Linfática Regional"
    REGIONAL_DIRECT_AND_LYMPHATIC_EXTENSION = (
        5,
        "Extensión Directa y Linfática Regional",
    )
    REMOTE_METASTASIS = 6, "Metástasis remota"
    NOT_APPLICABLE = 7, "No aplicable"
    UNKNOWN = 8, "Desconocido"


class NeoplasmClinicalStageChoices(IntegerChoices):
    IN_SITU = 0, "In Situ"
    I0 = 1, "I"
    IA = 2, "Ia"
    IB = 3, "Ib"
    IC = 4, "Ic"
    II = 5, "II"
    IIA = 6, "IIa"
    IIB = 7, "IIb"
    IIC = 8, "IIc"
    III = 9, "III"
    IIIA = 10, "IIIa"
    IIIB = 11, "IIIb"
    IIIC = 12, "IIIc"
    IV = 13, "IV"
    IVA = 14, "IVa"
    IVB = 15, "IVb"
    IVC = 16, "IVc"
    NOT_APPLICABLE = 17, "Desconocido"
    UNKNOWN = 18, "No Aplicable"


class NeoplasmSourceOfInfoChoices(IntegerChoices):
    PATHOLOGY = 1, "Anatomía patológica"
    HEMATOLOGY = 2, "Hematología"
    HOSPITAL_DISCHARGE = 3, "Egreso hospitalario"
    DECEASED_RECORD = 4, "Registro de fallecidos"


class NeoplasmQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class Neoplasm(Model):
    """
    Model representation of a neoplasm
    """

    patient = ForeignKey(
        Patient,
        on_delete=CASCADE,
        verbose_name="Paciente",
    )
    date_of_diagnosis = DateField(verbose_name="Fecha de diagnóstico", blank=True)
    primary_site = ForeignKey(
        Topography,
        verbose_name="Sitio primario",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    laterality = IntegerField(
        verbose_name="Lateralidad",
        choices=NeoplasmLateralityChoices.choices,
        blank=True,
    )
    diagnostic_confirmation = IntegerField(
        verbose_name="Confirmación del Diagnóstico",
        choices=NeoplasmDiagnosticConfirmationChoices.choices,
    )
    histologic_type = ForeignKey(
        Morphology,
        verbose_name="Tipo histológico",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    differentiation_grade = SmallIntegerField(
        verbose_name="Grado de diferenciación",
        choices=NeoplasmDifferentiationGradesChoices.choices,
        blank=True,
    )
    clinical_extension = SmallIntegerField(
        verbose_name="Extensión clínica",
        choices=NeoplasmClinicalExtensionsChoices.choices,
        blank=True,
    )
    clinical_stage = SmallIntegerField(
        verbose_name="Etapa clínica", choices=NeoplasmClinicalStageChoices.choices
    )
    is_pregnant = BooleanField(verbose_name="¿Embarazada?", default=False)
    trimester = IntegerField(verbose_name="Trimestre", blank=True)
    is_vih = BooleanField(verbose_name="¿Es VIH+?", default=False)
    source_of_info = IntegerField(
        verbose_name="Fuente de información",
        choices=NeoplasmSourceOfInfoChoices.choices,
        blank=True,
    )
    date_of_report = DateField(verbose_name="Fecha del reporte", blank=True)
    medic_that_report = CharField(
        verbose_name="Médico que reporta", max_length=128, blank=True
    )

    class Meta:
        verbose_name = "Neoplasia"
        verbose_name_plural = "Neoplasias"
        ordering = ["pk"]

    def __str__(self):
        return f"{self.subject}"
