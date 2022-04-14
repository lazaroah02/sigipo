from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from apps.classifiers.models import Morphology, Topography


class TopographyFactory(DjangoModelFactory):
    """Factory to handle Topography creation."""

    class Meta:
        model = Topography

    code = FuzzyText(length=5)
    description = FuzzyText(length=200)


class MorphologyFactory(DjangoModelFactory):
    """Factory to handle Morphology creation."""

    class Meta:
        model = Morphology

    code = FuzzyText(length=5)
    description = FuzzyText(length=200)
