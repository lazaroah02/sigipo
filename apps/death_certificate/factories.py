import datetime as dt

import pytz
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyDateTime, FuzzyText

from apps.death_certificate.models import (
    CertificationMadeByChoices,
    CivilStateChoices,
    ConfirmationCausesChoices,
    DeathCertificate,
    DeathPlaceChoices,
    LastSurgeriesChoices,
    PregnancyChoices,
    PregnancyResultChoices,
    ResidenceTypeChoices,
    ScholarshipLevelChoices,
    ViolentDeathCausesChoices,
)
from apps.geographic_location.factories import LocationFactory
from apps.patient.factories import PatientFactory


class DeathCertificateFactory(DjangoModelFactory):
    """Factory to handle death_certificate creation."""

    class Meta:
        model = DeathCertificate
        django_get_or_create = ("patient",)

    patient = SubFactory(PatientFactory)
    direct_death_cause = FuzzyText(length=16)
    indirect_death_cause_1 = {
        "cause": "asdf",
        "date": str(dt.datetime.now()),
        "code": 123,
    }
    indirect_death_cause_2 = {
        "cause": "asdf",
        "date": str(dt.datetime.now()),
        "code": 123,
    }
    indirect_death_cause_3 = {
        "cause": "asdf",
        "date": str(dt.datetime.now()),
        "code": 123,
    }
    other_contributing_diseases = {
        "cause": "asdf",
        "date": str(dt.datetime.now()),
        "code": 123,
    }
    datetime_of_death = FuzzyDateTime(
        dt.datetime.now(pytz.utc) - dt.timedelta(days=100),
        dt.datetime.now(pytz.utc) - dt.timedelta(days=10),
        force_day=1,
    )
    scholarship_level = FuzzyChoice(ScholarshipLevelChoices.values)
    civil_state = FuzzyChoice(CivilStateChoices.values)
    residence_type = FuzzyChoice(ResidenceTypeChoices.values)
    death_place = FuzzyChoice(DeathPlaceChoices.values)
    pregnancy = FuzzyChoice(PregnancyChoices.values)
    pregnancy_result = FuzzyChoice(PregnancyResultChoices.values)
    date_of_pregnancy = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    confirmation_causes = FuzzyChoice(ConfirmationCausesChoices.values)
    certification_made_by = FuzzyChoice(CertificationMadeByChoices.values)
    last_surgeries = FuzzyChoice(LastSurgeriesChoices.values)
    surgery_reasons = FuzzyText(length=16)
    violent_death_causes = FuzzyChoice(ViolentDeathCausesChoices.values)
    date_of_injury = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    place_where_injury_occurred = FuzzyText(length=16)
    event_description = FuzzyText(length=16)
    requesting_authority = FuzzyText(length=16)
    act_number = FuzzyText(length=16)
    death_location = SubFactory(LocationFactory)
