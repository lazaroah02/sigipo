from django.db import models


class ProcedimientoChoices(models.IntegerChoices):
    PONCHE = 1, "ponche"
    CONO_POR_ASA = 2, "cono por asa"
    OTRO = 3, "otro (especifique)"
    NO_ESPECIFICADO = 4, "no especificado"


class SitioTumorChoices(models.TextChoices):
    CUADRANTE_SUPERIOR_DERECHO = (
        "CUADRANTE_SUPERIOR_DERECHO",
        "Cuadrante superior, derecho",
    )
    CUADRANTE_SUPERIOR_IZQUIERDO = (
        "CUADRANTE_SUPERIOR_IZQUIERDO",
        "Cuadrante superior, izquierdo",
    )
    CUADRANTE_INFERIOR_DERECHO = (
        "CUADRANTE_INFERIOR_DERECHO",
        "Cuadrante inferior, derecho",
    )
    CUADRANTE_INFERIOR_IZQUIERDO = (
        "CUADRANTE_INFERIOR_IZQUIERDO",
        "Cuadrante inferior, izquierdo",
    )
    NO_DETERMINADO = "NO_DETERMINADO", "No puede ser determinado (explique)"


class TipoHistologicoChoices(models.IntegerChoices):
    CARCINOMA_CELULAS_ESCAMOSAS = 1, "carcinoma de células escamosas"
    CARCINOMA_CELULAS_ESCAMOSAS_QUERATINIZANTE = (
        2,
        "carcinoma de células escamosas, queratinizante",
    )
    CARCINOMA_CELULAS_ESCAMOSAS_NO_QUERATINIZANTE = (
        3,
        "carcinoma de células escamosas, no queratinizante",
    )
    CARCINOMA_CELULAS_ESCAMOSAS_BASALOIDE = (
        4,
        "carcinoma de células escamosas, basaloide",
    )
    CARCINOMA_CELULAS_ESCAMOSAS_VERRUCOSO = (
        5,
        "carcinoma de células escamosas, verrucoso",
    )
    CARCINOMA_CELULAS_ESCAMOSAS_PAPILAR = 6, "carcinoma de células escamosas, papilar"
    CARCINOMA_CELULA_ESCAMOSAS_LYMPHOEPITHELIOMA_LIKE = (
        7,
        "carcinoma de célula escamosas, lymphoepithelioma-like",
    )
    CARCINOMA_CELULAS_ESCAMOSAS_ESCAMOTRANSICIONAL = (
        8,
        "carcinoma de células escamosas, escamotransicional",
    )
    ADENOCARCINOMA_ENDOCERVICAL_TIPO_USUAL = (
        9,
        "Adenocarcionoma endocervical, tipo usual",
    )
    CARCINOMA_MUCINOUS = 10, "Carcinoma mucinous"
    CARCINOMA_MUCINOUS_TIPO_INTESTINAL = 11, "Carcinoma mucinous, tipo intestinal"
    CARCINOMA_MUCINOUS_TIPO_CELULAS_EN_ANILLO_DE_SELLO = (
        12,
        "Carcinoma mucinous, tipo células en anillo de sello",
    )
    CARCINOMA_MUCINOUS_TIPO_GASTRICO = 13, "Carcinoma mucinous, tipo gástrico"
    CARCINOMA_VILLOGLANDULAR = 14, "Carcinoma Villoglandular"
    CARCINOMA_ENDOMETRIOIDE = 15, "Carcinoma Endometrioide"
    CARCINOMA_DE_CELULAS_CLARAS = 16, "Carcinoma de células claras"
    CARCINOMA_SEROSO = 17, "Carcinoma seroso"
    CARCINOMA_MESONEFRICO = 18, "Carcinoma Mesonefrico"
    ADENOCARCINOMA_MEZCLADO_CON_CARCINOMA_NEUROENDOCRINO = (
        19,
        "Adenocarcinoma mezclado con carcinoma neuroendocrino",
    )
    CARCINOMA_ADENOSQUAMOUS = 20, "Carcinoma Adenosquamous"
    CARCINOMA_ADENOSQUAMOUS_VARIANTE_DE_LA_CELULA_VIDRIOSA = (
        21,
        "Carcinoma Adenosquamous, variante de la célula vidriosa",
    )
    CARCINOMA_ADENOIDEO_QUISTICO = 22, "Carcinoma adenoideo quistico"
    CARCINOMA_BASAL_ADENOIDEO = 23, "Carcinoma basal adenóideo"
    CARCINOMA_NEUROENDOCRINO_DE_CELULAS_PEQUENAS = (
        24,
        "Carcinoma neuroendocrino de células pequeñas",
    )
    CARCINOMA_NEUROENDOCRINE_DE_CELULAS_GRANDES = (
        25,
        "Carcinoma neuroendocrine de células grandes",
    )
    CARCINOMA_INDIFERENCIADO = 26, "Carcinoma indiferenciado"
    CARCINOSARCOMA = 27, "Carcinosarcoma"
    OTRO_TIPO_HISTOLOGICO = (
        28,
        "otro tipo histologico que no figura en la lista (especifique)",
    )
    CARCINOMA_DE_TIPO_QUE_NO_PUEDE_SER_DETERMINADO = (
        29,
        "Carcinoma de tipo que no puede ser determinado",
    )


class GradoHistologicoChoices(models.IntegerChoices):
    G1 = 1, "Poco diferenciado"
    G2 = 2, "Moderadamente diferenciado"
    G3 = 3, "Pobremente diferenciado"
    GX = 4, "No puede ser evaluado"
    NO_SE_APLICA = 5, "No se aplica"


class MargenAfectacionChoices(models.TextChoices):
    INFILTRADO = (
        "INFILTRADO",
        "Infiltrado por carcinoma invasor. Especifique posición, si es posible:",
    )
    NEOPLASIA = "NEOPLASIA", "Neoplasia intraepithelial"
    LESION = "LESION", "Lesión escamosa (CIN 2-3)"
    ADENOCARCINOMA = "ADENOCARCINOMA", "Adenocarcinoma en situ"


class InvasionLymphovascularChoices(models.IntegerChoices):
    AUSENTE = 1, "ausente"
    PRESENTE = 2, "presente"
    NO_DETERMINADO = 3, "no determinado"


class OtraPatologiaAsociada(models.TextChoices):
    NO_IDENTIFICO = "NO_IDENTIFICO", "No identificó"
    NIC_I = "NIC_I", "NIC I"
    NIC_II = "NIC_II", "NIC II"
    INFLAMACION = "INFLAMACION", "Inflamación"
    OTRO = "OTRO", "Otro del + (especifique)"


class ReseccionChoices(models.IntegerChoices):
    AMPUTACION = 1, "Amputación"
    HISTERECTOMIA_RADICAL = 2, "Histerectomía radical"
    HISTERECTOMIA_SIMPLE = 3, "Histerectomía simple"
    EXENTERACION_PELVICA = 4, "Exenteración pélvica (especifique órganos incluidos)"
    SALPINGO_OOPHORECTOMY_BILATERAL = 5, "Salpingo-oophorectomy bilateral"
    SALPINGO_OOPHORECTOMY_DERECHA = 6, "Salpingo-oophorectomy derecha"
    SALPINGO_OOPHORECTOMY_IZQUIERDO = 7, "Salpingo-oophorectomy izquierdo"
    SALPINGO_OOPHORECTOMY_LADO_NO_ESPECIFICADO = (
        8,
        "Salpingo-oophorectomy, lado no especificado",
    )
    OOPHORECTOMIA_DERECHA = 9, "Oophorectomía derecha"
    OOPHORECTOMIA_IZQUIERDO = 10, "Oophorectomía izquierdo"
    OOPHORECTOMIA_NO_TOME_PARTIDO_ESPECIFICADO = (
        11,
        "Oophorectomía, no tome partido especificado",
    )
    SALPINGECTOMIA_BILATERAL = 12, "Salpingectomía bilateral"
    SALPINGECTOMIA_DERECHA = 13, "Salpingectomía derecha"
    SALPINGECTOMIA_IZQUIERDA = 14, "Salpingectomía izquierda"
    SALPINGECTOMIAESPECIFICADO = 15, "Salpingectomíaespecificado"
    RESECCION_VAGINAL_DEL_MUÑON = 16, "Resección vaginal del muñón"
    OMENTECTOMIA = 17, "Omentectomía"
    OTRO = 18, "Otro (especifique)"


class TipoHysterectomyChoices(models.IntegerChoices):
    ABDOMINAL = 1, "Abdominal"
    VAGINAL = 2, "Vaginal"
    VAGINAL_LAPAROSCOPICO = 3, "Vaginal, de asistencia laparoscópico"
    LAPAROSCOPIC = 4, "Laparoscopic"
    LAPAROSCOPIC_ROBOTICO = 5, "Laparoscopic, de asistencia robótico"
    OTRO = 6, "Otro del + (especifique)"
    NO_ESPECIFICADO = 7, "No especificado"


class AfectacionOtrosOrganosChoices(models.IntegerChoices):
    NO_SE_APLICA = 1, "no se aplica"
    NO_IDENTIFICADO = 2, "no identificado"
    PARAMETRIO_DERECHO = 3, "parametrio derecho"
    PARAMETRIO_IZQUIERDO = 4, "parametrio izquierdo"
    PARAMETRIO_NO_ESPECIFICADO = 5, "parametrio (no especificado)"
    VAGINA = 6, "vagina"
    VAGINA_INFERIOR = 7, "vagina, 1/3 inferior"
    VAGINA_NO_ESPECIFICADA = 8, "vagina (la posición no especificada)"
    OVARIO_DERECHO = 9, "ovario derecho"
    OVARIO_IZQUIERDO = 10, "ovario izquierdo"
    OVARIO_NO_ESPECIFICADO = 11, "ovario (no especificado)"
    TROMPA_UTERINA_DERECHA = 12, "trompa uterina derecha"
    TROMPA_UTERINA_IZQUIERDA = 13, "trompa uterina izquierda"
    TROMPA_UTERINA_NO_ESPECIFICADO = 14, "trompa uterina (no especificado)"
    PARED_PELVICA = 15, "pared pélvica"
    PARED_DE_LA_VEJIGA = 16, "pared de la vejiga"
    MUCOSA_DE_LA_VEJIGA = 17, "mucosa de la vejiga"
    PARED_RECTAL = 18, "pared rectal"
    MUCOSA_DEL_INTESTINO = 19, "mucosa del intestino"
    OMENTUM = 20, "Omentum"
    OTRO_ORGANO = 21, "otro órgano (especifique)"
    NO_PUEDE_SER_DETERMINADO = 22, "no puede ser determinado (explique)"


class InvasionLymphovascularNotaGChoices(models.IntegerChoices):
    NO_IDENTIFICADO = 1, "no identificado"
    PRESENTE = 2, "presente"
    NO_PUEDE_ESTAR_RESUELTO = 3, "no puede estar resuelto"
