from django.db import models

class TipoDeMuestraChoices(models.IntegerChoices):
    RESECCION_ENDOSCOPIC = 1, 'resección endoscopica'
    GASTRECTOMIA_PARCIAL_PROXIMAL = 2, 'gastrectomia parcial, proximal'
    GASTRECTOMIA_PARCIAL_DISTAL = 3, 'gastrectomia parcial, distal'
    GASTRECTOMIA_PARCIAL_OTRO = 4, 'gastrectomía parcial, otro (especifique)'
    GASTRECTOMIA_TOTAL = 5, 'gastrectomía total'
    OTRO = 6, 'otro (especifique)'
    NO_ESPECIFICADO = 7, 'no especificado'

class SitioTumorChoices(models.IntegerChoices):
    CARDIAS = 1, 'cardias'
    FUNDUS_PARED_ANTERIOR = 2, 'fundus(pared anterior)'
    FUNDUS_PARED_POSTERIOR = 3, 'fundus(pared posterior)'
    CUERPO_PARED_ANTERIOR = 4, 'cuerpo(pared anterior)'
    CUERPO_PARED_POSTERIOR = 5, 'cuerpo(pared posterior)'
    CUERPO_CURVATURA_MENOR = 6, 'cuerpo(curvatura menor)'
    CUERPO_CURVATURA_MAYOR = 7, 'cuerpo(curvatura mayor)'
    ANTRO_PARED_ANTERIOR = 8, 'antro(pared anterior)'
    ANTRO_PARED_POSTERIOR = 9, 'antro(pared posterior)'
    ANTRO_CURVATURA_MENOR = 10, 'antro(curvatura menor)'
    ANTRO_CURVATURA_MAYOR = 11, 'antro(curvatura mayor)'
    PILORO = 12, 'píloro'
    OTRO = 13, 'otro (especifique)'
    NO_ESPECIFICADO = 14, 'no especificado'

class TipoHistologicoChoices(models.IntegerChoices):
    ADENOCARCINOMA_INTESTINAL = 1, 'adenocarcinoma tipo intestinal'
    ADENOCARCINOMA_DIFUSO = 2, 'adenocarcinoma tipo difuso(incluye carcinoma en anillo de sello, clasificado como > 50%) celulas en anillo de sello'
    ADENOCARCINOMA_MIXTO = 3, 'adenocarcinoma tipo mixto (aproximadamente igual cantidades de intestinal y difuso)'
    ADENOCARCINOMA_TUBULAR = 4, 'adenocarcinoma tubular (intestinal) carcinoma (incluyendo carcinoma de célula en anillo de sello y otras variantes)'
    ADENOCARCINOMA_MUCINOSO = 5, 'adenocarcinoma mucinoso ( > 50% de musina)'
    ADENOCARCINOMA_PAPILAR = 6, 'adenocarcinoma papilar'
    CARCINOMA_MIXTO = 7, 'carcinoma mixto ( mezcla de glandular (/ papillary tubular) y células en anillo de sello'
    ADENOCARCINOMA_HEPATOIDE = 8, 'adenocarcinoma Hepatoide'
    CARCINOMA_CON_ESTROMA_LINFOIDE = 9, 'carcinoma con estroma linfoide (el carcinoma medular)'
    CARCINOMA_NEUROENDOCRINO_DE_CELULA_GRANDE = 10, 'carcinoma neuroendocrino de célula grande'
    CARCINOMA_NEUROENDOCRINO_DE_CELULAS_PEQUENAS = 11, 'carcinoma neuroendocrino de células pequeñas'
    CARCINOMA_NEUROENDOCRINO_POBREMENTE_DIFERENCIADO = 12, 'carcinoma Neuroendocrino (pobremente diferenciado)'
    CARCINOMA_MIXTO_ADENONEUROENDOCRINE = 13, 'carcinoma mixto adenoneuroendocrine'
    CARCINOMA_DE_CELULA_ESCAMOSA = 14, 'carcinoma de célula escamosa'
    CARCINOMA_ADENOESCAMOSO = 15, 'carcinoma Adenoescamoso'
    CARCINOMA_INDIFERENCIADO = 16, 'el carcinoma indiferenciado'
    OTRO = 17, 'otro tipo del histologico que no figura en la lista (especifique)'
    
class GradoHistologicoChoices(models.IntegerChoices):
    G1 = 1, 'G1: El bien diferenciado'
    G2 = 2, 'G2: Moderadamente diferenciado'
    G3 = 3, 'G3: Pobremente diferenciado, no diferenciado'
    OTRO = 4, 'otro (especifique)'
    GX = 5, 'GX: No puede ser evaluado'
    NO_SE_APLICA = 6, 'no se aplica'

class ExtensionTumorChoices(models.IntegerChoices):
    NINGUNA_PRUEBA = 1, 'ninguna prueba de tumor primario'
    CARCINOMA_IN_SITU = 2, 'carcinoma in situ: tumor intraepithelial sin invasión de la lámina propia, displasia severa'
    TUMOR_INV_LAMINA = 3, 'tumor invade la lámina propia'
    TUMOR_INV_MUSC_MUC = 4, 'el tumor invade la muscularis mucosae'
    TUMOR_INV_SUBMUC = 5, 'el tumor invade la submucosa'
    TUMOR_INV_MUSC_PROP = 6, 'el tumor invade la muscular propia'
    TUMOR_PENETRA_SUBSERO = 7, 'el tumor penetra en el tejido conjuntivo subseroso sin invasión del peritoneo visceral o estructuras adyacentes'
    TUMOR_INV_SEROSA = 8, 'el tumor invade la serosa (el peritoneo visceral)'
    TUMOR_INV_ADYACENTES = 9, 'el tumor invade a estructures/órganos adyacentes (especifique)'
    NO_PUEDE_EVALUAR = 10, 'no puede ser evaluado'
    
class MargenProximalChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    INVOLUCRADO_INVASIVO = 2, 'Involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_INVASIVO = 3, 'no involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_DISPLASIA = 4, 'no involucrado por displasia'
    NO_INVOLUCRADO_IN_SITU = 5, 'no involucrado por carcinoma in situ (displasia de alto grado)'
    NO_INVOLUCRADO_DISPLASIA_BAJO = 6, 'no involucrado por displasia de bajo grado'
 
class MargenDistalChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    INVOLUCRADO_INVASIVO = 2, 'Involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_INVASIVO = 3, 'no involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_DISPLASIA = 4, 'no involucrado por displasia'
    NO_INVOLUCRADO_IN_SITU = 5, 'no involucrado por carcinoma in situ (displasia de alto grado)'
    NO_INVOLUCRADO_DISPLASIA_BAJO = 6, 'no involucrado por displasia de bajo grado'
    
class MargenRadialChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    INVOLUCRADO_INVASIVO = 2, 'involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_INVASIVO = 3, 'no involucrado por carcinoma invasivo'

class OtrosMargenesGastrectomiaChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    INVOLUCRADO_INVASIVO = 2, 'involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_INVASIVO = 3, 'no involucrado por carcinoma invasivo'    
    
class MargenMucosalChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    INVOLUCRADO_INVASIVO = 2, 'involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_INVASIVO = 3, 'no involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_DISPLASIA = 4, 'no involucrado por displasia'
    INVOLUCRADO_IN_SITU = 5, 'involucrado por carcinoma in situ (displasia de alta calidad)'
    INVOLUCRADO_DISPLASIA_BAJA = 6, 'involucrado por displasia de baja calidad'
    
class MargenProfundoChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    NO_INVOLUCRADO_INVASIVO = 2, 'no involucrado por carcinoma invasivo'
    INVOLUCRADO_INVASIVO = 3, 'involucrado por carcinoma invasivo'

class OtrosMargenesREChoices(models.IntegerChoices):
    NO_EVALUADO = 1, 'no puede ser evaluado'
    INVOLUCRADO_INVASIVO = 2, 'involucrado por carcinoma invasivo'
    NO_INVOLUCRADO_INVASIVO = 3, 'no involucrado por carcinoma invasivo'    

class InvasionLinfovascularChoices(models.IntegerChoices):
    NO_IDENTIFICADO = 1, 'no identificado'
    PRESENTE = 2, 'presente'
    NO_PUEDE_RESOLVER = 3, 'no puede estar resuelto'
    
class InvasionPerineuralChoices(models.IntegerChoices):
    NO_IDENTIFICADO = 1, 'No identificado'
    PRESENTE = 2, 'Presente'
    NO_PUEDE_DETERMINAR = 3, 'No Puede Ser determinado'

class ClasificacionTumorChoices(models.IntegerChoices):
    PT = 1, "PT"
    N = 2, "N"
    M = 3, "M"