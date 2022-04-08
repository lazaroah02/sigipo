from django.db.models import CASCADE, CharField, ForeignKey, Model


class Province(Model):
    """Model representation of a province."""

    name = CharField(verbose_name="Nombre", max_length=128)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["pk"]

    def __str__(self):
        """Returns the name of the province."""
        return self.name


class Municipality(Model):
    """Model representation of a municipality."""

    province = ForeignKey(Province, verbose_name="Provincia", on_delete=CASCADE)
    name = CharField(verbose_name="Nombre", max_length=128)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["pk"]

    def __str__(self):
        """Returns the name of the municipality."""
        return self.name
