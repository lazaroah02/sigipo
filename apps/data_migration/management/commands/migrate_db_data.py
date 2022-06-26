from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.db.models import Q

from apps.cancer_registry.models import Neoplasm
from apps.chemotherapy.models import Scheme
from apps.classifiers.models import Morphology, Topography
from apps.data_migration.models import (
    DatosTumor,
    Diagnostico,
    Esquema,
    Grupo,
    Localizacion,
    Medicamentos,
    Medico,
    Municipio,
    Paciente,
    Provincia,
)
from apps.drugs.models import Drug
from apps.employee.models import Doctor, Group
from apps.geographic_location.models import Municipality, Province
from apps.patient.models import Patient


class Command(BaseCommand):
    help = "Migrate MariaDB data to Postgres"

    def handle(self, *args, **options):
        with transaction.atomic():
            scheme_data = [scheme.to_postgres_db() for scheme in Esquema.objects.all()]
            Scheme.objects.bulk_create(scheme_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated scheme model '%s' instances"
                    % len(scheme_data)
                )
            )
            drug_data = [drug.to_postgres_db() for drug in Medicamentos.objects.all()]
            Drug.objects.bulk_create(drug_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated drug model '%s' instances" % len(drug_data)
                )
            )
            morphology_data = [
                morphology.to_postgres_db() for morphology in Diagnostico.objects.all()
            ]
            morphology_related = {
                morphology.pk: morphology for morphology in morphology_data
            }
            Morphology.objects.bulk_create(morphology_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated morphology model '%s' instances"
                    % len(morphology_data)
                )
            )
            topography_data = [
                topography.to_postgres_db() for topography in Localizacion.objects.all()
            ]
            topography_related = {
                topography.pk: topography for topography in topography_data
            }
            Topography.objects.bulk_create(topography_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated topography model '%s' instances"
                    % len(topography_data)
                )
            )
            group_data = [group.to_postgres_db() for group in Grupo.objects.all()]
            group_related = {group.pk: group for group in group_data}
            Group.objects.bulk_create(group_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated group model '%s' instances" % len(group_data)
                )
            )
            doctor_data = [
                doctor.to_postgres_db(group_related)
                for doctor in Medico.objects.select_related("grupo").all()
            ]
            doctor_related = {doctor.pk: doctor for doctor in doctor_data}
            Doctor.objects.bulk_create(doctor_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated group doctor '%s' instances"
                    % len(doctor_data)
                )
            )
            province_data = [
                province.to_postgres_db() for province in Provincia.objects.all()
            ]
            province_related = {province.pk: province for province in province_data}
            Province.objects.bulk_create(province_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated province model '%s' instances"
                    % len(province_data)
                )
            )
            municipality_data = [
                municipality.to_postgres_db(province_related)
                for municipality in Municipio.objects.select_related("provincia").all()
            ]
            municipality_related = {
                municipality.name: municipality for municipality in municipality_data
            }
            Municipality.objects.bulk_create(municipality_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated municipality model '%s' instances"
                    % len(municipality_data)
                )
            )
            patient_data = [
                patient.to_postgres_db(municipality_related)
                for patient in Paciente.objects.select_related("provincia").filter(
                    ~Q(ci=""), nombres__isnull=False, ci__isnull=False
                )
            ]
            patient_related = {
                patient.identity_card: patient for patient in patient_data
            }
            Patient.objects.bulk_create(patient_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated patient model '%s' instances"
                    % len(patient_data)
                )
            )
            tumor = [
                tumor.to_postgres_db(
                    {
                        "doctor": doctor_related,
                        "group": group_related,
                        "morphology": morphology_related,
                        "topography": topography_related,
                        "patient": patient_related,
                    }
                )
                for tumor in DatosTumor.objects.select_related(
                    "ci", "localizacion", "diagnostico", "regprof", "id_grupo"
                ).all()
            ]
            Neoplasm.objects.bulk_create(tumor)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated neoplasm model '%s' instances" % len(tumor)
                )
            )

        self.stdout.write(self.style.SUCCESS("Successfully migrated MARIA DB data"))
        self.stdout.write(self.style.SUCCESS("Resetting sequences"))
        with connection.cursor() as cursor:
            cursor.execute(
                """
                BEGIN;
                SELECT setval(pg_get_serial_sequence('"geographic_location_province"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "geographic_location_province";
                SELECT setval(pg_get_serial_sequence('"geographic_location_municipality"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "geographic_location_municipality";
                SELECT setval(pg_get_serial_sequence('"classifiers_topography"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "classifiers_topography";
                SELECT setval(pg_get_serial_sequence('"classifiers_morphology"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "classifiers_morphology";
                SELECT setval(pg_get_serial_sequence('"classifiers_study"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "classifiers_study";
                SELECT setval(pg_get_serial_sequence('"classifiers_radioisotope"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "classifiers_radioisotope";
                SELECT setval(pg_get_serial_sequence('"drugs_nuclearmedicinedrug"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "drugs_nuclearmedicinedrug";
                SELECT setval(pg_get_serial_sequence('"drugs_drug"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "drugs_drug";
                SELECT setval(pg_get_serial_sequence('"employee_group"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "employee_group";
                SELECT setval(pg_get_serial_sequence('"patient_patient"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "patient_patient";
                SELECT setval(pg_get_serial_sequence('"cancer_registry_neoplasm"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "cancer_registry_neoplasm";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_oncologicstudy"','sample_number'), coalesce(max("sample_number"), 1), max("sample_number") IS NOT null) FROM "nuclear_medicine_oncologicstudy";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_hormonalstudy"','sample_number'), coalesce(max("sample_number"), 1), max("sample_number") IS NOT null) FROM "nuclear_medicine_hormonalstudy";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_hormonalresult"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "nuclear_medicine_hormonalresult";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_oncologicresult"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "nuclear_medicine_oncologicresult";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_iodinedetection"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "nuclear_medicine_iodinedetection";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_serialiodinedetection"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "nuclear_medicine_serialiodinedetection";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_gammagraphy_requested_study"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "nuclear_medicine_gammagraphy_requested_study";
                SELECT setval(pg_get_serial_sequence('"nuclear_medicine_gammagraphy"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "nuclear_medicine_gammagraphy";
                SELECT setval(pg_get_serial_sequence('"chemotherapy_scheme"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "chemotherapy_scheme";
                SELECT setval(pg_get_serial_sequence('"chemotherapy_protocol"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "chemotherapy_protocol";
                SELECT setval(pg_get_serial_sequence('"chemotherapy_medication"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "chemotherapy_medication";
                SELECT setval(pg_get_serial_sequence('"chemotherapy_cycle"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "chemotherapy_cycle";
                SELECT setval(pg_get_serial_sequence('"chemotherapy_cyclemedication"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "chemotherapy_cyclemedication";
                COMMIT;
            """
            )
        self.stdout.write(self.style.SUCCESS("Migration Complete ;)"))
