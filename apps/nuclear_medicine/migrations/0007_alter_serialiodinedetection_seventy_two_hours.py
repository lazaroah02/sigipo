# Generated by Django 3.2.13 on 2022-05-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuclear_medicine", "0006_auto_20220510_0150"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serialiodinedetection",
            name="seventy_two_hours",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
