# Generated by Django 4.2.1 on 2023-11-14 19:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0028_remove_head_clasificacion_tumor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="neckbiopsydiagnostic",
            name="clasificacion_tumor",
        ),
    ]