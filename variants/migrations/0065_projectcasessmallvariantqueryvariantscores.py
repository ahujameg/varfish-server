# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-29 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("variants", "0064_auto_20191025_1403")]

    operations = [
        migrations.CreateModel(
            name="ProjectCasesSmallVariantQueryVariantScores",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("bin", models.IntegerField()),
                ("reference", models.CharField(max_length=512)),
                ("alternative", models.CharField(max_length=512)),
                ("score_type", models.CharField(help_text="The score type", max_length=64)),
                ("score", models.FloatField(help_text="The variant score")),
                ("info", models.JSONField(default={})),
                (
                    "query",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="variants.ProjectCasesSmallVariantQuery",
                    ),
                ),
            ],
        )
    ]
