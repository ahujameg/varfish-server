# Generated by Django 3.2.16 on 2023-01-31 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("svs", "0020_filtersvbgjob_svquery_svqueryresultrow_svqueryresultset"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="svqueryresultset",
            name="query_sql",
        ),
    ]
