from django.db import models

from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import (
    stomac_model_choices,
)


class StomacBiopsyDiagnostic(models.Model):
    biopsy = models.OneToOneField(
        "pathologic_anathomy.BiopsyRequest",
        on_delete=models.CASCADE,
        related_name="stomac_biopsy_diagnostic",
    )

    # A.Información clínica recibida en el departamento de Anatomía Patológica.
    # Tipo de muestra
    tipo_muestra = models.IntegerField(
        choices=stomac_model_choices.TipoDeMuestraChoices.choices,
        verbose_name="Tipo de Muestra",
    )
    tipo_muestra_otro = models.CharField(
        max_length=5000,
        verbose_name="Otro tipo de muestra (especifique)",
        blank=True,
        null=True,
    )

    # Sitio del Tumor
    sitio_tumor = models.IntegerField(
        choices=stomac_model_choices.SitioTumorChoices.choices,
        verbose_name="Sitio del Tumor",
    )
    sitio_tumor_otro = models.CharField(
        max_length=5000,
        verbose_name="Otro sitio del tumor (especifique)",
        blank=True,
        null=True,
    )

    # El Tamaño del Tumor
    tumor_max_size = models.FloatField(
        verbose_name="La Máxima Dimensión del Tumor (centímetros)",
    )
    tumor_size = models.FloatField(
        verbose_name="La Dimensión del Tumor (centímetros)",
    )
    no_puede_aplicable = models.CharField(
        max_length=5000,
        verbose_name="No puede aplicable (explique): ",
        blank=True,
        null=True,
    )

    # El Tipo Histológico
    tipo_histologico = models.IntegerField(
        choices=stomac_model_choices.TipoHistologicoChoices.choices,
        verbose_name="El Tipo Histológico",
    )
    tipo_histologico_otro = models.CharField(
        max_length=5000,
        verbose_name="Otro Tipo Histológico (especifique)",
        blank=True,
        null=True,
    )

    # El Grado del Histológico
    grado_histologico = models.IntegerField(
        choices=stomac_model_choices.GradoHistologicoChoices.choices,
        verbose_name="El Grado del Histológico",
    )
    grado_histologico_otro = models.CharField(
        max_length=5000,
        verbose_name="Otro Tipo Histológico (especifique)",
        blank=True,
        null=True,
    )

    # Extensión del Tumor
    extension_tumor = models.IntegerField(
        choices=stomac_model_choices.ExtensionTumorChoices.choices,
        verbose_name="Extensión del Tumor",
    )
    estructuras_adyacentes_invadidas = models.CharField(
        max_length=5000,
        verbose_name="""El tumor invade a estructuras/órganos adyacentes(especifique). Las estructuras adyacentes del estómago incluyen el bazo, el colon
            transverso, el hígado, el diafragma, el páncreas, la pared abdominal, la glándula suprarrenal, renale intestino delgado, y el retroperitoneo.
            La extensión intramural del duodeno o el esófago no es considerado invasión de una estructura adyacente, pero está clasificado usa la profundidad de la máxima invasión en cualquier
            de estos sitios.""",
        blank=True,
        null=True,
    )

    # Los Márgenes
    # Nota: Use esta sección sólo si todos los márgenes son involucrados y todos los márgenes pueden ser evaluados.
    todos_los_margenes_involucrados = models.BooleanField(
        verbose_name=""" Todos los márgenes son involucrados por carcinoma invasor y displasia""",
        default=False,
    )
    margenes_examinados = models.CharField(
        verbose_name="""Los márgenes examinados. Nota: Los márgenes pueden incluir a proximal, distal, omental(radial), mucosal, profundidad y otros.""",
        max_length=5000,
        blank=True,
        null=True,
    )
    distancia_carcinoma_invasivo_margen_cercano_cm = models.FloatField(
        verbose_name="""La distancia del carcinoma invasivo al margen más cercano
                (centímetros)""",
        blank=True,
        null=True,
    )
    distancia_carcinoma_invasivo_margen_cercano_mm = models.FloatField(
        verbose_name="""La distancia del carcinoma invasivo al margen más cercano
                (milímetros)""",
        blank=True,
        null=True,
    )
    margen_mas_cercano = models.CharField(
        verbose_name="""Especifique el margen más cercano:""",
        max_length=5000,
        blank=True,
        null=True,
    )
    # Solo para especímenes de gastrectomía
    margen_proximal = models.IntegerField(
        choices=stomac_model_choices.MargenProximalChoices.choices,
        verbose_name="""Margen Proximal(Solo para especímenes de gastrectomía)""",
        blank=True,
        null=True,
    )
    margen_distal = models.IntegerField(
        choices=stomac_model_choices.MargenDistalChoices.choices,
        verbose_name="Margen Distal(Solo para especímenes de gastrectomía)",
        blank=True,
        null=True,
    )
    margen_radial = models.IntegerField(
        choices=stomac_model_choices.MargenRadialChoices.choices,
        verbose_name="Márgenes Omental(Radial)(Solo para especímenes de gastrectomía)",
        blank=True,
        null=True,
    )
    mayor_margen_omental = models.FloatField(
        verbose_name="""El + que el Mayor margen del omental involucró por carcinoma del invasive""",
        blank=True,
        null=True,
    )
    inferior_margen_omental = models.FloatField(
        verbose_name="""El + que el margen Inferior del omental involucró por carcinoma del invasive""",
        blank=True,
        null=True,
    )
    otros_margenes_gastrectomia = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Otro Margen(s) (requerido único si aplicable). Especifique",
    )
    otros_margenes_gastrectomia_especificaciones = models.IntegerField(
        choices=stomac_model_choices.OtrosMargenesGastrectomiaChoices.choices,
        verbose_name="Otro Margen(s) Clasificación",
        blank=True,
        null=True,
    )
    # Para especímenes sólo de resección del endoscopic(RE)
    margen_mucosal = models.IntegerField(
        verbose_name="Margen Mucosal(Para especímenes sólo de resección del endoscopic)",
        choices=stomac_model_choices.MargenMucosalChoices.choices,
        blank=True,
        null=True,
    )
    margen_profundo = models.IntegerField(
        verbose_name="Margen Profundo(Para especímenes sólo de resección del endoscopic)",
        choices=stomac_model_choices.MargenProfundoChoices.choices,
        blank=True,
        null=True,
    )
    otros_margenes_RE = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Otro Margen(s) (requerido único si aplicable). Especifique",
    )
    otros_margenes_RE_especificaciones = models.IntegerField(
        choices=stomac_model_choices.OtrosMargenesREChoices.choices,
        verbose_name="Otro Margen(s) Clasificación",
        blank=True,
        null=True,
    )

    # La Invasión del Linfovascular
    invasion_linfovascular = models.IntegerField(
        verbose_name="Invasión Linfovascular",
        choices=stomac_model_choices.InvasionLinfovascularChoices.choices,
    )

    # Invasión Perineural
    invasion_perineural = models.IntegerField(
        verbose_name="Invasión Perineural",
        choices=stomac_model_choices.InvasionPerineuralChoices.choices,
    )

    # Ganglios Linfáticos Regionales
    ganglios_linfaticos_encontrados = models.BooleanField(
        verbose_name="Ganglios Linfáticos Encontrados",
        default=False,
    )

    # Examen del ganglio linfático (requerido solo si se marco la casilla anterior, es decir si los ganglios linfáticos están presentes en el espécimen)
    # Número de gânglios linfáticos Involucrados
    num_ganglios_linfaticos = models.IntegerField(
        verbose_name="Número de gânglios linfáticos Involucrados",
        blank=True,
        null=True,
    )
    # Num de ganglios no puede ser determinado
    num_ganglios_no_determinado = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El número de ganglios no puede ser determinado (explique)",
    )

    # clasificación del tumor
    clasificacion_tumor = models.IntegerField(
        choices=stomac_model_choices.ClasificacionTumorChoices.choices,
        verbose_name="Clasificación Tumor",
        default=1,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Diagnóstico Biopcia Digestivo(Estómago)"
        verbose_name_plural = "Diagnósticos Biopcia Digestivo(Estómago)"
        ordering = ["id"]

    def __str__(self):
        return f"Diagnóstico Biopcia Digestivo(Estómago) de la biopcia: {self.biopsy}"
