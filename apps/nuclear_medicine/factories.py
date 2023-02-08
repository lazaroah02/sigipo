from factory import SubFactory, post_generation
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat, FuzzyText

from apps.classifiers.factories import RadioIsotopeFactory, StudyFactory
from apps.drugs.factories import NuclearMedicineDrugFactory
from apps.nuclear_medicine.models import (
    Gammagraphy,
    HormonalResult,
    HormonalStudy,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    SerialIodineDetection,
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
        model = HormonalStudy

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


class GammagraphyFactory(DjangoModelFactory):
    """Factory to handle Gammagraphy creation."""

    class Meta:
        model = Gammagraphy

    patient = SubFactory(PatientFactory)
    drug = SubFactory(NuclearMedicineDrugFactory)
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
