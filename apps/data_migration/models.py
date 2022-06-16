import datetime as dt

from django.db import models

from apps.cancer_registry.models import (
    Neoplasm,
    NeoplasmClinicalExtensionsChoices,
    NeoplasmDiagnosticConfirmationChoices,
    NeoplasmDifferentiationGradesChoices,
    NeoplasmLateralityChoices,
)
from apps.classifiers.models import Morphology, Topography
from apps.employee.models import Doctor, Group
from apps.geographic_location.models import Municipality, Province
from apps.patient.models import Patient, PatientRace, SexChoices


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


def get_date(ci):
    siglo = ci[6]
    siglo = 18 if siglo == 9 else 19 if siglo in ("0", "1", "2", "3", "4", "5") else 20
    year = int(f"{siglo}{ci[0:2]}")
    mes = int(ci[2:4])
    day = int(ci[4:6])
    try:
        return dt.date(year=year, month=mes, day=day)
    except ValueError:
        return None


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
    municipio = models.CharField(
        max_length=255, db_column="municipio", blank=True, null=True
    )
    embarazada = models.IntegerField(db_column="embarazada", blank=True, null=True)
    trimestre = models.CharField(
        max_length=255, db_column="trimestre", blank=True, null=True
    )
    vih = models.IntegerField(db_column="vih+", blank=True, null=True)
    hc = models.CharField(max_length=255, db_column="hc", blank=True, null=True)

    def to_postgres_db(self, related=None):
        return Patient(
            identity_card=self.ci,
            first_name=self.nombres,
            last_name=f"{self.apellido1} {self.apellido2}",
            street=self.calle,
            number=self.numero,
            building=self.edificio,
            apartment=self.apartamento,
            sex=SexChoices.UNDEFINED
            if self.sexo not in ("F", "M")
            else SexChoices.FEMALE
            if self.sexo == "F"
            else SexChoices.MALE,
            date_of_birth=None
            if len(self.ci) != 11 or self.ci[6:11] == "00000"
            else get_date(self.ci),
            between_streets=self.entre,
            division=self.localidad,
            race=PatientRace.UNDEFINED
            if self.piel not in ("Blanca", "Mestiza", "Negra")
            else PatientRace.BLACK
            if self.piel == "Negra"
            else PatientRace.WHITE
            if self.piel == "Blanca"
            else PatientRace.HALF_BLOOD,
            medical_record=self.hc,
            residence_municipality=None
            if self.municipio is None
            else related.get(self.municipio, None),
            born_municipality=None
            if self.municipio is None
            else related.get(self.municipio, None),
            is_oncologic=True,
        )

    class Meta(DataMigrationModel.Meta):
        db_table = "t1_datosgeneralespaciente"


def get_confirmation(str_value: str):
    confirmation = None
    match str_value.lower():
        case "clínica":
            confirmation = NeoplasmDiagnosticConfirmationChoices.CLINIC
        case "investigación clínica":
            confirmation = NeoplasmDiagnosticConfirmationChoices.CLINIC_RESEARCH
        case "histología de una metástasis":
            confirmation = (
                NeoplasmDiagnosticConfirmationChoices.HISTOLOGY_OF_A_METASTASIS
            )
        case "citología":
            confirmation = NeoplasmDiagnosticConfirmationChoices.CYTOLOGY
        case "histología de tumor primario":
            confirmation = NeoplasmDiagnosticConfirmationChoices.PRIMARY_TUMOR_HISTOLOGY
        case "marcadores tumorales":
            confirmation = NeoplasmDiagnosticConfirmationChoices.TUMOR_MARKERS
        case "desconocido":
            confirmation = NeoplasmDiagnosticConfirmationChoices.UNKNOWN
    return confirmation


def get_grado(str_value: str):
    grado = None
    match str_value.lower():
        case "diferenciado":
            grado = NeoplasmDifferentiationGradesChoices.Differentiated
        case "moderadamente diferenciado":
            grado = NeoplasmDifferentiationGradesChoices.MODERATELY_DIFFERENTIATED
        case "no determinado o no aplicable":
            grado = NeoplasmDifferentiationGradesChoices.UNDETERMINED
        case "poco diferenciado":
            grado = NeoplasmDifferentiationGradesChoices.POORLY_DIFFERENTIATED
        case "indiferenciado":
            grado = NeoplasmDifferentiationGradesChoices.UNDIFFERENTIATED
        case "células t":
            grado = NeoplasmDifferentiationGradesChoices.T_CELLS
        case "células a":
            grado = NeoplasmDifferentiationGradesChoices.B_CELLS
        case "células b":
            grado = NeoplasmDifferentiationGradesChoices.B_CELLS
        case "células nk":
            grado = NeoplasmDifferentiationGradesChoices.NK_CELLS
        case "células nulas":
            grado = NeoplasmDifferentiationGradesChoices.NULL_CELLS
    return grado


def get_extension(str_value: str):
    extension = None
    match str_value.lower():
        case "in situ":
            extension = NeoplasmClinicalExtensionsChoices.IN_SITU
        case "localizada":
            extension = NeoplasmClinicalExtensionsChoices.LOCATED
        case "extensión directa":
            extension = NeoplasmClinicalExtensionsChoices.DIRECT_EXTENSION
        case "metástesis remota":
            extension = NeoplasmClinicalExtensionsChoices.REMOTE_METASTASIS
        case "extensión directa y linfática regional":
            extension = (
                NeoplasmClinicalExtensionsChoices.REGIONAL_DIRECT_AND_LYMPHATIC_EXTENSION
            )
        case "linfática regional":
            extension = NeoplasmClinicalExtensionsChoices.REGIONAL_LYMPHATIC
        case "no aplicable":
            extension = NeoplasmClinicalExtensionsChoices.NOT_APPLICABLE
        case "desconocido":
            extension = NeoplasmClinicalExtensionsChoices.UNKNOWN
    return extension


class DatosTumor(DataMigrationModel):
    fechainicio = models.DateField(null=True, blank=True, db_column="fechainicio")
    idtumor = models.IntegerField(db_column="idtumor", primary_key=True)
    ci = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column="CI")
    fechadiagnostico = models.DateField(
        null=True, blank=True, db_column="fechadiagnostico"
    )
    localizacion = models.ForeignKey(
        Localizacion, on_delete=models.CASCADE, db_column="localizacion"
    )
    lateralidad = models.CharField(
        max_length=255, db_column="bilateral", null=True, blank=True
    )
    diagnostico = models.ForeignKey(
        Diagnostico, on_delete=models.CASCADE, db_column="diagnostico"
    )
    t = models.CharField(max_length=255, db_column="T", null=True, blank=True)
    n = models.CharField(max_length=255, db_column="N", null=True, blank=True)
    m = models.CharField(max_length=255, db_column="M", null=True, blank=True)
    clinicopatolog = models.CharField(
        max_length=255, db_column="clinicopatolog", null=True, blank=True
    )
    psa = models.FloatField(db_column="psa", null=True, blank=True)
    tumorprimario = models.CharField(
        max_length=255, db_column="tumorprimario", null=True, blank=True
    )
    basediagnostico = models.CharField(
        max_length=255, db_column="basediagnostico", null=True, blank=True
    )
    extension = models.CharField(
        max_length=255, db_column="extension", null=True, blank=True
    )
    etapa = models.CharField(max_length=255, db_column="etapa", null=True, blank=True)
    grado = models.CharField(max_length=255, db_column="grado", null=True, blank=True)
    transf_hemat = models.IntegerField(db_column="transf_hemat", null=True, blank=True)
    fechaprsintomas = models.DateField(
        db_column="fechaprsintomas", null=True, blank=True
    )
    aguda = models.CharField(max_length=255, db_column="aguda", null=True, blank=True)
    cronica = models.CharField(
        max_length=255, db_column="cronica", null=True, blank=True
    )
    mieloide = models.CharField(
        max_length=255, db_column="mieloide", null=True, blank=True
    )
    mieloma = models.CharField(
        max_length=255, db_column="mieloma", null=True, blank=True
    )
    mieloidecronica = models.CharField(
        max_length=255, db_column="mieloidecronica", null=True, blank=True
    )
    fuente = models.CharField(max_length=255, db_column="fuente", null=True, blank=True)
    regprof = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column="regprof")
    id_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, db_column="id_grupo")
    fechareporte = models.DateField(null=True, blank=True, db_column="fechareporte")

    def to_postgres_db(self, related=None):
        return Neoplasm(
            pk=self.idtumor,
            patient=related["patient"][self.ci],
            date_of_diagnosis=self.fechadiagnostico,
            age_at_diagnosis=None,
            psa=self.psa,
            primary_site=related["topography"][self.localizacion.pk],
            laterality=NeoplasmLateralityChoices.NO
            if self.lateralidad == "no"
            else NeoplasmLateralityChoices.LEFT
            if self.lateralidad == "izquierdo"
            else NeoplasmLateralityChoices.RIGHT
            if self.lateralidad == "derecho"
            else None,
            diagnostic_confirmation=get_confirmation(self.basediagnostico),
            histologic_type=related["morphology"][self.diagnostico.pk],
            differentiation_grade=get_grado(self.grado),
            clinical_extension=get_extension(self.extension),
        )

    class Meta(DataMigrationModel.Meta):
        db_table = "t1_datosgeneralestumor"
