# Generated by Django 3.2.16 on 2023-07-03 10:41

import uuid

from django.db import migrations, models
import django.db.models.deletion

import varfish.utils


class Migration(migrations.Migration):
    dependencies = [
        ("variants", "0091_alter_casephenotypeterms_sodar_uuid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectcasessmallvariantquery",
            name="form_id",
        ),
        migrations.RemoveField(
            model_name="projectcasessmallvariantquery",
            name="form_version",
        ),
        migrations.RemoveField(
            model_name="smallvariantquery",
            name="form_id",
        ),
        migrations.RemoveField(
            model_name="smallvariantquery",
            name="form_version",
        ),
        migrations.AddField(
            model_name="projectcasessmallvariantquery",
            name="query_state",
            field=models.CharField(
                choices=[
                    ("initial", "initial"),
                    ("running", "running"),
                    ("done", "done"),
                    ("cancelled", "cancelled"),
                    ("failed", "failed"),
                    ("timeout", "timeout"),
                ],
                default="initial",
                help_text="The current query state",
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name="projectcasessmallvariantquery",
            name="query_state_msg",
            field=models.TextField(
                blank=True, help_text="Message related to the query state", null=True
            ),
        ),
        migrations.AddField(
            model_name="smallvariantquery",
            name="query_state",
            field=models.CharField(
                choices=[
                    ("initial", "initial"),
                    ("running", "running"),
                    ("done", "done"),
                    ("cancelled", "cancelled"),
                    ("failed", "failed"),
                    ("timeout", "timeout"),
                ],
                default="initial",
                help_text="The current query state",
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name="smallvariantquery",
            name="query_state_msg",
            field=models.TextField(
                blank=True, help_text="Message related to the query state", null=True
            ),
        ),
        migrations.CreateModel(
            name="SmallVariantQueryResultSet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="Record UUID", unique=True),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of modification"),
                ),
                ("result_row_count", models.IntegerField(help_text="Number of rows in the result")),
                ("start_time", models.DateTimeField(help_text="Date time of query start")),
                ("end_time", models.DateTimeField(help_text="Date time of query end")),
                ("elapsed_seconds", models.FloatField(help_text="Elapsed seconds")),
                (
                    "smallvariantquery",
                    models.ForeignKey(
                        help_text="The query that this result is for",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="variants.smallvariantquery",
                    ),
                ),
            ],
            options={
                "ordering": ("-date_created",),
            },
        ),
        migrations.CreateModel(
            name="SmallVariantQueryResultRow",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="Record UUID", unique=True),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("chromosome_no", models.IntegerField()),
                ("bin", models.IntegerField()),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("payload", varfish.utils.JSONField(help_text="The query result rows")),
                (
                    "smallvariantqueryresultset",
                    models.ForeignKey(
                        help_text="The owning SmallVariantQueryResultSet",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="variants.smallvariantqueryresultset",
                    ),
                ),
            ],
            options={
                "ordering": ("chromosome_no", "start", "end"),
            },
        ),
    ]
