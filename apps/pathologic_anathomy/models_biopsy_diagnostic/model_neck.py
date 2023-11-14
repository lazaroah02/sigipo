from django.db import models
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import neck_model_choices

class NeckBiopsyDiagnostic(models.Model):
    biopsy = models.OneToOneField("pathologic_anathomy.BiopsyRequest", on_delete=models.CASCADE)
    #A.	Información clínica recibida en el departamento de Anatomía Patológica.
    
    #Tipo de muestra
    tipo_muestra = models.IntegerField(
        choices=neck_model_choices.TipoMuestraChoices.choices,
        verbose_name = "Tipo de Muestra",
    )
    tipo_muestra_otro = models.CharField(
        max_length=5000,
        verbose_name = "Otro tipo de muestra (especifique)",
        blank = True,
        null=True,
    )
    
    #Sitio del Tumor
    sitio_tumor = models.IntegerField(
        choices=neck_model_choices.SitioTumorChoices.choices,
        verbose_name = "Sitio del Tumor",
    )
    sitio_tumor_otro = models.CharField(
        max_length=5000,
        verbose_name = "Otro sitio del tumor (especifique)",
        blank = True,
        null=True,
    )
    
    #Relación de Tumor con la unión Esophagogastric 
    relacion_tumor_union = models.IntegerField(
        choices = neck_model_choices.RelacionTumorUnionChoices.choices,
        verbose_name = "Relación de Tumor con la unión Esophagogastric",
    )
    distancia_centro_tumor_union = models.FloatField(
        verbose_name='''
            El protocolo de cáncer del estómago si ya sea: 
            (1) el tumor involucrara el EGJ, pero el punto medio es más que 2 cm del estómago proximal o 
            (2) el punto medio está menos de 2 cm del estómago proximal, pero el tumor no involucra al EGJ. 
            La distancia de centro del tumor a la unión esophagogastric (especifique, si aplicable) (los centímetros)
        ''',
        blank=True,
        null = True
    )
    
    #El Tamaño del Tumor
    tumor_max_size = models.FloatField(
        verbose_name="La Máxima Dimensión del Tumor (centímetros)",
    )
    tumor_size = models.FloatField(
        verbose_name="La Dimensión del Tumor (centímetros)",
    )
    no_puede_aplicable = models.CharField(
        max_length=5000,
        verbose_name = "No puede aplicable (explique): ",
        blank = True,
        null=True,
    )
    
    #El Tipo del Histología
    tipo_histologia = models.IntegerField(
        choices = neck_model_choices.TipoHistologiaChoices.choices,
        verbose_name="Tipo Histología. Nota: Seleccione esta opción sólo si el de células grande o célula pequeña no puede ser determinada",
        blank= True,
        null = True
    )
    
    #Grado Histológico
    grado_histolico = models.IntegerField(
        choices = neck_model_choices.GradoHistologicoChoices.choices,
        verbose_name='''Grado Histológico (El grado grado histológico no es aplicable para el carcinoma adenoideo quistito, 
            mucoepidermoide, el bien diferenciado, el tumor neuroendocrino y el carcinoma neuroendocrino). 
            ''',
        blank= True,
        null = True,
    )
    
    #La Extensión del Tumor 
    tumor_extension = models.IntegerField(
        choices = neck_model_choices.TumorExtensionChoices.choices,
        verbose_name='''La Extensión del Tumor. Nota: Las estructuras adyacentes del esófago incluyen la pleura, 
            el pericardio, la vena ácigos, el diafragma, el peritoneo, la aorta, cuerpo vertebral, y la vía aérea''',
    )
    
    #LOS MARGENES 
    todos_los_margenes_involucrados = models.BooleanField(
        verbose_name = ''' todos los márgenes son involucrados por carcinoma invasivo,
            displasia, y metaplasia intestinal''',
        default=False,    
    )
    #Nota: Use esta sección sólo si marco la casilla anterior, es decir todos los márgenes son involucrados y todos los márgenes pueden ser evaluados.
    margenes_examinados = models.CharField(
        verbose_name='''Los márgenes examinados. Nota: Los márgenes pueden incluir a proximal, distal, radial,
            mucosal, en profundidad, y otros.''',
        max_length=5000,
        blank=True,
        null = True
    )
    distancia_carcinoma_invasivo_margen_cercano_cm = models.FloatField(
        verbose_name='''La distancia del carcinoma invasivo al margen más cercano
                (centímetros)''',
        blank=True,
        null=True
    )
    distancia_carcinoma_invasivo_margen_cercano_mm = models.FloatField(
        verbose_name='''La distancia del carcinoma invasivo al margen más cercano
                (milímetros)''',
        blank=True,
        null=True
    )
    #Solo para esophagectomia y esophagogastrectomia(EE)
    margen_proximal = models.IntegerField(
        choices=neck_model_choices.MargenProximalChoices.choices,
        verbose_name='''Margen Proximal''',
        blank=True,
        null=True,
    )
    margen_distal = models.IntegerField(
        choices=neck_model_choices.MargenDistalChoices.choices,
        verbose_name="Margen Distal",
        blank=True,
        null=True,
    )
    margen_radial = models.IntegerField(
        choices=neck_model_choices.MargenRadialChoices.choices,
        verbose_name="Margen Radial",
        blank=True,
        null=True,
    )
    otros_margenes_EE = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name = "Otro Margen(s) (requerido único si es aplicable). Especifique",
    )
    otros_margenes_EE_especificaciones = models.IntegerField(
        choices=neck_model_choices.OtrosMargenesSophagectomiaEsophagogastrectomiaChoices.choices,
        verbose_name="Otro Margen(s)",
        blank=True,
        null=True,
    )
    #Para especímenes solo de resección endoscopica(RE)
    margen_mucosal = models.IntegerField(
        verbose_name="Margen Mucosal",
        choices=neck_model_choices.MargenMucosalChoices.choices,
        blank=True,
        null=True,
    )
    margen_profundo = models.IntegerField(
        verbose_name="Margen Profundo",
        choices=neck_model_choices.MargenProfundoChoices.choices,
        blank=True,
        null=True,
    )
    otros_margenes_RE = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name = "Otro Margen(s) (requerido único si es aplicable). Especifique",
    )
    otros_margenes_RE_especificaciones = models.IntegerField(
        choices=neck_model_choices.OtrosMargenesReseccionEndoscopicaChoices.choices,
        verbose_name="Otro Margen(s)",
        blank=True,
        null=True,
    )
    
    #Invasión Linfovascular
    invasion_linfovascular = models.IntegerField(
        verbose_name="Invasión Linfovascular",
        choices=neck_model_choices.InvasionLinfovascularChoices.choices,
    )
    
    #Invasión Perineural
    invasion_perineural = models.IntegerField(
        verbose_name="Invasión Perineural",
        choices=neck_model_choices.InvasionPerineuralChoices.choices,
    )
    
    #Ganglios Linfáticos Regionales
    ganglios_linfaticos_encontrados = models.BooleanField(
        verbose_name = "Ganglios Linfáticos Encontrados",
        default=False,
    )
    
    #Examen del ganglio linfático (requerido solo si se marco la casilla anterior, es decir si los ganglios linfáticos están presentes en el espécimen)
    #Número de gânglios linfáticos Involucrados
    num_ganglios_linfaticos = models.IntegerField(
        verbose_name="Número de gânglios linfáticos Involucrados",
        blank=True,
        null=True,
    )
    #Num de ganglios no puede ser determinado
    num_ganglios_no_determinado = models.CharField(
        max_length=5000,
        blank=True,
        null = True,
        verbose_name="El número de ganglios no puede ser determinado (explique)"
    )
    
    #clasificación del tumor 
    clasificacion_tumor = models.IntegerField(
        choices=neck_model_choices.ClasificacionTumorChoices.choices,
        verbose_name="Clasificación Tumor",
        blank=True,
        null=True,
        default=None
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Diagnóstico Biopcia de Cuello(Esófago)"
        verbose_name_plural = "Diagnósticos Biopcias de Cuello(Esófago)"
        ordering = ["id"]
    
    def __str__(self):
        return f"Diagnóstico Biopcia de Cuello(Esófago) de la biopcia: {self.biopsy}"