from factory import SubFactory, post_generation
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat, FuzzyText

from apps.drugs.factories import DrugFactory
from apps.nuclear_medicine.models import (
    Gammagraphy,
    HormonalResult,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    PatientHormonalStudy,
    RadioIsotope,
    SerialIodineDetection,
    Study,
)
from apps.patient.factories import PatientFactory


class OncologicStudyFactory(DjangoModelFactory):
    """Factory to handle OncologicStudy creation."""

    class Meta:
        model = OncologicStudy

    patient = SubFactory(PatientFactory)
    tests = "TSH"


class HormonalStudyFactory(DjangoModelFactory):
    """Factory to handle HormonalStudy creation."""

    class Meta:
        model = PatientHormonalStudy

    patient = SubFactory(PatientFactory)
    tests = "TSH"


class HormonalResultFactory(DjangoModelFactory):
    """Factory to handle HormonalResult creation."""

    class Meta:
        model = HormonalResult

    hormonal_study = SubFactory(HormonalStudyFactory)
    tsh = FuzzyFloat(0, high=100)


class OncologicResultFactory(DjangoModelFactory):
    """Factory to handle OncologicResult creation."""

    class Meta:
        model = OncologicResult

    oncologic_study = SubFactory(OncologicStudyFactory)
    tsh = FuzzyFloat(0, high=100)


class IodineDetectionFactory(DjangoModelFactory):
    """Factory to handle IodineDetection creation."""

    class Meta:
        model = IodineDetection

    patient = SubFactory(PatientFactory)
    two_hours = FuzzyFloat(0, 100)
    twenty_four_hours = FuzzyFloat(0, 100)


class SerialIodineDetectionFactory(DjangoModelFactory):
    """Factory to handle SerialIodineDetection creation."""

    class Meta:
        model = SerialIodineDetection

    patient = SubFactory(PatientFactory)
    two_hours = FuzzyFloat(0, 100)
    four_hours = FuzzyFloat(0, 100)
    eight_hours = FuzzyFloat(0, 100)
    twenty_four_hours = FuzzyFloat(0, 100)
    forty_eight_hours = FuzzyFloat(0, 100)
    seventy_two_hours = FuzzyFloat(0, 100)
    ninety_six_hours = FuzzyFloat(0, 100)


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


class GammagraphyFactory(DjangoModelFactory):
    """Factory to handle Gammagraphy creation."""

    class Meta:
        model = Gammagraphy

    patient = SubFactory(PatientFactory)
    drug = SubFactory(DrugFactory)
    radio_isotope = SubFactory(RadioIsotopeFactory)
    dose = FuzzyFloat(0, 100)
    report = FuzzyText(length=10)
    observation = FuzzyText(length=10)

    @post_generation
    def requested_study(self, create, extracted, **kwargs):
        if extracted:
            # A list of groups were passed in, use them
            for study in extracted:
                self.requested_study.add(study)
        else:
            self.requested_study.add(StudyFactory.create())
