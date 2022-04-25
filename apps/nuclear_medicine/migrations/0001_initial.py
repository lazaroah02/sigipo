# Generated by Django 3.2.13 on 2022-04-25 22:26

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("patient", "0003_patient_gender_view"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientOncologicStudy",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("sample_number", models.AutoField(primary_key=True, serialize=False)),
                (
                    "tests",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("TSH", "TSH"),
                            ("T3", "T3"),
                            ("T4", "T4"),
                            ("TG", "TG"),
                            ("ANTI-TG", "ANTI-TG"),
                            ("ANTI-TIPO", "ANTI-TIPO"),
                            ("CALCIT", "CALCIT"),
                            ("CA 19-9", "CA 19-9"),
                            ("CA 15-3", "CA 15-3"),
                            ("CA 125", "CA 125"),
                            ("PSA", "PSA"),
                            ("PSA Free", "PSA Free"),
                            ("CEA", "CEA"),
                            ("ALF", "ALF"),
                        ],
                        max_length=250,
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Estudio oncológico RIA-IRMA",
                "verbose_name_plural": "Estudios oncológicos RIA-IRMA",
                "ordering": ["pk"],
            },
        ),
    ]
