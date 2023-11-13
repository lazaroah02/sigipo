from django.db.models import IntegerChoices

class TipoMuestraTiroidesChoice(IntegerChoices):
    """Define el tipo de muestra de tiroides"""

    completamiento = 1, "Completamiento de tiroidectomía"
    excision_parcial_derecha = 2, "Excisión parcial derecha"
    excision_parcial_izquierda = 3, "Excisión parcial izquierda"
    excision_parcial_otro = 4, "Excisión parcial (especifique tipo, si es posible)"
    lobectomia_derecha = 5, "Lobectomía derecha"
    lobectomia_izquierda = 6, "Lobectomía izquierda"
    lobectomia_derecha_istmectomia = 7, "Lobectomía derecha con istmectomía (hemitiroidectomía)"
    lobectomia_izquierda_istmectomia = 8, "Lobectomía izquierda con istmectomía (hemitiroidectomía)"
    lobulo_derecho_lobectomia_parcial_izquierda = 9, "Lóbulo derecho con lobectomía parcial izquierda (tiroidectomía subtotal o casi total)"
    lobulo_izquierdo_lobectomia_parcial_derecha = 10, "Lóbulo izquierdo con lobectomía parcial derecha (tiroidectomía subtotal o casi total)"
    tiroidectomia_total = 11, "Tiroidectomía total"

class FocalidadTumorChoice(IntegerChoices):
    """Define la focalidad del tumor"""

    unifocal = 1, "Unifocal"
    multifocal = 2, "Multifocal"
    indeterminado = 3, "No puede ser determinado"

SITIO_TUMOR_CHOICES = [
        ("lobulo_derecho", "El lóbulo derecho"),
        ("lobulo_izquierdo", "El lóbulo izquierdo"),
        ("istmo", "El istmo"),
        ("lobulo_piramidal", "El lóbulo piramidal"),
        ("otro", "Otro (especifique)"),
    ]

class CarcinomaPapilarChoice(IntegerChoices):
    """Define el carcinoma papilar"""

    clasico = 1, "Carcinoma Papilar, Clásico (usual, convencional)"
    variante_folicular_encapsulado_invasivo = 2, "Carcinoma Papilar, variante folicular, encapsulado / bien delimitado, con invasión tumoral a la capsula"
    variante_folicular_encapsulado_noinvasivo = 3, "Carcinoma Papilar, variante folicular, encapsulado / bien delimitado, no-invasivo"
    variante_folicular_infiltrativo = 4, "Carcinoma Papilar, variante folicular, infiltrativo"
    variante_celulas_altas = 5, "Carcinoma Papilar, variante de células alta"
    variante_morular_cribiforme = 6, "Carcinoma Papilar, variante morular cribiforme"
    variante_esclerosis_difusa = 7, "Carcinoma Papilar, variante de esclerosis difusa"
    otra_variante = 8, "Carcinoma Papilar, otra variante (especifique)"
    carcinoma_papilar = 9, "Carcinoma Papilar"
    neoplasia_folicular_noinvasiva = 10, "Neoplasia tiroidea folicular na invasiva con caracteres nucleares similares al papilar"

class CarcinomaFolicularChoice(IntegerChoices):
    """Define el tipo de carcinoma folicular"""

    folicular_minimamente_invasivo = 1, "Carcinoma folicular, minimamente invasivo"
    folicular_angioinvasivo_encapsulado = 2, "Carcinoma folicular, angioinvasivo encapsulado"
    folicular_ampliamente_invasivo = 3, "Carcinoma folicular, ampliamente invasivo"
    folicular_minimamente_invasivo_oncocitico = 4, "Carcinoma folicular, minimamente invasivo, oncocítico (células de Hürthle)"
    folicular_angioinvasivo_encapsulado_oncocitico = 5, "Carcinoma folicular, angioinvasivo encapsulado, oncocítico (células de Hürthle)"
    folicular_ampliamente_invasivo_oncocitico = 6, "Carcinoma folicular, ampliamente invasivo, oncocítico (células de Hürthle)"
    folicular_minimamente_invasivo_otra_variante = 7, "Carcinoma folicular, minimamente invasivo, otra variante (especifique)"
    folicular_angioinvasivo_encapsulado_otra_variante = 8, "Carcinoma folicular, angioinvasivo encapsulado, otra variante (especifique)"
    folicular_ampliamente_invasivo_otra_variante = 9, "Carcinoma folicular, ampliamente invasivo, otra variante (especifique)"
    folicular = 10, "Carcinoma folicular"
    tiroideo_pobremente_diferenciado = 11, "Carcinoma tiroideo pobremente diferenciado"
    indiferenciado_focal = 12, "Carcinoma indiferenciado (anaplásico), con un componente focal o menor, sin extensión extra tiroidea"
    indiferenciado_mayor = 13, "Carcinoma indiferenciado (anaplásico), con un componente mayor"
    indiferenciado_no_especificado = 14, "Carcinoma indiferenciado (anaplásico), no especificado en otra forma"
    medular = 15, "Carcinoma medular"
    indeterminado = 16, "Carcinoma, el tipo no puede ser determinado"
    otro = 17, "Otro tipo del histológico que no figura en la lista (especifique)"

class MargenesChoice(IntegerChoices):
    """Define los márgenes"""

    no_evaluado = 1, "No puede ser evaluado"
    no_invadido = 2, "No invadido por el carcinoma"
    invadido = 3, "Invadido por el carcinoma"

class InvasionVascularChoice(IntegerChoices):
    """Define la invasión vascular"""

    no_identificado = 1, "No identificado"
    presente = 2, "Presente"
    no_determinado = 3, "No puede ser determinado"
    focal = 4, "Focal (menos de 4 vasos)"
    extensa = 5, "Extensa (4 o más vasos)"

class InvasionLinfaticaChoice(IntegerChoices):
    """Define la invasión linfática"""

    no_identificado = 1, "No identificado"
    presente = 2, "Presente"
    no_determinado = 3, "No puede ser determinado"

class InvasionPerineuralChoice(IntegerChoices):
    """Define la invasión peri-neural"""

    no_identificado = 1, "No identificado"
    presente = 2, "Presente"
    no_determinado = 3, "No puede ser determinado"

class ExtensionExtratiroideaChoice(IntegerChoices):
    """Define la extensión extra-tiroidea"""

    no_identificado = 1, "No identificado"
    presente = 2, "Presente"
    no_determinado = 3, "No puede ser determinado"

class ExtensionChoices(IntegerChoices):
    muscular = 1, "Invade solamente las bandas musculares (ie, pT3b)" 
    subcutaneo = 2, "Invade tejidos celular subcutáneo, laringe, tráquea, esófago o nervio laríngeo recurrente (ie, PT4a)"
    vascular = 3, "Invadiendo la fascia pre-vertebral o recubriendo la arteria carótida o los vasos mediastinales (ie,pT4b)"

NIVELES_GANGLIONARES_CHOICES = [
    ("nivel_Vi", "Nivel VI: pre- traqueal, para- traqueal y pre-laríngeo/Delphian, peri-tiroideos (disección del compartimiento central)"),
    ("nivel_VII", "Nivel VII (los ganglios linfáticos mediastinales superiores)"),
    ("nivel_IV_derecho", "Nivel I-V (disección lateral del cuello) Derecho"),
    ("nivel_IV_izquierdo", "Nivel I-V (disección lateral del cuello) Izquierda"),
]
    


