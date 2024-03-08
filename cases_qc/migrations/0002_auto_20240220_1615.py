# Generated by Django 3.2.24 on 2024-02-20 16:15

from django.db import migrations
import django_pydantic_field.compat.django
import django_pydantic_field.fields

import cases_qc.models.cramino
import cases_qc.models.dragen
import cases_qc.models.ngsbits
import cases_qc.models.samtools


class Migration(migrations.Migration):
    dependencies = [
        ("cases_qc", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="af",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsAfRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="dp",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsDpRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="idd",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsIddRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="qual",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsQualRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="sis",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsSisRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="sn",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsSnRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="st",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsStRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="bcftoolsstatsmetrics",
            name="tstv",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.BcftoolsStatsTstvRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="craminometrics",
            name="chrom_counts",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.cramino.CraminoChromNormalizedCountsRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="craminometrics",
            name="summary",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.cramino.CraminoSummaryRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragencnvmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenmappingmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenploidyestimationmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenregioncoveragemetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenregionhist",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenregionoverallmeancov",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenrohmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragensvmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragentimemetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragentrimmermetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenvchethomratiometrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenvcmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenwgscontigmeancovmetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleCoverage,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenwgscoveragemetrics",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="dragenwgsoverallmeancov",
            name="metrics",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.dragen.DragenStyleMetric,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="ngsbitsmappingqcmetrics",
            name="records",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.ngsbits.NgsbitsMappingqcRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsflagstatmetrics",
            name="qc_fail",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None, default=None, schema=cases_qc.models.samtools.SamtoolsFlagstatRecord
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsflagstatmetrics",
            name="qc_pass",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None, default=None, schema=cases_qc.models.samtools.SamtoolsFlagstatRecord
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsidxstatsmetrics",
            name="records",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsIdxstatsRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="chk",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsChkRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="cov",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsHistoRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="fbc",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsBasePercentagesRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="ffq",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsFqRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="frl",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsHistoRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="gcd",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsGcdRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="idd",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsIdRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="isize",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsIsRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="lbc",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsBasePercentagesRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="lfq",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsFqRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="lrl",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsHistoRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatsmainmetrics",
            name="sn",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsSnRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="gcc",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsBasePercentagesRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="gcf",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsGcRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="gcl",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsGcRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="gct",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsBasePercentagesRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="ic",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsIcRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="mapq",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsHistoRecord,)
                ),
            ),
        ),
        migrations.AlterField(
            model_name="samtoolsstatssupplementarymetrics",
            name="rl",
            field=django_pydantic_field.fields.PydanticSchemaField(
                config=None,
                default=None,
                schema=django_pydantic_field.compat.django.GenericContainer(
                    list, (cases_qc.models.samtools.SamtoolsStatsHistoRecord,)
                ),
            ),
        ),
    ]
