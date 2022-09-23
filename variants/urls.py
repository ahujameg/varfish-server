from django.conf.urls import url

from . import views, views_ajax, views_api

app_name = "variants"
ui_urlpatterns = [
    # Views for Case
    url(regex=r"^(?P<project>[0-9a-f-]+)/$", view=views.CaseListView.as_view(), name="case-list"),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/get-annotations/$",
        view=views.CaseListGetAnnotationsView.as_view(),
        name="case-list-get-annotations",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/get-qc/$",
        view=views.CaseListGetQCView.as_view(),
        name="case-list-get-qc",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/sync-upstream/$",
        view=views.CaseListSyncRemoteView.as_view(),
        name="case-list-sync-remote",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/api-qc/$",
        view=views.CaseListQcStatsApiView.as_view(),
        name="api-project-qc",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseDetailView.as_view(),
        name="case-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/update/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseUpdateView.as_view(),
        name="case-update",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/update-terms/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseUpdateTermView.as_view(),
        name="case-update-terms",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/case-fetch-upstream-terms/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseFetchUpstreamTermsView.as_view(),
        name="case-fetch-upstream-terms",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/delete/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseDeleteView.as_view(),
        name="case-delete",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/download-annotations/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseDownloadAnnotationsView.as_view(),
        name="case-download-annotations",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/download-annotations/$",
        view=views.ProjectDownloadAnnotationsView.as_view(),
        name="project-download-annotations",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case-delete-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.CaseDeleteJobDetailView.as_view(),
        name="case-delete-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/structuralvariants/delete/(?P<case>[0-9a-f-]+)/$",
        view=views.StructuralVariantsDeleteView.as_view(),
        name="structuralvariants-delete",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/smallvariants/delete/(?P<case>[0-9a-f-]+)/$",
        view=views.SmallVariantsDeleteView.as_view(),
        name="smallvariants-delete",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/fix-sex/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseFixSexView.as_view(),
        name="case-fix-sex",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases/fix-sex/$",
        view=views.ProjectCasesFixSexView.as_view(),
        name="project-cases-fix-sex",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/api-qc/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseDetailQcStatsApiView.as_view(),
        name="api-case-qc",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/filter/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseFilterView.as_view(),
        name="case-filter",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/filter/(?P<case>[0-9a-f-]+)/job/(?P<job>[0-9a-f-]+)/$",
        view=views.CaseFilterView.as_view(),
        name="case-filter-job",
    ),
    # Project-wide case filtration.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases/filter/$",
        view=views.ProjectCasesFilterView.as_view(),
        name="project-cases-filter",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases/filter/cohort/(?P<cohort>[0-9a-f-]+)/$",
        view=views.ProjectCasesFilterView.as_view(),
        name="project-cases-filter-cohort",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases/filter/job/(?P<job>[0-9a-f-]+)/$",
        view=views.ProjectCasesFilterView.as_view(),
        name="project-cases-filter-job",
    ),
    # View for list background jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/jobs/list/(?P<case>[0-9a-f-]+)/$",
        view=views.BackgroundJobListView.as_view(),
        name="job-list",
    ),
    # Views for project sync jobs.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/sync-job/(?P<job>[0-9a-f-]+)/$",
        view=views.SyncJobDetailView.as_view(),
        name="sync-job-detail",
    ),
    # Views for variants import job.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/import/(?P<job>[0-9a-f-]+)/$",
        view=views.ImportVariantsJobDetailView.as_view(),
        name="import-job-detail",
    ),
    # Views for single-case file export jobs.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/export-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.ExportFileJobDetailView.as_view(),
        name="export-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/export-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.ExportFileJobResubmitView.as_view(),
        name="export-job-resubmit",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/export-job/download/(?P<job>[0-9a-f-]+)/$",
        view=views.ExportFileJobDownloadView.as_view(),
        name="export-job-download",
    ),
    # Views for project-wide cases file export jobs.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-export-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.ExportProjectCasesFileJobDetailView.as_view(),
        name="project-cases-export-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-export-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.ExportProjectCasesFileJobResubmitView.as_view(),
        name="project-cases-export-job-resubmit",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-export-job/download/(?P<job>[0-9a-f-]+)/$",
        view=views.ExportProjectCasesFileJobDownloadView.as_view(),
        name="project-cases-export-job-download",
    ),
    # Views for MutationDistiller submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/distiller-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.DistillerSubmissionJobDetailView.as_view(),
        name="distiller-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/distiller-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.DistillerSubmissionJobResubmitView.as_view(),
        name="distiller-job-resubmit",
    ),
    # Views for CADD submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/cadd-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.CaddSubmissionJobDetailView.as_view(),
        name="cadd-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/cadd-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.CaddSubmissionJobResubmitView.as_view(),
        name="cadd-job-resubmit",
    ),
    # Views for SPANR submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/spanr-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.SpanrSubmissionJobDetailView.as_view(),
        name="spanr-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/spanr-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.SpanrSubmissionJobResubmitView.as_view(),
        name="spanr-job-resubmit",
    ),
    # Views for Project-wide Statistics Computation submission jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-stats-job/create/$",
        view=views.ProjectStatsJobCreateView.as_view(),
        name="project-stats-job-create",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-stats-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.ProjectStatsJobDetailView.as_view(),
        name="project-stats-job-detail",
    ),
    # API for accessing small variant flags and comments.
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/small-variant-flags/(?P<case>[0-9a-f-]+)/$",
        view=views.SmallVariantFlagsApiView.as_view(),
        name="small-variant-flags-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/small-variant-comment/(?P<case>[0-9a-f-]+)/$",
        view=views.SmallVariantCommentSubmitApiView.as_view(),
        name="small-variant-comment-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/multi-small-variant-flags-comment/$",
        view=views.MultiSmallVariantFlagsAndCommentApiView.as_view(),
        name="multi-small-variant-flags-comment-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/small-variant-comment-delete/(?P<case>[0-9a-f-]+)/$",
        view=views.SmallVariantCommentDeleteApiView.as_view(),
        name="small-variant-comment-delete-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/case-comments-delete/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseCommentsDeleteApiView.as_view(),
        name="case-comments-delete-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/small-variant-acmg-rating/(?P<case>[0-9a-f-]+)/$",
        view=views.AcmgCriteriaRatingApiView.as_view(),
        name="acmg-rating-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/case-notes/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseNotesStatusApiView.as_view(),
        name="case-notes-status-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/case-comments-submit/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseCommentsSubmitApiView.as_view(),
        name="case-comments-submit-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/case-comments-delete/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseCommentsDeleteApiView.as_view(),
        name="case-comments-delete-api",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/case-comments-count/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseCommentsCountApiView.as_view(),
        name="case-comments-count-api",
    ),
    # Views for filtering and storing case query results jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/filter-results/(?P<case>[0-9a-f-]+)/$",
        view=views.CasePrefetchFilterView.as_view(),
        name="case-filter-results",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/filter-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.FilterJobDetailView.as_view(),
        name="filter-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/filter-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.FilterJobResubmitView.as_view(),
        name="filter-job-resubmit",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/case/load-filter-results/(?P<case>[0-9a-f-]+)/$",
        view=views.CaseLoadPrefetchedFilterView.as_view(),
        name="case-load-filter-results",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/filter-job/status/$",
        view=views.FilterJobGetStatus.as_view(),
        name="filter-job-status",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/filter-job/previous/(?P<case>[0-9a-f-]+)/$",
        view=views.FilterJobGetPrevious.as_view(),
        name="filter-job-previous",
    ),
    # Views for filtering and storing project cases query results jobs
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases/filter-results/$",
        view=views.ProjectCasesPrefetchFilterView.as_view(),
        name="project-cases-filter-results",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/detail/(?P<job>[0-9a-f-]+)/$",
        view=views.ProjectCasesFilterJobDetailView.as_view(),
        name="project-cases-filter-job-detail",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/resubmit/(?P<job>[0-9a-f-]+)/$",
        view=views.ProjectCasesFilterJobResubmitView.as_view(),
        name="project-cases-filter-job-resubmit",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases/load-filter-results/$",
        view=views.ProjectCasesLoadPrefetchedFilterView.as_view(),
        name="project-cases-load-filter-results",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/status/$",
        view=views.ProjectCasesFilterJobGetStatus.as_view(),
        name="project-cases-filter-job-status",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/previous/$",
        view=views.ProjectCasesFilterJobGetPrevious.as_view(),
        name="project-cases-filter-job-previous",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/project-cases-filter-job/previous/cohort/(?P<cohort>[0-9a-f-]+)/$",
        view=views.ProjectCasesFilterJobGetPrevious.as_view(),
        name="project-cases-filter-job-previous-cohort",
    ),
    # Render details row
    url(
        regex=(
            r"^(?P<project>[0-9a-f-]+)/case/small-variant-details/(?P<case>[0-9a-f-]+)/"
            r"(?P<release>(GRCh37|GRCh38))-(?P<chromosome>(chr)?([0-9]{1,2}|[XY]|MT?))-(?P<start>[0-9]+)-(?P<end>[0-9]+)-"
            r"(?P<reference>[ACGT]+)-(?P<alternative>[ACGT]+)/(?P<database>[^/]+)/(?P<gene_id>[^/]+)/"
            r"(?P<ensembl_transcript_id>[^/]+)/(?P<training_mode>[01])/$"
        ),
        view=views.SmallVariantDetails.as_view(),
        name="small-variant-details",
    ),
    # Render details row
    url(
        regex=(
            r"^(?P<project>[0-9a-f-]+)/cohort/(?P<cohort>[0-9a-f-]+)/case/small-variant-details/(?P<case>[0-9a-f-]+)/"
            r"(?P<release>(GRCh37|GRCh38))-(?P<chromosome>(chr)?([0-9]{1,2}|[XY]|MT?))-(?P<start>[0-9]+)-(?P<end>[0-9]+)-"
            r"(?P<reference>[ACGT]+)-(?P<alternative>[ACGT]+)/(?P<database>[^/]+)/(?P<gene_id>[^/]+)/"
            r"(?P<ensembl_transcript_id>[^/]+)/(?P<training_mode>[01])/$"
        ),
        view=views.SmallVariantDetails.as_view(),
        name="small-variant-details-cohort",
    ),
    url(regex=r"^hpo-terms-api/$", view=views.HpoTermsApiView.as_view(), name="hpo-terms-api"),
    # Set last seen changelog version for user and redirect to changelog.
    # TODO: move to sodar-core?
    url(regex=r"^new-features/$", view=views.NewFeaturesView.as_view(), name="new-features"),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/kiosk-status/annotate_job/(?P<annotate_job>[0-9a-f-]+)/import_job/(?P<import_job>[0-9a-f-]+)/$",
        view=views.KioskStatusView.as_view(),
        name="kiosk-status",
    ),
    url(
        regex=r"^(?P<project>[0-9a-f-]+)/kiosk-get-status/annotate_job/(?P<annotate_job>[0-9a-f-]+)/import_job/(?P<import_job>[0-9a-f-]+)/$",
        view=views.KioskJobGetStatus.as_view(),
        name="kiosk-get-status",
    ),
    url(
        regex=r"^variant-validator/$",
        view=views.VariantValidatorApiView.as_view(),
        name="variant-validator-api",
    ),
    url(
        regex=r"^variant-carriers/$",
        view=views.VariantCarriersView.as_view(),
        name="variant-carriers",
    ),
    url(
        regex=r"^second-hit/(?P<case>[0-9a-f-]+)/(?P<database>[^/]+)/(?P<gene_id>[^/]+)/",
        view=views.SecondHitView.as_view(),
        name="second-hit",
    ),
    #: Detail views for site-wide maintenance jobs.
    url(
        regex=r"^clear-expired-job/(?P<job>[0-9a-f-]+)/$",
        view=views.ClearExpiredExportedFilesJobDetailView.as_view(),
        name="clear-expired-job-detail",
    ),
    url(
        regex=r"^clear-inactive-variant-set-job/(?P<job>[0-9a-f-]+)/$",
        view=views.ClearInactiveVariantSetsJobDetailView.as_view(),
        name="clear-inactive-variant-set-job",
    ),
    url(
        regex=r"^clear-old-kiosk-cases-job/(?P<job>[0-9a-f-]+)/$",
        view=views.ClearOldKioskCasesJobDetailView.as_view(),
        name="clear-old-kiosk-cases-job-detail",
    ),
    url(
        regex=r"^refresh-small-variant-summaries-job/(?P<job>[0-9a-f-]+)/$",
        view=views.RefreshSmallVariantSummaryJobDetailView.as_view(),
        name="refresh-small-variant-summaries-job-detail",
    ),
    url(
        regex=r"^vue3app/(?P<case>[0-9a-f-]+)/$",
        view=views.SmallVariantFilterForm.as_view(),
        name="entrypoint",
    ),
]

# Ajax API views
ajax_urlpatterns = [
    url(
        regex=r"^ajax/case/retrieve/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.CaseRetrieveAjaxView.as_view(),
        name="ajax-case-retrieve",
    ),
    url(
        regex=r"^ajax/query-case/list/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryListAjaxView.as_view(),
        name="ajax-query-case-list",
    ),
    url(
        regex=r"^ajax/query-case/create/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryCreateAjaxView.as_view(),
        name="ajax-query-case-create",
    ),
    url(
        regex=r"^ajax/query-case/retrieve/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryRetrieveAjaxView.as_view(),
        name="ajax-query-case-retrieve",
    ),
    url(
        regex=r"^ajax/query-case/status/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryStatusAjaxView.as_view(),
        name="ajax-query-case-status",
    ),
    url(
        r"^ajax/query-case/update/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryUpdateAjaxView.as_view(),
        name="ajax-query-case-update",
    ),
    url(
        r"^ajax/query-case/results/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryFetchResultsAjaxView.as_view(),
        name="ajax-query-case-fetch-results",
    ),
    url(
        r"^ajax/query-case/results-extended/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryFetchExtendedResultsAjaxView.as_view(),
        name="ajax-query-case-fetch-extended-results",
    ),
    url(
        r"^ajax/query-case/query-settings-shortcut/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQuerySettingsShortcutAjaxView.as_view(),
        name="ajax-query-settings-shortcut",
    ),
    url(
        r"^ajax/query-case/hpo-terms/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantQueryHpoTermsAjaxView.as_view(),
        name="ajax-query-case-hpo-terms",
    ),
    url(
        regex=(
            r"^ajax/small-variant-details/(?P<case>[0-9a-f-]+)/"
            r"(?P<release>(GRCh37|GRCh38))-(?P<chromosome>(chr)?([0-9]{1,2}|[XY]|MT?))-(?P<start>[0-9]+)-(?P<end>[0-9]+)-"
            r"(?P<reference>[ACGT]+)-(?P<alternative>[ACGT]+)/(?P<database>[^/]+)/(?P<gene_id>[^/]+)/$"
        ),
        view=views_ajax.SmallVariantDetailsApiView.as_view(),
        name="ajax-small-variant-details",
    ),
    url(
        r"^ajax/small-variant-comment/create/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantCommentCreateAjaxView.as_view(),
        name="ajax-small-variant-comment-create",
    ),
    url(
        r"^ajax/small-variant-comment/update/(?P<smallvariantcomment>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantCommentUpdateAjaxView.as_view(),
        name="ajax-small-variant-comment-update",
    ),
    url(
        r"^ajax/small-variant-comment/delete/(?P<smallvariantcomment>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantCommentDeleteAjaxView.as_view(),
        name="ajax-small-variant-comment-delete",
    ),
    url(
        r"^ajax/small-variant-flags/create/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantFlagsCreateAjaxView.as_view(),
        name="ajax-small-variant-flags-create",
    ),
    url(
        r"^ajax/small-variant-flags/update/(?P<smallvariantflags>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantFlagsUpdateAjaxView.as_view(),
        name="ajax-small-variant-flags-update",
    ),
    url(
        r"^ajax/small-variant-flags/delete/(?P<smallvariantflags>[0-9a-f-]+)/$",
        view=views_ajax.SmallVariantFlagsDeleteAjaxView.as_view(),
        name="ajax-small-variant-flags-delete",
    ),
    url(
        r"^ajax/acmg-criteria-rating/create/(?P<case>[0-9a-f-]+)/$",
        view=views_ajax.AcmgCriteriaRatingCreateAjaxView.as_view(),
        name="ajax-acmg-criteria-rating-create",
    ),
    url(
        r"^ajax/acmg-criteria-rating/update/(?P<acmgcriteriarating>[0-9a-f-]+)/$",
        view=views_ajax.AcmgCriteriaRatingUpdateAjaxView.as_view(),
        name="ajax-acmg-criteria-rating-update",
    ),
    url(
        r"^ajax/acmg-criteria-rating/delete/(?P<acmgcriteriarating>[0-9a-f-]+)/$",
        view=views_ajax.AcmgCriteriaRatingDeleteAjaxView.as_view(),
        name="ajax-acmg-criteria-rating-delete",
    ),
]

api_urlpatterns = [
    url(
        regex=r"^api/case/list/(?P<project>[0-9a-f-]+)/$",
        view=views_api.CaseListApiView.as_view(),
        name="api-case-list",
    ),
    url(
        regex=r"^api/case/retrieve/(?P<case>[0-9a-f-]+)/$",
        view=views_api.CaseRetrieveApiView.as_view(),
        name="api-case-retrieve",
    ),
    url(
        regex=r"^api/query-case/list/(?P<case>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryListApiView.as_view(),
        name="api-query-case-list",
    ),
    url(
        regex=r"^api/query-case/create/(?P<case>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryCreateApiView.as_view(),
        name="api-query-case-create",
    ),
    url(
        regex=r"^api/query-case/retrieve/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryRetrieveApiView.as_view(),
        name="api-query-case-retrieve",
    ),
    url(
        regex=r"^api/query-case/status/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryStatusApiView.as_view(),
        name="api-query-case-status",
    ),
    url(
        regex=r"^api/query-case/update/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryUpdateApiView.as_view(),
        name="api-query-case-update",
    ),
    url(
        regex=r"^api/query-case/results/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryFetchResultsApiView.as_view(),
        name="api-query-case-fetch-results",
    ),
    url(
        regex=r"^api/query-case/query-settings-shortcut/(?P<case>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQuerySettingsShortcutApiView.as_view(),
        name="api-query-settings-shortcut",
    ),
    url(
        regex=r"^api/query-case/hpo-terms/(?P<smallvariantquery>[0-9a-f-]+)/$",
        view=views_api.SmallVariantQueryHpoTermsApiView.as_view(),
        name="api-query-case-hpo-terms",
    ),
    url(
        regex=(
            r"^api/small-variant-details/(?P<case>[0-9a-f-]+)/"
            r"(?P<release>(GRCh37|GRCh38))-(?P<chromosome>(chr)?([0-9]{1,2}|[XY]|MT?))-(?P<start>[0-9]+)-(?P<end>[0-9]+)-"
            r"(?P<reference>[ACGT]+)-(?P<alternative>[ACGT]+)/(?P<database>[^/]+)/(?P<gene_id>[^/]+)/$"
        ),
        view=views_api.SmallVariantDetailsApiView.as_view(),
        name="api-small-variant-details",
    ),
    url(
        r"^api/small-variant-comment/create/(?P<case>[0-9a-f-]+)/$",
        view=views_api.SmallVariantCommentCreateApiView.as_view(),
        name="api-small-variant-comment-create",
    ),
    url(
        r"^api/small-variant-comment/update/(?P<smallvariantcomment>[0-9a-f-]+)/$",
        view=views_api.SmallVariantCommentUpdateApiView.as_view(),
        name="api-small-variant-comment-update",
    ),
    url(
        r"^api/small-variant-comment/delete/(?P<smallvariantcomment>[0-9a-f-]+)/$",
        view=views_api.SmallVariantCommentDeleteApiView.as_view(),
        name="api-small-variant-comment-delete",
    ),
    url(
        r"^api/small-variant-flags/create/(?P<case>[0-9a-f-]+)/$",
        view=views_api.SmallVariantFlagsCreateApiView.as_view(),
        name="api-small-variant-flags-create",
    ),
    url(
        r"^api/small-variant-flags/update/(?P<smallvariantflags>[0-9a-f-]+)/$",
        view=views_api.SmallVariantFlagsUpdateApiView.as_view(),
        name="api-small-variant-flags-update",
    ),
    url(
        r"^api/small-variant-flags/delete/(?P<smallvariantflags>[0-9a-f-]+)/$",
        view=views_api.SmallVariantFlagsDeleteApiView.as_view(),
        name="api-small-variant-flags-delete",
    ),
    url(
        r"^api/acmg-criteria-rating/create/(?P<case>[0-9a-f-]+)/$",
        view=views_api.AcmgCriteriaRatingCreateApiView.as_view(),
        name="api-acmg-criteria-rating-create",
    ),
    url(
        r"^api/acmg-criteria-rating/update/(?P<acmgcriteriarating>[0-9a-f-]+)/$",
        view=views_api.AcmgCriteriaRatingUpdateApiView.as_view(),
        name="api-acmg-criteria-rating-update",
    ),
    url(
        r"^api/acmg-criteria-rating/delete/(?P<acmgcriteriarating>[0-9a-f-]+)/$",
        view=views_api.AcmgCriteriaRatingDeleteApiView.as_view(),
        name="api-acmg-criteria-rating-delete",
    ),
]


urlpatterns = ui_urlpatterns + ajax_urlpatterns + api_urlpatterns
