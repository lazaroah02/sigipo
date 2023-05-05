from django.core.management.base import BaseCommand

from apps.accounts.factories import UserFactory
from apps.cancer_registry.factories import (
    DoctorFactory,
    GroupFactory,
    NeoplasmFactory,
    PatientFactory,
)
from apps.chemotherapy.factories import (
    CycleFactory,
    CycleMedicationFactory,
    DrugFactory,
    MedicationFactory,
    ProtocolFactory,
)
from apps.death_certificate.factories import DeathCertificateFactory
from apps.geographic_location.factories import LocationFactory, MunicipalityFactory
from apps.nuclear_medicine.factories import (
    GammagraphyFactory,
    HormonalResultFactory,
    HormonalStudyFactory,
    IodineDetectionFactory,
    OncologicResultFactory,
    OncologicStudyFactory,
    SerialIodineDetectionFactory,
    StudyFactory,
)

NUMBER_OF_INSTANCES_TO_CREATE = 5


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
        for _ in range(NUMBER_OF_INSTANCES_TO_CREATE):
            municipality = MunicipalityFactory.create()
            patient = PatientFactory.create(
                residence_municipality=municipality, born_municipality=municipality
            )
            group = GroupFactory.create()
            doctor = DoctorFactory.create(group=group)
            study = StudyFactory.create()
            NeoplasmFactory.create(
                patient=patient,
                group=group,
                medic_that_report=doctor,
            )
            protocol = ProtocolFactory.create(patient=patient, doctor=doctor)
            drug = DrugFactory.create()
            MedicationFactory.create(drug=drug, protocol=protocol)
            cycle = CycleFactory.create(protocol=protocol)
            CycleMedicationFactory.create(cycle=cycle, drug=drug)
            oncologic_study = OncologicStudyFactory.create(patient=patient)
            hormonal_study = HormonalStudyFactory.create(patient=patient)
            OncologicResultFactory.create(oncologic_study=oncologic_study)
            HormonalResultFactory.create(hormonal_study=hormonal_study)
            IodineDetectionFactory.create(patient=patient)
            SerialIodineDetectionFactory.create(patient=patient)
            GammagraphyFactory.create(
                patient=patient,
                requested_study=[study],
            )
            location = LocationFactory.create(municipality=municipality)
            DeathCertificateFactory.create(patient=patient, death_location=location)
        self.stdout.write("Created a samples of data.")
