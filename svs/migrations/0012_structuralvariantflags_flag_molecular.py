# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-02-13 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("svs", "0011_rename_partitions")]

    operations = [
        migrations.AddField(
            model_name="structuralvariantflags",
            name="flag_molecular",
            field=models.CharField(
                choices=[
                    ("positive", "positive"),
                    ("uncertain", "uncertain"),
                    ("negative", "negative"),
                    ("empty", "empty"),
                ],
                default="empty",
                max_length=32,
            ),
        )
    ]
