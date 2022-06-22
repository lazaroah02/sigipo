from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyFloat, FuzzyInteger, FuzzyText

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.chemotherapy.models import (
    Medication,
    Protocol,
    RoomChoices,
    RouteChoices,
    Scheme,
)
from apps.drugs.factories import DrugFactory
from apps.drugs.models import UnitChoicesChoices
from apps.employee.factories import DoctorFactory
from apps.patient.factories import PatientFactory


class SchemeFactory(DjangoModelFactory):
    """Factory to handle Scheme creation."""

    class Meta:
        model = Scheme

    name = FuzzyText(length=5)


class ProtocolFactory(DjangoModelFactory):
    """Factory to handle Protocol creation."""

    class Meta:
        model = Protocol

    patient = SubFactory(PatientFactory)
    scheme = SubFactory(SchemeFactory)
    room = FuzzyChoice(RoomChoices.values)
    height = FuzzyInteger(1, high=10)
    weight = FuzzyFloat(1, high=10)
    cycles = FuzzyInteger(0, high=10)
    stage = FuzzyChoice(NeoplasmClinicalStageChoices.values)
    doctor = SubFactory(DoctorFactory)
    suspended = FuzzyChoice((True, False))


class MedicationFactory(DjangoModelFactory):
    """Factory to handle Medication creation."""

    class Meta:
        model = Medication

    protocol = SubFactory(ProtocolFactory)
    drug = SubFactory(DrugFactory)
    days = FuzzyInteger(1, high=10)
    route = FuzzyChoice(RouteChoices.values)
    prescribed_dose = FuzzyFloat(1, high=10)
    unit = FuzzyChoice(UnitChoicesChoices.values)
    suspended = FuzzyChoice((True, False))
    cause = FuzzyText(length=5)
