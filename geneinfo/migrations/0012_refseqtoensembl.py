# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("geneinfo", "0011_ensembltorefseq")]

    operations = [
        migrations.CreateModel(
            name="RefseqToEnsembl",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("entrez_id", models.CharField(max_length=16)),
                ("ensembl_gene_id", models.CharField(max_length=16, null=True)),
                ("ensembl_transcript_id", models.CharField(max_length=16, null=True)),
            ],
        )
    ]
