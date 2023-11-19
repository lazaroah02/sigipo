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
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import neck_model_choices
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_neck import (
    NeckBiopsyDiagnostic,
)


class NeckBiopsyDiagnosticForm(ModelForm):
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
        label="",
        required=True,
    )

    # A.Información clínica recibida en el departamento de Anatomía Patológica.

    # tipo muestra
    tipo_muestra = EmptyChoiceField(
        empty_label="Seleccionar Tipo de muestra",
        choices=neck_model_choices.TipoMuestraChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo de muestra*",
        required=True,
    )
    tipo_muestra_otro = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro tipo de muestra (especifique):",
    )

    # Sitio del Tumor
    sitio_tumor = EmptyChoiceField(
        empty_label="Seleccionar Sitio del Tumor",
        choices=neck_model_choices.SitioTumorChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Sitio del Tumor*",
        required=True,
    )
    sitio_tumor_otro = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro sitio del tumor (especifique):",
    )

    # Relación de Tumor con la unión Esophagogastric
    relacion_tumor_union = EmptyChoiceField(
        empty_label="Seleccionar Relación de Tumor con la unión Esophagogastric",
        choices=neck_model_choices.RelacionTumorUnionChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Relación de Tumor con la unión Esophagogastric*",
        required=True,
    )
    distancia_centro_tumor_union = FloatField(
        label="""El protocolo de cáncer del estómago si ya sea:
            (1) el tumor involucrara el EGJ, pero el punto medio es más que 2 cm del estómago proximal o
            (2) el punto medio está menos de 2 cm del estómago proximal, pero el tumor no involucra al EGJ.
            La distancia de centro del tumor a la unión esophagogastric (especifique, si aplicable) (los centímetros)
            """,
        required=False,
    )

    # El Tamaño del Tumor
    tumor_max_size = FloatField(
        label="""La Máxima Dimensión del Tumor (centímetros)""", required=True
    )
    tumor_size = FloatField(
        label="""La Dimensión del Tumor (centímetros)""", required=True
    )
    no_puede_aplicable = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="No puede aplicable (explique):",
    )

    # El Tipo de Histología
    tipo_histologia = EmptyChoiceField(
        empty_label="Seleccionar Tipo Histología",
        choices=neck_model_choices.TipoHistologiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo Histología. Nota:Seleccione esta opción sólo si el de células grande o célula pequeña no puede ser determinada",
        required=False,
    )
    tipo_histologico_otro = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro Tipo Histológico (especifique):",
    )

    # Grado Histológico
    grado_histolico = EmptyChoiceField(
        empty_label="Seleccionar Grado Histológico",
        choices=neck_model_choices.GradoHistologicoChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Grado Histológico (El grado grado histológico no es aplicable para el carcinoma adenoideo quistito,
            mucoepidermoide, el bien diferenciado, el tumor neuroendocrino y el carcinoma neuroendocrino)""",
        required=False,
    )

    # La Extensión del Tumor
    tumor_extension = EmptyChoiceField(
        empty_label="Seleccionar La Extensión del Tumor",
        choices=neck_model_choices.TumorExtensionChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""La Extensión del Tumor*.""",
        required=True,
    )
    estructuras_adyacentes_invadidas = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""El tumor invade a estructuras/órganos adyacentes(especifique). Las estructuras adyacentes del estómago incluyen
            la pleura, el pericardio, la vena ácigos, el diafragma, el peritoneo, la aorta, cuerpo vertebral y la vía aérea.""",
    )

    # LOS MARGENES
    # ******Use esta seccion si todos los márgenes son involucrados y todos los márgenes pueden ser evaluados)******.
    todos_los_margenes_involucrados = BooleanField(
        label="""Todos los márgenes son involucrados por carcinoma invasivo,
            displasia, y metaplasia intestinal""",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )

    margenes_examinados = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""Los márgenes examinados. Nota: Los márgenes pueden incluir a proximal, distal, radial, mucosal, en profundidad, y otros.""",
    )
    distancia_carcinoma_invasivo_margen_cercano_cm = FloatField(
        label="""La distancia del carcinoma invasivo al margen más cercano (centímetros)""",
        required=False,
    )
    distancia_carcinoma_invasivo_margen_cercano_mm = FloatField(
        label="""La distancia del carcinoma invasivo al margen más cercano (milímetros)""",
        required=False,
    )
    margen_mas_cercano = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""Especifique el margen más cercano:""",
    )
    # Solo para esophagectomia y esophagogastrectomia(EE)
    margen_proximal = EmptyChoiceField(
        empty_label="Seleccionar Margen Proximal",
        choices=neck_model_choices.MargenProximalChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Proximal (Solo para esophagectomia y esophagogastrectomia)""",
        required=False,
    )
    margen_distal = EmptyChoiceField(
        empty_label="Seleccionar Margen Distal",
        choices=neck_model_choices.MargenDistalChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Distal (Solo para esophagectomia y esophagogastrectomia)""",
        required=False,
    )
    margen_radial = EmptyChoiceField(
        empty_label="Seleccionar Margen Radial",
        choices=neck_model_choices.MargenRadialChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Radial (Solo para esophagectomia y esophagogastrectomia)""",
        required=False,
    )
    otros_margenes_EE = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""Otro Margen(s) para esophagectomia y esophagogastrectomia (requerido único si es aplicable). Especifique""",
    )
    otros_margenes_EE_especificaciones = EmptyChoiceField(
        empty_label="Seleccionar",
        choices=neck_model_choices.OtrosMargenesEsophagectomiaEsophagogastrectomiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Otro Margen(s) clasificación""",
        required=False,
    )
    # Para especímenes solo de resección endoscopica(RE)
    margen_mucosal = EmptyChoiceField(
        empty_label="Seleccionar Margen Mucosal",
        choices=neck_model_choices.MargenMucosalChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Mucosal(Para especímenes solo de resección endoscopica)""",
        required=False,
    )
    margen_profundo = EmptyChoiceField(
        empty_label="Seleccionar Margen Profundo",
        choices=neck_model_choices.MargenProfundoChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Profundo(Para especímenes solo de resección endoscopica)""",
        required=False,
    )
    otros_margenes_RE = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""Otro Margen(s) para especímenes solo de resección endoscopica (requerido único si es aplicable). Especifique""",
    )
    otros_margenes_RE_especificaciones = EmptyChoiceField(
        empty_label="Seleccionar",
        choices=neck_model_choices.OtrosMargenesReseccionEndoscopicaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Otro Margen(s) Clasificacicación""",
        required=False,
    )

    # Invasión Linfovascular
    invasion_linfovascular = EmptyChoiceField(
        empty_label="Seleccionar Invasión Linfovascular",
        choices=neck_model_choices.InvasionLinfovascularChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Invasión Linfovascular""",
        required=True,
    )

    # Invasión Perineural
    invasion_perineural = EmptyChoiceField(
        empty_label="Seleccionar Invasión Perineural",
        choices=neck_model_choices.InvasionPerineuralChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Invasión Perineural""",
        required=True,
    )

    # Ganglios Linfáticos Regionales
    ganglios_linfaticos_encontrados = BooleanField(
        label="Ganglios Linfáticos Encontrados",
        required=False,
    )

    # Examen del ganglio linfático (requerido solo si se marco la casilla anterior, es decir si los ganglios linfáticos están presentes en el espécimen)
    # Número de gânglios linfáticos Involucrados
    num_ganglios_linfaticos = IntegerField(
        label="""
            ***EXAMEN DEL GANGLIO LINFÁTICO (requerido solo si se marco la casilla anterior, es decir si los ganglios
            linfáticos están presentes en el espécimen).***
            Número de gânglios linfáticos Involucrados
            """,
        required=False,
    )
    # Num de ganglios no puede ser determinado
    num_ganglios_no_determinado = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""El número de ganglios no puede ser determinado (explique)""",
    )

    # clasificación del tumor
    clasificacion_tumor = EmptyChoiceField(
        empty_label="Seleccionar Clasificación Tumor",
        choices=neck_model_choices.ClasificacionTumorChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Clasificación Tumor""",
        required=True,
    )

    class Meta:
        model = NeckBiopsyDiagnostic
        fields = "__all__"
        default_permissions = ()
