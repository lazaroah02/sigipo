from django.db import models
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import mama_cdis_model_choices
from multiselectfield import MultiSelectField

class MamaCDISBiopsyDiagnostic(models.Model):
    """
    Diagnostic model of Mama CDIS
    """
    biopsy = models.OneToOneField(
        "pathologic_anathomy.BiopsyRequest",
        on_delete=models.CASCADE,
        related_name="biopsy_diagnostic_mama_cdis",
    )

    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA
    # tipo de muestra
    tipo_muestra = models.IntegerField(
        choices = mama_cdis_model_choices.TipoDeMuestraChoices.choices,
        verbose_name = "Tipo de Muestra"
    )
    
    # Sitio del tumor y Lateralidad
    sitio_tumor_lateralidad = models.CharField(
        max_length = 5000,
        verbose_name = "Sitio del Tumor y Lateralidad"
    )
    
    #Método de localización 
    metodo_localizacion = models.IntegerField(
        choices = mama_cdis_model_choices.MetodoLocalizacionChoices.choices,
        verbose_name = "Método de localización"
    )
    
    #Historia Clínica actual (todas las que apliquen)
    historia_clinica_actual = MultiSelectField(
        max_length=100,
        verbose_name = "Historia Clínica actual (todas las que apliquen)",
        min_choices = 1,
        choices = mama_cdis_model_choices.HistoriaClinicaActualChoices.choices
    )
    hallazgos_radiologicos_otros = models.CharField(
        verbose_name="Hallazgos Radiológicos otros",
        blank=True,
        null=True,
        max_length=5000
    )
    historia_clinica_otro = models.CharField(
        verbose_name="Otra Historia Clínica actual",
        blank=True,
        null=True,
        max_length=5000
    )
    
    #Especificar localización, diagnóstico, y tratamiento anterior:
    esp_local_diagnost_tratam = models.CharField(
        verbose_name="Especificar localización, diagnóstico, y tratamiento anterior",
        max_length=5000
    )
    
    #Médico de asistencia
    medico_asistencia = models.CharField(
        verbose_name = "Médico de asistencia",
        max_length=1000
    )
    
    #Reporte macroscópico
    #Identificación de la muestra
    identificacion_muestra = models.IntegerField(
        verbose_name = "Identificación de la muestra",
        choices = mama_cdis_model_choices.IdentificacionDeLaMuestraChoices.choices,
    )
    identificacion_muestra_otro = models.CharField(
        verbose_name="Otra Identificación de la muestra",
        max_length=5000,
        blank=True,
        null = True
    )
    
    #Lateralidad
    lateralidad = models.IntegerField(
        verbose_name = "Lateralidad",
        choices = mama_cdis_model_choices.LateralidadChoices.choices,
    )
    
    #Sitio Tumor (seleccione todos los que apliquen)
    sitio_tumor = MultiSelectField(
        verbose_name = "Sitio Tumor (seleccione todos los que apliquen)",
        max_length=100,
        min_choices = 1,
        choices = mama_cdis_model_choices.SitioTumorChoices.choices,
    )
    
    #Posición
    posicion = models.IntegerField(
        verbose_name = "Posicion",
        choices = mama_cdis_model_choices.PosicionChoices.choices
    )
    otra_posicion = models.CharField(
        verbose_name="Otra Posición",
        max_length=5000,
        blank=True,
        null = True
    )
    
    #Tamaño (Extensión) del CDIS
    #Extensión máxima del CDI (mm)
    extension_maxima_cdi = models.FloatField(
        verbose_name = "Extensión máxima del CDI (mm)",
        blank = True,
        null = True
    )
    #Dimensiones adicionales del CDI (mm)
    dimensiones_adicionales_cdi = models.FloatField(
        verbose_name = "Extensiones adicionales del CDI (mm)",
        blank = True,
        null = True
    )
    #Número de bloques son CDIS: 
    num_bloques_cdi = models.IntegerField(
        verbose_name="Número de bloques son CDIS",
        blank=True,
        null=True
    )
    #Número de bloques examinados:
    num_bloques_examinados = models.IntegerField(
        verbose_name="Número de bloques examinados",
        blank=True,
        null=True
    )
    #Reportado por
    reportado_por = models.CharField(
        verbose_name="Reportado por",
        blank=True,
        null=True,
        max_length=1000
    )
    
    #Diagnóstico histopatológico
    #Patrón Arquitectural(todos los que apliquen)
    patron_arquitectural = MultiSelectField(
        verbose_name="Patron Arquitectural(todos los que apliquen)",
        choices=mama_cdis_model_choices.PatronArquitecturalChoices.choices,
        min_choices = 1,
        max_length=100
    )
    patron_arquitectural_otro = models.CharField(
        verbose_name="Otro Patron Arquitectural",
        max_length=5000,
        blank=True,
        null = True
    )
    
    #Grado Nuclear
    grado_nuclear = models.IntegerField(
        verbose_name = "Grado Nuclear",
        choices = mama_cdis_model_choices.GradoNuclearChoices.choices
    )
    
    #Heterogeneidad del grado nuclear
    heterogeneidad_grado_nuclear = models.IntegerField(
        verbose_name = "Heterogeneidad del grado nuclear",
        choices = mama_cdis_model_choices.HeterogeneidadGradoNuclearChoices.choices
    )

    #Necrosis
    necrosis = models.IntegerField(
        verbose_name = "Necrosis",
        choices=mama_cdis_model_choices.NecrosisChoices.choices
    )
    
    #Microcalcificaciones:
    microcalcificaciones1 = models.IntegerField(
        verbose_name = "Microcalcificaciones",
        choices=mama_cdis_model_choices.Microcalcificaciones1Choices.choices
    )
    size_extension = models.CharField(
        max_length=1000,
        verbose_name = "Tamaño y extensión:"
    )
    
    #Enfermedad de Paget
    enfermedad_paget = models.IntegerField(
        verbose_name = "Enfermedad de Paget",
        choices=mama_cdis_model_choices.EnfermedadPagetChoices.choices
    )
    
    #Neoplasia lobular
    neoplasia_lobular = models.IntegerField(
        verbose_name = "Neoplasia lobular",
        choices=mama_cdis_model_choices.NeoplasiaLobularChoices.choices
    )
    
    #Márgenes (todos los que apliquen)
    margenes = MultiSelectField(
        verbose_name = "Márgenes (todos los que apliquen)",
        max_length=100,
        min_choices = 1,
        choices = mama_cdis_model_choices.MargenesChoices.choices
    )
    
    #Distancia del margen más cercano(mm)
    distancia_margen_mas_cercano = models.FloatField(
        verbose_name="Distancia del margen más cercano(mm)",
    )
    #Márgen mas cercano
    margen_mas_cercano = models.CharField(
        max_length=5000,
        verbose_name="Márgen mas cercano",
    )
    #Especificar distancia a márgenes:
    diastancia_margen_superior = models.FloatField(
        verbose_name="Distancia al márgen superior(mm)",
    )
    diastancia_margen_inferior = models.FloatField(
        verbose_name="Distancia al márgen inferior(mm)",
    )
    diastancia_margen_medial = models.FloatField(
        verbose_name="Distancia al márgen medial(mm)",
    )
    diastancia_margen_lateral = models.FloatField(
        verbose_name="Distancia al márgen lateral(mm)",
    )
    diastancia_margen_anterior = models.FloatField(
        verbose_name="Distancia al márgen anterior(mm)",
    )
    diastancia_margen_posterior = models.FloatField(
        verbose_name="Distancia al márgen posterior(mm)",
    )
    distancia_otros_margenes = models.CharField(
        verbose_name="Distancia otros márgenes especificados",
        max_length=5000,
        blank=True,
        null=True
    )
    margen_especificado_especific = models.CharField(
        verbose_name="Margen especificado",
        max_length=5000,
        blank=True,
        null=True
    )
    margen_especificado_determ = models.IntegerField(
        verbose_name = "Margen especificado",
        choices=mama_cdis_model_choices.MargenEspecificadoChoices.choices
    )
    
    #Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva):
    margenes_positivos_anterior_size = models.FloatField(
        verbose_name = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Anterior"
    )
    margenes_positivos_posterior_size = models.FloatField(
        verbose_name = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Posterior"
    )
    margenes_positivos_superior_size = models.FloatField(
        verbose_name = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): SUperior"
    )
    margenes_positivos_inferior_size = models.FloatField(
        verbose_name = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Inferior"
    )
    margenes_positivos_medial_size = models.FloatField(
        verbose_name = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Medial"
    )
    margenes_positivos_lateral_size = models.FloatField(
        verbose_name = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Lateral"
    )
    margenes_positivos_otros = models.CharField(
        max_length = 5000,
        verbose_name="Otros Márgenes(especificar)",
        blank=True,
        null=True
    )
    
    #Ganglios Linfáticos Regionales
    ganglios_linfaticos = models.IntegerField(
        verbose_name="Ganglios Linfáticos Regionales",
        choices=mama_cdis_model_choices.GangliosLinfaticosRegionalesChoices.choices,
    )
    #Número de ganglios linfáticos que no pudieron ser determinados (explicar)
    num_ganglios_linfaticos_no_determ = models.CharField(
        verbose_name="Número de ganglios linfáticos que no pudieron ser determinados (explicar)",
        blank=True,
        null=True,
        max_length=5000
    )

    # Número de ganglios linfáticos examinados
    num_ganglios_linfaticos_exam = models.IntegerField(
        verbose_name=" Número de ganglios linfáticos examinados",
        blank=True,
        null=True
    )    
    #Número de ganglios linfáticos con macro metástasis (>2 mm):
    num_ganglios_linfaticos_hig_2 = models.IntegerField(
        verbose_name="Número de ganglios linfáticos con macro metástasis (>2 mm)",
        blank=True,
        null=True
    )    
    #Número de ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)
    num_ganglios_linfaticos_hig_200 = models.IntegerField(
        verbose_name="Número de ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)",
        blank=True,
        null=True
    )    
    #Número de ganglios linfáticos con células tumorales aisldas (≤0.2mm y/o ≤200 células)
    num_ganglios_linfaticos_low_200 = models.IntegerField(
        verbose_name="Número de ganglios linfáticos con células tumorales aisldas (≤0.2mm y/o ≤200 células)",
        blank=True,
        null=True
    )  
    #Tamaño de los mayores depósitos metastásicos(mm)
    size_depositos_metastaticos = models.FloatField(
        verbose_name="Tamaño de los mayores depósitos metastásicos(mm)",
        blank=True,
        null=True
    )
    
    #Extensión extraganglionar:
    extension_extraganglionar = models.IntegerField(
        verbose_name="Extensión extraganglionar:",
        choices=mama_cdis_model_choices.ExtensionExtraganglionarChoices.choices
    )
    
    #Microcalcificaciones (todas las que apliquen)
    microcalcificaciones2 = MultiSelectField(
        verbose_name="Microcalcificaciones(todas las que apliquen)",
        max_length=100,
        min_choices = 1,
        choices=mama_cdis_model_choices.Microcalcificaciones2Choices.choices
    )
    
    #Otros hallazgos histológicos
    otros_hallazgos_histologicos = models.CharField(
        verbose_name="Otros hallazgos histológicos",
        max_length=5000,
        blank=True,
        null=True
    )
    otros_estudios_ihq = models.CharField(
        blank=True,
        null=True,
        verbose_name="Otros estudios: IHQ",
        max_length = 5000
    )
    comentarios = models.CharField(
        blank=True,
        null=True,
        verbose_name="Comentarios",
        max_length = 5000
    )
    diagnosticado_por = models.CharField(
        blank=True,
        null=True,
        verbose_name="Diagnosticado por",
        max_length = 1000
    )
    
    reated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Diagnostico Biopcia de Mama(CDIS)"
        verbose_name_plural = "Diagnosticos Biopcias de Mama(CDIS)"
        ordering = ["id"]

    def __str__(self):
        return f"Diagnostico de la biopcia de tipo mama(cdis) de la biopcia: {self.biopsy}"
    