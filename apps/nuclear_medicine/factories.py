from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat

from apps.nuclear_medicine.models import (
    HormonalResult,
    OncologicResult,
    PatientHormonalStudy,
    PatientOncologicStudy,
)
from apps.patient.factories import PatientFactory


class OncologicStudyFactory(DjangoModelFactory):
    """Factory to handle OncologicStudy creation."""

    class Meta:
        model = PatientOncologicStudy

    patient = SubFactory(PatientFactory)
    tests = "TSH"


class HormonalStudyFactory(DjangoModelFactory):
    """Factory to handle HormonalStudy creation."""

    class Meta:
        model = PatientHormonalStudy

    patient = SubFactory(PatientFactory)
    tests = "TSH"


class HormonalResultFactory(DjangoModelFactory):
    """Factory to handle HormonalResult creation."""

    class Meta:
        model = HormonalResult

    hormonal_study = SubFactory(HormonalStudyFactory)
    tsh = FuzzyFloat(0, high=100)


class OncologicResultFactory(DjangoModelFactory):
    """Factory to handle OncologicResult creation."""

    class Meta:
        model = OncologicResult

    oncologic_study = SubFactory(OncologicStudyFactory)
    tsh = FuzzyFloat(0, high=100)
