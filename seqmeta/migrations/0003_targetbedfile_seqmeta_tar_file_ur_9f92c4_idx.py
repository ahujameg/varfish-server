# Generated by Django 3.2.20 on 2023-07-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seqmeta", "0002_alter_targetbedfile_file_uri"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="targetbedfile",
            index=models.Index(fields=["file_uri"], name="seqmeta_tar_file_ur_9f92c4_idx"),
        ),
    ]
