import datetime as dt

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyText

from apps.cancer_registry.models import (
    MetastasisChoices,
    Neoplasm,
    NeoplasmClassificationChoices,
    NeoplasmClinicalExtensionsChoices,
    NeoplasmClinicalStageChoices,
    NeoplasmDiagnosticConfirmationChoices,
    NeoplasmDifferentiationGradesChoices,
    NeoplasmLateralityChoices,
    NeoplasmSourceOfInfoChoices,
    NoduleChoices,
    TreatmentPerformedChoices,
    TumorChoices,
    TumorClassificationChoices,
)
from apps.classifiers.factories import MorphologyFactory, TopographyFactory
from apps.patient.factories import PatientFactory


class NeoplasmFactory(DjangoModelFactory):
    """Factory to handle Neoplasm creation."""

    class Meta:
        model = Neoplasm

    patient = SubFactory(PatientFactory)
    primary_site = SubFactory(TopographyFactory)
    histologic_type = SubFactory(MorphologyFactory)
    medic_that_report = FuzzyText()
    date_of_report = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    date_of_diagnosis = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    laterality = FuzzyChoice(NeoplasmLateralityChoices.values)
    diagnostic_confirmation = FuzzyChoice(NeoplasmDiagnosticConfirmationChoices.values)
    differentiation_grade = FuzzyChoice(NeoplasmDifferentiationGradesChoices.values)
    clinical_extension = FuzzyChoice(NeoplasmClinicalExtensionsChoices.values)
    clinical_stage = FuzzyChoice(NeoplasmClinicalStageChoices.values)
    source_of_info = FuzzyChoice(NeoplasmSourceOfInfoChoices.values)
    trimester = FuzzyChoice((None, 1, 2, 3))
    is_pregnant = FuzzyChoice((True, False))
    is_vih = FuzzyChoice((True, False))
    treatment_performed = FuzzyChoice(TreatmentPerformedChoices.values)
    tumor = FuzzyChoice(TumorChoices.values)
    nodule = FuzzyChoice(NoduleChoices.values)
    metastasis = FuzzyChoice(MetastasisChoices.values)
    neoplasm_classification = FuzzyChoice(NeoplasmClassificationChoices.values)
    tumor_classification = FuzzyChoice(TumorClassificationChoices.values)
