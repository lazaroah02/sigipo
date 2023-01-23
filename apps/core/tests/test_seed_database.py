from io import StringIO

from django.core.management import call_command

from apps.accounts.models import User
from apps.cancer_registry.models import Neoplasm
from apps.chemotherapy.models import (
    Cycle,
    CycleMedication,
    Medication,
    Protocol,
    Scheme,
)
from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography
from apps.core.test import TestCase
from apps.drugs.models import Drug, NuclearMedicineDrug
from apps.employee.models import Doctor, Group
from apps.geographic_location.models import Province
from apps.nuclear_medicine.models import (
    Gammagraphy,
    HormonalResult,
    HormonalStudy,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    SerialIodineDetection,
)
from apps.patient.models import Municipality, Patient


class SeedDatabaseTest(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "seed_database",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_province_instances_number(self):
        self.call_command()
        user = User.objects.all().count()
        provinces = Province.objects.all().count()
        municipality = Municipality.objects.all().count()
        patient = Patient.objects.all().count()
        group = Group.objects.all().count()
        doctor = Doctor.objects.all().count()
        topography = Topography.objects.all().count()
        morphology = Morphology.objects.all().count()
        study = Study.objects.all().count()
        radioisotope = RadioIsotope.objects.all().count()
        neoplasm = Neoplasm.objects.all().count()
        scheme = Scheme.objects.all().count()
        protocol = Protocol.objects.all().count()
        drug = Drug.objects.all().count()
        nuclearmedicinedrug = NuclearMedicineDrug.objects.all().count()
        medication = Medication.objects.all().count()
        cycle = Cycle.objects.all().count()
        cyclemedication = CycleMedication.objects.all().count()
        oncologicstudy = OncologicStudy.objects.all().count()
        hormonalstudy = HormonalStudy.objects.all().count()
        oncologicresult = OncologicResult.objects.all().count()
        hormonalresult = HormonalResult.objects.all().count()
        iodinedetection = IodineDetection.objects.all().count()
        serialiodinedetection = SerialIodineDetection.objects.all().count()
        gammagraphy = Gammagraphy.objects.all().count()

        self.assertEqual(provinces, 5, "Provincias")
        self.assertEqual(municipality, 5, "Municipios")
        self.assertEqual(patient, 5, "Pacientes")
        self.assertEqual(group, 5, "Grupos")
        self.assertEqual(doctor, 5, "Doctor")
        self.assertEqual(topography, 5, "Topografía")
        self.assertEqual(morphology, 5, "Morfología")
        self.assertEqual(study, 5, "Estudios")
        self.assertEqual(radioisotope, 5, "Radioisótopos")
        self.assertEqual(neoplasm, 5, "Neoplastias")
        self.assertEqual(scheme, 5, "Esquemas")
        self.assertEqual(protocol, 5, "Protocolos")
        self.assertEqual(drug, 5, "Fármacos")
        self.assertEqual(nuclearmedicinedrug, 5, "Fármacos-MN")
        self.assertEqual(medication, 5, "Medicación")
        self.assertEqual(cycle, 5, "Ciclo")
        self.assertEqual(cyclemedication, 5, "Cyclos de Medicación")
        self.assertEqual(oncologicstudy, 5, "Estudio Oncológico")
        self.assertEqual(hormonalstudy, 5, "Estudio Hormonal")
        self.assertEqual(oncologicresult, 5, "Resultados Oncológicos")
        self.assertEqual(hormonalresult, 5, "Resultados Hormonales")
        self.assertEqual(user, 1, "Usuario")
        self.assertEqual(iodinedetection, 5, "Detección de Yodo")
        self.assertEqual(serialiodinedetection, 5, "Detección de Yodo Seriada")
        self.assertEqual(gammagraphy, 5, "Gammagrafías")
