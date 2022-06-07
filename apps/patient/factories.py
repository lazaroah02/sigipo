import string

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from apps.geographic_location.factories import MunicipalityFactory
from apps.patient.models import Patient, PatientRace


class PatientFactory(DjangoModelFactory):
    """Factory to handle Patient creation."""

    class Meta:
        model = Patient

    identity_card = FuzzyText(length=11, chars=string.digits)
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
    address = FuzzyText(length=10)
    race = FuzzyChoice(PatientRace.values)
    medical_record = FuzzyText(length=32)
    is_oncologic = FuzzyChoice((True, False))
    residence_municipality = SubFactory(MunicipalityFactory)
    born_municipality = SubFactory(MunicipalityFactory)
    street = FuzzyText(length=4)
    number = FuzzyText(length=4)
    building = FuzzyText(length=4)
    apartment = FuzzyText(length=4)
    between_streets = FuzzyText(length=4)
    division = FuzzyText(length=4)
