# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("svs", "0002_pgplsql_overlapping_bins")]

    operations = [
        migrations.RemoveField(model_name="structuralvariant", name="containing_bins"),
        migrations.RemoveField(model_name="structuralvariantcomment", name="containing_bins"),
        migrations.RemoveField(model_name="structuralvariantflags", name="containing_bins"),
    ]
