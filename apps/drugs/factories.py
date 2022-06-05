from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from apps.drugs.models import Drug, DrugTypeChoices


class DrugFactory(DjangoModelFactory):
    """Factory to handle Drugs creation."""

    class Meta:
        model = Drug

    name = FuzzyText(length=5)
    drug_type = FuzzyChoice(DrugTypeChoices.values)
