# Generated by Django 3.2.16 on 2023-07-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("variants", "0092_auto_20230703_1041"),
    ]

    operations = [
        migrations.AddField(
            model_name="smallvariantqueryresultrow",
            name="alternative",
            field=models.CharField(default="A", max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smallvariantqueryresultrow",
            name="reference",
            field=models.CharField(default="A", max_length=512),
            preserve_default=False,
        ),
    ]
