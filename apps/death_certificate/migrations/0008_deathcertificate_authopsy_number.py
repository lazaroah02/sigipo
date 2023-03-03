# Generated by Django 3.2.16 on 2023-03-03 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pathological_anatomy', '0004_alter_pathology_authopsy_number'),
        ('death_certificate', '0007_auto_20230303_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathcertificate',
            name='authopsy_number',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pathological_anatomy.pathology'),
        ),
    ]
