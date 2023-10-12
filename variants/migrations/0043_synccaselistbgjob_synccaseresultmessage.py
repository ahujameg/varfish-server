# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-21 09:24
from __future__ import unicode_literals

import uuid

import bgjobs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projectroles", "0009_rename_projectsetting"),
        ("bgjobs", "0005_auto_20190128_1210"),
        ("variants", "0042_auto_20190619_1636"),
    ]

    operations = [
        migrations.CreateModel(
            name="SyncCaseListBgJob",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="Job UUID", unique=True),
                ),
                (
                    "bg_job",
                    models.ForeignKey(
                        help_text="Background job for state etc.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="variants_synccaselistbgjob_related",
                        to="bgjobs.BackgroundJob",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        help_text="Project that is to be synced",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectroles.Project",
                    ),
                ),
            ],
            bases=(bgjobs.models.JobModelMessageMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SyncCaseResultMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="Message UUID", unique=True),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("debug", "debug"),
                            ("info", "info"),
                            ("warning", "warning"),
                            ("error", "error"),
                        ],
                        help_text="Level of log entry",
                        max_length=50,
                    ),
                ),
                ("message", models.TextField(help_text="Log level's message")),
                (
                    "project",
                    models.ForeignKey(
                        help_text="Project for the message",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectroles.Project",
                    ),
                ),
            ],
        ),
    ]
