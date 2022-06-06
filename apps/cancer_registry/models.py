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
    TextChoices,
)
from django.db.models.manager import Manager

from apps.classifiers.models import Morphology, Topography
from apps.employee.models import Doctor, Group
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
    """Manager to handle related models."""

    def get_queryset(self):
        """Fetch the related models."""
        return (
            super()
            .get_queryset()
            .select_related(
                "patient",
                "primary_site",
                "histologic_type",
                "medic_that_report",
                "group",
            )
        )


class TreatmentPerformedChoices(IntegerChoices):
    SURGERY = 1, "Cirugía"
    CHEMOTHERAPY = 2, "Quimioterapia"
    RADIOTHERAPY = 3, "Radioterapia"
    HORMONE_THERAPY = 4, "Hormonoterapia"
    NONE_TREATMENT = 0, "Ninguno"


class TumorChoices(TextChoices):
    TX = "TX" "TX"
    T0 = "T0", "T0"
    TIS = "Tis", "Tis"
    T1 = "T1", "T1"
    T2 = "T2", "T2"
    T3 = "T3", "T3"
    T4 = "T4", "T4"


class NoduleChoices(TextChoices):
    NX = "NX", "NX"
    N0 = "N0", "N0"
    N1 = "N1", "N1"
    N2 = "N2", "N2"
    N3 = "N3", "N3"


class MetastasisChoices(TextChoices):
    MX = "MX", "MX"
    M0 = "M0", "M0"
    M1 = "M1", "M1"


class NeoplasmClassificationChoices(IntegerChoices):
    CLINIC = 1, "Clínico"
    PATHOLOGICAL = 2, "Patológico"


class TumorClassificationChoices(IntegerChoices):
    PRIMARY = 1, "Tumor primario"
    METASTASIS = 2, "Metástasis sin tumor primario conocido"


class AcuteLymphoidLeukemiaChoices(IntegerChoices):
    L1 = 1, "L1"
    L2 = 2, "L2"
    L3 = 3, "L3"


class ChronicLymphoidLeukemiaChoices(IntegerChoices):
    _0 = 1, "0"
    _I = 2, "I"
    II = 3, "II"
    III = 4, "III"
    IV = 5, "IV"


class AcuteMyeloidLeukemiaChoices(IntegerChoices):
    M0 = 0, "M0"
    M1 = 1, "M1"
    M2 = 2, "M2"
    M3 = 3, "M3"
    M4 = 4, "M4"
    M5 = 5, "M5"
    M6 = 6, "M6"
    M7 = 7, "M7"


class MultipleMyelomaChoices(IntegerChoices):
    IA = 1, "Ia"
    IB = 2, "Ib"
    IIA = 3, "IIa"
    IIB = 4, "IIb"
    IIIA = 5, "IIIa"
    IIIB = 6, "IIIb"


class ChronicMyeloidLeukemiaChoices(IntegerChoices):
    STABLE = 1, "Estable"
    ACCELERATED = 2, "Acelerada"
    BLAST_CRISIS = 3, "Crisis blástica "


class Neoplasm(Model):
    """
    Model representation of a neoplasm
    """

    patient = ForeignKey(
        Patient,
        on_delete=CASCADE,
        verbose_name="Paciente",
    )
    date_of_diagnosis = DateField(
        verbose_name="Fecha de diagnóstico",
        blank=True,
        null=True,
    )
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
        null=True,
    )
    diagnostic_confirmation = IntegerField(
        verbose_name="Confirmación del Diagnóstico",
        choices=NeoplasmDiagnosticConfirmationChoices.choices,
        blank=True,
        null=True,
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
        null=True,
    )
    clinical_extension = SmallIntegerField(
        verbose_name="Extensión clínica",
        choices=NeoplasmClinicalExtensionsChoices.choices,
        blank=True,
        null=True,
    )
    clinical_stage = SmallIntegerField(
        verbose_name="Etapa clínica",
        choices=NeoplasmClinicalStageChoices.choices,
        blank=True,
        null=True,
    )
    is_pregnant = BooleanField(verbose_name="¿Embarazada?", default=False)
    trimester = IntegerField(verbose_name="Trimestre", blank=True, null=True)
    is_vih = BooleanField(verbose_name="¿Es VIH+?", default=False)
    source_of_info = IntegerField(
        verbose_name="Fuente de información",
        choices=NeoplasmSourceOfInfoChoices.choices,
        blank=True,
        null=True,
    )
    date_of_report = DateField(
        verbose_name="Fecha del reporte",
        blank=True,
        null=True,
    )
    medic_that_report = ForeignKey(
        Doctor,
        verbose_name="Médico que reporta",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    tumor = CharField(
        verbose_name="Tumor",
        choices=TumorChoices.choices,
        max_length=10,
        blank=True,
        null=True,
    )
    nodule = CharField(
        verbose_name="Nódulo",
        choices=NoduleChoices.choices,
        max_length=10,
        blank=True,
        null=True,
    )
    metastasis = CharField(
        verbose_name="Metástasis",
        choices=MetastasisChoices.choices,
        max_length=10,
        blank=True,
        null=True,
    )
    neoplasm_classification = IntegerField(
        verbose_name="Clínico o Patológico",
        blank=True,
        null=True,
        choices=NeoplasmClassificationChoices.choices,
    )
    tumor_classification = IntegerField(
        verbose_name="Clasificación",
        blank=True,
        null=True,
        choices=TumorClassificationChoices.choices,
    )
    treatment_performed = IntegerField(
        verbose_name="Tratamiento realizado",
        blank=True,
        null=True,
        choices=TreatmentPerformedChoices.choices,
    )
    group = ForeignKey(
        Group,
        verbose_name="Grupo que reporta",
        on_delete=CASCADE,
        blank=True,
        null=True,
    )
    hematological_transformation = BooleanField(
        verbose_name="Transformación hematológica", default=False
    )
    date_of_first_symptoms = DateField(
        verbose_name="Fecha de primeros síntomas",
        blank=True,
        null=True,
    )
    acute_lymphoid_leukemia = IntegerField(
        verbose_name="Leucemia linfoide aguda (FAB)",
        blank=True,
        null=True,
        choices=AcuteLymphoidLeukemiaChoices.choices,
    )
    chronic_lymphoid_leukemia = IntegerField(
        verbose_name="Leucemia linfoide crónica (Rail)",
        blank=True,
        null=True,
        choices=ChronicLymphoidLeukemiaChoices.choices,
    )
    acute_myeloid_leukemia = IntegerField(
        verbose_name="Leucemia mieloide aguda (FAB)",
        blank=True,
        null=True,
        choices=AcuteMyeloidLeukemiaChoices.choices,
    )
    multiple_myeloma = IntegerField(
        verbose_name="Mieloma múltiple (Durie-Salmon)",
        blank=True,
        null=True,
        choices=MultipleMyelomaChoices.choices,
    )
    chronic_myeloid_leukemia = IntegerField(
        verbose_name="Leucemia mieloide crónica",
        blank=True,
        null=True,
        choices=ChronicMyeloidLeukemiaChoices.choices,
    )
    objects = NeoplasmQuerysetManager()

    class Meta:
        verbose_name = "Neoplasia"
        verbose_name_plural = "Neoplasias"
        ordering = ["pk"]

    def __str__(self):
        return f"{self.patient}"
