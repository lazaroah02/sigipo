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
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import (
    stomac_model_choices,
)
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_stomac import (
    StomacBiopsyDiagnostic,
)


class StomacBiopsyDiagnosticForm(ModelForm):
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

    # A.Información clínica recibida en el departamento de Anatomía Patológica.

    # tipo muestra
    tipo_muestra = EmptyChoiceField(
        empty_label="Seleccionar Tipo de muestra",
        choices=stomac_model_choices.TipoDeMuestraChoices.choices,
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
        choices=stomac_model_choices.SitioTumorChoices.choices,
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
    tipo_histologico = EmptyChoiceField(
        empty_label="Seleccionar Tipo Histológico",
        choices=stomac_model_choices.TipoHistologicoChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo Histológico*",
        required=True,
    )
    tipo_histologico_otro = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro Tipo Histológico (especifique):",
    )

    # Grado Histológico
    grado_histologico = EmptyChoiceField(
        empty_label="Seleccionar Grado Histológico",
        choices=stomac_model_choices.GradoHistologicoChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""El Grado Histológico:""",
        required=True,
    )
    grado_histologico_otro = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="Otro Grado Histológico (especifique):",
    )

    # La Extensión del Tumor
    extension_tumor = EmptyChoiceField(
        empty_label="Seleccionar La Extensión del Tumor",
        choices=stomac_model_choices.ExtensionTumorChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""La Extensión del Tumor:*""",
        required=True,
    )
    estructuras_adyacentes_invadidas = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""El tumor invade a estructuras/órganos adyacentes(especifique). Las estructuras adyacentes del estómago incluyen el bazo, el colon
            transverso, el hígado, el diafragma, el páncreas, la pared abdominal, la glándula suprarrenal, renale intestino delgado, y el retroperitoneo.
            La extensión intramural del duodeno o el esófago no es considerado invasión de una estructura adyacente, pero está clasificado usa la profundidad de la máxima invasión en cualquier
            de estos sitios.""",
    )

    # LOS MARGENES
    # ******Use esta seccion si todos los márgenes son involucrados y todos los márgenes pueden ser evaluados)******.
    todos_los_margenes_involucrados = BooleanField(
        label="""Todos los márgenes son involucrados por carcinoma invasor y displasia""",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )

    margenes_examinados = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""Los márgenes examinados. Nota: Los márgenes pueden incluir a proximal, distal, omental(radial), mucosal, profundidad y otros.""",
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
    # Solo para especímenes de gastrectomía
    margen_proximal = EmptyChoiceField(
        empty_label="Seleccionar Margen Proximal",
        choices=stomac_model_choices.MargenProximalChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Proximal(Solo para especímenes de gastrectomía)""",
        required=False,
    )
    margen_distal = EmptyChoiceField(
        empty_label="Seleccionar Margen Distal",
        choices=stomac_model_choices.MargenDistalChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Distal(Solo para especímenes de gastrectomía)""",
        required=False,
    )
    margen_radial = EmptyChoiceField(
        empty_label="Seleccionar Margen Radial",
        choices=stomac_model_choices.MargenRadialChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Márgenes Omental(Radial)(Solo para especímenes de gastrectomía)""",
        required=False,
    )
    mayor_margen_omental = FloatField(
        label="""El + que el Mayor margen del omental involucró por carcinoma del invasive""",
        required=False,
    )
    inferior_margen_omental = FloatField(
        label="""El + que el margen Inferior del omental involucró por carcinoma del invasive""",
        required=False,
    )
    otros_margenes_gastrectomia = CharField(
        max_length=5000,
        widget=Textarea(attrs={"class": "form-control"}),
        required=False,
        label="""Otro Margen(s) (requerido único si aplicable). Especifique""",
    )
    otros_margenes_gastrectomia_especificaciones = EmptyChoiceField(
        empty_label="Seleccionar",
        choices=stomac_model_choices.OtrosMargenesGastrectomiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Otro Margen(s) clasificación""",
        required=False,
    )
    # Para especímenes sólo de resección del endoscopic(RE)
    margen_mucosal = EmptyChoiceField(
        empty_label="Seleccionar Margen Mucosal",
        choices=stomac_model_choices.MargenMucosalChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Mucosal(Para especímenes sólo de resección del endoscopic)""",
        required=False,
    )
    margen_profundo = EmptyChoiceField(
        empty_label="Seleccionar Margen Profundo",
        choices=stomac_model_choices.MargenProfundoChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Margen Profundo(Para especímenes sólo de resección del endoscopic)""",
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
        choices=stomac_model_choices.OtrosMargenesREChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Otro Margen(s) Clasificacicación""",
        required=False,
    )

    # Invasión Linfovascular
    invasion_linfovascular = EmptyChoiceField(
        empty_label="Seleccionar Invasión Linfovascular",
        choices=stomac_model_choices.InvasionLinfovascularChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Invasión Linfovascular""",
        required=True,
    )

    # Invasión Perineural
    invasion_perineural = EmptyChoiceField(
        empty_label="Seleccionar Invasión Perineural",
        choices=stomac_model_choices.InvasionPerineuralChoices.choices,
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
        choices=stomac_model_choices.ClasificacionTumorChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="""Clasificación Tumor""",
        required=True,
    )

    class Meta:
        model = StomacBiopsyDiagnostic
        fields = "__all__"
        default_permissions = ()
