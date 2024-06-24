# Generated by Django 3.2.24 on 2024-03-01 11:41

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("variants", "0098_alter_acmgcriteriarating_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="annotationreleaseinfo",
            name="sodar_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, help_text="Small variant flags SODAR UUID", null=True
            ),
        ),
        migrations.AddField(
            model_name="smallvariantset",
            name="sodar_uuid",
            field=models.UUIDField(
                default=uuid.uuid4, help_text="Small variant flags SODAR UUID", null=True
            ),
        ),
    ]
