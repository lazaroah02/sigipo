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
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import mama_cdis_model_choices
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_mama_cdis import MamaCDISBiopsyDiagnostic

class MamaCDISBiopsyForm(ModelForm):
    """
    Diagnostic form of Mama CDIS
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
                "hidden":"true"
            },
        ),
        required=True,
        label = ""
    )
    
    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA
    # tipo de muestra
    tipo_muestra = EmptyChoiceField(
        choices = mama_cdis_model_choices.TipoDeMuestraChoices.choices,
        label = "Tipo de Muestra",
        required=True,
        empty_label="Seleccionar Tipo de Muestra",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    # Sitio del tumor y Lateralidad
    sitio_tumor_lateralidad = CharField(
        max_length = 5000,
        label = "Sitio del Tumor y Lateralidad",
        required=False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Método de localización 
    metodo_localizacion = EmptyChoiceField(
        choices = mama_cdis_model_choices.MetodoLocalizacionChoices.choices,
        label = "Método de localización",
        empty_label="Seleccionar Método de localización",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Historia Clínica actual (todas las que apliquen)
    historia_clinica_actual = forms.CustomMultiSelectFormField(
        label = "Historia Clínica actual (todas las que apliquen)",
        choices = mama_cdis_model_choices.HistoriaClinicaActualChoices.choices,
        required = True
    )
    hallazgos_radiologicos_otros = CharField(
        label="Hallazgos Radiológicos otros",
        required = False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    historia_clinica_otro = CharField(
        label="Otra Historia Clínica actual",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Especificar localización, diagnóstico, y tratamiento anterior:
    esp_local_diagnost_tratam = CharField(
        label="Especificar localización, diagnóstico, y tratamiento anterior",
        max_length=5000,
        required=True,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Médico de asistencia
    medico_asistencia = CharField(
        label = "Médico de asistencia",
        max_length=1000,
        required = True,
    )
    
    #Reporte macroscópico
    #Identificación de la muestra
    identificacion_muestra = EmptyChoiceField(
        label = "Identificación de la muestra",
        empty_label="Seleccionar Identificación de la muestra",
        choices = mama_cdis_model_choices.IdentificacionDeLaMuestraChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    identificacion_muestra_otro = CharField(
        label="Otra Identificación de la muestra",
        max_length=5000,
        required = False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Lateralidad
    lateralidad = EmptyChoiceField(
        label = "Lateralidad",
        empty_label="Seleccionar Lateralidad",
        choices = mama_cdis_model_choices.LateralidadChoices.choices,
        required = True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Sitio Tumor (seleccione todos los que apliquen)
    sitio_tumor = forms.CustomMultiSelectFormField(
        label = "Sitio Tumor (seleccione todos los que apliquen)",
        required = True,
        choices = mama_cdis_model_choices.SitioTumorChoices.choices,
    )
    
    #Posición
    posicion = EmptyChoiceField(
        label = "Posicion",
        empty_label="Seleccionar Posicion",
        choices = mama_cdis_model_choices.PosicionChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    otra_posicion = CharField(
        label="Otra Posición",
        max_length=5000,
        required = False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Tamaño (Extensión) del CDIS
    #Extensión máxima del CDI (mm)
    extension_maxima_cdi = FloatField(
        label = "Extensión máxima del CDI (mm)",
        required = False
    )
    #Dimensiones adicionales del CDI (mm)
    dimensiones_adicionales_cdi = FloatField(
        label = "Extensiones adicionales del CDI (mm)",
        required = False
    )
    #Número de bloques son CDIS: 
    num_bloques_cdi = IntegerField(
        label="Número de bloques son CDIS",
        required = False
    )
    #Número de bloques examinados:
    num_bloques_examinados = IntegerField(
        label="Número de bloques examinados",
        required = False
    )
    #Reportado por
    reportado_por = CharField(
        label="Reportado por",
        required = False,
        max_length=1000
    )
    
    #Diagnóstico histopatológico
    #Patrón Arquitectural(todos los que apliquen)
    patron_arquitectural = forms.CustomMultiSelectFormField(
        label="Patron Arquitectural(todos los que apliquen)",
        choices=mama_cdis_model_choices.PatronArquitecturalChoices.choices,
        required = True
    )
    patron_arquitectural_otro = CharField(
        label="Otro Patron Arquitectural",
        max_length=5000,
        required = False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Grado Nuclear
    grado_nuclear = EmptyChoiceField(
        label = "Grado Nuclear",
        empty_label="Seleccionar Grado Nuclear",
        choices = mama_cdis_model_choices.GradoNuclearChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Heterogeneidad del grado nuclear
    heterogeneidad_grado_nuclear = EmptyChoiceField(
        label = "Heterogeneidad del grado nuclear",
        empty_label="Seleccionar Heterogeneidad del grado nuclear",
        choices = mama_cdis_model_choices.HeterogeneidadGradoNuclearChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    #Necrosis
    necrosis = EmptyChoiceField(
        label = "Necrosis",
        empty_label="Seleccionar Necrosis",
        choices=mama_cdis_model_choices.NecrosisChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Microcalcificaciones:
    microcalcificaciones1 = EmptyChoiceField(
        label = "Microcalcificaciones",
        empty_label="Seleccionar Microcalcificaciones",
        choices=mama_cdis_model_choices.Microcalcificaciones1Choices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    size_extension = CharField(
        max_length=1000,
        label = "Tamaño y extensión:",
        required=True
    )
    
    #Enfermedad de Paget
    enfermedad_paget = EmptyChoiceField(
        label = "Enfermedad de Paget",
        empty_label="Seleccionar Enfermedad de Paget",
        choices=mama_cdis_model_choices.EnfermedadPagetChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Neoplasia lobular
    neoplasia_lobular = EmptyChoiceField(
        label = "Neoplasia lobular",
        empty_label="Seleccionar Neoplasia lobular",
        choices=mama_cdis_model_choices.NeoplasiaLobularChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Márgenes (todos los que apliquen)
    margenes = forms.CustomMultiSelectFormField(
        label = "Márgenes (todos los que apliquen)",
        required = True,
        choices = mama_cdis_model_choices.MargenesChoices.choices
    )
    
    #Distancia del margen más cercano(mm)
    distancia_margen_mas_cercano = FloatField(
        label="Distancia del margen más cercano(mm)",
        required=True
    )
    #Márgen mas cercano
    margen_mas_cercano = CharField(
        max_length=5000,
        label="Márgen mas cercano",
        required=True,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    #Especificar distancia a márgenes:
    diastancia_margen_superior = FloatField(
        label="Distancia al márgen superior(mm)",
        required=True
    )
    diastancia_margen_inferior = FloatField(
        label="Distancia al márgen inferior(mm)",
        required=True
    )
    diastancia_margen_medial = FloatField(
        label="Distancia al márgen medial(mm)",
        required=True
    )
    diastancia_margen_lateral = FloatField(
        label="Distancia al márgen lateral(mm)",
        required=True
    )
    diastancia_margen_anterior = FloatField(
        label="Distancia al márgen anterior(mm)",
        required=True
    )
    diastancia_margen_posterior = FloatField(
        label="Distancia al márgen posterior(mm)",
        required=True
    )
    distancia_otros_margenes = CharField(
        label="Distancia otros márgenes especificados",
        max_length=5000,
        required=False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    margen_especificado_especific = CharField(
        label="Margen especificado",
        max_length=5000,
        required = False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    margen_especificado_determ = EmptyChoiceField(
        label = "Margen especificado",
        empty_label="Seleccionar Margen especificado",
        choices=mama_cdis_model_choices.MargenEspecificadoChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva):
    margenes_positivos_anterior_size = FloatField(
        label = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Anterior",
        required=True
    )
    margenes_positivos_posterior_size = FloatField(
        label = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Posterior",
        required=True
    )
    margenes_positivos_superior_size = FloatField(
        label = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): SUperior",
        required=True
    )
    margenes_positivos_inferior_size = FloatField(
        label = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Inferior",
        required=True
    )
    margenes_positivos_medial_size = FloatField(
        label = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Medial",
        required=True
    )
    margenes_positivos_lateral_size = FloatField(
        label = "Para márgenes positivos, especificar extensión (focal, minima/moderate, or extensiva): Lateral",
        required=True
    )
    margenes_positivos_otros = CharField(
        max_length = 5000,
        label="Otros Márgenes(especificar)",
        required=False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #Ganglios Linfáticos Regionales
    ganglios_linfaticos = EmptyChoiceField(
        label="Ganglios Linfáticos Regionales",
        empty_label="Seleccionar Ganglios Linfáticos Regionales",
        choices=mama_cdis_model_choices.GangliosLinfaticosRegionalesChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    #Número de ganglios linfáticos que no pudieron ser determinados (explicar)
    num_ganglios_linfaticos_no_determ = CharField(
        label="Número de ganglios linfáticos que no pudieron ser determinados (explicar)",
        required=False,
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    # Número de ganglios linfáticos examinados
    num_ganglios_linfaticos_exam = IntegerField(
        label=" Número de ganglios linfáticos examinados",
        required=False
    )    
    #Número de ganglios linfáticos con macro metástasis (>2 mm):
    num_ganglios_linfaticos_hig_2 = IntegerField(
        label="Número de ganglios linfáticos con macro metástasis (>2 mm)",
        required = False
    )    
    #Número de ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)
    num_ganglios_linfaticos_hig_200 = IntegerField(
        label="Número de ganglios linfáticos con micro metástasis (>0.2 mm to 2 mm y/o >200 células)",
        required = False
    )    
    #Número de ganglios linfáticos con células tumorales aisldas (≤0.2mm y/o ≤200 células)
    num_ganglios_linfaticos_low_200 = IntegerField(
        label="Número de ganglios linfáticos con células tumorales aisldas (≤0.2mm y/o ≤200 células)",
        required = False
    )  
    #Tamaño de los mayores depósitos metastásicos(mm)
    size_depositos_metastaticos = FloatField(
        label="Tamaño de los mayores depósitos metastásicos(mm)",
        required=False
    )
    
    #Extensión extraganglionar:
    extension_extraganglionar = EmptyChoiceField(
        label="Extensión extraganglionar:",
        empty_label="Seleccionar Extensión extraganglionar",
        choices=mama_cdis_model_choices.ExtensionExtraganglionarChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Microcalcificaciones (todas las que apliquen)
    microcalcificaciones2 = forms.CustomMultiSelectFormField(
        label="Microcalcificaciones(todas las que apliquen)",
        required = True,
        choices=mama_cdis_model_choices.Microcalcificaciones2Choices.choices
    )
    
    #Otros hallazgos histológicos
    otros_hallazgos_histologicos = CharField(
        label="Otros hallazgos histológicos",
        max_length=5000,
        required=False,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    otros_estudios_ihq = CharField(
        required = False,
        label="Otros estudios: IHQ",
        max_length = 5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    comentarios = CharField(
        required=False,
        label="Comentarios",
        max_length = 5000,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    diagnosticado_por = CharField(
        required=False,
        label="Diagnosticado por",
        max_length = 1000,
    )
    
    class Meta:
        model = MamaCDISBiopsyDiagnostic
        fields = "__all__"
        default_permissions = ()
