# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("variants", "0035_auto_20190403_0911")]

    operations = [
        migrations.RemoveIndex(model_name="smallvariant", name="variants_sm_case_id_e96e11_idx"),
        migrations.AddIndex(
            model_name="smallvariant",
            index=models.Index(
                fields=["case_id", "ensembl_gene_id"], name="variants_sm_case_id_5d52f6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="smallvariant",
            index=models.Index(
                fields=["case_id", "refseq_gene_id"], name="variants_sm_case_id_1f4f31_idx"
            ),
        ),
    ]
