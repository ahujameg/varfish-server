# Generated by Django 3.2.9 on 2021-11-29 14:43

from django.db import migrations

import varfish.utils


class Migration(migrations.Migration):
    dependencies = [
        ("clinvar", "0006_clinvarpathogenicgenes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinvar",
            name="details",
            field=varfish.utils.JSONField(),
        ),
    ]
