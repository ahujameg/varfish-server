# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("variants", "0041_array_cat_agg")]

    operations = [
        migrations.RemoveIndex(
            model_name="smallvariantcomment", name="variants_sm_release_ca2019_idx"
        ),
        migrations.RenameField(
            model_name="acmgcriteriarating", old_name="position", new_name="start"
        ),
        migrations.RenameField(model_name="smallvariant", old_name="position", new_name="start"),
        migrations.RenameField(
            model_name="smallvariantcomment", old_name="position", new_name="start"
        ),
        migrations.RenameField(
            model_name="smallvariantflags", old_name="position", new_name="start"
        ),
        migrations.RenameField(
            model_name="smallvariantqueryvariantscores", old_name="position", new_name="start"
        ),
        migrations.AddField(
            model_name="acmgcriteriarating",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="acmgcriteriarating",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariant",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariant",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantcomment",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantcomment",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantflags",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantflags",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantqueryvariantscores",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantqueryvariantscores",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="smallvariantflags",
            unique_together=set(
                [("release", "chromosome", "start", "reference", "alternative", "case")]
            ),
        ),
        migrations.AddIndex(
            model_name="smallvariant",
            index=models.Index(
                fields=["case_id", "chromosome", "bin"], name="variants_sm_case_id_3efbb1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="smallvariantcomment",
            index=models.Index(
                fields=["release", "chromosome", "start", "reference", "alternative", "case"],
                name="variants_sm_release_961b97_idx",
            ),
        ),
    ]
