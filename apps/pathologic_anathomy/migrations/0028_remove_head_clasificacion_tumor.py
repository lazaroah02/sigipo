# Generated by Django 4.2.1 on 2023-11-14 19:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0027_alter_head_clasificacion_tumor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="head",
            name="clasificacion_tumor",
        ),
    ]
