# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-01 08:45
from __future__ import unicode_literals
import uuid

import bgjobs.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projectroles", "0015_fix_appsetting_constraint"),
        ("bgjobs", "0006_auto_20200526_1657"),
        ("variants", "0079_auto_20210204_1006"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpanrSubmissionBgJob",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="Case SODAR UUID", unique=True),
                ),
                (
                    "query_args",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        help_text="(Validated) query parameters"
                    ),
                ),
                (
                    "spanr_job_url",
                    models.CharField(help_text="The SPANR job URL", max_length=100, null=True),
                ),
                (
                    "bg_job",
                    models.ForeignKey(
                        help_text="Background job for state etc.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spanr_submission_bg_job",
                        to="bgjobs.BackgroundJob",
                    ),
                ),
                (
                    "case",
                    models.ForeignKey(
                        help_text="The case to export",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="variants.Case",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        help_text="Project in which this objects belongs",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectroles.Project",
                    ),
                ),
            ],
            bases=(bgjobs.models.JobModelMessageMixin, models.Model),
        ),
    ]
