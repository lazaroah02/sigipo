from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Q

from apps.cancer_registry.models import Neoplasm
from apps.classifiers.models import Morphology, Topography
from apps.data_migration.models import (
    DatosTumor,
    Diagnostico,
    Grupo,
    Localizacion,
    Medico,
    Municipio,
    Paciente,
    Provincia,
)
from apps.employee.models import Doctor, Group
from apps.geographic_location.models import Municipality, Province
from apps.patient.models import Patient


class Command(BaseCommand):
    help = "Migrate MariaDB data to Postgres"

    def handle(self, *args, **options):
        with transaction.atomic():
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
