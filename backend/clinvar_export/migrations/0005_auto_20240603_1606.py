# Generated by Django 3.2.25 on 2024-06-03 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clinvar_export", "0004_auto_20221028_0657"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clinvarreport",
            name="submission_set",
        ),
        migrations.AlterUniqueTogether(
            name="family",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="family",
            name="case",
        ),
        migrations.RemoveField(
            model_name="family",
            name="project",
        ),
        migrations.RemoveField(
            model_name="individual",
            name="family",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="assertion_method",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="individuals",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="submission_set",
        ),
        migrations.AlterUniqueTogether(
            name="submissionindividual",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="submissionindividual",
            name="individual",
        ),
        migrations.RemoveField(
            model_name="submissionindividual",
            name="submission",
        ),
        migrations.RemoveField(
            model_name="submissionset",
            name="organisations",
        ),
        migrations.RemoveField(
            model_name="submissionset",
            name="project",
        ),
        migrations.RemoveField(
            model_name="submissionset",
            name="submitter",
        ),
        migrations.AlterUniqueTogether(
            name="submittingorg",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="submittingorg",
            name="organisation",
        ),
        migrations.RemoveField(
            model_name="submittingorg",
            name="submission_set",
        ),
        migrations.DeleteModel(
            name="AssertionMethod",
        ),
        migrations.DeleteModel(
            name="ClinVarReport",
        ),
        migrations.DeleteModel(
            name="Family",
        ),
        migrations.DeleteModel(
            name="Individual",
        ),
        migrations.DeleteModel(
            name="Organisation",
        ),
        migrations.DeleteModel(
            name="Submission",
        ),
        migrations.DeleteModel(
            name="SubmissionIndividual",
        ),
        migrations.DeleteModel(
            name="SubmissionSet",
        ),
        migrations.DeleteModel(
            name="Submitter",
        ),
        migrations.DeleteModel(
            name="SubmittingOrg",
        ),
    ]
