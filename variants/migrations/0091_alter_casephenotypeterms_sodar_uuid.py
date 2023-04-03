# Generated by Django 3.2.16 on 2022-11-09 14:38

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variants", "0090_populate_uuids"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casephenotypeterms",
            name="sodar_uuid",
            field=models.UUIDField(default=uuid.uuid4, help_text="Record UUID", unique=True),
        ),
    ]
