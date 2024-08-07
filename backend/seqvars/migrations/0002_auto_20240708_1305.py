# Generated by Django 3.2.25 on 2024-07-08 13:05

import typing

import django.core.serializers.json
from django.db import migrations
import django_pydantic_field.compat.django
import django_pydantic_field.fields

import seqvars.models


class Migration(migrations.Migration):

    dependencies = [
        ("seqvars", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_exomes_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_exomes_frequency",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_exomes_hemizygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_exomes_heterozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_exomes_homozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_genomes_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_genomes_frequency",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_genomes_hemizygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_genomes_heterozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_genomes_homozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="helixmtdb_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="helixmtdb_frequency",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="helixmtdb_heteroplasmic",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="helixmtdb_homoplasmic",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="inhouse_carriers",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="inhouse_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="inhouse_hemizygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="inhouse_heterozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerypresetsfrequency",
            name="inhouse_homozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_exomes_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_exomes_frequency",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_exomes_hemizygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_exomes_heterozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_exomes_homozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_genomes_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_genomes_frequency",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_genomes_hemizygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_genomes_heterozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_genomes_homozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="helixmtdb_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="helixmtdb_frequency",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="helixmtdb_heteroplasmic",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="helixmtdb_homoplasmic",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="inhouse_carriers",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="inhouse_enabled",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="inhouse_hemizygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="inhouse_heterozygous",
        ),
        migrations.RemoveField(
            model_name="seqvarsquerysettingsfrequency",
            name="inhouse_homozygous",
        ),
        migrations.AddField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_exomes",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union,
                    (seqvars.models.GnomadNuclearFrequencySettingsPydantic, type(None)),
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_genomes",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union,
                    (seqvars.models.GnomadNuclearFrequencySettingsPydantic, type(None)),
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerypresetsfrequency",
            name="gnomad_mitochondrial",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union,
                    (seqvars.models.GnomadMitochondrialFrequencySettingsPydantic, type(None)),
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerypresetsfrequency",
            name="helixmtdb",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union, (seqvars.models.HelixmtDbFrequencySettingsPydantic, type(None))
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerypresetsfrequency",
            name="inhouse",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union, (seqvars.models.InhouseFrequencySettingsPydantic, type(None))
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_exomes",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union,
                    (seqvars.models.GnomadNuclearFrequencySettingsPydantic, type(None)),
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_genomes",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union,
                    (seqvars.models.GnomadNuclearFrequencySettingsPydantic, type(None)),
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettingsfrequency",
            name="gnomad_mitochondrial",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union,
                    (seqvars.models.GnomadMitochondrialFrequencySettingsPydantic, type(None)),
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettingsfrequency",
            name="helixmtdb",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union, (seqvars.models.HelixmtDbFrequencySettingsPydantic, type(None))
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettingsfrequency",
            name="inhouse",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default=None,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union, (seqvars.models.InhouseFrequencySettingsPydantic, type(None))
                ),
            ),
        ),
    ]
