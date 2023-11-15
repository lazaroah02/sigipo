from django.forms import (
    BooleanField,
    CharField,
    CheckboxSelectMultiple,
    FloatField,
    ModelChoiceField,
    Select,
    Textarea,
)

from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.nuclear_medicine import forms
from apps.core.forms import ModelForm
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import linfoma_model_choices
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_linfoma import LinfomaBiopsyDiagnostic

class LinfomaBiopsyDiagnosticForm(ModelForm):
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
    
    #El espécimen (seleccione todo lo que aplique)
    especimen = forms.CustomMultiSelectFormField(
        label="El espécimen (seleccione todo lo que aplique)*",
        choices=linfoma_model_choices.ESPECIMEN_CHOICES,
        required=True,
    )
    otro_especimen = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro Espécimen (especifique)",
    )
    
    #El sitio del tumor (seleccione todo lo que aplique)
    sitio_tumor = forms.CustomMultiSelectFormField(
        label="El sitio del tumor (seleccione todo lo que aplique)*",
        choices=linfoma_model_choices.SITIO_TUMOR_CHOICES,
        required=True,
    )
    sitio_tumor_especificacion = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Especifique sitio(s) del tumor",
    )
    otro_tejido_fino_u_organo = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro tejido fino (s) u otro órgano (s) (especifique)",
    )
    no_especificado = BooleanField(
        label="No especificicado",
        required=False,
    )
    no_especificado_just = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="No especificado(justifique)",
    )
    
    #HistologicType (basada en la clasificación de 2008 quienes)
    histologic_type = EmptyChoiceField(
        empty_label="Seleccionar Histologic Type",
        choices=linfoma_model_choices.HistologicTypeChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Histologic Type (basada en la clasificación de 2008 quienes)*",
        required=True,
    )
    #Extensión Patológica del Tumor (seleccione todo lo que aplique)
    pathologic_tumor_extensions = forms.CustomMultiSelectFormField(
        label="Extensión Patológica del Tumor (seleccione todo lo que aplique)*",
        choices=linfoma_model_choices.PATHOLOGIC_TUMOR_EXTENSIONS,
        required=True,
    )
    #Inmunofenotipo (IHQ) en la lesión del sitio específico:
    inmunofenotipo = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Inmunofenotipo(IHQ) en la lesión del sitio específico:*",
    )
    inmunofenotipo_no_realizado = BooleanField(
        label="Inmunofenotipo no realizado",
        required=False,
    )
    #Especifique método(s) y resultados
    metodos_y_resultados = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Especifique método(s) y resultados:*",
    )
    
    #Factores Pronóstico e Índices (seleccione todo lo que aplique)
    #Puntuación de Pronóstico
    puntuacion_pronostico = FloatField(
        label="Puntuación de Pronóstico",
        required=True,
    )
    #Especificar el sistema utilizado
    sistema_utilizado = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Especificar el sistema utilizado:*",
    )
    
    class Meta:
        model = LinfomaBiopsyDiagnostic
        fields = [
            "biopsy",
            "especimen",
            "otro_especimen",
            "sitio_tumor",
            "sitio_tumor_especificacion",
            "otro_tejido_fino_u_organo",
            "no_especificado",
            "no_especificado_just",
            "histologic_type",
            "pathologic_tumor_extensions",
            "inmunofenotipo",
            "inmunofenotipo_no_realizado",
            "metodos_y_resultados",
            "puntuacion_pronostico",
            "sistema_utilizado",
        ]
        default_permissions = ()
