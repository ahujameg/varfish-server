# Generated by Django 3.2.16 on 2022-11-09 14:26

import uuid

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("variants", "0088_auto_20221104_1450"),
    ]

    operations = [
        migrations.AddField(
            model_name="casephenotypeterms",
            name="date_created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="DateTime of creation",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="casephenotypeterms",
            name="date_modified",
            field=models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
        ),
        migrations.AddField(
            model_name="casephenotypeterms",
            name="sodar_uuid",
            field=models.UUIDField(default=uuid.uuid4, help_text="Record UUID", null=True),
        ),
    ]
