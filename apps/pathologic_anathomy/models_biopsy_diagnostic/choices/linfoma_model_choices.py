from django.db import models


class EspecimenChoices(models.TextChoices):
    EL_GANGLIO_LINFATICO = "el ganglio linfático(s)", "El ganglio linfático(s)"
    NO_ESPECIFICADO_EL_PROCEDIMIENTO = (
        "no especificado el procedimiento",
        "No especificado el procedimiento",
    )
    LA_BIOPSIA = "la biopsia", "La biopsia"
    LA_RESECCION = "la resección", "La resección"
    OTRO = "otro", "Otro (especifique)"
    NO_ESPECIFICADO = "no especificado", "No especificado"


class SitioTumorChoices(models.TextChoices):
    EL_GANGLIO_LINFATICO = "el ganglio linfático(s)", "El ganglio linfático(s)"
    EL_SITIO_NO_ESPECIFICADO = "el sitio no especificado", "El sitio no especificado"


class HistologicTypeChoices(models.IntegerChoices):
    HODGKIN_LYMPHOMA = 1, "Hodgkin Lymphoma, histologic no puede ser determinado"
    CLASSIC_HODGKIN_LYMPHOMA = (
        2,
        "Linfoma de Hodgkin clásico, subtipo histológico no puede ser determinado",
    )
    PREDOMINIO_NODULAR = 3, "Linfoma de Hodgkin con predominio nodular"
    NODULAR_SCLEROSIS = 4, "Linfoma de Hodgkin esclerosis nodular"
    MIXED_CELLULARITY = 5, "Linfoma de Hodgkin clásico celularidad mixta"
    LYMPHOCYTE_RICH = 6, "Linfoma de Hodgkin clásico rico en linfocitos"
    LYMPHOCYTE_DEPLETED = 7, "Linfoma de Hodgkin con depleción linfocítica"


class PathologicTumorExtensionChoices(models.TextChoices):
    AFECTA_LA_MEDULA_OSEA = "Afecta la médula ósea", "Afecta la médula ósea"
    AFECTA_EL_SITIO_ESPECIFICO = (
        "Afecta el sitio específico",
        "Afecta el sitio específico",
    )
    AFECTA_OTRO_SITIO = "Afecta otro sitio", "Afecta otro sitio"
