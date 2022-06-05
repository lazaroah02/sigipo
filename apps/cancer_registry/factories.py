import datetime as dt

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate

from apps.cancer_registry.models import (
    AcuteLymphoidLeukemiaChoices,
    AcuteMyeloidLeukemiaChoices,
    ChronicLymphoidLeukemiaChoices,
    ChronicMyeloidLeukemiaChoices,
    MetastasisChoices,
    MultipleMyelomaChoices,
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
from apps.employee.factories import DoctorFactory, GroupFactory
from apps.patient.factories import PatientFactory


class NeoplasmFactory(DjangoModelFactory):
    """Factory to handle Neoplasm creation."""

    class Meta:
        model = Neoplasm

    patient = SubFactory(PatientFactory)
    primary_site = SubFactory(TopographyFactory)
    histologic_type = SubFactory(MorphologyFactory)
    medic_that_report = SubFactory(DoctorFactory)
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
    group = SubFactory(GroupFactory)
    hematological_transformation = FuzzyChoice((True, False))
    date_of_first_symptoms = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    acute_lymphoid_leukemia = FuzzyChoice(AcuteLymphoidLeukemiaChoices.values)
    chronic_lymphoid_leukemia = FuzzyChoice(ChronicLymphoidLeukemiaChoices.values)
    acute_myeloid_leukemia = FuzzyChoice(AcuteMyeloidLeukemiaChoices.values)
    multiple_myeloma = FuzzyChoice(MultipleMyelomaChoices.values)
    chronic_myeloid_leukemia = FuzzyChoice(ChronicMyeloidLeukemiaChoices.values)
