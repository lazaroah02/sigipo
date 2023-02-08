from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from apps.employee.models import Doctor, Group


class GroupFactory(DjangoModelFactory):
    """Factory to handle Group creation."""

    class Meta:
        model = Group

    name = FuzzyText(length=5)


class DoctorFactory(DjangoModelFactory):
    """Factory to handle Doctor creation."""

    class Meta:
        model = Doctor

    first_name = FuzzyChoice(
        (
            "Mario",
            "Maria",
            "Juan",
            "Juana",
            "Miguel",
            "Sofia",
            "Ana",
            "Laura",
            "Pedro",
            "Jose",
            "Raul",
            "Isabel",
            "Vicente",
            "Cecilia",
            "Adriana",
            "Andrea",
            "Aurora",
            "Claudia",
            "Daniela",
            "Daniel",
            "Diana",
            "Frank",
        )
    )
    last_name = FuzzyChoice(
        (
            "Gonzales",
            "Fernandez",
            "del Rio",
            "Castillo",
            "del Valle",
            "Álvarez",
            "Castillo",
            "Diaz",
            "de Leon",
            "Garcia",
        )
    )
    group = SubFactory(GroupFactory)
    personal_record_number = FuzzyText(length=6)
