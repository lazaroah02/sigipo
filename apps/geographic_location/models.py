from django.db.models import CASCADE, CharField, ForeignKey, Model


class Province(Model):
    """Provincia."""

    name = CharField(verbose_name="Nombre", max_length=128)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["pk"]

    def __str__(self):
        return self.name


class Municipality(Model):
    """Municipio."""

    province = ForeignKey(Province, verbose_name="Provincia", on_delete=CASCADE)
    name = CharField(verbose_name="Nombre", max_length=128)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["pk"]

    def __str__(self):
        return self.name
