# Generated by Django 3.2.20 on 2023-07-24 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("variants", "0094_auto_20230719_1406"),
    ]

    operations = [
        migrations.AddField(
            model_name="smallvariantqueryresultset",
            name="case",
            field=models.ForeignKey(
                blank=True,
                help_text="The case that this result is for",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="variants.case",
            ),
        ),
        migrations.AlterField(
            model_name="smallvariantqueryresultset",
            name="smallvariantquery",
            field=models.ForeignKey(
                blank=True,
                help_text="The query that this result is for",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="variants.smallvariantquery",
            ),
        ),
    ]
