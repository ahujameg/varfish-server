# Generated by Django 3.2.25 on 2024-07-12 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("seqvars", "0002_auto_20240708_1305"),
    ]

    operations = [
        migrations.AddField(
            model_name="seqvarsquerysettings",
            name="predefinedquery",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="seqvars.seqvarspredefinedquery",
            ),
        ),
    ]
