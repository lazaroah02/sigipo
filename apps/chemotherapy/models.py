from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DecimalField,
    ExpressionWrapper,
    F,
    FloatField,
    ForeignKey,
    IntegerChoices,
    IntegerField,
    Model,
    QuerySet,
)
from django.db.models.functions import Cast
from django.db.models.manager import Manager

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.core.models import Round2, TimeStampedModel
from apps.drugs.models import Drug, UnitChoicesChoices
from apps.employee.models import Doctor
from apps.patient.models import Patient


class Scheme(Model):
    name = CharField(verbose_name="Nombre", max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Esquema"
        verbose_name_plural = "Esquemas"
        ordering = ["pk"]
        default_permissions = ()


class RoomChoices(IntegerChoices):
    CHEMOTHERAPY = 1, "Quimioterapia"
    ROOM_1 = 2, "Sala 1"


class ProtocolQuerysetManager(Manager):
    def get_queryset(self) -> QuerySet:
        return (
            super()
            .get_queryset()
            .select_related("patient", "scheme", "doctor")
            .annotate(
                body_surface=Round2(
                    Cast(
                        ExpressionWrapper(
                            (0.007184 * F("weight") ** 0.425 * F("height") ** 0.725),
                            output_field=DecimalField(decimal_places=2, max_digits=10),
                        ),
                        output_field=DecimalField(decimal_places=2, max_digits=10),
                    ),
                    output_field=FloatField(),
                )
            )
        )

    def not_suspended(self) -> QuerySet:
        return self.get_queryset().filter(suspended=False)


class Protocol(TimeStampedModel):
    patient = ForeignKey(Patient, verbose_name="Paciente", on_delete=CASCADE)
    scheme = ForeignKey(Scheme, verbose_name="Esquema", on_delete=CASCADE)
    room = IntegerField(
        verbose_name="Lugar", null=True, blank=True, choices=RoomChoices.choices
    )
    height = IntegerField(verbose_name="Talla")
    weight = FloatField(verbose_name="Peso")
    cycles = IntegerField(verbose_name="Cantidad de ciclos")
    stage = IntegerField(
        verbose_name="Etapa", choices=NeoplasmClinicalStageChoices.choices
    )
    doctor = ForeignKey(Doctor, verbose_name="Doctor", on_delete=CASCADE)
    suspended = BooleanField()
    objects = ProtocolQuerysetManager()

    def __str__(self):
        return f"Protocolo de {self.patient} con esquema {self.scheme}"

    class Meta:
        verbose_name = "Protocolo"
        verbose_name_plural = "Protocolos"
        ordering = ["pk"]
        default_permissions = ()


class RouteChoices(IntegerChoices):
    INTRAMUSCULAR = 0, "Intramuscular"
    INTRAVENOUS = 1, "Intravenosa"
    SUBCUTANEOUS = 2, "Subcutaneo"
    INTRADERMAL = 3, "Intradérmica"
    ORAL = 4, "Oral"


class MedicationQuerysetManager(Manager):
    def get_queryset(self) -> QuerySet:
        return (
            super()
            .get_queryset()
            .select_related("protocol", "drug", "protocol__patient", "protocol__scheme")
        )


class Medication(Model):
    protocol = ForeignKey(Protocol, verbose_name="Protocolo", on_delete=CASCADE)
    drug = ForeignKey(Drug, verbose_name="Medicamento", on_delete=CASCADE)
    days = IntegerField(verbose_name="Días")
    route = IntegerField(
        verbose_name="Via de administración", choices=RouteChoices.choices
    )
    prescribed_dose = FloatField(verbose_name="Dosis prescrita")
    unit = IntegerField(
        verbose_name="Unidad", null=True, blank=True, choices=UnitChoicesChoices.choices
    )
    suspended = BooleanField(verbose_name="Suspendido")
    cause = CharField(verbose_name="Causa", max_length=255, null=True, blank=True)
    objects = MedicationQuerysetManager()

    def __str__(self) -> str:
        return f"{self.drug} en {self.protocol}"

    class Meta:
        verbose_name = "Medicación"
        verbose_name_plural = "Medicaciones"
        ordering = ["pk"]
        default_permissions = ()
