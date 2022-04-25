from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from apps.nuclear_medicine.models import PatientOncologicStudy
from apps.patient.factories import PatientFactory


class OncologicStudyFactory(DjangoModelFactory):
    """Factory to handle OncologicStudy creation."""

    class Meta:
        model = PatientOncologicStudy

    province = SubFactory(PatientFactory)
    name = FuzzyText(prefix="Municipio-", length=20)
