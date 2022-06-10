from django.core.management.base import BaseCommand
from django.db import transaction

from apps.classifiers.models import Morphology, Topography
from apps.data_migration.models import (
    Diagnostico,
    Grupo,
    Localizacion,
    Medico,
    Municipio,
    Provincia,
)
from apps.employee.models import Doctor, Group
from apps.geographic_location.models import Municipality, Province


class Command(BaseCommand):
    help = "Migrate MariaDB data to Postgres"

    def handle(self, *args, **options):
        with transaction.atomic():
            morphology_data = [
                morphology.to_postgres_db() for morphology in Diagnostico.objects.all()
            ]
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
                doctor.to_postgres_db(group_related) for doctor in Medico.objects.all()
            ]
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
                for municipality in Municipio.objects.all()
            ]
            Municipality.objects.bulk_create(municipality_data)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully migrated municipality model '%s' instances"
                    % len(municipality_data)
                )
            )

        self.stdout.write(self.style.SUCCESS("Successfully migrated MARIA DB data"))
