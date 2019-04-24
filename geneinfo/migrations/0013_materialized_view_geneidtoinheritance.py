# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 14:28
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


operations = [
    migrations.CreateModel(
        name="GeneIdToInheritance",
        fields=[
            (
                "id",
                models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                ),
            ),
            ("entrez_id", models.CharField(max_length=16)),
            ("ensembl_gene_id", models.CharField(max_length=32)),
            (
                "mode_of_inheritance",
                models.CharField(
                    choices=[
                        ("AR", "Autosomal recessive"),
                        ("AD", "Autosomal dominant"),
                        ("X-linked", "X-linked"),
                        ("XR", "X-linked recessive"),
                        ("XD", "X-linked dominant"),
                    ],
                    default="AR",
                    max_length=8,
                ),
            ),
        ],
        options={"db_table": "geneinfo_geneidtoinheritance", "managed": settings.IS_TESTING},
    ),
    migrations.AddField(model_name="hpo", name="decipher_id", field=models.IntegerField(null=True)),
    migrations.AddField(model_name="hpo", name="omim_id", field=models.IntegerField(null=True)),
    migrations.AddField(model_name="hpo", name="orpha_id", field=models.IntegerField(null=True)),
    migrations.AddIndex(
        model_name="hpo",
        index=models.Index(fields=["omim_id"], name="geneinfo_hp_omim_id_b96394_idx"),
    ),
]


if not settings.IS_TESTING:
    operations.append(
        migrations.RunSQL(
            """
            CREATE MATERIALIZED VIEW geneinfo_geneidtoinheritance
            AS
                SELECT
                    DISTINCT
                    CASE
                        WHEN 'HP:0000006' = hpo_id THEN 'AD'
                        WHEN 'HP:0000007' = hpo_id THEN 'AR'
                        WHEN 'HP:0001417' = hpo_id THEN 'X-linked'
                        WHEN 'HP:0001419' = hpo_id THEN 'XR'
                        WHEN 'HP:0001423' = hpo_id THEN 'XD'
                        ELSE NULL
                    END AS mode_of_inheritance,
                    entrez_id,
                    ensembl_gene_id
                FROM geneinfo_hpo
                LEFT OUTER JOIN geneinfo_mim2genemedgen USING (omim_id)
                LEFT OUTER JOIN geneinfo_hgnc USING (entrez_id)
                WHERE
                    entrez_id IS NOT NULL
                    AND hpo_id IN ('HP:0000006', 'HP:0000007', 'HP:0001417', 'HP:0001419', 'HP:0001423')
            WITH DATA;
            CREATE INDEX geneinfo_geneidtoinheritance_ensembl_gene_id ON geneinfo_geneidtoinheritance (
                ensembl_gene_id
            );
            CREATE INDEX geneinfo_geneidtoinheritance_entrez_id ON geneinfo_geneidtoinheritance (
                entrez_id
            );
            CREATE INDEX geneinfo_geneidtoinheritance_mode_of_inheritance ON geneinfo_geneidtoinheritance (
                mode_of_inheritance
            );
            """,
            """
            DROP MATERIALIZED VIEW geneinfo_geneidtoinheritance;
            """,
        )
    )


class Migration(migrations.Migration):

    dependencies = [("geneinfo", "0012_refseqtoensembl")]

    operations = operations
