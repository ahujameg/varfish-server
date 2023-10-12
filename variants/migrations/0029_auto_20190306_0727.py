# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("variants", "0028_auto_20190219_0738")]

    operations = [
        migrations.RemoveIndex(
            model_name="smallvariantcomment", name="variants_sm_release_40b8cc_idx"
        ),
        migrations.RemoveField(model_name="smallvariantcomment", name="ensembl_gene_id"),
        migrations.AlterUniqueTogether(
            name="smallvariantflags",
            unique_together=set(
                [("release", "chromosome", "position", "reference", "alternative", "case")]
            ),
        ),
        migrations.AddIndex(
            model_name="smallvariantcomment",
            index=models.Index(
                fields=["release", "chromosome", "position", "reference", "alternative", "case"],
                name="variants_sm_release_ca2019_idx",
            ),
        ),
        migrations.RemoveField(model_name="smallvariantflags", name="ensembl_gene_id"),
    ]
