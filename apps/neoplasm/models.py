from django.db.models import IntegerChoices


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
