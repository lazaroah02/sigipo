from django.db import models

from apps.classifiers.models import Morphology, Topography
from apps.employee.models import Doctor, Group
from apps.geographic_location.models import Municipality, Province


class MariaDBManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using("maria_db")


class DataMigrationModel(models.Model):
    objects = MariaDBManager()

    def to_postgres_db(self, related=None):
        pass

    class Meta:
        abstract = True
        managed = False


class Diagnostico(DataMigrationModel):
    diagnostico = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True, db_column="Id")

    def to_postgres_db(self, related=None):
        return Morphology(name=self.diagnostico, pk=self.id)

    class Meta(DataMigrationModel.Meta):
        db_table = "tn_diagnostico"


class Localizacion(DataMigrationModel):
    localizacion = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)

    def to_postgres_db(self, related=None):
        return Topography(name=self.localizacion, pk=self.id)

    class Meta(DataMigrationModel.Meta):
        db_table = "tn_localizacion"


class Grupo(DataMigrationModel):
    grupo = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True, db_column="id_grupo")

    def to_postgres_db(self, related=None):
        return Group(name=self.grupo, pk=self.id)

    class Meta(DataMigrationModel.Meta):
        db_table = "tn_grupo"


class Medico(DataMigrationModel):
    nombre = models.CharField(max_length=255)
    id = models.CharField(primary_key=True, db_column="regprof", max_length=255)
    grupo = models.ForeignKey(Grupo, db_column="grupo", on_delete=models.CASCADE)

    def to_postgres_db(self, related=None):
        return Doctor(
            first_name=self.nombre,
            pk=self.id,
            group=related[self.grupo.pk],
        )

    class Meta(DataMigrationModel.Meta):
        db_table = "tn_medicos"


class Provincia(DataMigrationModel):
    provincia = models.CharField(max_length=255, db_column="Provincia")
    id = models.IntegerField(primary_key=True, db_column="codigo")

    def to_postgres_db(self, related=None):
        return Province(
            name=self.provincia,
            pk=self.id,
        )

    class Meta(DataMigrationModel.Meta):
        db_table = "tn_provincias"


class Municipio(DataMigrationModel):
    municipio = models.CharField(max_length=255, db_column="municipio")
    provincia = models.ForeignKey(
        Provincia, db_column="provincia", on_delete=models.CASCADE
    )
    id = models.IntegerField(primary_key=True, db_column="id_municipio")

    def to_postgres_db(self, related=None):
        return Municipality(
            pk=self.id,
            name=self.municipio,
            province=related[self.provincia.pk],
        )

    class Meta(DataMigrationModel.Meta):
        db_table = "tn_municipios"


class Paciente(DataMigrationModel):
    ci = models.CharField(max_length=255, db_column="CI", primary_key=True)
    apellido1 = models.CharField(
        max_length=255, db_column="apellido1", blank=True, null=True
    )
    apellido2 = models.CharField(
        max_length=255, db_column="apellido2", blank=True, null=True
    )
    nombres = models.CharField(
        max_length=255, db_column="nombres", blank=True, null=True
    )
    edad = models.IntegerField(db_column="edad", blank=True, null=True)
    sexo = models.CharField(max_length=255, db_column="sexo", blank=True, null=True)
    piel = models.CharField(max_length=255, db_column="piel", blank=True, null=True)
    calle = models.CharField(max_length=255, db_column="calle", blank=True, null=True)
    numero = models.CharField(max_length=255, db_column="numero", blank=True, null=True)
    edificio = models.CharField(
        max_length=255, db_column="edificio", blank=True, null=True
    )
    apartamento = models.IntegerField(db_column="apartamento", blank=True, null=True)
    entre = models.CharField(max_length=255, db_column="entre", blank=True, null=True)
    localidad = models.CharField(
        max_length=255, db_column="localidad", blank=True, null=True
    )
    provincia = models.ForeignKey(
        Provincia,
        db_column="provincia",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    municipio = models.ForeignKey(
        Municipio,
        db_column="municipio",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    embarazada = models.IntegerField(db_column="embarazada", blank=True, null=True)
    trimestre = models.CharField(
        max_length=255, db_column="trimestre", blank=True, null=True
    )
    vih = models.IntegerField(db_column="vih+", blank=True, null=True)
    hc = models.CharField(max_length=255, db_column="hc", blank=True, null=True)

    class Meta(DataMigrationModel.Meta):
        db_table = "t1_datosgeneralespaciente"
