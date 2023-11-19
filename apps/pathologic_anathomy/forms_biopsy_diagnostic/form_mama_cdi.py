from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    FloatField,
    IntegerField,
    ModelChoiceField,
    Select,
    Textarea,
)

from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.nuclear_medicine import forms
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import (
    mama_cdi_model_choices,
)
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_mama_cdi import (
    MamaCDIBiopsyDiagnostic,
)


class MamaCDIBiopsyForm(ModelForm):
    """
    Diagnostic form of Mama CDI
    """

    biopsy = ModelChoiceField(
        queryset=BiopsyRequest.objects.all(),
        widget=Select(
            attrs={
                "class": "form-control",
                "data-placeholder": "Biopsia",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
                "hidden": "true",
            },
        ),
        required=True,
        label="",
    )

    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA
    # tipo de muestra
    tipo_muestra = EmptyChoiceField(
        choices=mama_cdi_model_choices.TipoDeMuestraChoices.choices,
        label="Tipo de Muestra",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
        empty_label="Seleccionar Tipo de Muestra",
    )

    # Sitio del tumor y Lateralidad
    sitio_tumor_lateralidad = CharField(
        max_length=5000,
        label="Sitio del Tumor y Lateralidad",
        required=True,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Método de localización
    metodo_localizacion = EmptyChoiceField(
        choices=mama_cdi_model_choices.MetodoLocalizacionChoices.choices,
        label="Método de localización",
        empty_label="Seleccionar Método de localización",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    # Otra información clínica relevante (Dx clínico, resultados de imagen, resultados de laboratorio,  neoadyuvancia)
    otra_info_relevante = CharField(
        label="Otra información clínica relevante (Dx clínico, resultados de imagen, resultados de laboratorio,  neoadyuvancia)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Médico de asistencia
    medico_asistencia = CharField(
        label="Médico de asistencia",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Reporte macroscópico
    # Número de muestras enviadas
    num_muestras_enviadas = IntegerField(
        label="Numero de muestras enviadas",
    )
    # Lateralidad
    lateralidad = EmptyChoiceField(
        choices=mama_cdi_model_choices.LateralidadChoices.choices,
        label="Lateralidad",
        empty_label="Seleccione Lateralidad",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # tipo de muestra
    reporte_tipo_muestra = CharField(
        label="Tipo de Muestra",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Diagnóstico intraoperatorio
    diagnóstico_intraoperatorio = EmptyChoiceField(
        choices=mama_cdi_model_choices.DiagnosticoOperatorioChoices.choices,
        label="Diagnóstico intraoperatorio",
        empty_label="Seleccionar Diagnóstico intraoperatorio",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Sitio del Tumor
    sitio_tumor = forms.CustomMultiSelectFormField(
        label="Sitio del Tumor",
        required=True,
        choices=mama_cdi_model_choices.SitioDelTumorChoices.choices,
    )
    # Posición
    posicion = EmptyChoiceField(
        choices=mama_cdi_model_choices.PosicionChoices.choices,
        label="Posición",
        required=True,
        empty_label="Seleccionar Posición",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    posicion_otra = CharField(
        label="Otra posición(especificar)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Orientación del espécimen:
    orientacion_especimen = EmptyChoiceField(
        choices=mama_cdi_model_choices.OrientacionEspecimenChoices.choices,
        label="Orientación del espécimen",
        required=True,
        empty_label="Seleccionar Orientación del espécimen",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    orientacion_sitio = CharField(
        label=" Orientación del espécimen. Sitio al que corresponde",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Método de localización
    metodo_localizacion = CharField(
        label="Método de localización",
        max_length=5000,
        required=True,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Tamaño del espécimen
    especimen_size = CharField(
        max_length=100, label="Tamaño del espécimen(mm o cm)", required=True
    )
    # Tumor macroscópicamente visible
    tumor_macro_visible = EmptyChoiceField(
        choices=mama_cdi_model_choices.TumorMacroVisibleChoices.choices,
        label="Tumor macroscópicamente visible",
        empty_label="Seleccionar Tumor macroscópicamente visible",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    num_focos_presentes = IntegerField(
        label="Número de focos presentes", required=False
    )
    # Descripción macroscópica del tumor(es)
    decripcion_macro_tumor = CharField(
        label="Descripción macroscópica del tumor(es)",
        required=False,
        max_length=5000,
    )
    # Tamaño del tumor(mm o cm)
    tumor_size = CharField(
        label="Tamaño del tumor(es)(mm o cm)", max_length=100, required=True
    )
    # Distancia del foco tumoral más cercano
    distancia_foco_tumoral = FloatField(
        label="Distancia del foco tumoral más cercano", required=True
    )
    # Distancia del tumor(es) de los márgenes quirúrgicos (mm)
    distancia_tumor_margenes = FloatField(
        label="Distancia del tumor(es) de los márgenes quirúrgicos(mm)", required=True
    )
    # Piel
    piel_presente = BooleanField(
        label="Piel presente",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )
    piel_presente_dimenciones = CharField(
        label="Dimensiones(__x__(mm)) de la piel en caso de estar presente:",
        max_length=100,
        required=True,
    )
    # Alteraciones
    alteraciones = CharField(
        label="Alteraciones",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Músculo
    musculo_presente = BooleanField(
        label="Musculo presente",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )
    # Si Ganglio linfático centinela. Por cada ganglio recibido, anotar: Sitio, Color, Tamaño _______x_______x________  mm,
    si_ganglio_linfatico_report = CharField(
        max_length=100000,
        required=False,
        label="Si Ganglio linfático centinela. Por cada ganglio recibido, anotar: Sitio, Color, Tamaño _______x_______x________  mm",
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Ganglios linfáticos no centinelas
    ganglios_linfaticos_no_centinelas = IntegerField(
        label="Ganglios linfáticos no centinelas", required=False
    )
    # Número total de ganglios
    num_total_ganglios = IntegerField(label="Número total de ganglios", required=False)
    # Tamaño promedio (mm o cm )
    average_size = FloatField(label="Tamaño promedio (mm o cm )", required=False)
    # Descripción
    descripcion = CharField(
        label="Descripción",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Otros hallazgos macroscópicos
    otros_hallazgos_macros = CharField(
        label="Descripción",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Relación de cortes
    relacion_cortes = CharField(
        label="Relación de cortes",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Reportado por
    reportado_por = CharField(label="Reportado por", required=False, max_length=5000)

    # Reporte histológico
    # Tumores múltiples , si están presentes
    tumores_multiples_presentes = CharField(
        label="Tumores múltiples , si están presentes",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Cuadrantes involucrados
    cuadrantes_involucrados = CharField(
        label="Cuadrantes involucrados",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Número total de focos tumorales
    num_total_focos_tumorales = IntegerField(
        label="Número total de focos tumorales", required=True
    )
    # Para cada tumor identificado, tamaño máximo(mm)
    max_size_by_tumor = CharField(
        label="Para cada tumor identificado, tamaño máximo(mm)",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=True,
    )

    # Tipo Histológico
    tipo_histologico = EmptyChoiceField(
        choices=mama_cdi_model_choices.TipoHistologicoChoices.choices,
        label="Tipo Histologico",
        empty_label="Seleccionar Tipo Histologico",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    tipo_histologico_otros = CharField(
        label="Otros Tipos Histologicos(especifique)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Grado histológico (Nottingham Histologic Score)
    grado_histologico = CharField(
        max_length=1000,
        label="Grado histológico(Nottingham Histologic Score)",
        required=True,
    )
    # Diferenciación Glandular (Acinar)/Tubular
    diferenciacion_glandular = CharField(
        max_length=1000,
        label="Diferenciación Glandular (Acinar)/Tubular",
        required=True,
    )
    # Pleomorfismo Nuclear
    pleomorfismo_nuclear = CharField(
        max_length=1000, label="Pleomorfismo Nuclear", required=True
    )
    # Índice Mitótico
    indice_mitotico = FloatField(label="Indice Mitótico", required=True)

    # Invasión linfovascular
    invasion_linfovascular = EmptyChoiceField(
        choices=mama_cdi_model_choices.InvasionLinfovascularChoices.choices,
        label="Invasión linfovascular",
        empty_label="Seleccionar Invasión linfovascular",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Invasión lymphovascular dérmica
    invasion_linfovascular_dermica = EmptyChoiceField(
        choices=mama_cdi_model_choices.InvasionLymphovascularDermicaChoices.choices,
        label="Invasión linfovascular dérmica",
        empty_label="Seleccionar Invasión linfovascular dérmica",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Necrosis
    necrosis = EmptyChoiceField(
        choices=mama_cdi_model_choices.NecrosisChoices.choices,
        label="Necrosis",
        empty_label="Seleccionar Necrosis",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Fibrosis intratumoral
    fibrosis_intratumoral = EmptyChoiceField(
        choices=mama_cdi_model_choices.FibrosisIntratumoralChoices.choices,
        label="Fibrosis Intratumoral",
        empty_label="Seleccionar Fibrosis Intratumoral",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Desmoplasia  intratumoral
    desmoplasia_intratumoral = EmptyChoiceField(
        choices=mama_cdi_model_choices.DesmoplasiaIntratumoralChoices.choices,
        label="Desmoplasia Intratumoral",
        empty_label="Seleccionar Desmoplasia Intratumoral",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Infiltrado mononuclear intratumoral
    infiltrado_mononuclear_intratumoral = EmptyChoiceField(
        choices=mama_cdi_model_choices.InfiltradoMononuclearIntratumoralChoices.choices,
        label="Infiltrado mononuclear intratumoral",
        empty_label="Seleccionar Infiltrado mononuclear intratumoral",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    infiltrado_mononuclear_intratumoral_otro = CharField(
        label="Otro tipo celular(especifique)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Infiltrado mononuclear peritumoral
    infiltrado_mononuclear_peritumoral = EmptyChoiceField(
        choices=mama_cdi_model_choices.InfiltradoMononuclearPeritumoralChoices.choices,
        label="Infiltrado mononuclear peritumoral",
        empty_label="Seleccionar Infiltrado mononuclear peritumoral",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    infiltrado_mononuclear_peritumoral_otro = CharField(
        label="Otro tipo celular(especifique)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Presencia de Carcinoma Ductal In Situ (DCIS)
    presencia_dcis = EmptyChoiceField(
        choices=mama_cdi_model_choices.PresenciaDCISChoices.choices,
        label="Presencia de Carcinoma Ductal In Situ (DCIS)",
        empty_label="Seleccionar Presencia de Carcinoma Ductal In Situ (DCIS)",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Tamaño (extensión) del CDIS (mayor dimensión usando la evaluación macro and microscópica) (milímetros)
    cdis_size = FloatField(
        label="Tamaño (extensión) del CDIS (mayor dimensión usando la evaluación macro and microscópica) (milímetros)",
        required=True,
    )
    # Dimensions adicionales (millimeters)
    adittional_size = FloatField(
        label="Dimensions adicionales (millimeters)", required=True
    )
    # Número de bloques con CDIS
    num_bloques_cdis = IntegerField(label="Número de bloques con CDIS", required=True)
    # Número de bloques examinados
    num_bloques_examinados = IntegerField(
        label="Número de bloques examinados", required=True
    )
    # Patrón arquitectural (todos los que apliquen)
    patron_arquitectural = forms.CustomMultiSelectFormField(
        label="Patrón arquitectural (todos los que apliquen)",
        choices=mama_cdi_model_choices.PatronArquitecturalChoices.choices,
    )
    patron_arquitectural = CharField(
        label="Otro Patrón arquitectural(especifique)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # grado
    grado = EmptyChoiceField(
        choices=mama_cdi_model_choices.GradoChoices.choices,
        label="Grado",
        empty_label="Seleccionar Grado",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Lobular Carcinoma In Situ(LCIS) Presente
    lcis_presente = BooleanField(
        label="Lobular Carcinoma In Situ(LCIS) Presente",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    # Extensión tumoral a la piel
    extension_tumoral_piel = EmptyChoiceField(
        choices=mama_cdi_model_choices.ExtensionTumoralPielChoices.choices,
        label="Extensión tumoral a la piel",
        empty_value="Seleccionar Extensión tumoral a la piel",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Pezones Afectado por CDIS (Enf Paget)
    pezones_afectados = IntegerField(
        label="Pezones Afectado por CDIS (Enf Paget)", required=True
    )
    # Invasión a músculo
    invasion_musculo = BooleanField(
        label="Invasión a músculo",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    # Invasión Músculo y pared toráxcica
    invasion_musculo_pared_torxacica = BooleanField(
        label="Invasión Músculo y pared toráxcica",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    # Los Márgenes
    margenes = EmptyChoiceField(
        choices=mama_cdi_model_choices.MargenesChoices.choices,
        label="Los Margenes",
        empty_label="Seleccionar Los Márgenes",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    distancia_a_los_margenes = FloatField(
        label="Distancia a los Márgenes", required=True
    )
    # Para los márgenes positivos, especificar la  extensión (unifocal, multifocal, o extensivo):
    # Anterior:
    margen_anterior = CharField(max_length=1000, label="Anterior", required=True)
    # Posterior:
    margen_posterior = CharField(max_length=1000, label="Posterior", required=False)
    # Superior:
    margen_superior = CharField(max_length=1000, label="Superior", required=False)
    # Inferior:
    margen_inferior = CharField(max_length=1000, label="Inferior", required=False)
    # Medial:
    margen_medial = CharField(max_length=1000, label="Medial", required=False)
    # Lateral:
    margen_lateral = CharField(max_length=1000, label="Lateral", required=False)
    # Otros (especificar márgenes):
    margen_otros = CharField(
        max_length=1000, label="Otros márgenes(especificar)", required=False
    )

    # Márgenes con CDIS
    margenes_con_cdis = EmptyChoiceField(
        choices=mama_cdi_model_choices.MargenesCDISChoices.choices,
        label="Márgenes con CDIS",
        empty_label="Seleccionar Márgenes con CDIS",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    distancia = FloatField(label="Distancia a los márgenes (mm): ", required=True)
    # Para los márgenes positivos, especificar la  extensión (unifocal, multifocal, o extensivo):
    # Anterior:
    margen_anterior_cdis = CharField(max_length=1000, label="Anterior", required=False)
    # Posterior:
    margen_posterior_cdis = CharField(
        max_length=1000, label="Posterior", required=False
    )
    # Superior:
    margen_superior_cdis = CharField(max_length=1000, label="Superior", required=False)
    # Inferior:
    margen_inferior_cdis = CharField(max_length=1000, label="Inferior", required=False)
    # Medial:
    margen_medial_cdis = CharField(max_length=1000, label="Medial", required=False)
    # Lateral:
    margen_lateral_cdis = CharField(max_length=1000, label="Lateral", required=False)
    # Otros (especificar márgenes):
    margen_otros_cdis = CharField(
        max_length=5000,
        label="Otros márgenes(especificar)",
        required=False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Ganglios Linfáticos Regionales
    # No enviados
    num_gang_linf_reg_not_send = IntegerField(
        label="Ganglios Linfáticos Regionales no enviados", required=False
    )
    # No encontrados
    num_gang_linf_reg_not_found = IntegerField(
        label="Ganglios Linfáticos Regionales no encontrados", required=False
    )
    # Número de ganglios linfáticos que no pudieron ser determinados (explicar):
    num_gang_linf_reg_not_determinated = CharField(
        label="Número de ganglios linfáticos que no pudieron ser determinados (explicar)",
        max_length=5000,
        required=False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    # Número de  ganglios linfáticos examinados
    num_gang_linf_reg_examinated = IntegerField(
        label="Ganglios Linfáticos Regionales examinados", required=False
    )
    # Número de  ganglios linfáticos con macro metástasis (>2 mm):
    num_gang_linf_macro_mayor2 = IntegerField(
        label="Número de  ganglios linfáticos con macro metástasis (>2 mm)",
        required=False,
    )
    # Número de  ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)
    num_gang_linf_macro_mayor02 = IntegerField(
        label="Número de  ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)",
        required=False,
    )
    # Número de  ganglios linfáticos con células tumorales aisldas (≤0.2  mm y/o ≤200 células):
    num_gang_linf_macro_mayor02_aisladas = IntegerField(
        label="Número de  ganglios linfáticos con células tumorales aisldas (≤0.2  mm y/o ≤200 células):",
        required=False,
    )
    # Tamaño de los mayores depósitos metastásicos(mm)
    num_gang_linf_macro_mayor02_aisladas = FloatField(
        label="Tamaño de los mayores depósitos metastásicos(mm)", required=False
    )

    # Extensión extraganglionar:
    extension_extraganglionar = EmptyChoiceField(
        choices=mama_cdi_model_choices.ExtensionExtraganglionarChoices.choices,
        label="Extensión extraganglionar:",
        empty_label="Seleccionar Extensión extraganglionar",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    # Número de  ganglios centinelas examined(si proceder):
    num_gang_centinelas_examinated = IntegerField(
        label="Número de  ganglios centinelas examined(si proceder):", required=False
    )

    # Efectos del tratamiento en el tumor(si neoadyuvancia)
    efecto_tratamiento = EmptyChoiceField(
        choices=mama_cdi_model_choices.EfectosTratamientoChoices.choices,
        label="Efectos del tratamiento en el tumor(si neoadyuvancia)",
        empty_label="Seleccionar Efectos del tratamiento en el tumor(si neoadyuvancia)",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    # Efectos del tratamiento en los GL (si neoadyuvancia)
    efectos_tratamiento_gl = EmptyChoiceField(
        choices=mama_cdi_model_choices.EfectosTratamientoGLChoices.choices,
        label="Efectos del tratamiento en los GL (si neoadyuvancia)",
        empty_label="Seleccionar Efectos del tratamiento en los GL (si neoadyuvancia)",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    # Efecto del tratamiento (después de neoadyuvancia hormonal o quimioterapia si se hubiera realizado)
    efecto_tratamiento_realizado = EmptyChoiceField(
        choices=mama_cdi_model_choices.EfectoTratamientoRealizadoChoices.choices,
        label="Efecto del tratamiento (después de neoadyuvancia hormonal o quimioterapia si se hubiera realizado)",
        empty_label="Seleccionar Efecto del tratamiento (después de neoadyuvancia hormonal o quimioterapia si se hubiera realizado)",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    # Si respuesta parcial :% de celularidad del cáncer invasor
    porciento_celularidad_cancer = FloatField(
        label="Si hubo respuesta parcial .Indique el % de celularidad del cáncer invasor ",
        required=False,
    )
    # Especificar sistema de evaluación de respuesta a la neoadyuvancia utilizado
    sistema_evaluacion_respuesta_utilizado = CharField(
        required=False,
        label="Especificar sistema de evaluación de respuesta a la neoadyuvancia utilizado",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Otros estudios: IHQ
    otros_estudios_ihq = CharField(
        required=False,
        label="Otros estudios: IHQ",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    comentarios = CharField(
        required=False,
        label="Comentarios",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    diagnosticado_por = CharField(
        required=False, label="Diagnosticado por", max_length=1000
    )

    class Meta:
        model = MamaCDIBiopsyDiagnostic
        fields = "__all__"
        default_permissions = ()
