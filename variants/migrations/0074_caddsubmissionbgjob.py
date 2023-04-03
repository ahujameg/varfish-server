# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-29 14:04
from __future__ import unicode_literals

import uuid

import bgjobs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projectroles", "0015_fix_appsetting_constraint"),
        ("bgjobs", "0006_auto_20200526_1657"),
        (
            "variants",
            "0073_clearexpiredexportedfilesbgjob_clearinactivevariantsetsbgjob_clearoldkioskcasesbgjob_refreshsmallvar",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="CaddSubmissionBgJob",
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
                    models.JSONField(help_text="(Validated) query parameters"),
                ),
                (
                    "cadd_version",
                    models.CharField(
                        help_text="The CADD version used for the annotation", max_length=100
                    ),
                ),
                (
                    "cadd_job_id",
                    models.CharField(
                        help_text="The project ID that CADD assigned on submission",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "bg_job",
                    models.ForeignKey(
                        help_text="Background job for state etc.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cadd_submission_bg_job",
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
