# Generated by Django 3.2.25 on 2024-07-12 12:36

import typing

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import django_pydantic_field.compat.django
import django_pydantic_field.fields

import seqvars.models


class Migration(migrations.Migration):

    dependencies = [
        ("seqvars", "0003_seqvarsquerysettings_predefinedquery"),
    ]

    operations = [
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="clinvarpresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetsclinvar",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="columnspresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetscolumns",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="consequencepresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetsconsequence",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="frequencypresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetsfrequency",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="genotypepresets",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default={"choice": None},
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union, (seqvars.models.SeqvarsGenotypePresetsPydantic, type(None))
                ),
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="locuspresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetslocus",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="phenotypepriopresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetsphenotypeprio",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="qualitypresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetsquality",
            ),
        ),
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="variantpriopresets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="seqvars.seqvarsquerypresetsvariantprio",
            ),
        ),
        migrations.AlterField(
            model_name="seqvarspredefinedquery",
            name="genotype",
            field=django_pydantic_field.fields.PydanticSchemaField(
                blank=True,
                config=None,
                default={"choice": None},
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    typing.Union, (seqvars.models.SeqvarsGenotypePresetsPydantic, type(None))
                ),
            ),
        ),
    ]
