from django.db import models


class TipoMuestraChoices(models.IntegerChoices):
    RESECCION_ENDOSCOPICA = 1, "Resección Endoscópica"
    ESOPHAGECTOMIA = 2, "Esophagectomía"
    ESOPHAGOGASTRECTOMIA = 3, "Esophagogastrectomía"
    OTRO = 4, "otro (especifique):"
    NO_ESPECIFICADO = 5, "no especificado"


class SitioTumorChoices(models.IntegerChoices):
    ESOFAGO_CERVICAL = 1, "Esófago cervical (proximal)"
    MEDIO_ESOFAGO_SUPERIOR = 2, "Medio esófago, el superior esófago torácico"
    MEDIO_ESOFAGO_INTERMEDIO = 3, "Medio esófago, el intermedio esófago torácico"
    MEDIO_ESOFAGO_NO_ESPECIFICADO = 4, "Medio esófago, no especificado en otra forma"
    ESOFAGO_DISTAL = 5, "Esófago distal ( esófago torácico)"
    UNION_ESOFAGOGASTRICA = 6, "Unión Esophagogastrica (EGJ)"
    ESTOMAGO_CARDIAS_PROXIMAL = 7, "Estómago /cardias Proximal"
    OTRO = 8, "otro (especifique):"
    ESOFAGO_NO_ESPECIFICADO = 9, "El esófago, no especificado en otra forma"


class RelacionTumorUnionChoices(models.IntegerChoices):
    TUBULAR = (
        1,
        "el tumor está enteramente ubicado dentro del esófago tubular y no involucra la unión esophagogastrica",
    )
    DISTAL = (
        2,
        "el punto medio del tumor yace en el esófago del distal y el tumor involucra la unió esophagogastrica",
    )
    UNION = 3, "el punto medio del tumor está localizado en la unión esophagogastrica"
    PROXIMAL = (
        4,
        "el punto medio del tumor es 2 cm o menos en el estómago  proximal o el cardias y el tumor involucra la unión esophagogastrica",
    )
    NO_ESPECIFICADO = 5, "no especificado"
    NO_EVALUADO = 6, "no puede ser evaluado"

class TipoHistologiaChoices(models.IntegerChoices):
    ADENOCARCINOMA = 1, "Adenocarcinoma"
    CARCINOMA_ADENOIDEO_QUISTICO = 2, "Carcinoma  adenóideo quistito"
    CARCINOMA_MUCOEPIDERMICO = 3, "Carcinoma Mucoepidermoide"
    CARCINOMA_MIXTO_ADENONEUROENDOCRINO = 4, "Carcinoma mixto  adenoneuroendocrino"
    CARCINOMA_INDIFERENCIADO_GLANDULAR = (
        5,
        "Carcinoma indiferenciado con componente glandular",
    )
    CARCINOMA_CELULA_ESCAMOSO = 6, "Carcinoma de  célula escamoso"
    CARCINOMA_CELULA_ESCAMOSO_BASALOIDE = 7, "Carcinoma de la célula escamoso Basaloide"
    CARCINOMA_ADENOESCAMOSO = 8, "Carcinoma Adenoescamoso"
    CARCINOMA_CELULAS_FUSIFORME = 9, "Carcinoma de celulas fusiforme (escamoso)"
    CARCINOMA_VERRUCOSO = 10, "Carcinoma Verrucoso (escamoso)"
    CARCINOMA_INDIFERENCIADO_ESCAMOSO = (
        11,
        "Carcinoma indiferenciado con componente escamoso",
    )
    CARCINOMA_INDIFERENCIADO = 12, "Carcinoma indiferenciado"
    CARCINOMA_NEUROENDOCRINO_CELULA_GRANDE = (
        13,
        "Carcinoma  neuroendocrino de  célula grande",
    )
    CARCINOMA_NEUROENDOCRINO_CELULA_PEQUENAS = (
        14,
        "Carcinoma neuroendocrino de  célula pequeñas",
    )
    CARCINOMA_NEUROENDOCRINO_POBREMENTE_DIFERENCIADO = (
        15,
        "Carcinoma Neuroendocrino (pobremente diferenciado)",
    )
    OTRO = 16, "Otro tipo  histológico que no figura en la lista (especifique):"
    CARCINOMA_NO_DETERMINADO = 17, "Carcinoma, el tipo no puede ser determinado"


class GradoHistologicoChoices(models.IntegerChoices):
    G1 = 1, "G1: Bien diferenciado"
    G2 = 2, "G2: Moderadamente diferenciado"
    G3 = 3, "G3: Pobremente diferenciado, no diferenciado"
    GX = 4, "GX: No puede ser evaluado"
    
class TumorExtensionChoices(models.IntegerChoices):
    NINGUNA = 1, "Ninguna evidencia de tumor primario"
    DISPLASIA = (
        2,
        "displasia de alto grado/  carcinoma  in situ, definido como  células cancerosas confinaron al epitelio sin atravesar membrana basal",
    )
    LAMINA = 3, "el tumor invade la lámina  propia"
    MUSCULARIS = 4, "el tumor invade la muscularis mucosae"
    SUBMUCOSA = 5, "el tumor invade la submucosa"
    MUSCULAR = 6, "el tumor invade la muscular propia"
    ADVENTICIA = 7, "el tumor invade la adventicia"
    ADYACENTES = 8, "el tumor invade  estructuras/órgano # adyacentes (especifique):"
    NO_EVALUADO = 9, "no puede ser evaluado"


class MargenProximalChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    INVOLUCRADO_INVASIVO = 2, "involucrado por carcinoma invasivo"
    NO_INVOLUCRADO_INVASIVO = 3, "no involucrado por carcinoma invasivo"
    INVOLUCRADO_DISPLASIA = 4, "involucrado por displasia"
    INVOLUCRADO_DISPLASIA_ESCAMOSA_BAJO = (
        5,
        "involucrado por displasia escamosa de bajo grado",
    )
    INVOLUCRADO_DISPLASIA_ESCAMOSA_ALTO = (
        6,
        "involucrado por displasia escamosa de alto grado",
    )
    INVOLUCRADO_DISPLASIA_GLANDULAR_BAJO = (
        7,
        "involucrado por displasia glandular de bajo grado",
    )
    INVOLUCRADO_DISPLASIA_GLANDULAR_ALTO = (
        8,
        "involucrado por displasia glandular de alto grado",
    )
    INVOLUCRADO_METAPLASIA_INTESTINAL = (
        9,
        "involucrado por metaplasia intestinal (el esófago Barrett) sin displasia",
    )


class MargenDistalChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    INVOLUCRADO_INVASIVO = 2, "involucrado por carcinoma invasivo"
    NO_INVOLUCRADO_INVASIVO = 3, "no involucrado por carcinoma invasivo"
    INVOLUCRADO_DISPLASIA = 4, "involucrado por displasia"
    INVOLUCRADO_DISPLASIA_ESCAMOSA_BAJO = (
        5,
        "involucrado por displasia escamosa de bajo grado",
    )
    INVOLUCRADO_DISPLASIA_ESCAMOSA_ALTO = (
        6,
        "involucrado por displasia escamosa de alto grado",
    )
    INVOLUCRADO_DISPLASIA_GLANDULAR_BAJO = (
        7,
        "involucrado por displasia glandular de bajo grado",
    )
    INVOLUCRADO_DISPLASIA_GLANDULAR_ALTO = (
        8,
        "involucrado por displasia glandular de alto grado",
    )
    INVOLUCRADO_METAPLASIA_INTESTINAL = (
        9,
        "involucrado por metaplasia intestinal (el esófago Barrett) sin displasia",
    )


class MargenRadialChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    NO_INVOLUCRADO_INVASIVO = 2, "no involucrado por carcinoma invasivo"
    INVOLUCRADO_INVASIVO = 3, "involucrado por carcinoma invasivo"

class OtrosMargenesEsophagectomiaEsophagogastrectomiaChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    NO_INVOLUCRADO_INVASIVO = 2, "no involucrado por carcinoma invasivo"
    INVOLUCRADO_INVASIVO = 3, "involucrado por carcinoma invasivo"


class MargenMucosalChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    INVOLUCRADO_INVASIVO = 2, "involucrado por carcinoma invasivo"
    NO_INVOLUCRADO_INVASIVO = 3, "no involucrado por carcinoma invasivo"
    INVOLUCRADO_DISPLASIA = 4, "involucrado por displasia"
    INVOLUCRADO_DISPLASIA_ESCAMOSO_BAJO = (
        5,
        "involucrado por displasia escamoso de bajo grado",
    )
    INVOLUCRADO_DISPLASIA_ESCAMOSO_ALTO = (
        6,
        "involucrado por displasia escamoso de alto grado",
    )
    INVOLUCRADO_DISPLASIA_GLANDULAR_BAJO = (
        7,
        "involucrado por displasia glandular de bajo grado",
    )
    INVOLUCRADO_DISPLASIA_GLANDULAR_ALTO = (
        8,
        "involucrado por displasia glandular de alto grado",
    )
    INVOLUCRADO_METAPLASIA_INTESTINAL = (
        9,
        "involucrado por metaplasia intestinal (el esófago Barrett) sin displasia",
    )


class MargenProfundoChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    NO_INVOLUCRADO_INVASIVO = 2, "No involucrado por carcinoma invasivo"
    INVOLUCRADO_INVASIVO = 3, "involucrado por carcinoma invasivo"


class OtrosMargenesReseccionEndoscopicaChoices(models.IntegerChoices):
    NO_EVALUADO = 1, "no puede ser evaluado"
    NO_INVOLUCRADO_INVASIVO = 2, "no involucrado por carcinoma invasivo"
    INVOLUCRADO_INVASIVO = 3, "involucrado por carcinoma invasivo"


class InvasionLinfovascularChoices(models.IntegerChoices):
    NO_IDENTIFICADO = 1, "No identificado"
    PRESENTE = 2, "presente"
    NO_RESUELTO = 3, "no puede estar resuelto"


class InvasionPerineuralChoices(models.IntegerChoices):
    NO_IDENTIFICADO = 1, "No identificado"
    PRESENTE = 2, "presente"
    NO_RESUELTO = 3, "no puede estar resuelto"


class ClasificacionTumorChoices(models.IntegerChoices):
    PT = 1, "PT"
    N = 2, "N"
    M = 3, "M"
