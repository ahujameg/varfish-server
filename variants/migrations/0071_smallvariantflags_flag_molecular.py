# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-02-13 17:09
from __future__ import unicode_literals

from django.db import migrations, models

from variants.models import SmallVariantComment, SmallVariantFlags


# Was in migration 0062 before. Didn't work anymore, because of the new field in SmallVariantFlags
def update_chromosome_no_in_existing_flags_and_comments(apps, schema_editor):
    if not schema_editor.connection.alias == "default":
        return
    for o in list(SmallVariantFlags.objects.all()) + list(SmallVariantComment.objects.all()):
        o.save()


class Migration(migrations.Migration):

    dependencies = [
        ("variants", "0070_smallvariant_create_index_chromosome_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="smallvariantflags",
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
        ),
        # Was in migration 0062 before. Didn't work anymore, because of the new field in SmallVariantFlags
        migrations.RunPython(update_chromosome_no_in_existing_flags_and_comments),
    ]
