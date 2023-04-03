# Generated by Django 3.2.7 on 2021-10-08 10:15

from django.db import migrations

import varfish.utils


class Migration(migrations.Migration):

    dependencies = [
        ("regmaps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="regelement",
            name="extra_data",
            field=varfish.utils.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name="reginteraction",
            name="extra_data",
            field=varfish.utils.JSONField(null=True),
        ),
    ]
