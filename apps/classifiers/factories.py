from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography


class TopographyFactory(DjangoModelFactory):
    """Factory to handle Topography creation."""

    class Meta:
        model = Topography

    code = FuzzyText(length=5)
    description = FuzzyText(length=20)


class MorphologyFactory(DjangoModelFactory):
    """Factory to handle Morphology creation."""

    class Meta:
        model = Morphology

    code = FuzzyText(length=5)
    description = FuzzyText(length=20)


class StudyFactory(DjangoModelFactory):
    """Factory to handle Study creation."""

    class Meta:
        model = Study

    name = FuzzyText(length=5)


class RadioIsotopeFactory(DjangoModelFactory):
    """Factory to handle RadioIsotope creation."""

    class Meta:
        model = RadioIsotope

    name = FuzzyText(length=5)
