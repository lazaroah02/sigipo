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
    MASTECTOMIA_RADICAL_POST_NEOADYUVANCIA = 10, "Mastectomía radical post-neoadyuvancia"
    NO_ESPECIFICADA = 11, "No especificada"
    OTRAS = 12, "Otras"

class MetodoLocalizacionChoices(models.IntegerChoices):
    TUMOR_NUEVO = 1 ,"Tumor nuevo primario"
    RECURRENCIA = 2,"Recurrencia"    

class LateralidadChoices(models.IntegerChoices):
    DERECHA = 1,"Derecha"   
    IZQUIERDA = 2,"Izquierda"   
    BILATERAL = 3,"Bilateral"    

class DiagnosticoOperatorioChoices(models.IntegerChoices):
    SI = 1,"SI"     
    NO = 2,"NO"

SITIO_DEL_TUMOR_CHOICES = [
    ("CLS", "Cuadrante lateral superior"),
    ("CLI", "Cuadrante lateral inferior"),
    ("CMS", "Cuadrante medial superior"),
    ("CMI", "Cuadrante medial inferior"),
    ("CEN", "Central"),
    ("PEZ", "Pezón"),
]
class PosicionChoices(models.IntegerChoices):
    HORAS_RELOJ = 1,"Horas del Reloj"     
    NO_ESPECIFICADA = 2,"No Especificada"
    OTRAS = 3,"Otras (especificar)"

class OrientacionEspecimenChoices(models.IntegerChoices):
    MARCAJE = 1, "Marcaje y sitio al que corresponde"
    NO_ORIENTADO = 2, "No orientado" 

class TumorMacroVisibleChoices(models.IntegerChoices):
    AUSENTE = 1, "Ausente"
    PRESENTE = 2, "Presente(Indicar el Número de focos )"    

# Define una clase para representar los tipos histológicos de carcinoma
class TipoHistologicoChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    CARCINOMA_DUCTAL_INFILTRANTE_SOE = 1, "Carcinoma ductal infiltrante sin otra especificación (SOE)"
    CARCINOMA_MICRO_INFILTRANTE = 2, "Carcinoma micro-infiltrante"
    CARCINOMA_LOBULAR_INFILTRANTE = 3, "Carcinoma lobular infiltrante"
    CARCINOMA_INFILTRANTE_CON_CAMBIOS_LOBULARES = 4, "Carcinoma infiltrante con cambios lobulares"
    CARCINOMA_INFILTRANTE_CON_CAMBIOS_DUCTALES_Y_LOBULARES = 5, "Carcinoma infiltrante con cambios ductales and lobulares (“carcinoma tipo mixto”)"
    CARCINOMA_MUCINOSO = 6, "Carcinoma mucinoso"
    CARCINOMA_TUBULAR = 7, "Carcinoma tubular"
    CARCINOMA_INVASIVO_VARIANTE_TUBULO_LOBULAR = 8, "Carcinoma invasivo, variante tubulo-lobular"
    CARCINOMA_INVASIVO_CRIBRIFORME = 9, "Carcinoma invasivo cribriforme"
    CARCINOMA_INVASIVO_MICROPAPILAR = 10, "Carcinoma invasivo micropapilar"
    CARCINOMA_INVASIVO_PAPILLAR = 11, "Carcinoma invasivo papillar"
    CARCINOMA_MEDULAR = 12, "Carcinoma medular"
    CARCINOMA_INVASIVO_CON_CAMBIOS_MEDULARES = 13, "Carcinoma invasivo con cambios medulares"
    CARCINOMA_METAPLASICO = 14, "Carcinoma metaplàsico"
    CARCINOMA_ADENOESCAMOSO_DE_BAJO_GRADO = 15, "Carcinoma adenoescamoso de bajo grado"
    CARCINOMA_FIBROMATOSIS_LIKE_METAPLASTIC = 16, "Carcinoma fibromatosis-like metaplastic"
    CARCINOMA_METAPLASICO_SPINDLE_CELL_TYPE = 17, "Carcinoma metaplàsico, spindle cell type"
    CARCINOMA_METAPLASICO_TIPO_MIXTO_EPITHELIAL_Y_MESENQUIMATOSO = 18, "Carcinoma metaplàsico typo mixto epithelial and mesenquimatoso"
    CARCINOMA_INVASIVE_CON_CAMBIOS_METAPLASICO = 19, "Carcinoma Invasive con cambios metaplàsico"
    CARCINOMA_DE_CELULAS_ESCAMOSAS = 20, "Carcinoma de células escamosas"
    CARCINOMA_ADENOIDEO_QUISTICO = 21, "Carcinoma adenoideo quístico"
    CARCINOMA_INVASIVO_CON_CAMBIOS_APOCRINOS = 22, "Carcinoma invasivo con cambios apocrinos"
    CARCINOMA_INVASIVO_CON_CAMBIOS_CLEAR_CELL = 23, "Carcinoma invasivo concambios clear cell (glycogen rich)"
    CARCINOMA_INVASIVO_WITH_NEUROENDOCRINE_FEATURES = 24, "Carcinoma invasivo with neuroendocrine features"
    CARCINOMA_INVASIVE_CON_CELULAS_EN_ANILLO_DE_SELLO_FEATURES = 25, "Carcinoma invasive con células en anillo de sello features"
    CARCINOMA_SECRETOR = 26, "Carcinoma secretor"
    CARCINOMA_INVASIVE_TYPE_CANNOT_BE_DETERMINED = 27, "Carcinoma Invasive, type cannot be determined"
    CARCINOMA_INVASIVE_NO_RESIDUAL = 28, "Carcinoma invasive no residual"
    OTROS_TIPOS_HISTOLOGICOS = 29, "Otros tipos histológicos"

# Define una clase para representar la invasión linfovascular
class InvasionLinfovascularChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NOT_IDENTIFICADA = 1, "Not identificada"
    PRESENTE = 2, "Presente"
    NO_PUDO_SER_DETERMINADA = 3, "No pudo ser determinada"
    
# Define una clase para representar la invasión lymphovascular dérmica
class InvasionLymphovascularDermicaChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    PIEL_NO_PRESENTE = 1, "Piel no presente"
    NO_IDENTIFICADA = 2, "No identificada"
    PRESENTE = 3, "Presente"
    NO_PUDO_SER_DETERMINADA = 4, "No pudo ser determinada"

# Define una clase para representar la necrosis
class NecrosisChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NOT_IDENTIFIED = 1, "Not identified"
    PRESENTE_FOCAL = 2, "Presente, focal (foco pequeños o necrosis celular aislada)"
    PRESENTE_CENTRAL = 3, "Presente, central (necrosis expansive “comedo”)"

# Define una clase para representar la fibrosis intratumoral
class FibrosisIntratumoralChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_IDENTIFICADA = 1, "No identificada"
    PRESENTE = 2, "Presente"
    SOSPECHOSA = 3, "Sospechosa"
    
# Define una clase para representar la desmoplasia intratumoral
class DesmoplasiaIntratumoralChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_IDENTIFICADA = 1, "No identificada"
    PRESENTE = 2, "Presente"
    SOSPECHOSA = 3, "Sospechosa"
   
# Define una clase para representar el infiltrado mononuclear intratumoral
class InfiltradoMononuclearIntratumoralChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    AUSENTE = 1, "Ausente"
    PRESENTE = 2, "Presente"
    SOSPECHOSA = 3, "Sospechosa"
    OTRO_TIPO = 4, "Otro tipo celular (especificar)"
    
# Define una clase para representar el infiltrado mononuclear peritumoral
class InfiltradoMononuclearPeritumoralChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    AUSENTE = 1, "Ausente"
    PRESENTE = 2, "Presente"
    SOSPECHOSA = 3, "Sospechosa"
    OTRO_TIPO = 4, "Otro tipo celular (especificar)"
    
# Define una clase para representar la presencia de carcinoma ductal in situ (DCIS)
class PresenciaDCISChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_DCIS_EN_LA_MUESTRA = 1, "No DCIS en la muestra"
    DCIS_PRESENTE_NEGATIVE_EIC = 2, "DCIS presente.Negative for extensive intraductal component (EIC)"
    DCIS_PRESENTE_POSITIVE_EIC = 3, "DCIS presente.Positive for EIC"
    DCIS_PRESENTE_DESPUES_TTO = 4, "DCIS presente.Solo presente después de tto presurgical (neoadjuvant)"

from django.db import models

PATRON_ARQUITECTURAL_CHOICES = [
    ("COMEDO", "Comedo"),
    ("PAGET", "Enfermedad de Paget (DCIS involving nipple skin)"),
    ("CRIBRIFORME", "Cribriforme"),
    ("MICROPAPILAR", "Micropapilar"),
    ("PAPILAR", "Papilar"),
    ("SOLIDO", "Sólido"),
    ("OTROS", "Otros (especificar)"),
]

# Define una clase para representar el grado del carcinoma
class GradoChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    GRADO_I = 1, "Grado I (low)"
    GRADO_II = 2, "Grado II (intermediate)"
    GRADO_III = 3, "Grado III (high)"

# Define una clase para representar la extensión tumoral a la piel
class ExtensionTumoralPielChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    INVADE_DIRECTAMENTE_SIN_ULCERACION = 1, "Invade directamente la dermis o epidermis sin ulceración"
    INVADE_DIRECTAMENTE_CON_ULCERACION = 2, "Invade directamente la dermis o epidermis con ulceración"
    PRESENCIA_DE_FOCOS_SATELITES = 3, "Presencia de focos satélites"
    
# Define una clase para representar los márgenes del carcinoma
class MargenesChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_PUEDEN_SER_EVALUADOS = 1, "No pueden ser evaluados"
    NO_AFECTADOS = 2, "No afectados"
    POSITIVE_PARA_CARCINOMA_INVASIVO = 3, "Positive para carcinoma invasivo"

# Define una clase para representar los márgenes con CDIS
class MargenesCDISChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_PUEDEN_SER_EVALUADOS = 1, "No pueden ser evaluados"
    NO_CDIS_EN_LA_MUESTRA = 2, "No CDIS en la muestra"
    POSITIVE_PARA_CDIS = 3, "Positive para CDIS"
    
# Define una clase para representar la extensión extraganglionar
class ExtensionExtraganglionarChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_IDENTIFICADA = 1, "No identificada"
    PRESENTE = 2, "Presente"
    NO_PUEDE_SER_DETERMINADA = 3, "No puede ser determinada"
   
# Define una clase para representar los efectos del tratamiento en el tumor
class EfectosTratamientoChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    TRATAMIENTO_PRE_QUIRURGICO_NO_CONOCIDO = 1, "Tratamiento pre quirúrgico no conocido"
    NO_SE_DEFINE_RESPUESTA_A_TRATAMIENTO_PRE_QUIRURGICO = 2, "No se define respuesta a tratamiento pre quirúrgico"
    RESPUESTA_PROBABLE_O_DEFINIDA_A_TRATAMIENTO_PRE_QUIRURGICO = 3, "Respuesta probable o definida a tratamiento pre quirúrgico"
    NO_CARCINOMA_RESIDUAL_INVASOR_LUEGO_DE_TRATAMIENTO_PRE_QQCO = 4, "No carcinoma residual invasor luego de tratamiento pre qqco"
    
# Define una clase para representar los efectos del tratamiento en los GL
class EfectosTratamientoGLChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    NO_EXERESIS_DE_GL = 1, "No exéresis de GL."
    NO_SE_DEFINE_RESPUESTA_A_TTO_PRE_QUIRURGICO = 2, "No se define respuesta a tto pre quirúrgico"
    RESPUESTA_PROBABLE_O_DEFINIDA_RESPONSE_A_TTO_PRE_QUIRURGICO = 3, "Respuesta probable o definida response a tto pre quirúrgico"
    NO_GL_METASTASICOS_CICATRIZ_FIBROSA_POSIBLEMENTE_EN_RELACION_CON_METASTASIS_CON_RESPUESTA_PATOLOGICA_COMPLETA = 4, "No GL metastásicos. Cicatriz fibrosa posiblemente en relación con metástasis con respuesta patológica completa."
    NO_GL_METASTASICOS_Y_NO_CICATRIZ_FIBROSA = 5, "No GL metastásicos y no cicatriz fibrosa"
    
# Define una clase para representar el efecto del tratamiento
class EfectoTratamientoRealizadoChoices(models.IntegerChoices):
    # Define las opciones del modelo usando el formato (valor, etiqueta)
    SIN_RESPUESTA = 1, "Sin respuesta"
    RESPUESTA_PARCIAL = 2, "Respuesta parcial"
    RESPUESTA_COMPLETA = 3, "Respuesta completa"
    