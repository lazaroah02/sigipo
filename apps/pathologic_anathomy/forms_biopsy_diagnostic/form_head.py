from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    CheckboxSelectMultiple,
    FloatField,
    IntegerField,
    MultipleChoiceField,
    Select,
    Textarea,
)

from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import head_model_choices
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_head import Head


class HeadBiopsyForm(ModelForm):
    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA
    # tipo de muestra
    tipo_muestra = EmptyChoiceField(
        empty_label="Seleccionar Tipo de muestra",
        choices=head_model_choices.TipoMuestraTiroidesChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo de muestra*",
        required=True,
    )
    tipo_extension_parcial = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        label="Tipo de extensión parcial(en caso de haber seleccionado 'Extensión parcial')",
        required=False,
    )

    # focalidad del tumor
    focalidad_tumor = EmptyChoiceField(
        empty_label="Seleccionar Focalidad del Tumor",
        choices=head_model_choices.FocalidadTumorChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Focalidad del tumor*",
        required=True,
    )

    # sitio o localizacion del tumor
    localizacion_tumor = MultipleChoiceField(
        label="Localización del Tumor*",
        choices=head_model_choices.SITIO_TUMOR_CHOICES,
        widget=CheckboxSelectMultiple(attrs={}),
        required=True,
    )
    localizacion_tumor_otro = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otra localización (especificar)",
    )

    # tumor size
    max_tumor_size = FloatField(
        label="La máxima dimensión del tumor (centímetros)*:", required=True
    )
    additional_tumor_size = FloatField(
        label="Las dimensiones adicionales del tumor (centímetros)*:", required=True
    )
    tumor_size_imposible_to_determinate = CharField(
        label="Dimensiones imposibles de determinar. Explique porque:",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
    )

    # TIPOS HISTOLOGICOS
    # Carcinoma papilar
    carcinoma_papilar = EmptyChoiceField(
        empty_label="Seleccionar Carcinoma Papilar",
        choices=head_model_choices.CarcinomaPapilarChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Carcinoma Papilar*:",
        required=True,
    )

    # carcinomas foliculares
    carcinomas_foliculares = EmptyChoiceField(
        empty_label="Seleccionar Carcinoma Foliculares",
        choices=head_model_choices.CarcinomaFolicularChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Carcinoma Foliculares*:",
        required=True,
    )
    otro_tipo_carcinoma_folicular = CharField(
        label="Otro tipo del histológico que no figura en la lista (especifique):",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
    )

    # margenes
    margenes = EmptyChoiceField(
        empty_label="Seleccionar Los Margenes",
        choices=head_model_choices.MargenesChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Los Margenes*:",
        required=True,
    )
    distancia_carcinoma_mas_cercano = FloatField(
        label="La distancia del carcinoma invasivo de los  márgenes más cercano (milímetros):",
        required=False,
    )
    sitios_invasion = CharField(
        label="Sitio(s) de Invasión:",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
    )

    # invasion vascular
    invasion_vascular = EmptyChoiceField(
        empty_label="Seleccionar Invasion Vacular",
        choices=head_model_choices.InvasionVascularChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Invasion Vacular*:",
        required=True,
    )

    # invasion linfatica(nota j)
    invasion_linfatica = EmptyChoiceField(
        empty_label="Seleccionar Invasión Linfática",
        choices=head_model_choices.InvasionVascularChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Invasión Linfática (Nota J)*:",
        required=True,
    )

    # indice de mitosis
    indice_mitosis = FloatField(
        label="""Índice de mitosis (por 2 mm^2):
            Nota: La Mitosis debería ser contada en 10 campos de alto poder consecutivos (HPF) a 400x en el área más activa de mitosis.
            Para la mayoría de los microscopios, 10 (HPF) es aproximadamente equivalente a 2.5 mm2""",
        required=True,
    )

    # invasion peri-neural
    invasion_perineural = EmptyChoiceField(
        empty_label="Seleccionar Invasión peri-neural",
        choices=head_model_choices.InvasionPerineuralChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Invasión peri-neural*:",
        required=True,
    )

    # extension extra-tiroidea
    extension_extratiroidea = EmptyChoiceField(
        empty_label="Seleccionar Extensión Extra-tiroidea:",
        choices=head_model_choices.ExtensionExtratiroideaChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Extensión Extra-tiroidea*:",
        required=True,
    )
    extension = EmptyChoiceField(
        empty_label="Seleccionar Invasiñon de la Extensión",
        choices=head_model_choices.ExtensionChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="La extensión (requiere clínica /invasión macroscópica y microscópica del tumor):",
        required=True,
    )

    # Ganglios Linfáticos Regionales
    ganglio_linfatico_encontrado = BooleanField(
        label="Ganglio linfático presente o encontrado*",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=True,
    )

    # Examen del ganglio linfatico(El examen del ganglio linfático (es únicamente requerido si hay ganglios linfáticos presentes en el espécimen))
    num_ganglios_linfaticos = IntegerField(
        label="Número de Ganglios linfáticos involucrados", required=False
    )
    num_ganglios_no_determinados = CharField(
        label="El número de ganglios no puede ser determinado (explique):",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
    )
    niveles_ganglionares = MultipleChoiceField(
        label="Especifique Niveles Ganglionares (seleccione todo lo que aplique)",
        choices=head_model_choices.NIVELES_GANGLIONARES_CHOICES,
        widget=CheckboxSelectMultiple(attrs={}),
        required=False,
    )
    niveles_ganglionares_otros = CharField(
        label="Otros niveles ganglionares (especifique):",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
    )
    num_ganglios_linfaticos_examinados = IntegerField(
        label="El Número de Ganglios Linfáticos Examinados:", required=False
    )
    num_ganglios_linfaticos_examinados_no_determinado = CharField(
        label="El número de Ganglios Linfáticos no puede ser determinado (explique):",
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Head
        fields = [
            "tipo_muestra",
        ]
        default_permissions = ()
