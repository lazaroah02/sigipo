import datetime as dt

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyFloat, FuzzyInteger, FuzzyText

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.chemotherapy.models import (
    Cycle,
    CycleMedication,
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


class CycleFactory(DjangoModelFactory):
    """Factory to handle Cycle creation."""

    class Meta:
        model = Cycle

    protocol = SubFactory(ProtocolFactory)
    next_date = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())


class CycleMedicationFactory(DjangoModelFactory):
    """Factory to handle CycleMedication creation."""

    class Meta:
        model = CycleMedication

    cycle = SubFactory(CycleFactory)
    drug = SubFactory(DrugFactory)
    dose = FuzzyFloat(1, high=10)
    unit = FuzzyChoice(UnitChoicesChoices.values)
