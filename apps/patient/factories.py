import datetime as dt
import string

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyText

from apps.geographic_location.factories import MunicipalityFactory
from apps.patient.models import Patient, PatientRace, SexChoices


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
    race = FuzzyChoice(PatientRace.values)
    medical_record = FuzzyText(length=32)
    is_oncologic = FuzzyChoice((True, False))
    residence_municipality = SubFactory(MunicipalityFactory)
    date_of_birth = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    sex = FuzzyChoice(choices=SexChoices.values)
    born_municipality = SubFactory(MunicipalityFactory)
    street = FuzzyText(length=4)
    number = FuzzyText(length=4)
    building = FuzzyText(length=4)
    apartment = FuzzyText(length=4)
    between_streets = FuzzyText(length=4)
    division = FuzzyText(length=4)
