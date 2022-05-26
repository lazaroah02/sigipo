# Generated by Django 3.2.13 on 2022-05-23 00:17

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("drugs", "0001_initial"),
        ("patient", "0001_initial"),
        ("classifiers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SerialIodineDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("two_hours", models.FloatField(blank=True, null=True)),
                ("four_hours", models.FloatField(blank=True, null=True)),
                ("eight_hours", models.FloatField(blank=True, null=True)),
                ("twenty_four_hours", models.FloatField(blank=True, null=True)),
                ("forty_eight_hours", models.FloatField(blank=True, null=True)),
                ("seventy_two_hours", models.FloatField(blank=True, null=True)),
                ("ninety_six_hours", models.FloatField(blank=True, null=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Detección de yodo seriada",
                "verbose_name_plural": "Detección de yodo seriada",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="HormonalStudy",
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
                            ("T3F", "T3F"),
                            ("T4F", "T4F"),
                            ("PRL", "PRL"),
                            ("FSH", "FSH"),
                            ("LH", "LH"),
                            ("PRG", "PRG"),
                            ("E2", "E2"),
                            ("CORT", "CORT"),
                            ("INS", "INS"),
                            ("TEST", "TEST"),
                            ("GH", "GH"),
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
                "verbose_name": "Estudio hormonal RIA-IRMA",
                "verbose_name_plural": "Estudios hormonales RIA-IRMA",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="OncologicStudy",
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
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="OncologicResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("tsh", models.FloatField(blank=True, null=True)),
                ("t3", models.FloatField(blank=True, null=True)),
                ("t4", models.FloatField(blank=True, null=True)),
                ("tg", models.FloatField(blank=True, null=True)),
                ("anti_tg", models.FloatField(blank=True, null=True)),
                ("anti_tipo", models.FloatField(blank=True, null=True)),
                ("calcit", models.FloatField(blank=True, null=True)),
                ("ca19_9", models.FloatField(blank=True, null=True)),
                ("ca15_3", models.FloatField(blank=True, null=True)),
                ("ca125", models.FloatField(blank=True, null=True)),
                ("cea", models.FloatField(blank=True, null=True)),
                ("alf", models.FloatField(blank=True, null=True)),
                ("psa", models.FloatField(blank=True, null=True)),
                ("psafree", models.FloatField(blank=True, null=True)),
                (
                    "oncologic_study",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nuclear_medicine.oncologicstudy",
                    ),
                ),
            ],
            options={
                "verbose_name": "Resultado oncología RIA-IRMA",
                "verbose_name_plural": "Resultados oncología RIA-IRMA",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="IodineDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("two_hours", models.FloatField(blank=True, null=True)),
                ("twenty_four_hours", models.FloatField(blank=True, null=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Detección de yodo",
                "verbose_name_plural": "Detección de yodo",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="HormonalResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("tsh", models.FloatField(blank=True, null=True)),
                ("t3", models.FloatField(blank=True, null=True)),
                ("t4", models.FloatField(blank=True, null=True)),
                ("t3f", models.FloatField(blank=True, null=True)),
                ("t4f", models.FloatField(blank=True, null=True)),
                ("prl", models.FloatField(blank=True, null=True)),
                ("fsh", models.FloatField(blank=True, null=True)),
                ("lh", models.FloatField(blank=True, null=True)),
                ("prg", models.FloatField(blank=True, null=True)),
                ("e2", models.FloatField(blank=True, null=True)),
                ("cort", models.FloatField(blank=True, null=True)),
                ("ins", models.FloatField(blank=True, null=True)),
                ("test", models.FloatField(blank=True, null=True)),
                ("gh", models.FloatField(blank=True, null=True)),
                (
                    "hormonal_study",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nuclear_medicine.hormonalstudy",
                    ),
                ),
            ],
            options={
                "verbose_name": "Resultado hormonal RIA-IRMA",
                "verbose_name_plural": "Resultados hormonales RIA-IRMA",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Gammagraphy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("dose", models.FloatField()),
                ("report", models.TextField(max_length=5000)),
                ("observation", models.TextField(max_length=5000)),
                (
                    "drug",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="drugs.drug"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
                (
                    "radio_isotope",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classifiers.radioisotope",
                    ),
                ),
                ("requested_study", models.ManyToManyField(to="classifiers.Study")),
            ],
            options={
                "verbose_name": "Gammagrafía",
                "verbose_name_plural": "Gammagrafias",
                "ordering": ["pk"],
            },
        ),
    ]
