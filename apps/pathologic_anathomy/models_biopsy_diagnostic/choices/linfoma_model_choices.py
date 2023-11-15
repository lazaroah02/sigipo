from django.db import models

ESPECIMEN_CHOICES = [
    ("el ganglio linfático(s)", "El ganglio linfático(s)"),
    ("otro", "Otro (especifique)"),
    ("no especificado el procedimiento", "No especificado el procedimiento"),
    ("la biopsia", "La biopsia"),
    ("la resección", "La resección"),
    ("otro (especifique)", "Otro (especifique)"),
    ("no especificado", "No especificado"),
]

SITIO_TUMOR_CHOICES = [
    ("el ganglio linfático(s)", "El ganglio linfático(s)"),
    ("el sitio no especificado", "El sitio no especificado"),
]


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


PATHOLOGIC_TUMOR_EXTENSIONS = [
    ("Afecta la médula ósea", "Afecta la médula ósea"),
    ("Afecta el sitio específico", "Afecta el sitio específico"),
    ("Afecta otro sitio", "Afecta otro sitio"),
]
