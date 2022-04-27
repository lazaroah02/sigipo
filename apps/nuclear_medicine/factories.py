from factory import SubFactory
from factory.django import DjangoModelFactory

from apps.nuclear_medicine.models import PatientHormonalStudy, PatientOncologicStudy
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
