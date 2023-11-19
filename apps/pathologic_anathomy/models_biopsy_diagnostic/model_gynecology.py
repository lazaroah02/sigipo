from django.db import models
from multiselectfield import MultiSelectField

from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import (
    gynecology_model_choices,
)


class GynecologyBiopsyDiagnostic(models.Model):
    """
    Gynecology(Cervix) Biopsy Diagnostic Model
    """

    biopsy = models.OneToOneField(
        "pathologic_anathomy.BiopsyRequest",
        on_delete=models.CASCADE,
        related_name="biopsy_diagnostic_gynecology",
    )
    # INFORMACION CLINICA RECIVIDA EN EL DEPARTAMENTEO DE ANATOMIA PATOLOGICA

    # Cuello Uterino
    # El Procedimiento
    procedimiento = models.IntegerField(
        choices=gynecology_model_choices.ProcedimientoChoices.choices,
        verbose_name="El Procedimiento",
    )
    procedimiento_otro = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otro procedimiento(especifique): ",
    )

    # El sitio del Tumor (seleccione todo lo que aplique)
    sitio_tumor = MultiSelectField(
        max_length=100,
        verbose_name="El sitio del Tumor (seleccione todo lo que aplique)",
        choices=gynecology_model_choices.SitioTumorChoices.choices,
        min_choices=1,
    )
    sitio_no_determinado = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El sitio del tumor no puede ser determinado(explique): ",
    )

    # El Tamaño del Tumor
    tumor_max_size = models.FloatField(
        verbose_name="La máxima dimensión del tumor(centímetros)", blank=True, null=True
    )
    additional_tumor_size = models.FloatField(
        verbose_name="Las dimensiones adicionales del tumor(centímetros)",
        blank=True,
        null=True,
    )
    size_no_determinado = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Las dimensiones no pueden ser determinadas(explique): ",
    )

    # Información Anatomopatológica.
    # El Tipo del Histológico
    tipo_histologico = models.IntegerField(
        choices=gynecology_model_choices.TipoHistologicoChoices.choices,
        verbose_name="El Tipo del Histológico",
    )
    tipo_histologico_otro = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otro tipo histologico que no figura en la lista (especifique): ",
    )

    # El Grado del Histológico
    grado_histologico = models.IntegerField(
        choices=gynecology_model_choices.GradoHistologicoChoices.choices,
        verbose_name="El Grado del Histológico",
    )

    # Invasión del Estroma
    mm_invasion_en_profundidad = models.FloatField(
        verbose_name="mm de invasión en profundidad", blank=True, null=True
    )
    invasion_en_profundidad = models.CharField(
        max_length=5000, blank=True, null=True, verbose_name="Invasión en profundidad: "
    )
    profundidad_no_determinada = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="La profundidad no puede ser determinada(explique):",
    )
    extensio_horizontal = models.FloatField(
        verbose_name="Extensión horizontal(mm)", blank=True, null=True
    )
    longitud_longitudinal = models.FloatField(
        verbose_name="Longitud longitudinal(mm)", blank=True, null=True
    )
    extension_longitud_no_determinada = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="La extensión no puede ser determinada(explique):",
    )
    extensio_horizontal = models.FloatField(
        verbose_name="Extensión horizontal(mm)", blank=True, null=True
    )
    anchura_circunferencial = models.FloatField(
        verbose_name="Anchura circunferencial(mm)", blank=True, null=True
    )
    extension_anchura_no_determinada = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="La extensión no puede ser determinada (explique):",
    )

    # Los Márgenes
    # Margen endocervical
    margen_endocervical_no_puede_evaluarce = models.BooleanField(
        default=False, verbose_name="Margen Endocervical no puede ser evaluado"
    )
    margen_endocervical_no_evaluado_explique = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Margen Endocervical no puede ser evaluado (explique):",
    )
    margen_endocervical_no_afectado = models.BooleanField(
        default=False, verbose_name="Margen Endocervical no afectado"
    )
    margen_endocervical_distancia_carcinoma = models.FloatField(
        verbose_name="La distancia del carcinoma al margen(mm)",
        blank=True,
        null=True,
    )
    margen_endocervical_afectado_por = MultiSelectField(
        choices=gynecology_model_choices.MargenAfectacionChoices.choices,
        max_length=100,
        min_choices=0,
        verbose_name="Afectado por:",
    )
    margen_endocervical_posicion_especifica = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="La posición especifica(si es posible):",
    )

    # Margen ectocervical
    margen_ectocervical_no_puede_evaluarce = models.BooleanField(
        default=False, verbose_name="Margen Ectocervical no puede ser evaluado"
    )
    margen_ectocervical_no_evaluado_explique = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Margen Ectocervical no puede ser evaluado (explique):",
    )
    margen_ectocervical_no_afectado = models.BooleanField(
        default=False, verbose_name="Margen Ectocervical no afectado"
    )
    margen_ectocervical_distancia_carcinoma = models.FloatField(
        verbose_name="La distancia del carcinoma al margen ectocervical(mm)",
        blank=True,
        null=True,
    )
    margen_ectocervical_afectado_por = MultiSelectField(
        max_length=100,
        min_choices=0,
        verbose_name="Afectado por:",
        choices=gynecology_model_choices.MargenAfectacionChoices.choices,
    )
    margen_ectocervical_posicion_especifica = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="La posición especifica(si es posible):",
    )

    # El Margen Profundo
    margen_profundo_no_puede_evaluarce = models.BooleanField(
        default=False, verbose_name="Margen Profundo no puede ser evaluado"
    )
    margen_profundo_no_evaluado_explique = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Margen Profundo no puede ser evaluado (explique):",
    )
    margen_profundo_no_afectado = models.BooleanField(
        default=False, verbose_name="Margen Profundo no afectado"
    )
    margen_profundo_distancia_carcinoma = models.FloatField(
        verbose_name="La distancia del carcinoma al margen profundo(mm)",
        blank=True,
        null=True,
    )
    margen_profundo_afectado_por = MultiSelectField(
        max_length=100,
        min_choices=0,
        verbose_name="Afectado por:",
        choices=gynecology_model_choices.MargenAfectacionChoices.choices,
    )
    margen_profundo_posicion_especifica = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="La posición especifica(si es posible):",
    )

    # La Invasión del Lymphovascular
    invasion_limphovascular = models.IntegerField(
        choices=gynecology_model_choices.InvasionLymphovascularChoices.choices,
        verbose_name="La Invasión del Lymphovascular",
    )

    # Otra patología asociada(seleccione todo lo que aplique)
    otra_patologia_asociada = MultiSelectField(
        verbose_name="Otra patología asociada(seleccione todo lo que aplique)",
        max_length=100,
        min_choices=1,
        choices=gynecology_model_choices.OtraPatologiaAsociada.choices,
    )
    otra_patologia_asociada_especifique = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El otro del + (especifique): ",
    )

    # La resección
    reseccion = models.IntegerField(
        choices=gynecology_model_choices.ReseccionChoices.choices,
        verbose_name="La resección",
    )
    exenteracion_pelvica_especifique = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Exenteración pélvica(especifique órganos incluidos): ",
    )
    otra_reseccion_especifique = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otra Resección(especifique):",
    )

    # Tipo Hysterectomy
    tipo_hysterectomy = models.IntegerField(
        verbose_name="Tipo Hysterectomy",
        choices=gynecology_model_choices.TipoHysterectomyChoices.choices,
    )
    otro_tipo_hysterectomy = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otro del + (especifique): ",
    )

    # Afectación de otros órganos
    afectacion_otros_organos = models.IntegerField(
        verbose_name="Afectación de otros órganos",
        choices=gynecology_model_choices.AfectacionOtrosOrganosChoices.choices,
    )
    afectacion_otro_organo = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Afectación de otro órgano(especifique):",
    )
    afectacion_no_determinada = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Afectación no puede ser determinada(explique):",
    )

    # Los Márgenes(la Nota F)
    # Ectocervical Margin
    ectocervical_margin_no_puede_evaluarce = models.BooleanField(
        verbose_name="Ectocervical Margin no puede ser evaluado", default=False
    )
    ectocervical_margin_no_evaluado_especif = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Ectocervical Margin no puede ser evaluado (explique)",
    )
    ectocervical_uninvol_carci_invasive = models.BooleanField(
        verbose_name="Uninvolved por carcinoma del invasive", default=False
    )
    ectocervical_margin_distancia_carcinoma = models.FloatField(
        verbose_name="La distancia del + de carcinoma del invasive de margen(los milímetros):",
        blank=True,
        null=True,
    )
    ectocervical_margin_posicion_specify1 = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El + la posición(especificar):",
    )
    ectocervical_involucrado_carcinoma_invasive = models.BooleanField(
        verbose_name="Involucrado por carcinoma del invasive", default=False
    )
    ectocervical_especifique_posicion = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Especifique posición(si es posible)",
    )
    ectocervical_uninvolved_intra_neop = models.BooleanField(
        verbose_name="Uninvolved por intraepithelial neoplasia", default=False
    )
    ectocervical_invol_lesion_escam = models.BooleanField(
        verbose_name="Involucrado por lesión escamosa (CIN 2-3) del intraepithelial de calidad superior",
        default=False,
    )
    ectocervical_margin_posicion_specify2 = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El + la posición(especificar):",
    )
    ectocervical_invol_adenocarcinoma = models.BooleanField(
        verbose_name="Involucrado por adenocarcinoma en situ(las IAs)", default=False
    )
    ectocervical_margin_posicion_specify3 = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El + la posición(especificar):",
    )

    # El Margen Radial (Circunferencial)
    radial_margin_no_puede_evaluarce = models.BooleanField(
        verbose_name="Radial Margin no puede ser evaluado", default=False
    )
    radial_margin_no_evaluado_especif = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Radial Margin no puede ser evaluado (explique)",
    )
    radial_uninvol_carci_invasive = models.BooleanField(
        verbose_name="Uninvolved por carcinoma del invasive", default=False
    )
    radial_margin_distancia_carcinoma = models.FloatField(
        verbose_name="La distancia del + de carcinoma del invasive de margen(los milímetros):",
        blank=True,
        null=True,
    )
    radial_margin_posicion_specify = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El + la posición(especificar):",
    )
    radial_involucrado_carcinoma_invasive = models.BooleanField(
        verbose_name="Involucrado por carcinoma del invasive", default=False
    )
    radial_especifique_posicion = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Especifique posición(si es posible)",
    )

    # La Invasión del Lymphovascular(la Nota G)
    # La Invasión del Lymphovascular
    invasion_limphovascular_notaG = models.IntegerField(
        choices=gynecology_model_choices.InvasionLymphovascularNotaGChoices.choices,
        verbose_name="La Invasión del Lymphovascular(la Nota G)",
    )

    # Los Ganglios Linfáticos Regionales
    """
    Nota: Los ganglios linfáticos denominados como pélvico, parametrial, obturador, interno parte exterior ilíaco (hipo-gástrico),
    ilíaco, común ilíaco El sacro, el presacro y para aórtico son considerados ganglios linfáticos regionales.
    Cualquier otros nodos involucrados deberían ser clasificados en categorías como Las metástasis (pM1) y comentado en adentro
    la sección distante de metástasis. La presencia de celdas del tumor aisladas no mayores que 0.2 El mm en ganglio linfático
    regional (s) es considerado N0 (yo +).
    """
    ganglios_linfaticos_encontrados = models.BooleanField(
        default=False,
        verbose_name="Ninguno de los ganglios linfáticos se sometieron o encontraron",
    )
    # El examen del ganglio linfático (requeridos únicos si los nodos de la linfa están presentes en espécimen)
    num_nodos_con_metastasis = models.IntegerField(
        verbose_name="El número de Nodos con Metástasis (excluye a ITCs):",
        blank=True,
        null=True,
    )
    num_no_puede_determinarce = models.BooleanField(
        default=False, verbose_name="El número no puede ser determinado"
    )
    num_no_determinado_especif = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El número no puede ser determinado (explique):",
    )
    num_nodos_celdas_aisladas = models.IntegerField(
        verbose_name="El número de Nodos con Celdas Aisladas (ITCs) del Tumor (0.2 mm o menos) (si aplicable)",
        blank=True,
        null=True,
    )
    num_nodos_no_puede_determinarce = models.BooleanField(
        default=False, verbose_name="El número no puede ser determinado "
    )
    num_nodos_no_determinado_especif = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El número de nodos no puede ser determinado (explique):",
    )
    num_ganglios_con_tumor = models.IntegerField(
        verbose_name="Especifique el número de Ganglio Linfático(s) con Tumor (si aplicable)",
        blank=True,
        null=True,
    )
    total_num_nodos_examinados = models.IntegerField(
        verbose_name="Número total de Nodo Examinado (el señalizador y el poco señalizador)",
        blank=True,
        null=True,
    )
    num_total_no_puede_determinarce = models.BooleanField(
        default=False, verbose_name="El número no puede ser determinado "
    )
    num_total_no_determinado_especif = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El número no puede ser determinado (explique):",
    )
    sitios_especif = models.CharField(
        max_length=5000, blank=True, null=True, verbose_name="Especifique Sitio(s) "
    )
    num_nodos_senalizador_exami = models.IntegerField(
        verbose_name="Numere de Nodos del Señalizador Examinados:",
        blank=True,
        null=True,
    )
    num_serial_no_puede_determinarce = models.BooleanField(
        default=False, verbose_name="El número no puede ser determinado "
    )
    num_serial_no_determinado_especif = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="El número no puede ser determinado (explique):",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Diagnostico Biopcia de Ginecología(Cervix)"
        verbose_name_plural = "Diagnosticos Biopcias de Ginecología(Cervix)"
        ordering = ["id"]

    def __str__(self):
        return f"Diagnostico de Ginecología(Cervix) de la biopcia: {self.biopsy}"
