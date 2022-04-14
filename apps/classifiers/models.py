from django.db import models


class Topography(models.Model):
    """Model representation of a topography."""

    code = models.CharField(verbose_name="Código", max_length=5)
    description = models.CharField(verbose_name="Descripción", max_length=255)

    class Meta:
        verbose_name = "Topografía"
        verbose_name_plural = "Topografías"
        ordering = ["pk"]

    def __str__(self):
        """String representation of topography."""
        return f"{self.description}"


class Morphology(models.Model):
    """Model representation of a morphology."""

    code = models.CharField(verbose_name="Código", max_length=10)
    description = models.CharField(verbose_name="Descripción", max_length=255)

    class Meta:
        verbose_name = "Morfología"
        verbose_name_plural = "Morfologías"
        ordering = ["pk"]

    def __str__(self):
        """String representation of morphology."""
        return f"{self.description}"
