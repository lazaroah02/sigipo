# Generated by Django 3.2.13 on 2022-06-08 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_migration", "0004_auto_20220608_2311"),
    ]

    operations = [
        migrations.CreateModel(
            name="Municipio",
            fields=[
                ("municipio", models.CharField(db_column="municipio", max_length=255)),
                (
                    "id",
                    models.IntegerField(
                        db_column="id_municipio", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "tn_municipios",
                "abstract": False,
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Provincia",
            fields=[
                ("provincia", models.CharField(db_column="Provincia", max_length=255)),
                (
                    "id",
                    models.IntegerField(
                        db_column="codigo",
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            options={
                "db_table": "tn_provincias",
                "abstract": False,
                "managed": False,
            },
        ),
    ]
