from django.db import models
from multiselectfield import MultiSelectField
from apps.pathologic_anathomy.models_biopsy_diagnostic.choices import (
    linfoma_model_choices,
)


class LinfomaBiopsyDiagnostic(models.Model):
    biopsy = models.OneToOneField(
        "pathologic_anathomy.BiopsyRequest", 
        on_delete=models.CASCADE,
        related_name="linfoma_byopsy_diagnostic"
    )

    # A.Información clínica recibida en el departamento de Anatomía Patológica.
    # El espécimen (seleccione todo lo que aplique)
    especimen = MultiSelectField(
        verbose_name="El espécimen (seleccione todo lo que aplique)", 
        max_length=100,
        min_choices = 1,
        choices = linfoma_model_choices.EspecimenChoices.choices
    )
    otro_especimen = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otro Espécimen (especifique)",
    )

    # El sitio del tumor (seleccione todo lo que aplique)
    sitio_tumor = MultiSelectField(
        verbose_name="El sitio del tumor (seleccione todo lo que aplique)",
        max_length=100,
        min_choices = 1,
        choices=linfoma_model_choices.SitioTumorChoices.choices
    )
    sitio_tumor_especificacion = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Especifique sitio(s) del tumor",
    )
    otro_tejido_fino_u_organo = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Otro tejido fino (s) u otro órgano (s) (especifique)",
    )
    no_especificado = models.BooleanField(verbose_name="No especificado", default=False)
    no_especificado_just = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="No especificado(justifique)",
    )

    # HistologicType (basada en la clasificación de 2008 quienes)
    histologic_type = models.IntegerField(
        choices=linfoma_model_choices.HistologicTypeChoices.choices,
        verbose_name="HistologicType (basada en la clasificación de 2008 quienes)",
    )
    # Extensión Patológica del Tumor (seleccione todo lo que aplique)
    pathologic_tumor_extensions = MultiSelectField(
        verbose_name="Extensión Patológica del Tumor (seleccione todo lo que aplique)",
        max_length=100,
        min_choices = 1,
        choices = linfoma_model_choices.PathologicTumorExtensionChoices.choices
    )
    # Inmunofenotipo (IHQ) en la lesión del sitio específico:
    inmunofenotipo = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Inmunofenotipo (IHQ) en la lesión del sitio específico:",
    )
    inmunofenotipo_no_realizado = models.BooleanField(
        verbose_name="Inmunofenotipo no realizado"
    )
    # Especifique método (s) y resultados
    metodos_y_resultados = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Especifique método (s) y resultados",
    )

    # Factores Pronóstico e Índices (seleccione todo lo que aplique)
    # Puntuación de Pronóstico
    puntuacion_pronostico = models.FloatField(verbose_name="Puntuación de Pronóstico")
    # Especificar el sistema utilizado
    sistema_utilizado = models.CharField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Especificar el sistema utilizado",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Diagnostico Biopcia de Linfoma"
        verbose_name_plural = "Diagnosticos Biopcias de Linfoma"
        ordering = ["id"]

    def __str__(self):
        return f"Diagnostico de Linfoma de la biopcia: {self.biopsy}"
