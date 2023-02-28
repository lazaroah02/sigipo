from django.db.models import (
    CASCADE,
    AutoField,
    FloatField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    TextChoices,
    TextField,
    DateTimeField,
    DateField,
    TimeField,
    CharField,
    IntegerField,
)
from django.db.models.manager import Manager
from multiselectfield import MultiSelectField

from apps.core.models import TimeStampedModel
from apps.patient.models import Patient

class ExternalBeamTreatmentChoices(TextChoices):
    """Types of Radiotherapy"""

    TRC3D = "Radioterapia de conformacion tridimensional", "Radioterapia de conformacion tridimensional"
    IMRT = "Radioterapia de intensidad modulada", "Radioterapia de intensidad modulada"
    IGRT = "Radioterapia guiada por imagenes", "Radioterapia guiada por imagenes"
    TomoThpy = "Tomoterapia", "Tomoterapia"
    StRdSurgery = "Radiocirugia estereotactica", "Radiocirugia estereotactica"
    StBdRdTherapy = "Radioterapia estereotactica corporal", "Radioterapia estereotactica corporal"


class ExternalBeamTreatQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class ExternalBeamTreat(TimeStampedModel):
    """Model representation of External Beam Treatment."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    treat_number = AutoField(verbose_name ='Número de Tratamiento',primary_key=True, unique=True)
    biopsy = TextField(verbose_name ='Biopsia',null=True, blank=True)
    dosis = FloatField(verbose_name ='Dosis',null=True, blank=True)
    time_table = DateField(verbose_name ='Fecha',null=True, blank=True)
    target_volume = FloatField(verbose_name ='Volumen Diana',null=True, blank=True)
    radiation_time = TimeField(verbose_name ='Tiempo de Radiación',null=True, blank=True)
    fractionation = FloatField(verbose_name ='Fraccionamiento',null=True, blank=True)
    # target_precision = FloatField(verbose_name ='Precision al Objetivo',null=True, blank=True)
    dosis_distribution = FloatField(verbose_name ='Distribucion de Dosis',null=True, blank=True)
    # external_beam_config = TextField(verbose_name = 'Configuracion del Haz Externo',null=True, blank=True)
    tests = MultiSelectField(
        choices=ExternalBeamTreatmentChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )
    objects = ExternalBeamTreatQuerysetManager()

    class Meta:
        verbose_name = "Tratamiento Radiación Haz Externo"
        verbose_name_plural = "Tratamientos Radiación Haz Externo"
        ordering = ["created_at"]
        default_permissions = ()

    def __str__(self):
        """Returns the str representation for the model."""
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"

#************************************************************************************

class ExternalBeamRegQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class ExternalBeamReg(TimeStampedModel):
    """Model representation of External Beam Treatment."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    treat_number = OneToOneField(ExternalBeamTreat, to_field="treat_number", null=False, blank=False, on_delete=CASCADE, primary_key=True)
    # treat_number = ForeignKey(ExternalBeamTreat, to_field = "treat_number", null=False, blank=False, on_delete=CASCADE,primary_key=True)
    # treat_number = AutoField(verbose_name ='Numero de Tratamiento',primary_key=True) #must be a foreignkey
    dosis = FloatField(verbose_name ='Dosis' ,null=True, blank=True)
    time_table = DateField(verbose_name ='Fecha',null=True, blank=True)
    target_volume = FloatField(verbose_name ='Volumen Diana',null=True, blank=True)
    radiation_time = TimeField(verbose_name ='Tiempo de Radioacion',null=True, blank=True)
    # fractionation = FloatField(verbose_name ='Fraccionamiento',null=True, blank=True)
    target_precision = FloatField(verbose_name ='Precision al Objetivo',null=True, blank=True)
    dosis_distribution = FloatField(verbose_name ='Distribucion de Dosis',null=True, blank=True)
    session_number = IntegerField(verbose_name ='Numero de Sesión',null=True, blank=True)
    external_beam_config = TextField(verbose_name = 'Configuracion del Haz Externo',null=True, blank=True)
    tests = MultiSelectField(
        choices=ExternalBeamTreatmentChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )
    objects = ExternalBeamRegQuerysetManager()

    class Meta:
        verbose_name = "Registro Radiacion Haz Externo"
        verbose_name_plural = "Registros Radiacion Haz Externo"
        ordering = ["created_at"]
        default_permissions = ()

    def __str__(self):
        """Returns the str representation for the model."""
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"

#**************************************Internal Radiation*********************************************

class InternalRadiationTreatmentChoices(TextChoices):
    """Types of Internal Radiation Treat"""

    LDR = "Implates con indices de dosis bajas", "Implates con indices de dosis bajas"
    HDR = "Implates con indices de dosis altas", "Implates con indices de dosis bajas"
    PermImpl = "Implantes permanentes", "Implantes permanentes"


class InternalRadiationTreatmentQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class InternalRadiationTreatment(TimeStampedModel):
    """Model representation of Internal Radiation Treat."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    treat_number = AutoField(verbose_name ='Numero de Tratamiento' ,primary_key=True, unique=True)
    biopsy = TextField(verbose_name ='Biopsia',null=True, blank=True)
    dosis = FloatField(verbose_name ='Dosis' ,null=True, blank=True)
    time_table = DateField(verbose_name ='Fecha',null=True, blank=True)
    target_volume = FloatField(verbose_name ='Volumen Diana',null=True, blank=True)
    radiation_time = TimeField(verbose_name ='Tiempo de Radioacion',null=True, blank=True)
    fractionation = FloatField(verbose_name ='Fraccionamiento',null=True, blank=True)
    target_precision = FloatField(verbose_name ='Precision al Objetivo',null=True, blank=True)
    dosis_distribution = FloatField(verbose_name ='Distribucion de Dosis',null=True, blank=True)
    radioisotope = CharField(verbose_name ='Radioisotopos',max_length=256 ,null=True, blank=True)
    tests = MultiSelectField(
        choices=InternalRadiationTreatmentChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )
    objects = InternalRadiationTreatmentQuerysetManager()


    class Meta:
        verbose_name = "Tratamiento Radiacion Interna"
        verbose_name_plural = "Tratamiento Radiacion Interna"
        ordering = ["created_at"]
        default_permissions = ()

    def __str__(self):
        """Returns the str representation for the model."""
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"

#****************************************************************************************************

class InternalRadiationRegQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")


class InternalRadiationReg(TimeStampedModel):
    """Model representation of Internal Radiation Treat."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    treat_number = OneToOneField(InternalRadiationTreatment, to_field="treat_number", null=False, blank=False, on_delete=CASCADE, primary_key=True)
    # treat_number = ForeignKey(InternalRadiationTreatment, to_field = "treat_number", null=False, blank=False, on_delete=CASCADE,primary_key=True)
    # treat_number = AutoField(verbose_name ='Numero de Tratamiento' ,primary_key=True) #must be a Freignkey
    dosis = FloatField(verbose_name ='Dosis' ,null=True, blank=True)
    time_table = DateField(verbose_name ='Fecha',null=True, blank=True)
    target_volume = FloatField(verbose_name ='Volumen Diana',null=True, blank=True)
    radiation_time = TimeField(verbose_name ='Tiempo de Radioacion',null=True, blank=True)
    # fractionation = FloatField(verbose_name ='Fraccionamiento',null=True, blank=True)
    target_precision = FloatField(verbose_name ='Precision al Objetivo',null=True, blank=True)
    dosis_distribution = FloatField(verbose_name ='Distribucion de Dosis',null=True, blank=True)
    session_number = IntegerField(verbose_name ='Numero de Sesión',null=True, blank=True)
    radioisotope = CharField(verbose_name ='Radioisotopos',max_length=256 ,null=True, blank=True)
    tests = MultiSelectField(
        choices=InternalRadiationTreatmentChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )
    objects = InternalRadiationRegQuerysetManager()
    

    class Meta:
        verbose_name = "Registro Radiacion Interna"
        verbose_name_plural = "Registros Radiacion Interna"
        ordering = ["created_at"]
        default_permissions = ()

    def __str__(self):
        """Returns the str representation for the model."""
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"
