# Generated by Django 3.2.4 on 2021-06-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frequencies", "0007_auto_20200211_1625"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mtdb",
            name="synonymous",
            field=models.BooleanField(null=True),
        ),
    ]
