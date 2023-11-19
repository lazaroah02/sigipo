# Generated by Django 3.2.16 on 2023-11-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0065_mamacdisbiopsydiagnostic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mamacdisbiopsydiagnostic",
            name="num_bloques_examinados",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Número de bloques examinados"
            ),
        ),
    ]