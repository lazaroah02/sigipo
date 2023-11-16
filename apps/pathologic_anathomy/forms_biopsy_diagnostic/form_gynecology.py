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
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import gynecology_model_choices
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_gynecology import GynecologyBiopsyDiagnostic

class GynecologyBiopsyForm(ModelForm):
    biopsy = ModelChoiceField(
        queryset=BiopsyRequest.objects.all(),
        widget=Select(
            attrs={
                "class": "form-control",
                "data-placeholder": "Biopsia",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
        ),
        label="Biopcia",
        required=True,
    )
    
    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA
    
    #Cuello Uterino
    #El Procedimiento
    procedimiento = EmptyChoiceField(
        choices=gynecology_model_choices.ProcedimientoChoices.choices,
        label="El Procedimiento",
        empty_label="Seleccionar el procedimiento",
        widget=Select(attrs={"class": "form-control form-select"}),
        required = True
    )
    procedimiento_otro = CharField(
        max_length = 5000, 
        required = False, 
        label = "Otro procedimiento(especifique):",
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #El sitio del Tumor (seleccione todo lo que aplique) 
    sitio_tumor = forms.CustomMultiSelectFormField(
        required = True,
        label = "El sitio del Tumor (seleccione todo lo que aplique)",
        choices = gynecology_model_choices.SITIO_TUMOR_CHOICES
    )
    sitio_no_determinado = CharField(
        max_length=5000, 
        required = False,
        label = "El sitio del tumor no puede ser determinado(explique):",
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #El Tamaño del Tumor 
    tumor_max_size = FloatField(
        label = "La máxima dimensión del tumor(centímetros)",
        required = False
    )
    additional_tumor_size = FloatField(
        label = "Las dimensiones adicionales del tumor(centímetros)",
        required = False
    )
    size_no_determinado = CharField(
        max_length=5000, 
        required = False, 
        widget=Textarea(attrs={"class": "form-control"}),
        label="Las dimensiones no pueden ser determinadas(explique): "
    )
    
    #Información Anatomopatológica.
    #El Tipo del Histológico
    tipo_histologico = EmptyChoiceField(
        choices=gynecology_model_choices.TipoHistologicoChoices.choices,
        label="El Tipo del Histológico",
        empty_label="Seleccionar el Tipo Histológico",
        required = True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    tipo_histologico_otro = CharField(
        max_length=5000, 
        required = False, 
        label="Otro tipo histologico que no figura en la lista (especifique): ",
        widget=Textarea(attrs={"class": "form-control"}),
    )
    
    #El Grado del Histológico
    grado_histologico = EmptyChoiceField(
        choices=gynecology_model_choices.GradoHistologicoChoices.choices,
        label="El Grado del Histológico",
        widget=Select(attrs={"class": "form-control form-select"}),
        empty_label="Seleccionar el Grado Histológico",
        required = True,
    )
    
    #Invasión del Estroma
    mm_invasion_en_profundidad = FloatField(
        label="mm de invasión en profundidad",
        required = False,
    )
    invasion_en_profundidad = CharField(
        max_length=5000, 
        required = False, 
        label="Invasión en profundidad: ",
        widget=Textarea(attrs={"class": "form-control"}),
    )
    profundidad_no_determinada = CharField(
        max_length=5000, 
        required = False, 
        label="La profundidad no puede ser determinada(explique):",
        widget=Textarea(attrs={"class": "form-control"}),
    )
    extensio_horizontal = FloatField(
        label="Extensión horizontal(mm)",
        required=False
    )
    longitud_longitudinal  =FloatField(
        label="Longitud longitudinal(mm)",
        required = False
    )
    extension_longitud_no_determinada = CharField(
        max_length=5000, 
        required = False, 
        label="La extensión no puede ser determinada(explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    extensio_horizontal = FloatField(
        label="Extensión horizontal(mm)",
        required = False
    )
    anchura_circunferencial = FloatField(
        label="Anchura circunferencial(mm)",
        required = False
    )
    extension_anchura_no_determinada = CharField(
        max_length=5000, 
        required = False, 
        label="La extensión no puede ser determinada (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #Los Márgenes
    #Margen endocervical
    margen_endocervical_no_puede_evaluarce = BooleanField(
        label = "Margen Endocervical no puede ser evaluado",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    margen_endocervical_no_evaluado_explique = CharField(
        max_length=5000, 
        required = False, 
        label="Margen Endocervical no puede ser evaluado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    margen_endocervical_no_afectado = BooleanField(
        label = "Margen Endocervical no afectado",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    margen_endocervical_distancia_carcinoma = FloatField(
        label = "La distancia del carcinoma al margen(mm)",
        required=False
    )
    margen_endocervical_afectado_por = forms.CustomMultiSelectFormField(
        required = False,
        label = "Afectado por:",
        choices = gynecology_model_choices.MARGEN_AFECTACION_CHOICES
    )
    margen_endocervical_posicion_especifica = CharField(
        max_length=5000, 
        required = False, 
        label="La posición especifica(si es posible):",
        widget=Textarea(attrs={"class": "form-control"})
    )

    #Margen ectocervical 
    margen_ectocervical_no_puede_evaluarce = BooleanField(
        required = False,
        label = "Margen Ectocervical no puede ser evaluado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    margen_ectocervical_no_evaluado_explique = CharField(
        max_length=5000, 
        required = False, 
        label="Margen Ectocervical no puede ser evaluado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    margen_ectocervical_no_afectado = BooleanField(
        required = False,
        label = "Margen Ectocervical no afectado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    margen_ectocervical_distancia_carcinoma = FloatField(
        label = "La distancia del carcinoma al margen ectocervical(mm)",
        required = False
    )
    margen_ectocervical_afectado_por = forms.CustomMultiSelectFormField(
        choices = gynecology_model_choices.MARGEN_AFECTACION_CHOICES,
        label = "Afectado por:",
        required = False,
    )
    margen_ectocervical_posicion_especifica = CharField(
        max_length=5000, 
        required = False, 
        label="La posición especifica(si es posible):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #El Margen Profundo 
    margen_profundo_no_puede_evaluarce = BooleanField(
        required=False,
        label = "Margen Profundo no puede ser evaluado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    margen_profundo_no_evaluado_explique = CharField(
        max_length=5000, 
        required = False, 
        label="Margen Profundo no puede ser evaluado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    margen_profundo_no_afectado = BooleanField(
        required=False,
        label = "Margen Profundo no afectado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    margen_profundo_distancia_carcinoma = FloatField(
        label = "La distancia del carcinoma al margen profundo(mm)",
        required = False
    )
    margen_profundo_afectado_por = forms.CustomMultiSelectFormField(
        max_length = 100,
        required = False,
        label = "Afectado por:",
        choices = gynecology_model_choices.MARGEN_AFECTACION_CHOICES
    )
    margen_profundo_posicion_especifica = CharField(
        max_length=5000, 
        required = False, 
        label="La posición especifica(si es posible):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #La Invasión del Lymphovascular 
    invasion_limphovascular = EmptyChoiceField(
        choices=gynecology_model_choices.InvasionLymphovascularChoices.choices,
        label = "La Invasión del Lymphovascular",
        required=True,
        empty_label="SeleccionaInvasión del Lymphovascular",
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Otra patología asociada(seleccione todo lo que aplique)
    otra_patologia_asociada = forms.CustomMultiSelectFormField(
        label="Otra patología asociada(seleccione todo lo que aplique)",
        required = True,
        choices = gynecology_model_choices.OTRA_PATOLOGIA_ASOCIADA_CHOICES
    )
    otra_patologia_asociada_especifique = CharField(
        max_length=5000, 
        required = False, 
        label="El otro del + (especifique): ",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #La resección
    reseccion = EmptyChoiceField(
        choices = gynecology_model_choices.ReseccionChoices.choices,
        label="La resección",
        empty_label = "Seleccione la resección",
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    exenteracion_pelvica_especifique = CharField(
        max_length=5000, 
        required = False, 
        label="Exenteración pélvica(especifique órganos incluidos): ",
        widget=Textarea(attrs={"class": "form-control"})
    )
    otra_reseccion_especifique = CharField(
        max_length=5000, 
        required = False, 
        label="Otra Resección(especifique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #Tipo Hysterectomy
    tipo_hysterectomy = EmptyChoiceField(
        label="Tipo Hysterectomy",
        empty_label="Seleccione Tipo Hysterectomy",
        choices=gynecology_model_choices.TipoHysterectomyChoices.choices,
        required=True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    otro_tipo_hysterectomy = CharField(
        max_length=5000, 
        required = False, 
        label="Otro del + (especifique): ",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #Afectación de otros órganos
    afectacion_otros_organos = EmptyChoiceField(
        label="Afectación de otros órganos",
        empty_label="Seleccione Afectación de otros órganos",
        choices=gynecology_model_choices.AfectacionOtrosOrganosChoices.choices,
        required = True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    afectacion_otro_organo = CharField(
        max_length=5000, 
        required = False, 
        label="Afectación de otro órgano(especifique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    afectacion_no_determinada = CharField(
        max_length=5000, 
        required = False, 
        label="Afectación no puede ser determinada(explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #Los Márgenes(la Nota F)
    #Ectocervical Margin
    ectocervical_margin_no_puede_evaluarce = BooleanField(
        label="Ectocervical Margin no puede ser evaluado",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    ectocervical_margin_no_evaluado_especif = CharField(
        max_length=5000, 
        required = False, 
        label="Ectocervical Margin no puede ser evaluado (explique)",
        widget=Textarea(attrs={"class": "form-control"})
    )
    ectocervical_uninvol_carci_invasive = BooleanField(
        label="Uninvolved por carcinoma del invasive",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    ectocervical_margin_distancia_carcinoma = FloatField(
        label="La distancia del + de carcinoma del invasive de margen(los milímetros):",
        required = False
    )
    ectocervical_margin_posicion_specify1 = CharField(
        max_length=5000, 
        required = False, 
        label="El + la posición(especificar):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    ectocervical_involucrado_carcinoma_invasive = BooleanField(
        label="Involucrado por carcinoma del invasive",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    ectocervical_especifique_posicion = CharField(
        max_length=5000, 
        required = False, 
        label="Especifique posición(si es posible)",
        widget=Textarea(attrs={"class": "form-control"})
    )
    ectocervical_uninvolved_intra_neop = BooleanField(
        label="Uninvolved por intraepithelial neoplasia",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    ectocervical_invol_lesion_escam = BooleanField(
        label = "Involucrado por lesión escamosa (CIN 2-3) del intraepithelial de calidad superior",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    ectocervical_margin_posicion_specify2 = CharField(
        max_length=5000, 
        required = False, 
        label="El + la posición(especificar):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    ectocervical_invol_adenocarcinoma = BooleanField(
        label = "Involucrado por adenocarcinoma en situ(las IAs)",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    ectocervical_margin_posicion_specify3 = CharField(
        max_length=5000, 
        required = False, 
        label="El + la posición(especificar):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #El Margen Radial (Circunferencial)
    radial_margin_no_puede_evaluarce = BooleanField(
        label="Radial Margin no puede ser evaluado",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    radial_margin_no_evaluado_especif = CharField(
        max_length=5000, 
        required = False, 
        label="Radial Margin no puede ser evaluado (explique)",
        widget=Textarea(attrs={"class": "form-control"})
    )
    radial_uninvol_carci_invasive = BooleanField(
        label="Uninvolved por carcinoma del invasive",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    radial_margin_distancia_carcinoma = FloatField(
        label="La distancia del + de carcinoma del invasive de margen(los milímetros):",
        required = False
    )
    radial_margin_posicion_specify = CharField(
        max_length=5000, 
        required = False, 
        label="El + la posición(especificar):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    radial_involucrado_carcinoma_invasive = BooleanField(
        label="Involucrado por carcinoma del invasive",
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    radial_especifique_posicion = CharField(
        max_length=5000, 
        required = False, 
        label="Especifique posición(si es posible)",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    #La Invasión del Lymphovascular(la Nota G)
    #La Invasión del Lymphovascular 
    invasion_limphovascular_notaG = EmptyChoiceField(
        choices=gynecology_model_choices.InvasionLymphovascularNotaGChoices.choices,
        label = "La Invasión del Lymphovascular(la Nota G)",
        empty_label="Seleccione La Invasión del Lymphovascular(la Nota G)",
        required = True,
        widget=Select(attrs={"class": "form-control form-select"}),
    )
    
    #Los Ganglios Linfáticos Regionales
    '''
    Nota: Los ganglios linfáticos denominados como pélvico, parametrial, obturador, interno parte exterior ilíaco (hipo-gástrico), 
    ilíaco, común ilíaco El sacro, el presacro y para aórtico son considerados ganglios linfáticos regionales. 
    Cualquier otros nodos involucrados deberían ser clasificados en categorías como Las metástasis (pM1) y comentado en adentro 
    la sección distante de metástasis. La presencia de celdas del tumor aisladas no mayores que 0.2 El mm en ganglio linfático 
    regional (s) es considerado N0 (yo +). 
    '''
    ganglios_linfaticos_encontrados = BooleanField(
        required=False,
        label = "Ninguno de los ganglios linfáticos se sometieron o encontraron",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        )
    #El examen del ganglio linfático (requeridos únicos si los nodos de la linfa están presentes en espécimen)
    num_nodos_con_metastasis = IntegerField(
        label = "El número de Nodos con Metástasis (excluye a ITCs):",
        required = False
    )
    num_no_puede_determinarce = BooleanField(
        required = False,
        label = "El número no puede ser determinado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    num_no_determinado_especif = CharField(
        max_length=5000, 
        required = False, 
        label="El número no puede ser determinado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    num_nodos_celdas_aisladas = IntegerField(
        label = "El número de Nodos con Celdas Aisladas (ITCs) del Tumor (0.2 mm o menos) (si aplicable)",
        required = False
    )
    num_nodos_no_puede_determinarce = BooleanField(
        required = False,
        label = "El número no puede ser determinado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    num_nodos_no_determinado_especif = CharField(
        max_length=5000, 
        required = False, 
        label="El número de nodos no puede ser determinado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    num_ganglios_con_tumor = IntegerField(
        label = "Especifique el número de Ganglio Linfático(s) con Tumor (si aplicable)",
        required = False
    )
    total_num_nodos_examinados = IntegerField(
        label = "Número total de Nodo Examinado (el señalizador y el poco señalizador)",
        required = False
    )
    num_total_no_puede_determinarce = BooleanField(
        required = False,
        label = "El número no puede ser determinado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    num_total_no_determinado_especif = CharField(
        max_length=5000, 
        required = False, 
        label="El número no puede ser determinado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    sitios_especif = CharField(
        max_length=5000, 
        required = False, 
        label="Especifique Sitio(s)",
        widget=Textarea(attrs={"class": "form-control"})
    )
    num_nodos_senalizador_exami = IntegerField(
        label = "Numere de Nodos del Señalizador Examinados:",
        required = False
    )
    num_serial_no_puede_determinarce = BooleanField(
        required = False,
        label = "El número no puede ser determinado",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )
    num_serial_no_determinado_especif = CharField(
        max_length=5000, 
        required = False, 
        label="El número no puede ser determinado (explique):",
        widget=Textarea(attrs={"class": "form-control"})
    )
    
    class Meta:
        model = GynecologyBiopsyDiagnostic
        fields = "__all__"
        default_permissions = ()