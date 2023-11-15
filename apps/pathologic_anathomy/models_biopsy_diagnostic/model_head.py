from django.db import models

from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import head_model_choices


class Head(models.Model):
    """
    Diagnostic model of head (Tiroides)
    """

    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA

    # tipo de muestra
    biopsy = models.OneToOneField(
        "pathologic_anathomy.BiopsyRequest",
        on_delete=models.CASCADE,
        related_name="biopsy_diagnostic_head",
    )
    tipo_muestra = models.IntegerField(
        choices=head_model_choices.TipoMuestraTiroidesChoice.choices,
        verbose_name="Tipo de muestra:",
    )
    tipo_extension_parcial = models.CharField(
        max_length=5000, blank=True, null=True, verbose_name="Tipo de extensión parcial"
    )

    # focalidad del tumor
    focalidad_tumor = models.IntegerField(
        choices=head_model_choices.FocalidadTumorChoice.choices,
        verbose_name="Focalidad del Tumor:",
    )

    # sitio o localizacion del tumor
    localizacion_tumor = models.CharField(
        verbose_name="El sitio (o localización) del tumor (seleccione todo lo que aplique):",
        max_length=100,
    )
    localizacion_tumor_otro = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otra localización del tumor (especificar)",
    )

    # tumor size
    max_tumor_size = models.FloatField(
        verbose_name="La máxima dimensión del tumor en centímetros:",
    )
    aditional_tumor_size = models.FloatField(
        verbose_name="Las dimensiones adicionales del tumor (centímetros):", default=0
    )
    tumor_size_imposible_to_determinate = models.CharField(
        verbose_name="Dimensiones imposibles de determinar. Explique porque:",
        max_length=5000,
        blank=True,
        null=True,
    )

    # TIPOS HISTOLOGICOS

    # Carcinoma papilar
    carcinoma_papilar = models.IntegerField(
        choices=head_model_choices.CarcinomaPapilarChoice.choices,
        verbose_name="Carcinoma Papilar:",
    )

    # carcinomas foliculares
    carcinomas_foliculares = models.IntegerField(
        choices=head_model_choices.CarcinomaFolicularChoice.choices,
        verbose_name="Carcinomas Foliculares",
    )
    otro_tipo_carcinoma_folicular = models.CharField(
        max_length=5000,
        verbose_name="Otro tipo del histológico que no figura en la lista (especifique): ",
        blank=True,
        null=True,
    )

    # margenes
    margenes = models.IntegerField(
        choices=head_model_choices.MargenesChoice.choices, verbose_name="Los Margenes"
    )
    distancia_carcinoma_mas_cercano = models.FloatField(
        verbose_name="La distancia del carcinoma invasivo de los  márgenes más cercano (milímetros):",
        blank=True,
        null=True,
    )
    sitios_invasion = models.CharField(
        max_length=5000, blank=True, null=True, verbose_name="Sitio(s) de Invasión:"
    )

    # invasion vascular
    invasion_vascular = models.IntegerField(
        choices=head_model_choices.InvasionVascularChoice.choices,
        verbose_name="Invasion Vacular",
    )

    # invasion linfatica(nota j)
    invasion_linfatica = models.IntegerField(
        choices=head_model_choices.InvasionLinfaticaChoice.choices,
        verbose_name="Invasión Linfática (Nota J)",
    )

    # indice de mitosis
    indice_mitosis = models.FloatField(
        verbose_name="""Índice de mitosis por 2 mm2:
        Nota: La Mitosis debería ser contada en 10 campos de alto poder consecutivos (HPF) a 400x en el área más activa de mitosis.
        Para la mayoría de los microscopios, 10 (HPF) es aproximadamente equivalente a 2.5 mm2""",
        default=0,
    )

    # invasion peri-neural
    invasion_perineural = models.IntegerField(
        choices=head_model_choices.InvasionPerineuralChoice.choices,
        verbose_name="Invasión peri-neural",
    )

    # extension extra-tiroidea
    extension_extratiroidea = models.IntegerField(
        choices=head_model_choices.ExtensionExtratiroideaChoice.choices,
        verbose_name="Extensión Extra-tiroidea:",
    )
    extension = models.IntegerField(
        choices=head_model_choices.ExtensionChoices.choices,
        blank=True,
        null=True,
        verbose_name="La extensión (requiere clínica /invasión macroscópica y microscópica del tumor):",
    )

    # Ganglios Linfáticos Regionales
    ganglio_linfatico_encontrado = models.BooleanField(
        default=False, verbose_name="Ganglio linfático presente o encontrado"
    )

    # Examen del ganglio linfatico(El examen del ganglio linfático (es únicamente requerido si hay ganglios linfáticos presentes en el espécimen))
    num_ganglios_linfaticos = models.IntegerField(
        verbose_name="Número de Ganglios linfáticos involucrados", blank=True, null=True
    )
    num_ganglios_no_determinados = models.CharField(
        max_length=5000,
        verbose_name="El número de ganglios no puede ser determinado (explique):",
        blank=True,
        null=True,
    )
    niveles_ganglionares = models.CharField(
        verbose_name="Especifique Niveles Ganglionares (seleccione todo lo que aplique)",
        max_length=100,
    )
    niveles_ganglionares_otros = models.CharField(
        max_length=5000,
        verbose_name="Otros niveles ganglionares",
        blank=True,
        null=True,
    )
    num_ganglios_linfaticos_examinados = models.IntegerField(
        verbose_name="El Número de Ganglios Linfáticos Examinados: "
    )
    num_ganglios_linfaticos_examinados_no_determinado = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El número de Ganglios Linfáticos no puede ser determinado (explique): ",
    )

    # clasificación del tumor
    clasificacion_tumor = models.IntegerField(
        choices=head_model_choices.ClasificacionTumorChoices.choices,
        verbose_name="Clasificación Tumor",
        default=1
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Diagnostico Biopcia de Cabeza(Tiroides)"
        verbose_name_plural = "Diagnosticos Biopcias de Cabeza(Tiroides)"
        ordering = ["id"]

    def __str__(self):
        return f"Diagnostico de la cabeza(tiroides) de la biopcia: {self.biopsy}"
