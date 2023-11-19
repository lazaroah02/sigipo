from django.db import models


class TipoDeMuestraChoices(models.IntegerChoices):
    BIOPSIA_CON_AGUJA_DE_CORTE = 1, "Biopsia con aguja de corte"
    BIOPSIA_POR_ESTEREOTAXIA = 2, "Biopsia por estereotaxia"
    BIOPSIA_GUIADA_POR_ARPON = 3, "Biopsia guiada por arpón"
    BIOPSIA_EXCISIONAL_NODULECTOMIA = 4, "Biopsia excisional Nodulectomía"
    BIOPSIA_EXCISIONAL_PARCIAL = 5, "Biopsia excisional Mastectomía parcial"
    BIOPSIA_EXCISIONAL_CUADRANTECTOMIA = 6, "Biopsia excisional Cuadrantectomía"
    BIOPSIA_EXCISIONAL_SEGMENTECTOMIA = 7, "Biopsia excisional Segmentectomía"
    RE_ESCISION = 8, "Re-escisión"
    MASTECTOMIA_RADICAL = 9, "Mastectomía radical"
    MASTECTOMIA_RADICAL_POST_NEOADYUVANCIA = (
        10,
        "Mastectomía radical post-neoadyuvancia",
    )
    NO_ESPECIFICADA = 11, "No especificada"
    OTRAS = 12, "Otras"


class MetodoLocalizacionChoices(models.IntegerChoices):
    TUMOR_NUEVO = 1, "Tumor nuevo primario"
    RECURRENCIA = 2, "Recurrencia"


class HistoriaClinicaActualChoices(models.TextChoices):
    MASA_PALPABLE = "MP", "Masa palpable"
    HALLAZGOS_RADIOLOGICOS = "HR", "Hallazgos Radiológicos"
    HALLAZGOS_RADIOLOGICOS_MASA_O_DISTORSION = (
        "MD",
        "Hallazgos Radiológicos. Masa o distorsión arquitectural",
    )
    HALLAZGOS_RADIOLOGICOS_CALCIFICACIONES = (
        "CA",
        "Hallazgos Radiológicos. Calcificaciones",
    )
    HALLAZGOS_RADIOLOGICOS_OTRA_HR = "OH", "Hallazgos Radiológicos otros"
    DESCARGA_POR_EL_PEZON = "DP", "Descarga por el Pezón"
    OTRA_HISTORIA = "OT", "Otra"
    HISTORIA_PREVIA = "HP", "Historia previa de cáncer de mama"


class IdentificacionDeLaMuestraChoices(models.IntegerChoices):
    EXCISIONAL = 0, "Excisional"
    MASTECTOMIA_TOTAL = 1, "Mastectomía total"
    NO_ESPECIFICADA = 2, "No especificada"
    OTRA = 3, "Otra (especificar)"


class LateralidadChoices(models.IntegerChoices):
    DERECHA = 0, "Derecha"
    IZQUIERDA = 1, "Izquierda"
    BILATERAL = 2, "Bilateral"
    NO_ESPECIFICADA = 3, "No especificada"


class SitioTumorChoices(models.TextChoices):
    CUADRANTE_LATERAL_SUPERIOR = "CLS", "Cuadrante lateral superior"
    CUADRANTE_LATERAL_INFERIOR = "CLI", "Cuadrante lateral inferior"
    CUADRANTE_MEDIAL_SUPERIOR = "CMS", "Cuadrante medial superior"
    CUADRANTE_MEDIAL_INFERIOR = "CMI", "Cuadrante medial inferior"
    CENTRAL = "CEN", "Central"
    PEZON = "PEZ", "Pezón"


class PosicionChoices(models.IntegerChoices):
    HORAS_DEL_RELOJ = 0, "Horas del reloj"
    NO_ESPECIFICADA = 1, "No especificada"
    OTRAS = 2, "Otras (especificar)"


class PatronArquitecturalChoices(models.TextChoices):
    COMEDO = "COMEDO", "Comedo"
    PAGET = "PAGET", "Paget disease"
    CRIBRIFORME = "CRIBRIFORME", "Cribriform"
    MICROPAPILAR = "MICROPAPILAR", "Micropapillary"
    PAPILAR = "PAPILAR", "Papillary"
    SOLIDO = "SOLIDO", "Solid"
    OTRO = "OTRO", "Otro (especificar)"


class GradoNuclearChoices(models.IntegerChoices):
    GRADO_I = 0, "Grado I (bajo)"
    GRADO_II = 1, "Grado II (intermedio)"
    GRADO_III = 2, "Grado III (alto)"


class HeterogeneidadGradoNuclearChoices(models.IntegerChoices):
    AUSENTE = 1, "Ausente"
    PRESENTE_BAJA = 2, "Presente - Baja"
    PRESENTE_INTERMEDIA = 3, "Presente - Intermedia"
    PRESENTE_ALTA = 4, "Presente - Alta"


class NecrosisChoices(models.IntegerChoices):
    NO_IDENTIFICADA = 0, "No identificada"
    PRESENTE_FOCAL = 1, "Presente, focal"
    PRESENTE_CENTRAL = 2, "Presente, central"


class Microcalcificaciones1Choices(models.IntegerChoices):
    AUSENTE = 1, "Ausente"
    PRESENTE_CDIS = 2, "Presente en el propio CDIS"
    PRESENTE_TEJIDO_BENIGNO = 3, "Presente en tejido benigno"


class EnfermedadPagetChoices(models.IntegerChoices):
    AUSENTE = 1, "Ausente"
    PRESENTE = 2, "Presente"


class NeoplasiaLobularChoices(models.IntegerChoices):
    AUSENTE = 1, "Ausente"
    PRESENTE_CLASICA = 2, "Presente - Clásica"
    PRESENTE_VARIANTE = 3, "Presente - Variante"
    PRESENTE_MARGEN = 4, "Presente en el margen"


class MargenesChoices(models.TextChoices):
    NO_PUEDE_SER_EVALUADO = "NPE", "No puede ser evaluado"
    POSITIVO_PARA_CDIS = "PPC", "Positivo para CDIS"
    POSITIVO_PARA_CDI = "PPD", "Positivo para CDI"
    POSITIVO_PARA_CDIS_Y_CDI = "PPY", "Positivo para CDIS y CDI"
    NO_AFECTADO_POR_CDIS = "NAP", "No afectado por CDIS"


class MargenEspecificadoChoices(models.IntegerChoices):
    POSITIVO_CDIS = 1, "Positivo para CDIS"
    NO_DETERMINADO = 2, "No determinado"


class GangliosLinfaticosRegionalesChoices(models.IntegerChoices):
    NO_ENVIADOS = 1, "No enviados"
    NO_IDENTIFICADOS = 2, "No identificados"


class ExtensionExtraganglionarChoices(models.IntegerChoices):
    NO_IDENTIFICADA = 0, "No identificada"
    PRESENTE = 1, "Presente"
    NO_PUEDE_SER_DETERMINADA = 2, "No puede ser determinada"


class Microcalcificaciones2Choices(models.TextChoices):
    NO_IDENTIFICADA = "NI", "No identificada"
    PRESENTE_EN_CDIS = "PC", "Presente en CDIS"
    PRESENTE_EN_TEJIDO_NO_NEOPLASICO = "PN", "Presente en tejido no neoplásico"
    OTRO = "OT", "Otro (especificar)"
