# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-30 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hgmd", "0003_hgmdpubliclocus_bin")]

    operations = [
        migrations.RemoveIndex(model_name="hgmdpubliclocus", name="hgmd_hgmdpu_release_27246d_idx"),
        migrations.AddIndex(
            model_name="hgmdpubliclocus",
            index=models.Index(
                fields=["release", "chromosome", "start", "end"],
                name="hgmd_hgmdpu_release_a5d0c3_idx",
            ),
        ),
    ]
