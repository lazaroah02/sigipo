from factory import SubFactory
from factory.django import DjangoModelFactory

from apps.classifiers.factories import MorphologyFactory, TopographyFactory
from apps.neoplasm.models import Neoplasm
from apps.patient.factories import PatientFactory


class NeoplasmFactory(DjangoModelFactory):
    """Factory to handle Neoplasm creation."""

    class Meta:
        model = Neoplasm

    patient = SubFactory(PatientFactory)
    primary_site = SubFactory(TopographyFactory)
    histologic_type = SubFactory(MorphologyFactory)
