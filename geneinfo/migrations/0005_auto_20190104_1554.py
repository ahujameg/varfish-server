# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-04 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geneinfo', '0004_auto_20181204_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hgnc',
            old_name='namit_trnadb',
            new_name='mamit_trnadb',
        ),
    ]
