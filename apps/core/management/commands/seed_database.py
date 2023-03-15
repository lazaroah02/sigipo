from django.core.management.base import BaseCommand

from apps.accounts.factories import UserFactory
from apps.cancer_registry.factories import (
    DoctorFactory,
    GroupFactory,
    MorphologyFactory,
    NeoplasmFactory,
    PatientFactory,
    TopographyFactory,
)
from apps.chemotherapy.factories import (
    CycleFactory,
    CycleMedicationFactory,
    DrugFactory,
    MedicationFactory,
    ProtocolFactory,
    SchemeFactory,
)
from apps.geographic_location.factories import MunicipalityFactory, ProvinceFactory
from apps.nuclear_medicine.factories import (
    GammagraphyFactory,
    HormonalResultFactory,
    HormonalStudyFactory,
    IodineDetectionFactory,
    NuclearMedicineDrugFactory,
    OncologicResultFactory,
    OncologicStudyFactory,
    RadioIsotopeFactory,
    SerialIodineDetectionFactory,
    StudyFactory,
)


class Command(BaseCommand):
    """
    It Generates 5 instances of all models and creates
    a user with administrative credentials.
    """

    help = "Generates 5 instances of all models"

    def handle(self, *args, **options):
        """
        default handle method to execute the management command functionality.
        """
        UserFactory.create(username="admin", password="123")
        for _ in range(5):
            province = ProvinceFactory.create()
            municipality = MunicipalityFactory.create(province=province)
            patient = PatientFactory.create(
                residence_municipality=municipality, born_municipality=municipality
            )
            group = GroupFactory.create()
            doctor = DoctorFactory.create(group=group)
            topography = TopographyFactory.create()
            morphology = MorphologyFactory.create()
            study = StudyFactory.create()
            radioisotope = RadioIsotopeFactory.create()
            NeoplasmFactory.create(
                patient=patient,
                primary_site=topography,
                histologic_type=morphology,
                group=group,
                medic_that_report=doctor,
            )
            scheme = SchemeFactory.create()
            protocol = ProtocolFactory.create(
                patient=patient, scheme=scheme, doctor=doctor
            )
            drug = DrugFactory.create()
            nuclearmedicinedrug = NuclearMedicineDrugFactory.create()
            MedicationFactory.create(drug=drug, protocol=protocol)
            cycle = CycleFactory.create(protocol=protocol)
            CycleMedicationFactory.create(cycle=cycle, drug=drug)
            oncologicstudy = OncologicStudyFactory.create(patient=patient)
            hormonalstudy = HormonalStudyFactory.create(patient=patient)
            OncologicResultFactory.create(oncologic_study=oncologicstudy)
            HormonalResultFactory.create(hormonal_study=hormonalstudy)
            IodineDetectionFactory.create(patient=patient)
            SerialIodineDetectionFactory.create(patient=patient)
            GammagraphyFactory.create(
                patient=patient,
                drug=nuclearmedicinedrug,
                radio_isotope=radioisotope,
                requested_study=[study],
            )
