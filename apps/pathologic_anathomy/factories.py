import datetime as dt
import string

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyText

from apps.employee.factories import DoctorFactory
from apps.pathologic_anathomy.models import (
    BiopsyRequest,
    BiopsyTypeChoice,
    HospitalChoice,
)
from apps.patient.factories import PatientFactory


class BiopsyRequestFactory(DjangoModelFactory):
    """Factory to handle Biopsy Request creation."""

    class Meta:
        model = BiopsyRequest

    biopsy_id = FuzzyText(length=11, chars=string.digits)
    hospital = FuzzyChoice(HospitalChoice.values)
    sample_date = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    health_area = FuzzyText(length=4)
    especialty = FuzzyText(length=4)
    patient = SubFactory(PatientFactory)
    biopsy_type = FuzzyChoice(BiopsyTypeChoice.values)
    sample_biopsy = FuzzyText(length=4)
    clinic_data = FuzzyText(length=4)
    clinic_diagnostic = FuzzyText(length=4)
    medic_that_report = SubFactory(DoctorFactory)
