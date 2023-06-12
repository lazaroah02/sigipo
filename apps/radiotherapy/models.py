from django.conf import settings
from django.db.models import (
    CASCADE,
    SET_NULL,
    AutoField,
    BooleanField,
    CharField,
    DateField,
    FloatField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
    Manager,
    Model,
    TextField,
)

from apps.core.models import TimeStampedModel
from apps.employee.models import Doctor
from apps.patient.models import Patient


#  Dosimetry   #########################################################################################
class AnatomicDataChoices(IntegerChoices):
    "Defines t5hye anatomic data aquisition"

    PATIENT_MESUREMENTS = 0, "Medidas del Paciente"
    CONTOUR = 1, "Contorno"
    RADIOGRAPHY = 2, "Radiografías"
    TAC = 3, "TAC"


class DosimetryPlan(Model):
    modality = CharField(verbose_name="Modalidad", max_length=256)
    radiation_therapist_in_charge = CharField(
        verbose_name="Radioterapeuta a cargo", max_length=256
    )
    team = CharField(verbose_name="Equipo", max_length=256)
    doctor_asigned = ForeignKey(Doctor, on_delete=CASCADE)
    patient = ForeignKey(Patient, on_delete=CASCADE)
    plan = TextField(verbose_name="Etiqueta del Plan")
    fractial_dosis = FloatField(verbose_name="Dosis por Fracción")
    total_dosis = FloatField(verbose_name="Dosis Total")
    session_number = IntegerField(verbose_name="Número de aplicaciones")
    anatomic_data_aquisition = IntegerField(
        verbose_name="Adquisición de datos Anatómicos",
        choices=AnatomicDataChoices.choices,
        blank=True,
        null=True,
    )
    icru_dosis = FloatField(verbose_name="Dosis en ICRU/Isocentro")
    max_dosis = FloatField(verbose_name="Dosis máxima (%)")

    class Meta:
        verbose_name = "Plan de Dosimentría"
        verbose_name_plural = "Planes de Dosimentría"
        ordering = ["pk"]

    def __str__(self):
        """String representation of Dosimetry_Plan."""
        return f"{self.patient}"


# Fisica Medica ###############################################################################
class ModalityChoices(IntegerChoices):
    TELETHERAPY = 0, "Teleterapia"
    BRACHYTHERAPY = 1, "Braquiterapia"


class Energy(Model):
    energy = CharField(verbose_name="Energía", max_length=256)
    enable = BooleanField(verbose_name="Habilitado")

    class Meta:
        verbose_name = "Energía"
        verbose_name_plural = "Energías"
        ordering = ["pk"]

    def __str__(self):
        """String representation of Energy."""
        return f"{self.energy}"


class EquipmentQuerySetManager(Manager):
    """Manager to handle Equipment."""

    def get_queryset(self):
        """Fetch the related Energy."""
        return super().get_queryset().select_related("energy")


class Equipment(Model):
    name = CharField(verbose_name="Nombre del equipo", max_length=256)
    modality = IntegerField(
        verbose_name="Modalidad", choices=ModalityChoices.choices, blank=True, null=True
    )
    energy = ForeignKey(Energy, verbose_name="Energía", on_delete=CASCADE)
    objects = EquipmentQuerySetManager()

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ["pk"]

    def __str__(self):
        """String representation of Equipment."""
        return f"{self.name}"


class AccesoriesQuerySetManager(Manager):
    """Manager to handle Accesories."""

    def get_queryset(self):
        """Fetch the related Accesories."""
        return super().get_queryset().select_related("enable_equipment")


class Accessories(Model):
    name = CharField(verbose_name="Nombre", max_length=256)
    type = CharField(verbose_name="Tipo", max_length=256)
    eid = CharField(verbose_name="ID", max_length=256)
    enable_equipment = ForeignKey(Equipment, null=True, blank=True, on_delete=SET_NULL)
    objects = AccesoriesQuerySetManager()

    class Meta:
        verbose_name = "Accesorios"
        verbose_name_plural = "Accesorios"
        ordering = ["pk"]

    def __str__(self):
        """String representation of Dosimetry_Plan."""
        return f"{self.name}"


class OAR_TV_TypeChoices(IntegerChoices):
    OAR = 0, "Órganos de Riesgo"
    TV = 1, "Volumen Diana"


class RiskOrgans(Model):
    name = CharField(verbose_name="Nombre del Órgano", max_length=256)
    type = IntegerField(
        verbose_name="Tipo de Órganos",
        choices=OAR_TV_TypeChoices.choices,
        blank=True,
        null=True,
    )
    alpha_beta = IntegerField(default=0, verbose_name="Alpha/Beta")
    dosis_limit = FloatField(verbose_name="Límite de Dosis")

    class Meta:
        verbose_name = "Órganos de Riesgo"
        verbose_name_plural = "Órganos de Riesgos"
        ordering = ["pk"]

    def __str__(self):
        """String representation of Risk_Organs."""
        return f"{self.name}"


#  Prescripcion Formulario #######################################################################################


class PrescriptionQuerySetManager(Manager):
    """Manager to handle Prescription."""

    def get_queryset(self):
        """Fetch the related Prescription."""
        return (
            super()
            .get_queryset()
            .select_related(
                "equipo",
                "organs_at_risk",
                "registred_by",
                "radiotherapist_in_charge",
                "patient",
            )
        )


class Prescription(Model):
    treatment_serie = CharField(verbose_name="Serie de Tratamiento", max_length=256)
    modality = IntegerField(
        verbose_name="Modalidad", choices=ModalityChoices.choices, blank=True, null=True
    )
    equipo = ForeignKey(Equipment, null=True, blank=True, on_delete=SET_NULL)
    irradiate_other_locations = BooleanField(default=False)
    reirradiated_patient = BooleanField(default=False)
    status = CharField(
        verbose_name="Estado", max_length=256
    )  ##########################
    location = CharField(verbose_name="Localizacion", max_length=256)  #####Lista
    fractial_dosis = FloatField(verbose_name="Dosis por Fracción")
    total_dosis = FloatField(verbose_name="Dosis Total")
    session_number = IntegerField(verbose_name="Número de aplicaciones")
    weekly_session = IntegerField(verbose_name="Sesión semanal")
    daily_session = IntegerField(default=1, verbose_name="Sesión diaria")
    organs_at_risk = ForeignKey(
        RiskOrgans,
        verbose_name="Órganos en riesgo/ Volúmen diana",
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )
    registred_by = ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Registrado por",
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )
    radiotherapist_in_charge = ForeignKey(Doctor, on_delete=CASCADE)
    patient = ForeignKey(Patient, on_delete=SET_NULL, null=True, blank=True)
    objects = PrescriptionQuerySetManager()

    class Meta:
        verbose_name = "Prescripción"
        verbose_name_plural = "Prescripciones"
        ordering = ["pk"]

    def __str__(self):
        """String representation of Prescription."""
        return f"{self.treatment_serie}"


# Secretaria #####################################################################################


class MedicalTurnQuerysetManager(Manager):
    """Manager to handle Medical Turn."""

    def get_queryset(self):
        """Fetch the related Medical Turn."""
        return super().get_queryset().select_related("patient", "doctor")


class MedicalTurn(TimeStampedModel):
    patient = ForeignKey(Patient, on_delete=CASCADE, verbose_name="Paciente")
    list_number = AutoField(primary_key=True)
    objects = MedicalTurnQuerysetManager()
    cid = IntegerField(verbose_name="CID")
    id = CharField(verbose_name="ID", max_length=256)
    address = CharField(verbose_name="Dirección", null=True, blank=True, max_length=256)
    location = CharField(
        verbose_name="Localización", null=True, blank=True, max_length=256
    )
    stage = CharField(verbose_name="Etapa", null=True, blank=True, max_length=256)
    doctor = ForeignKey(
        Doctor, on_delete=CASCADE, verbose_name="Doctor", null=True, blank=True
    )
    waiting_list = BooleanField(
        default=False, verbose_name="Añadir a la lista de espera", null=True, blank=True
    )
    date_first_apointment = DateField(
        verbose_name="Fecha de la primera consulta", null=True, blank=True
    )
    date_culmination_treatment = DateField(
        verbose_name="Fecha de culminación del tratamiento", null=True, blank=True
    )
    # date_of_registration = DateField(verbose_name="Fecha de Registro", null=True, blank=True)

    class Meta:
        verbose_name = "Turno Médico"
        verbose_name_plural = "Turnos Médicos"
        ordering = ["list_number"]

    def __str__(self):
        """String representation of MedicalTurn."""
        return f"{self.id}"


# Simulacion #############################################################################################################


class TACStudy(Model):
    patient = ForeignKey(Patient, on_delete=CASCADE, verbose_name="Paciente")
    location = CharField(verbose_name="Localización", max_length=256)
    chunck_distance = FloatField(verbose_name="Distancia entre cortes (mm)")
    patient_position = CharField(verbose_name="Posición del Paciente", max_length=256)
    protocol = CharField(verbose_name="Protocolo utilizado", max_length=256)
    doctor = ForeignKey(
        Doctor, on_delete=SET_NULL, verbose_name="Doctor", null=True, blank=True
    )

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
        ordering = ["pk"]

    def __str__(self):
        """String representation of TACStudy."""
        return f"{self.patient}"


# class Simulation(Model):

#     doctor = ForeignKey(User.objects.filter(groups__name="Doctor"),on_delete=SET_NULL)
