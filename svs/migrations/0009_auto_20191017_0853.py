# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-17 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("svs", "0008_set_unlogged_table")]

    operations = [
        migrations.AddField(
            model_name="structuralvariantflags",
            name="flag_doesnt_segregate",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="structuralvariantflags",
            name="flag_no_disease_association",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="structuralvariantflags",
            name="flag_segregates",
            field=models.BooleanField(default=False),
        ),
    ]
