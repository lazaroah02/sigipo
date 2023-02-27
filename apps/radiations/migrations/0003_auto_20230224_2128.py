# Generated by Django 3.2.16 on 2023-02-24 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radiations', '0002_auto_20230224_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalbeamreg',
            name='treat_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='radiations.externalbeamtreat'),
        ),
        migrations.AlterField(
            model_name='internalradiationreg',
            name='treat_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='radiations.internalradiationtreatment'),
        ),
    ]
