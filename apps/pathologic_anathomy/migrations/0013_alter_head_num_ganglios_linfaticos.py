# Generated by Django 3.2.16 on 2023-11-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0012_alter_head_invasion_vascular"),
    ]

    operations = [
        migrations.AlterField(
            model_name="head",
            name="num_ganglios_linfaticos",
            field=models.IntegerField(
                verbose_name="Número de Ganglios linfáticos involucrados"
            ),
        ),
    ]
