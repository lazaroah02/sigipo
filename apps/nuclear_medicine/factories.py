from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat

from apps.nuclear_medicine.models import (
    HormonalResult,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    PatientHormonalStudy,
    SerialIodineDetection,
)
from apps.patient.factories import PatientFactory


class OncologicStudyFactory(DjangoModelFactory):
    """Factory to handle OncologicStudy creation."""

    class Meta:
        model = OncologicStudy

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


class IodineDetectionFactory(DjangoModelFactory):
    """Factory to handle IodineDetection creation."""

    class Meta:
        model = IodineDetection

    patient = SubFactory(PatientFactory)
    two_hours = FuzzyFloat(0, 100)
    twenty_four_hours = FuzzyFloat(0, 100)


class SerialIodineDetectionFactory(DjangoModelFactory):
    """Factory to handle SerialIodineDetection creation."""

    class Meta:
        model = SerialIodineDetection

    patient = SubFactory(PatientFactory)
    two_hours = FuzzyFloat(0, 100)
    four_hours = FuzzyFloat(0, 100)
    eight_hours = FuzzyFloat(0, 100)
    twenty_four_hours = FuzzyFloat(0, 100)
    forty_eight_hours = FuzzyFloat(0, 100)
    seventy_two_hours = FuzzyFloat(0, 100)
    ninety_six_hours = FuzzyFloat(0, 100)
