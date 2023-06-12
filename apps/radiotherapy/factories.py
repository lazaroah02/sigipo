import datetime as dt

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyFloat, FuzzyInteger, FuzzyText

from apps.employee.factories import DoctorFactory
from apps.patient.factories import PatientFactory
from apps.radiotherapy.models import (
    Accessories,
    AnatomicDataChoices,
    DosimetryPlan,
    Energy,
    Equipment,
    MedicalTurn,
    ModalityChoices,
    OAR_TV_TypeChoices,
    Prescription,
    RiskOrgans,
    TACStudy,
)


class DosimetryPlanFactory(DjangoModelFactory):
    class Meta:
        model = DosimetryPlan

    patient = SubFactory(PatientFactory)
    radiation_therapist_in_charge = FuzzyText(length=16)
    team = FuzzyText(length=16)
    doctor_asigned = SubFactory(DoctorFactory)
    plan = FuzzyText(length=16)
    fractial_dosis = FuzzyFloat(0, 100)
    total_dosis = FuzzyFloat(0, 100)
    session_number = FuzzyInteger(0, 100)
    anatomic_data_aquisition = FuzzyChoice(AnatomicDataChoices.values)
    icru_dosis = FuzzyFloat(0, 100)
    max_dosis = FuzzyFloat(0, 100)
    modality = FuzzyText(length=16)


class EnergyFactory(DjangoModelFactory):
    class Meta:
        model = Energy

    energy = FuzzyText(length=16)
    enable = FuzzyChoice((True, False))


class EquipmentFactory(DjangoModelFactory):
    name = FuzzyText(length=16)
    modality = FuzzyChoice(ModalityChoices.values)
    energy = SubFactory(EnergyFactory)

    class Meta:
        model = Equipment


class AccessoriesFactory(DjangoModelFactory):
    class Meta:
        model = Accessories

    name = FuzzyText(length=16)
    type = FuzzyText(length=16)
    eid = FuzzyText(length=16)
    enable_equipment = SubFactory(EquipmentFactory)


class RiskOrgansFactory(DjangoModelFactory):
    class Meta:
        model = RiskOrgans

    name = FuzzyText(length=16)
    type = FuzzyChoice(OAR_TV_TypeChoices.values)
    alpha_beta = FuzzyInteger(0, 100)
    dosis_limit = FuzzyFloat(0, 100)


class PrescriptionFactory(DjangoModelFactory):
    class Meta:
        model = Prescription

    treatment_serie = FuzzyText(length=16)
    modality = FuzzyChoice(ModalityChoices.values)
    equipo = SubFactory(EquipmentFactory)
    irradiate_other_locations = FuzzyChoice((True, False))
    reirradiated_patient = FuzzyChoice((True, False))
    status = FuzzyText(length=16)
    location = FuzzyText(length=16)
    fractial_dosis = FuzzyFloat(0, 100)
    total_dosis = FuzzyFloat(0, 100)
    session_number = FuzzyInteger(0, 100)
    weekly_session = FuzzyInteger(0, 100)
    daily_session = FuzzyInteger(0, 100)
    organs_at_risk = SubFactory(RiskOrgansFactory)
    # registred_by = SubFactory(ad)
    radiotherapist_in_charge = SubFactory(DoctorFactory)
    patient = SubFactory(PatientFactory)


class MedicalTurnFactory(DjangoModelFactory):
    class Meta:
        model = MedicalTurn

    patient = SubFactory(PatientFactory)
    cid = FuzzyInteger(0, 100)
    id = FuzzyText(length=16)
    address = FuzzyText(length=16)
    location = FuzzyText(length=16)
    stage = FuzzyText(length=16)
    doctor = SubFactory(DoctorFactory)
    waiting_list = FuzzyChoice((True, False))
    date_first_apointment = FuzzyDate(dt.date(1990, 1, 1), end_date=dt.date.today())
    date_culmination_treatment = FuzzyDate(
        dt.date(1990, 1, 1), end_date=dt.date.today()
    )


class TACStudyFactory(DjangoModelFactory):
    class Meta:
        model = TACStudy

    patient = SubFactory(PatientFactory)
    location = FuzzyText(length=16)
    chunck_distance = FuzzyFloat(1, 100)
    patient_position = FuzzyText(length=16)
    protocol = FuzzyText(length=16)
    doctor = SubFactory(DoctorFactory)
