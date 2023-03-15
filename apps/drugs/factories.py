from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyFloat, FuzzyText

from apps.drugs.models import (
    Drug,
    DrugTypeChoices,
    NuclearMedicineDrug,
    PresentationChoicesChoices,
    UnitChoicesChoices,
)


class DrugFactory(DjangoModelFactory):
    """Factory to handle Drugs creation."""

    class Meta:
        model = Drug

    name = FuzzyText(length=5)
    drug_type = FuzzyChoice(DrugTypeChoices.values)
    presentation = FuzzyChoice(PresentationChoicesChoices.values)
    amount = FuzzyFloat(low=0.1, high=100)
    unit = FuzzyChoice(UnitChoicesChoices.values)
    out_of_stock = FuzzyChoice((True, False))


class NuclearMedicineDrugFactory(DjangoModelFactory):
    """Factory to handle NuclearMedicineDrug creation."""

    class Meta:
        model = NuclearMedicineDrug

    name = FuzzyText(length=5)
