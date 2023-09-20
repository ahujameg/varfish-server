"""Tests for the ``CaseImportBackgroundJobExecutor`` and related code.

This has been broken away from ``test_models.py`` for better structure.
"""
import os
from unittest import mock

from projectroles.app_settings import AppSettingAPI
from snapshottest.unittest import TestCase as TestCaseSnapshot
from test_plus import TestCase

from cases.models import Case
from cases.tests.factories import IndividualFactory, PedigreeFactory
from cases_import.models import CaseImportAction, CaseImportBackgroundJobExecutor
from cases_import.tests.factories import CaseImportActionFactory, CaseImportBackgroundJobFactory
from cases_qc.models import CaseQc, DragenCnvMetrics
from seqmeta.tests.factories import TargetBedFileFactory
from variants.tests.factories import CaseFactory


class ExecutorTestMixin:
    def _setUpExecutor(self, action, fac_kwargs=None):
        super().setUp()
        self.user = self.make_user()
        self.caseimportaction = CaseImportActionFactory(
            action=action,
            state=CaseImportAction.STATE_SUBMITTED,
            overwrite_terms=True,
            **(fac_kwargs or {}),
        )
        self.caseimportbackgroundjob = CaseImportBackgroundJobFactory(
            caseimportaction=self.caseimportaction,
            user=self.user,
        )
        self.project = self.caseimportbackgroundjob.project
        self.executor = CaseImportBackgroundJobExecutor(self.caseimportbackgroundjob.pk)
        self.targetbedfile = TargetBedFileFactory(
            file_uri=self.caseimportaction.payload["proband"]["files"][0]["uri"]
        )

        app_settings = AppSettingAPI()
        app_settings.set(
            app_name="cases_import",
            setting_name="import_data_protocol",
            value="file",
            project=self.project,
        )


class ImportCreateTest(ExecutorTestMixin, TestCaseSnapshot, TestCase):
    """Test the executor with action=create

    This will only create the external files objects but not perform an import of quality
    control data etc because the ``family.yaml`` file does not contain actionable files.
    """

    def setUp(self):
        self._setUpExecutor(CaseImportAction.ACTION_CREATE)

    def test_run(self):
        self.assertEqual(Case.objects.count(), 0)
        self.executor.run()
        self.assertEqual(Case.objects.count(), 1)


class ImportCreateWithDragenQcTest(ExecutorTestMixin, TestCaseSnapshot, TestCase):
    """Test the executor with action=create and external files for Dragen QC.

    This will actually run the import of the Dragen QC files.
    """

    def setUp(self):
        self.maxDiff = None
        self._setUpExecutor(
            CaseImportAction.ACTION_CREATE,
            fac_kwargs={
                "path_phenopacket_yaml": "cases_import/tests/data/singleton_dragen_qc.yaml"
            },
        )

    @mock.patch("cases_qc.io.dragen.load_cnv_metrics")
    @mock.patch("cases_qc.io.dragen.load_fragment_length_hist")
    @mock.patch("cases_qc.io.dragen.load_mapping_metrics")
    @mock.patch("cases_qc.io.dragen.load_ploidy_estimation_metrics")
    @mock.patch("cases_qc.io.dragen.load_roh_metrics")
    @mock.patch("cases_qc.io.dragen.load_sv_metrics")
    @mock.patch("cases_qc.io.dragen.load_time_metrics")
    @mock.patch("cases_qc.io.dragen.load_trimmer_metrics")
    @mock.patch("cases_qc.io.dragen.load_vc_hethom_ratio_metrics")
    @mock.patch("cases_qc.io.dragen.load_vc_metrics")
    @mock.patch("cases_qc.io.dragen.load_wgs_contig_mean_cov")
    @mock.patch("cases_qc.io.dragen.load_wgs_coverage_metrics")
    @mock.patch("cases_qc.io.dragen.load_wgs_fine_hist")
    @mock.patch("cases_qc.io.dragen.load_wgs_hist")
    @mock.patch("cases_qc.io.dragen.load_wgs_overall_mean_cov")
    @mock.patch("cases_qc.io.dragen.load_region_coverage_metrics")
    @mock.patch("cases_qc.io.dragen.load_region_fine_hist")
    @mock.patch("cases_qc.io.dragen.load_region_hist")
    @mock.patch("cases_qc.io.dragen.load_region_overall_mean_cov")
    def test_run(
        self,
        load_region_overall_mean_cov,
        load_region_hist,
        load_region_fine_hist,
        load_region_coverage_metrics,
        mock_load_wgs_overall_mean_cov,
        mock_load_wgs_hist_metrics,
        mock_load_wgs_fine_hist,
        mock_load_wgs_coverage_metrics,
        mock_load_wgs_contig_mean_cov,
        mock_load_vc_metrics,
        mock_load_vc_hethom_ratio_metrics,
        mock_load_trimmer_metrics,
        mock_load_time_metrics,
        mock_load_sv_metrics,
        mock_load_roh_metrics,
        mock_load_ploidy_estimation_metrics,
        mock_load_mapping_metrics,
        mock_load_fragment_length_hist,
        mock_load_cnv_metrics,
    ):
        """Test import of a case with full set of Dragen QC files.

        This test is pretty long because there are a lot of files to import ;-).
        """
        self.assertEqual(Case.objects.count(), 0)
        self.assertEqual(CaseQc.objects.count(), 0)

        self.executor.run()

        self.assertEqual(Case.objects.count(), 1)
        self.assertEqual(CaseQc.objects.count(), 1)
        caseqc = CaseQc.objects.first()

        mock_load_cnv_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_cnv_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.cnv_metrics.csv"),
        )

        mock_load_fragment_length_hist.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_fragment_length_hist.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.fragment_length_hist.csv"),
        )

        mock_load_mapping_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_mapping_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.mapping_metrics.csv"),
        )

        mock_load_ploidy_estimation_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_ploidy_estimation_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.ploidy_estimation_metrics.csv"),
        )

        mock_load_roh_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_roh_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.roh_metrics.csv"),
        )

        mock_load_sv_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_sv_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.sv_metrics.csv"),
        )

        mock_load_time_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_time_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.time_metrics.csv"),
        )

        mock_load_trimmer_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_trimmer_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.trimmer_metrics.csv"),
        )

        mock_load_vc_hethom_ratio_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_vc_hethom_ratio_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.vc_hethom_ratio_metrics.csv"),
        )

        mock_load_vc_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_vc_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.vc_metrics.csv"),
        )

        mock_load_wgs_contig_mean_cov.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_wgs_contig_mean_cov.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.wgs_contig_mean_cov.csv"),
        )

        mock_load_wgs_coverage_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_wgs_coverage_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.wgs_coverage_metrics.csv"),
        )

        mock_load_wgs_fine_hist.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_wgs_fine_hist.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.wgs_fine_hist.csv"),
        )

        mock_load_wgs_hist_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_wgs_hist_metrics.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.wgs_hist.csv"),
        )

        mock_load_wgs_overall_mean_cov.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            mock_load_wgs_overall_mean_cov.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.wgs_overall_mean_cov.csv"),
        )

        load_region_overall_mean_cov.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            region_name="region-3",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            load_region_overall_mean_cov.call_args[1]["input_file"].name,
            os.path.realpath(
                "cases_qc/tests/data/sample.qc-coverage-region-3_overall_mean_cov.csv"
            ),
        )

        load_region_hist.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            region_name="region-3",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            load_region_hist.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.qc-coverage-region-3_hist.csv"),
        )

        load_region_fine_hist.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            region_name="region-3",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            load_region_fine_hist.call_args[1]["input_file"].name,
            os.path.realpath("cases_qc/tests/data/sample.qc-coverage-region-3_fine_hist.csv"),
        )

        load_region_coverage_metrics.assert_called_once_with(
            sample="NA12878-PCRF450-1",
            region_name="region-3",
            input_file=mock.ANY,
            caseqc=caseqc,
        )
        self.assertEqual(
            load_region_coverage_metrics.call_args[1]["input_file"].name,
            os.path.realpath(
                "cases_qc/tests/data/sample.qc-coverage-region-3_coverage_metrics.csv"
            ),
        )


class ImportUpdateTest(ExecutorTestMixin, TestCaseSnapshot, TestCase):
    """Test the executor with action=update"""

    def setUp(self):
        super().setUp()
        self._setUpExecutor(CaseImportAction.ACTION_UPDATE)
        self.case = CaseFactory(
            project=self.project,
            name=self.caseimportaction.payload["pedigree"]["persons"][0]["familyId"],
        )
        self.pedigree = PedigreeFactory(case=self.case)
        self.keep_invidual = IndividualFactory(
            pedigree=self.pedigree,
            name=self.caseimportaction.payload["proband"]["id"],
        )
        self.abundant_individual = IndividualFactory(
            pedigree=self.pedigree,
        )

    def test_run(self):
        self.assertEqual(Case.objects.count(), 1)
        self.executor.run()
        self.assertEqual(Case.objects.count(), 1)


class ImportDeleteTest(ExecutorTestMixin, TestCaseSnapshot, TestCase):
    """Test the executor with action=delete"""

    def setUp(self):
        super().setUp()
        self._setUpExecutor(CaseImportAction.ACTION_DELETE)
        self.case = CaseFactory(
            project=self.project,
            name=self.caseimportaction.payload["pedigree"]["persons"][0]["familyId"],
        )

    def test_run(self):
        self.assertEqual(Case.objects.count(), 1)
        self.executor.run()
        self.assertEqual(Case.objects.count(), 0)
