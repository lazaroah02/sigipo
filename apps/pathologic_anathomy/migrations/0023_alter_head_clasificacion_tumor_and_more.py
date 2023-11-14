# Generated by Django 4.2.1 on 2023-11-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathologic_anathomy', '0022_alter_neckbiopsydiagnostic_clasificacion_tumor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='clasificacion_tumor',
            field=models.IntegerField(blank=True, choices=[(1, 'PT'), (2, 'N'), (3, 'M')], default=None, null=True, verbose_name='Clasificación Tumor'),
        ),
        migrations.AlterField(
            model_name='neckbiopsydiagnostic',
            name='clasificacion_tumor',
            field=models.IntegerField(blank=True, choices=[(1, 'PT'), (2, 'N'), (3, 'M')], default=None, null=True, verbose_name='Clasificación Tumor'),
        ),
    ]
