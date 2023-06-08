from django.db.models import CASCADE, CharField, ForeignKey, Model
from django.db.models.manager import Manager


class Province(Model):
    """Model representation of a province."""

    name = CharField(verbose_name="Nombre", max_length=128)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["pk"]

    def __str__(self):
        """Returns the name of the province."""
        return f"{self.name}"


class MunicipalityQuerysetManager(Manager):
    """Manager to handle Municipality."""

    def get_queryset(self):
        """Fetch related provinces."""
        return super().get_queryset().select_related("province")


class Municipality(Model):
    """Model representation of a municipality."""

    province = ForeignKey(Province, verbose_name="Provincia", on_delete=CASCADE)
    name = CharField(verbose_name="Nombre", max_length=128)
    objects = MunicipalityQuerysetManager()

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["pk"]

    def __str__(self):
        """Returns the name of the municipality."""
        return f"{self.name} - {self.province.name}"


class LocationQuerysetManager(Manager):
    """Manager to handle Location."""

    def get_queryset(self):
        """Fetch related Municipalities."""
        return super().get_queryset().select_related("municipality","municipality__province")


class Location(Model):
    """Model representation of a municipality."""

    name = CharField(verbose_name="Nombre", max_length=128)
    municipality = ForeignKey(Municipality, verbose_name="Municipio", on_delete=CASCADE)
    objects = LocationQuerysetManager()

    class Meta:
        verbose_name = "Loacalidad"
        verbose_name_plural = "Loacalidades"
        ordering = ["pk"]

    def __str__(self):
        """Returns the name of the Loacation."""
        return f"{self.name} - {self.municipality.name} - {self.municipality.province.name}"
