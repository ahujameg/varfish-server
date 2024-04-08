from django.conf.urls import url

from variants import views
from variants.urls.annos import annos_ajax_urlpatterns
from variants.urls.presets import presets_ajax_urlpatterns
from variants.views import ajax as views_ajax
from variants.views import api as views_api

app_name = "variants"
ui_urlpatterns = [
    # Views for Case
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case-delete-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.CaseDeleteJobDetailView.as_view(),
        name="case-delete-job-detail",
    ),
    # View for list background jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/jobs/list/(?P<case>[0-9a-f-]+)/?$",
        view=views.BackgroundJobListView.as_view(),
        name="job-list",
    ),
    # Views for project sync jobs.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/sync-job/(?P<job>[0-9a-f-]+)/?$",
        view=views.SyncJobDetailView.as_view(),
        name="sync-job-detail",
    ),
    # Views for variants import job.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/import/(?P<job>[0-9a-f-]+)/?$",
        view=views.ImportVariantsJobDetailView.as_view(),
        name="import-job-detail",
    ),
    # Views for single-case file export jobs.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/export-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.ExportFileJobDetailView.as_view(),
        name="export-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/export-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.ExportFileJobResubmitView.as_view(),
        name="export-job-resubmit",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/export-job/download/(?P<job>[0-9a-f-]+)/?$",
        view=views.ExportFileJobDownloadView.as_view(),
        name="export-job-download",
    ),
    # Views for project-wide cases file export jobs.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-export-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.ExportProjectCasesFileJobDetailView.as_view(),
        name="project-cases-export-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-export-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.ExportProjectCasesFileJobResubmitView.as_view(),
        name="project-cases-export-job-resubmit",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-export-job/download/(?P<job>[0-9a-f-]+)/?$",
        view=views.ExportProjectCasesFileJobDownloadView.as_view(),
        name="project-cases-export-job-download",
    ),
    # Views for MutationDistiller submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/distiller-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.DistillerSubmissionJobDetailView.as_view(),
        name="distiller-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/distiller-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.DistillerSubmissionJobResubmitView.as_view(),
        name="distiller-job-resubmit",
    ),
    # Views for CADD submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/cadd-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.CaddSubmissionJobDetailView.as_view(),
        name="cadd-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/cadd-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.CaddSubmissionJobResubmitView.as_view(),
        name="cadd-job-resubmit",
    ),
    # Views for SPANR submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/spanr-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.SpanrSubmissionJobDetailView.as_view(),
        name="spanr-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/spanr-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.SpanrSubmissionJobResubmitView.as_view(),
        name="spanr-job-resubmit",
    ),
    # Views for Project-wide Statistics Computation submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-stats-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.ProjectStatsJobDetailView.as_view(),
        name="project-stats-job-detail",
    ),
    # Views for filtering and storing case query results jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/filter-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.FilterJobDetailView.as_view(),
        name="filter-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/filter-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.FilterJobResubmitView.as_view(),
        name="filter-job-resubmit",
    ),
    # Views for filtering and storing project cases query results jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/detail/(?P<job>[0-9a-f-]+)/?$",
        view=views.ProjectCasesFilterJobDetailView.as_view(),
        name="project-cases-filter-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/resubmit/(?P<job>[0-9a-f-]+)/?$",
        view=views.ProjectCasesFilterJobResubmitView.as_view(),
        name="project-cases-filter-job-resubmit",
    ),
    # Set last seen changelog version for user and redirect to changelog.
    # TODO: move to sodar-core?
    url(regex=r"^new-features/?$", view=views.NewFeaturesView.as_view(), name="new-features"),
    #: Detail views for site-wide maintenance jobs.
    url(
        regex=r"^clear-expired-job/(?P<job>[0-9a-f-]+)/?$",
        view=views.ClearExpiredExportedFilesJobDetailView.as_view(),
        name="clear-expired-job-detail",
    ),
    url(
        regex=r"^clear-inactive-variant-set-job/(?P<job>[0-9a-f-]+)/?$",
        view=views.ClearInactiveVariantSetsJobDetailView.as_view(),
        name="clear-inactive-variant-set-job",
    ),
    url(
        regex=r"^clear-old-kiosk-cases-job/(?P<job>[0-9a-f-]+)/?$",
        view=views.ClearOldKioskCasesJobDetailView.as_view(),
        name="clear-old-kiosk-cases-job-detail",
    ),
    url(
        regex=r"^refresh-small-variant-summaries-job/(?P<job>[0-9a-f-]+)/?$",
        view=views.RefreshSmallVariantSummaryJobDetailView.as_view(),
        name="refresh-small-variant-summaries-job-detail",
    ),
]

# Ajax API views
ajax_urlpatterns = [
    url(
        regex=r"^ajax/project/qc/(?P<project>[0-9a-f-]+)/?$",
        view=views_ajax.CaseListQcStatsAjaxView.as_view(),
        name="ajax-project-qc",
    ),
    url(
        regex=r"^ajax/case/retrieve/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseRetrieveAjaxView.as_view(),
        name="ajax-case-retrieve",
    ),
    url(
        regex=r"^ajax/query-case/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryListAjaxView.as_view(),
        name="ajax-query-case-list",
    ),
    url(
        regex=r"^ajax/query/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryListCreateAjaxView.as_view(),
        name="ajax-query-list-create",
    ),
    url(
        regex=r"^ajax/query/retrieve-update-destroy/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryRetrieveUpdateDestroyAjaxView.as_view(),
        name="ajax-query-retrieve-update-destroy",
    ),
    url(
        regex=r"^ajax/query-result-set/list/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryResultSetListAjaxView.as_view(),
        name="ajax-query-result-set-list",
    ),
    url(
        regex=r"^ajax/query-result-set/retrieve/(?P<smallvariantqueryresultset>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryResultSetRetrieveAjaxView.as_view(),
        name="ajax-query-result-set-retrieve",
    ),
    url(
        regex=r"^ajax/query-result-row/list/(?P<smallvariantqueryresultset>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryResultRowListAjaxView.as_view(),
        name="ajax-query-result-row-list",
    ),
    url(
        regex=r"^ajax/query-result-row/retrieve/(?P<smallvariantqueryresultrow>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryResultRowRetrieveAjaxView.as_view(),
        name="ajax-query-result-row-retrieve",
    ),
    url(
        r"^ajax/query-case/query-settings-shortcut/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQuerySettingsShortcutAjaxView.as_view(),
        name="ajax-query-settings-shortcut",
    ),
    url(
        r"^ajax/query-case/hpo-terms/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryHpoTermsAjaxView.as_view(),
        name="ajax-query-case-hpo-terms",
    ),
    url(
        r"^ajax/query-case/download/generate/tsv/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryDownloadGenerateAjaxView.as_view(),
        name="ajax-query-case-download-generate-tsv",
    ),
    url(
        r"^ajax/query-case/download/generate/vcf/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryDownloadGenerateAjaxView.as_view(),
        name="ajax-query-case-download-generate-vcf",
    ),
    url(
        r"^ajax/query-case/download/generate/xlsx/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryDownloadGenerateAjaxView.as_view(),
        name="ajax-query-case-download-generate-xlsx",
    ),
    url(
        r"^ajax/query-case/download/serve/(?P<exportfilebgjob>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryDownloadServeAjaxView.as_view(),
        name="ajax-query-case-download-serve",
    ),
    url(
        r"^ajax/query-case/download/status/(?P<exportfilebgjob>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantQueryDownloadStatusAjaxView.as_view(),
        name="ajax-query-case-download-status",
    ),
    url(
        r"^ajax/small-variant-comment/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantCommentListCreateAjaxView.as_view(),
        name="ajax-small-variant-comment-list-create",
    ),
    url(
        r"^ajax/small-variant-comment/list-project/(?P<project>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantCommentListProjectAjaxView.as_view(),
        name="ajax-small-variant-comment-list-project",
    ),
    url(
        r"^ajax/small-variant-comment/update/(?P<smallvariantcomment>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantCommentUpdateAjaxView.as_view(),
        name="ajax-small-variant-comment-update",
    ),
    url(
        r"^ajax/small-variant-comment/delete/(?P<smallvariantcomment>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantCommentDeleteAjaxView.as_view(),
        name="ajax-small-variant-comment-delete",
    ),
    url(
        r"^ajax/small-variant-flags/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantFlagsListCreateAjaxView.as_view(),
        name="ajax-small-variant-flags-list-create",
    ),
    url(
        r"^ajax/small-variant-flags/update/(?P<smallvariantflags>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantFlagsUpdateAjaxView.as_view(),
        name="ajax-small-variant-flags-update",
    ),
    url(
        r"^ajax/small-variant-flags/delete/(?P<smallvariantflags>[0-9a-f-]+)/?$",
        view=views_ajax.SmallVariantFlagsDeleteAjaxView.as_view(),
        name="ajax-small-variant-flags-delete",
    ),
    url(
        r"^ajax/acmg-criteria-rating/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.AcmgCriteriaRatingListCreateAjaxView.as_view(),
        name="ajax-acmg-criteria-rating-list-create",
    ),
    url(
        r"^ajax/acmg-criteria-rating/update/(?P<acmgcriteriarating>[0-9a-f-]+)/?$",
        view=views_ajax.AcmgCriteriaRatingUpdateAjaxView.as_view(),
        name="ajax-acmg-criteria-rating-update",
    ),
    url(
        r"^ajax/acmg-criteria-rating/delete/(?P<acmgcriteriarating>[0-9a-f-]+)/?$",
        view=views_ajax.AcmgCriteriaRatingDeleteAjaxView.as_view(),
        name="ajax-acmg-criteria-rating-delete",
    ),
    url(
        r"^ajax/extra-anno-fields/?$",
        view=views_ajax.ExtraAnnoFieldsApiView.as_view(),
        name="ajax-extra-anno-fields",
    ),
    url(
        regex=r"^ajax/hpo-terms/?$",
        view=views_ajax.HpoTermsAjaxView.as_view(),
        name="ajax-hpo-terms",
    ),
]

api_urlpatterns = [
    url(
        regex=r"^api/project/qc/(?P<project>[0-9a-f-]+)/?$",
        view=views_api.CaseListQcStatsApiView.as_view(),
        name="api-project-qc",
    ),
    url(
        regex=r"^api/case/retrieve/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.CaseRetrieveApiView.as_view(),
        name="api-case-retrieve",
    ),
    url(
        regex=r"^api/query-case/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryListApiView.as_view(),
        name="api-query-case-list",
    ),
    url(
        regex=r"^api/query/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryListCreateApiView.as_view(),
        name="api-query-list-create",
    ),
    url(
        regex=r"^api/query/retrieve-update-destroy/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryRetrieveUpdateDestroyApiView.as_view(),
        name="api-query-retrieve-update-destroy",
    ),
    url(
        regex=r"^api/query-result-set/list/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryResultSetListApiView.as_view(),
        name="api-query-result-set-list",
    ),
    url(
        regex=r"^api/query-result-set/retrieve/(?P<smallvariantqueryresultset>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryResultSetRetrieveApiView.as_view(),
        name="api-query-result-set-retrieve",
    ),
    url(
        regex=r"^api/query-result-row/list/(?P<smallvariantqueryresultset>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryResultRowListApiView.as_view(),
        name="api-query-result-row-list",
    ),
    url(
        regex=r"^api/query-result-row/retrieve/(?P<smallvariantqueryresultrow>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryResultRowRetrieveApiView.as_view(),
        name="api-query-result-row-retrieve",
    ),
    url(
        regex=r"^api/query-case/query-settings-shortcut/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQuerySettingsShortcutApiView.as_view(),
        name="api-query-settings-shortcut",
    ),
    url(
        regex=r"^api/query-case/quick-presets/?$",
        view=views_api.SmallVariantQuickPresetsApiView.as_view(),
        name="api-quick-presets",
    ),
    url(
        regex=r"^api/query-case/category-presets/(?P<category>[a-zA-Z0-9\._-]+)/?$",
        view=views_api.SmallVariantCategoryPresetsApiView.as_view(),
        name="api-category-presets",
    ),
    url(
        regex=r"^api/query-case/inheritance-presets/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantInheritancePresetsApiView.as_view(),
        name="api-inheritance-presets",
    ),
    url(
        regex=r"^api/query-case/hpo-terms/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryHpoTermsApiView.as_view(),
        name="api-query-case-hpo-terms",
    ),
    url(
        regex=r"^api/query-case/download/generate/tsv/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryDownloadGenerateApiView.as_view(),
        name="api-query-case-download-generate-tsv",
    ),
    url(
        regex=r"^api/query-case/download/generate/vcf/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryDownloadGenerateApiView.as_view(),
        name="api-query-case-download-generate-vcf",
    ),
    url(
        regex=r"^api/query-case/download/generate/xlsx/(?P<smallvariantquery>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryDownloadGenerateApiView.as_view(),
        name="api-query-case-download-generate-xlsx",
    ),
    url(
        regex=r"^api/query-case/download/serve/(?P<exportfilebgjob>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryDownloadServeApiView.as_view(),
        name="api-query-case-download-serve",
    ),
    url(
        regex=r"^api/query-case/download/status/(?P<exportfilebgjob>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantQueryDownloadStatusApiView.as_view(),
        name="api-query-case-download-status",
    ),
    url(
        r"^api/small-variant-comment/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantCommentListCreateApiView.as_view(),
        name="api-small-variant-comment-list-create",
    ),
    url(
        r"^api/small-variant-comment/list-project/(?P<project>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantCommentListProjectApiView.as_view(),
        name="api-small-variant-comment-list-project",
    ),
    url(
        r"^api/small-variant-comment/update/(?P<smallvariantcomment>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantCommentUpdateApiView.as_view(),
        name="api-small-variant-comment-update",
    ),
    url(
        r"^api/small-variant-comment/delete/(?P<smallvariantcomment>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantCommentDeleteApiView.as_view(),
        name="api-small-variant-comment-delete",
    ),
    url(
        r"^api/small-variant-flags/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantFlagsListCreateApiView.as_view(),
        name="api-small-variant-flags-list-create",
    ),
    url(
        r"^api/small-variant-flags/update/(?P<smallvariantflags>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantFlagsUpdateApiView.as_view(),
        name="api-small-variant-flags-update",
    ),
    url(
        r"^api/small-variant-flags/delete/(?P<smallvariantflags>[0-9a-f-]+)/?$",
        view=views_api.SmallVariantFlagsDeleteApiView.as_view(),
        name="api-small-variant-flags-delete",
    ),
    url(
        r"^api/acmg-criteria-rating/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.AcmgCriteriaRatingListCreateApiView.as_view(),
        name="api-acmg-criteria-rating-list-create",
    ),
    url(
        r"^api/acmg-criteria-rating/update/(?P<acmgcriteriarating>[0-9a-f-]+)/?$",
        view=views_api.AcmgCriteriaRatingUpdateApiView.as_view(),
        name="api-acmg-criteria-rating-update",
    ),
    url(
        r"^api/acmg-criteria-rating/delete/(?P<acmgcriteriarating>[0-9a-f-]+)/?$",
        view=views_api.AcmgCriteriaRatingDeleteApiView.as_view(),
        name="api-acmg-criteria-rating-delete",
    ),
    url(
        r"^api/extra-anno-fields/?$",
        view=views_api.ExtraAnnoFieldsApiView.as_view(),
        name="api-extra-anno-fields",
    ),
    url(regex=r"^api/hpo-terms/?$", view=views_api.HpoTermsApiView.as_view(), name="api-hpo-terms"),
]


urlpatterns = (
    ui_urlpatterns
    + ajax_urlpatterns
    + annos_ajax_urlpatterns
    + presets_ajax_urlpatterns
    + api_urlpatterns
)
