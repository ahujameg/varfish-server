# Generated by Django 3.2.16 on 2022-10-06 11:34

import uuid

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GenePanel",
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
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, help_text="Record SODAR UUID", unique=True
                    ),
                ),
                (
                    "identifier",
                    models.CharField(
                        help_text="Identifier of the gene panel, e.g., 'osteoporosis.basic' or 'osteoporosis.extended'",
                        max_length=128,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Identifier may only contain alphanumeric characters, dots, hyphens, and underscores",
                                regex="^[\\w\\._-]+$",
                            )
                        ],
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[["draft", "draft"], ["active", "active"], ["retired", "retired"]],
                        default="draft",
                        help_text="State of teh gene panel version",
                        max_length=32,
                    ),
                ),
                (
                    "version_major",
                    models.IntegerField(
                        default=1, help_text="Major version of the gene panel (by identifier)"
                    ),
                ),
                (
                    "version_minor",
                    models.IntegerField(
                        default=1, help_text="Minor version of the gene panel (by identifier)"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the gene panel, only used for informative purposes",
                        max_length=128,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, help_text="Description of the panel", null=True),
                ),
            ],
            options={
                "ordering": ("identifier", "version_major", "version_minor"),
            },
        ),
        migrations.CreateModel(
            name="GenePanelCategory",
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
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, help_text="Record SODAR UUID", unique=True
                    ),
                ),
                ("title", models.CharField(help_text="Title of the category", max_length=128)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Optional description of the category", null=True
                    ),
                ),
            ],
            options={
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="GenePanelEntry",
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
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, help_text="Record SODAR UUID", unique=True
                    ),
                ),
                (
                    "symbol",
                    models.CharField(
                        help_text="Official gene symbol, only used for informative purposes as such symbols are NOT guaranteed to be stable, e.g., 'TGDS'",
                        max_length=128,
                    ),
                ),
                (
                    "hgnc_id",
                    models.CharField(
                        help_text="The stable HGNC ID, e.g., 'HGNC:20324", max_length=64
                    ),
                ),
                (
                    "ensembl_id",
                    models.CharField(
                        help_text="The stable ENSEMBL gene identifier, e.g., 'ENSG00000088451",
                        max_length=64,
                    ),
                ),
                (
                    "ncbi_id",
                    models.CharField(
                        help_text="The stable NCBI/Entrez gene identifier, e.g., '23483'",
                        max_length=64,
                    ),
                ),
                (
                    "panel",
                    models.ForeignKey(
                        help_text="The gene panel that this entry belongs to",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="genepanels.genepanel",
                    ),
                ),
            ],
            options={
                "ordering": ("symbol",),
            },
        ),
        migrations.AddField(
            model_name="genepanel",
            name="category",
            field=models.ForeignKey(
                help_text="Category of the gene panel",
                on_delete=django.db.models.deletion.PROTECT,
                to="genepanels.genepanelcategory",
            ),
        ),
        migrations.AddField(
            model_name="genepanel",
            name="signed_off_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The user who signed off the panel into active state",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="genepanel",
            unique_together={("identifier", "version_major", "version_minor")},
        ),
    ]
