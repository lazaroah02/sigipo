# Generated by Django 4.2.1 on 2023-11-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0049_alter_head_localizacion_tumor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="linfomabiopsydiagnostic",
            name="especimen",
            field=models.CharField(
                max_length=100,
                verbose_name="El espécimen (seleccione todo lo que aplique)",
            ),
        ),
        migrations.AlterField(
            model_name="linfomabiopsydiagnostic",
            name="pathologic_tumor_extensions",
            field=models.CharField(
                max_length=100,
                verbose_name="Extensión Patológica del Tumor (seleccione todo lo que aplique)",
            ),
        ),
        migrations.AlterField(
            model_name="linfomabiopsydiagnostic",
            name="sitio_tumor",
            field=models.CharField(
                max_length=100,
                verbose_name="El sitio del tumor (seleccione todo lo que aplique)",
            ),
        ),
    ]
