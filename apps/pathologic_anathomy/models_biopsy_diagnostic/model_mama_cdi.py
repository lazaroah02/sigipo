from django.db import models
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import mama_cdi_model_choices
from multiselectfield import MultiSelectField

class MamaCDIBiopsyDiagnostic(models.Model):
    """
    Diagnostic model of Mama CDI
    """
    biopsy = models.OneToOneField(
        "pathologic_anathomy.BiopsyRequest",
        on_delete=models.CASCADE,
        related_name="biopsy_diagnostic_mama_cdi",
    )

    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA
    # tipo de muestra
    tipo_muestra = models.IntegerField(
        choices = mama_cdi_model_choices.TipoDeMuestraChoices.choices,
        verbose_name = "Tipo de Muestra"
    )
    
    # Sitio del tumor y Lateralidad
    sitio_tumor_lateralidad = models.CharField(
        max_length = 5000,
        verbose_name = "Sitio del Tumor y Lateralidad"
    )
    
    #Método de localización 
    metodo_localizacion = models.IntegerField(
        choices = mama_cdi_model_choices.MetodoLocalizacionChoices.choices,
        verbose_name = "Método de localización"
    )
    
    #Otra información clínica relevante (Dx clínico, resultados de imagen, resultados de laboratorio,  neoadyuvancia) 
    otra_info_relevante = models.CharField(
        verbose_name = "Otra información clínica relevante (Dx clínico, resultados de imagen, resultados de laboratorio,  neoadyuvancia)",
        null = True,
        blank = True,
        max_length=5000
    )
    
    #Médico de asistencia
    medico_asistencia = models.CharField(
        verbose_name = "Médico de asistencia",
        null = True,
        blank = True,
        max_length=5000
    )
    
    #Reporte macroscópico 
    #Número de muestras enviadas 
    num_muestras_enviadas = models.IntegerField(
        verbose_name = "Numero de muestras enviadas",
    )
    #Lateralidad
    lateralidad = models.IntegerField(
        choices = mama_cdi_model_choices.LateralidadChoices.choices,
        verbose_name = "Lateralidad"
    )
    #tipo de muestra
    reporte_tipo_muestra = models.CharField(
        verbose_name = "Tipo de Muestra",
        null = True,
        blank = True,
        max_length=5000
    )
    #Diagnóstico intraoperatorio
    diagnóstico_intraoperatorio = models.IntegerField(
        choices = mama_cdi_model_choices.DiagnosticoOperatorioChoices.choices,
        verbose_name = "Diagnóstico intraoperatorio"
    )
    #Sitio del Tumor
    sitio_tumor = MultiSelectField(
        verbose_name = "Sitio del Tumor",
        max_length = 10,
        min_choices = 1,
        choices = mama_cdi_model_choices.SitioDelTumorChoices.choices
    )
    #Posición
    posicion = models.IntegerField(
        choices = mama_cdi_model_choices.PosicionChoices.choices,
        verbose_name = "Posición"
    )
    posicion_otra = models.CharField(
        verbose_name = "Otra posición(especificar)",
        null = True,
        blank = True,
        max_length=5000
    )
    #Orientación del espécimen: 
    orientacion_especimen = models.IntegerField(
        choices = mama_cdi_model_choices.OrientacionEspecimenChoices.choices,
        verbose_name = "Orientación del espécimen"
    )
    orientacion_sitio = models.CharField(
        verbose_name = " Orientación del espécimen. Sitio al que corresponde",
        null = True,
        blank = True,
        max_length=5000
    )
    #Método de localización
    metodo_localizacion = models.CharField(
        verbose_name = "Método de localización",
        max_length=5000
    )
    #Tamaño del espécimen
    especimen_size = models.CharField(
        max_length=100,
        verbose_name = "Tamaño del espécimen(mm o cm)"
    )
    #Tumor macroscópicamente visible 
    tumor_macro_visible = models.IntegerField(
        choices = mama_cdi_model_choices.TumorMacroVisibleChoices.choices,
        verbose_name = "Tumor macroscópicamente visible"
    )
    num_focos_presentes = models.IntegerField(
        verbose_name = "Número de focos presentes",
        blank = True,
        null =True
    )
    #Descripción macroscópica del tumor(es)
    decripcion_macro_tumor = models.CharField(
        verbose_name = "Descripción macroscópica del tumor(es)",
        null = True,
        blank = True,
        max_length=5000
    )
    #Tamaño del tumor(mm o cm) 
    tumor_size = models.CharField(
        verbose_name = "Tamaño del tumor(es)(mm o cm)",
        max_length=100
    )
    #Distancia del foco tumoral más cercano
    distancia_foco_tumoral = models.FloatField(
        verbose_name = "Distancia del foco tumoral más cercano",
    )
    #Distancia del tumor(es) de los márgenes quirúrgicos (mm)
    distancia_tumor_margenes = models.FloatField(
        verbose_name="Distancia del tumor(es) de los márgenes quirúrgicos(mm)"
    )
    #Piel
    piel_presente = models.BooleanField(
        verbose_name = "Piel presente"
    )
    piel_presente_dimenciones = models.CharField(
        verbose_name = "Dimensiones(__x__(mm)) de la piel en caso de estar presente:",
        max_length=100
    )
    #Alteraciones
    alteraciones = models.CharField(
        verbose_name = "Alteraciones",
        null = True,
        blank = True,
        max_length=5000
    )
    #Músculo
    musculo_presente = models.BooleanField(
        verbose_name = "Musculo presente"
    )
    #Si Ganglio linfático centinela. Por cada ganglio recibido, anotar: Sitio, Color, Tamaño _______x_______x________  mm, 
    si_ganglio_linfatico_report = models.CharField(
        max_length=100000,
        blank=True,
        null = True,
        verbose_name = ""
        )
    #Ganglios linfáticos no centinelas
    ganglios_linfaticos_no_centinelas = models.IntegerField(
        verbose_name = "Ganglios linfáticos no centinelas",
        blank = True,
        null = True,
    )     
    #Número total de ganglios 
    num_total_ganglios = models.IntegerField(
        verbose_name = "Número total de ganglios",
        blank = True,
        null = True,
    )
    #Tamaño promedio (mm o cm )
    average_size = models.FloatField(
        verbose_name = "Tamaño promedio (mm o cm )",
        blank = True,
        null = True,
    )
    #Descripción
    descripcion = models.CharField(
        verbose_name = "Descripción",
        null = True,
        blank = True,
        max_length=5000
    )    
    
    #Otros hallazgos macroscópicos 
    otros_hallazgos_macros = models.CharField(
        verbose_name = "Descripción",
        null = True,
        blank = True,
        max_length=5000
    )
    #Relación de cortes 
    relacion_cortes = models.CharField(
        verbose_name = "Relación de cortes",
        null = True,
        blank = True,
        max_length=5000
    )
    #Reportado por 
    reportado_por = models.CharField(
        verbose_name = "Reportado por",
        null = True,
        blank = True,
        max_length=5000
    )
    
    #Reporte histológico
    #Tumores múltiples , si están presentes
    tumores_multiples_presentes = models.CharField(
        verbose_name = "Tumores múltiples , si están presentes",
        null = True,
        blank = True,
        max_length=5000
    )
    #Cuadrantes involucrados 
    cuadrantes_involucrados = models.CharField(
        verbose_name = "Cuadrantes involucrados",
        null = True,
        blank = True,
        max_length=5000
    )
    #Número total de focos tumorales 
    num_total_focos_tumorales = models.IntegerField(
        verbose_name = "Número total de focos tumorales"
    )
    #Para cada tumor identificado, tamaño máximo(mm)
    max_size_by_tumor = models.CharField(
        verbose_name = "Para cada tumor identificado, tamaño máximo(mm)",
        max_length=5000
    )
    
    #Tipo Histológico 
    tipo_histologico = models.IntegerField(
        choices = mama_cdi_model_choices.TipoHistologicoChoices.choices,
        verbose_name = "Tipo Histologico"
    )
    tipo_histologico_otros = models.CharField(
        verbose_name = "Otros Tipos Histologicos(especifique)",
        null = True,
        blank = True,
        max_length=5000
    )
    
    #Grado histológico (Nottingham Histologic Score) 
    grado_histologico = models.CharField(
        max_length = 1000,
        verbose_name = "Grado histológico(Nottingham Histologic Score)"
    )
    #Diferenciación Glandular (Acinar)/Tubular 
    diferenciacion_glandular = models.CharField(
        max_length = 1000,
        verbose_name = "Diferenciación Glandular (Acinar)/Tubular"
    )
    #Pleomorfismo Nuclear 
    pleomorfismo_nuclear = models.CharField(
        max_length = 1000,
        verbose_name = "Pleomorfismo Nuclear"
    )
    #Índice Mitótico 
    indice_mitotico = models.FloatField(
        verbose_name = "Indice Mitótico"
    )
    
    #Invasión linfovascular 
    invasion_linfovascular = models.IntegerField(
        choices = mama_cdi_model_choices.InvasionLinfovascularChoices.choices,
        verbose_name = "Invasión linfovascular"
    )
    #Invasión lymphovascular dérmica
    invasion_linfovascular_dermica = models.IntegerField(
        choices = mama_cdi_model_choices.InvasionLymphovascularDermicaChoices.choices,
        verbose_name = "Invasión linfovascular dérmica"
    )
    #Necrosis
    necrosis = models.IntegerField(
        choices = mama_cdi_model_choices.NecrosisChoices.choices,
        verbose_name = "Necrosis"
    )
    #Fibrosis intratumoral
    fibrosis_intratumoral = models.IntegerField(
        choices = mama_cdi_model_choices.FibrosisIntratumoralChoices.choices,
        verbose_name = "Fibrosis Intratumoral"
    )
    #Desmoplasia  intratumoral
    desmoplasia_intratumoral = models.IntegerField(
        choices = mama_cdi_model_choices.DesmoplasiaIntratumoralChoices.choices,
        verbose_name = "Desmoplasia Intratumoral"
    )
    #Infiltrado mononuclear intratumoral
    infiltrado_mononuclear_intratumoral = models.IntegerField(
        choices = mama_cdi_model_choices.InfiltradoMononuclearIntratumoralChoices.choices,
        verbose_name = "Infiltrado mononuclear intratumoral"
    )
    infiltrado_mononuclear_intratumoral_otro = models.CharField(
        verbose_name = "Otro tipo celular(especifique)",
        null = True,
        blank = True,
        max_length=5000
    )
    #Infiltrado mononuclear peritumoral
    infiltrado_mononuclear_peritumoral = models.IntegerField(
        choices = mama_cdi_model_choices.InfiltradoMononuclearPeritumoralChoices.choices,
        verbose_name = "Infiltrado mononuclear peritumoral"
    )
    infiltrado_mononuclear_peritumoral_otro = models.CharField(
        verbose_name = "Otro tipo celular(especifique)",
        null = True,
        blank = True,
        max_length=5000
    )
    #Presencia de Carcinoma Ductal In Situ (DCIS)
    presencia_dcis = models.IntegerField(
        choices = mama_cdi_model_choices.PresenciaDCISChoices.choices,
        verbose_name = "Presencia de Carcinoma Ductal In Situ (DCIS)"
    )
    #Tamaño (extensión) del CDIS (mayor dimensión usando la evaluación macro and microscópica) (milímetros)
    cdis_size = models.FloatField(
        verbose_name = "Tamaño (extensión) del CDIS (mayor dimensión usando la evaluación macro and microscópica) (milímetros)"
    )
    #Dimensions adicionales (millimeters)
    adittional_size = models.FloatField(
        verbose_name = "Dimensions adicionales (millimeters)"
    )
    #Número de bloques con CDIS
    num_bloques_cdis = models.IntegerField(
        verbose_name="Número de bloques con CDIS"
    )
    #Número de bloques examinados
    num_bloques_examinados = models.IntegerField(
        verbose_name="Número de bloques examinados"
    )
    #Patrón arquitectural (todos los que apliquen)
    patron_arquitectural = MultiSelectField(
        max_length=100,
        verbose_name = "Patrón arquitectural (todos los que apliquen)",
        min_choices = 1,
        choices = mama_cdi_model_choices.PatronArquitecturalChoices.choices
    )
    patron_arquitectural = models.CharField(
        verbose_name = "Otro Patrón arquitectural(especifique)",
        null = True,
        blank = True,
        max_length=5000
    )
    #grado
    grado = models.IntegerField(
        choices = mama_cdi_model_choices.GradoChoices.choices,
        verbose_name = "Grado"
    )
    #Lobular Carcinoma In Situ(LCIS) Presente
    lcis_presente = models.BooleanField(
        verbose_name = "Lobular Carcinoma In Situ(LCIS) Presente"
    )
    #Extensión tumoral a la piel
    extension_tumoral_piel = models.IntegerField(
        choices = mama_cdi_model_choices.ExtensionTumoralPielChoices.choices,
        verbose_name = "Extensión tumoral a la piel"
    )
    #Pezones Afectado por CDIS (Enf Paget)
    pezones_afectados = models.IntegerField(
        verbose_name = "Pezones Afectado por CDIS (Enf Paget)"
    )
    #Invasión a músculo
    invasion_musculo = models.BooleanField(
        verbose_name = "Invasión a músculo"
    )
    #Invasión Músculo y pared toráxcica
    invasion_musculo_pared_torxacica = models.BooleanField(
        verbose_name = "Invasión Músculo y pared toráxcica"
    )
    #Los Márgenes
    margenes = models.IntegerField(
        choices = mama_cdi_model_choices.MargenesChoices.choices
    )
    distancia_a_los_margenes = models.FloatField(
        verbose_name = "Distancia a los Márgenes",
    )
    #Para los márgenes positivos, especificar la  extensión (unifocal, multifocal, o extensivo):
    #Anterior:
    margen_anterior = models.CharField(
        max_length = 1000,
        verbose_name = "Anterior"
    )
    #Posterior:
    margen_posterior = models.CharField(
        max_length = 1000,
        verbose_name = "Posterior",
        blank=True,
        null = True
    )
    #Superior: 	
    margen_superior = models.CharField(
        max_length = 1000,
        verbose_name = "Superior",
        blank=True,
        null = True
    )
    #Inferior:	
    margen_inferior = models.CharField(
        max_length = 1000,
        verbose_name = "Inferior",
        blank=True,
        null = True
    )
    #Medial:
    margen_medial = models.CharField(
        max_length = 1000,
        verbose_name = "Medial",
        blank=True,
        null = True
    )
    #Lateral:
    margen_lateral = models.CharField(
        max_length = 1000,
        verbose_name = "Lateral",
        blank=True,
        null = True
    )
    #Otros (especificar márgenes):
    margen_otros = models.CharField(
        max_length = 5000,
        verbose_name = "Otros márgenes(especificar)",
        blank = True,
        null = True
    )
    
    #Márgenes con CDIS 
    margenes_con_cdis = models.IntegerField(
        choices = mama_cdi_model_choices.MargenesCDISChoices.choices,
        verbose_name = "Márgenes con CDIS",
    )
    distancia = models.FloatField(
        verbose_name = "Distancia a los márgenes (mm): "
    )
    #Para los márgenes positivos, especificar la  extensión (unifocal, multifocal, o extensivo):
    #Anterior:
    margen_anterior_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Anterior",
        blank=True,
        null = True
    )
    #Posterior:
    margen_posterior_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Posterior",
        blank=True,
        null = True
    )
    #Superior: 	
    margen_superior_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Superior",
        blank=True,
        null = True
    )
    #Inferior:	
    margen_inferior_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Inferior",
        blank=True,
        null = True
    )
    #Medial:
    margen_medial_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Medial",
        blank=True,
        null = True
    )
    #Lateral:
    margen_lateral_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Lateral",
        blank=True,
        null = True
    )
    #Otros (especificar márgenes):
    margen_otros_cdis = models.CharField(
        max_length = 1000,
        verbose_name = "Otros márgenes(especificar)",
        blank = True,
        null = True
    )
    #Ganglios Linfáticos Regionales
    #No enviados
    num_gang_linf_reg_not_send = models.IntegerField(
        verbose_name = "Ganglios Linfáticos Regionales no enviados",
        blank=True,
        null = True
    )
    #No encontrados
    num_gang_linf_reg_not_found = models.IntegerField(
        verbose_name = "Ganglios Linfáticos Regionales no encontrados",
        blank=True,
        null = True
    )
    #Número de ganglios linfáticos que no pudieron ser determinados (explicar):
    num_gang_linf_reg_not_determinated = models.CharField(
        verbose_name = "Número de ganglios linfáticos que no pudieron ser determinados (explicar)",
        max_length =5000,
        blank = True,
        null = True
    )
    #Número de  ganglios linfáticos examinados
    num_gang_linf_reg_examinated = models.IntegerField(
        verbose_name = "Ganglios Linfáticos Regionales examinados",
        blank=True,
        null = True
    )
    #Número de  ganglios linfáticos con macro metástasis (>2 mm): 
    num_gang_linf_macro_mayor2 = models.IntegerField(
        verbose_name = "Número de  ganglios linfáticos con macro metástasis (>2 mm)",
        blank=True,
        null = True
    )
    #Número de  ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)
    num_gang_linf_macro_mayor02 = models.IntegerField(
        verbose_name = "Número de  ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)",
        blank=True,
        null = True
    )
    #Número de  ganglios linfáticos con células tumorales aisldas (≤0.2  mm y/o ≤200 células):
    num_gang_linf_macro_mayor02_aisladas = models.IntegerField(
        verbose_name = "Número de  ganglios linfáticos con células tumorales aisldas (≤0.2  mm y/o ≤200 células):",
        blank=True,
        null = True
    )
    #Tamaño de los mayores depósitos metastásicos(mm)
    num_gang_linf_macro_mayor02_aisladas = models.FloatField(
        verbose_name = "Tamaño de los mayores depósitos metastásicos(mm)",
        blank=True,
        null = True
    )
    
    #Extensión extraganglionar:
    extension_extraganglionar = models.IntegerField(
        choices=mama_cdi_model_choices.ExtensionExtraganglionarChoices.choices,
        verbose_name = "Extensión extraganglionar:"
    )
    
    #Número de  ganglios centinelas examined(si proceder):
    num_gang_centinelas_examinated = models.IntegerField(
        verbose_name = "Número de  ganglios centinelas examined(si proceder):",
        blank=True,
        null=True
    )
    
    #Efectos del tratamiento en el tumor(si neoadyuvancia)
    efecto_tratamiento = models.IntegerField(
        choices=mama_cdi_model_choices.EfectosTratamientoChoices.choices,
        verbose_name = "Efectos del tratamiento en el tumor(si neoadyuvancia)"
    )
    
    #Efectos del tratamiento en los GL (si neoadyuvancia)
    efectos_tratamiento_gl =  models.IntegerField(
        choices=mama_cdi_model_choices.EfectosTratamientoGLChoices.choices,
        verbose_name = "Efectos del tratamiento en los GL (si neoadyuvancia)"
    )
    
    #Efecto del tratamiento (después de neoadyuvancia hormonal o quimioterapia si se hubiera realizado) 
    efecto_tratamiento_realizado = models.IntegerField(
        choices=mama_cdi_model_choices.EfectoTratamientoRealizadoChoices.choices,
        verbose_name = "Efecto del tratamiento (después de neoadyuvancia hormonal o quimioterapia si se hubiera realizado)"
    )
    #Si respuesta parcial :% de celularidad del cáncer invasor 
    porciento_celularidad_cancer = models.FloatField(
        verbose_name = "Si hubo respuesta parcial .Indique el % de celularidad del cáncer invasor ",
        null = True,
        blank = True,
    )
    #Especificar sistema de evaluación de respuesta a la neoadyuvancia utilizado 
    sistema_evaluacion_respuesta_utilizado = models.CharField(
        blank=True,
        null=True,
        verbose_name="Especificar sistema de evaluación de respuesta a la neoadyuvancia utilizado",
        max_length = 5000
    )
    
    #Otros estudios: IHQ
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
        verbose_name = "Diagnostico Biopcia de Mama(CDI)"
        verbose_name_plural = "Diagnosticos Biopcias de Mama(CDI)"
        ordering = ["id"]

    def __str__(self):
        return f"Diagnostico de la biopcia de tipo mama(cdi) de la biopcia: {self.biopsy}"
    
    