from django.conf.urls import url

from cases import views, views_ajax, views_api

app_name = "cases"
ui_urlpatterns = [
    url(
        regex=r"^vueapp/(?P<project>[0-9a-f-]+)/?$",
        view=views.EntrypointView.as_view(),
        name="entrypoint",
    ),
]

ajax_urlpatterns = [
    url(
        regex=r"^ajax/case/list/(?P<project>[0-9a-f-]+)/?$",
        view=views_ajax.CaseListAjaxView.as_view(),
        name="ajax-case-list",
    ),
    url(
        regex=r"^ajax/case/retrieve-update-destroy/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseRetrieveUpdateDestroyAjaxView.as_view(),
        name="ajax-case-retrieveupdatedestroy",
    ),
    url(
        regex=r"^ajax/case-comment/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseCommentListCreateAjaxView.as_view(),
        name="ajax-casecomment-listcreate",
    ),
    url(
        regex=r"^ajax/case-comment/retrieve-update-destroy/(?P<casecomment>[0-9a-f-]+)/?$",
        view=views_ajax.CaseCommentRetrieveUpdateDestroyAjaxView.as_view(),
        name="ajax-casecomment-retrieveupdatedestroy",
    ),
    url(
        regex=r"^ajax/case-phenotype-terms/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CasePhenotypeTermsListCreateAjaxView.as_view(),
        name="ajax-casephenotypeterms-listcreate",
    ),
    url(
        regex=r"^ajax/case-phenotype-terms/retrieve-update-destroy/(?P<casephenotypeterms>[0-9a-f-]+)/?$",
        view=views_ajax.CasePhenotypeTermsRetrieveUpdateDestroyAjaxView.as_view(),
        name="ajax-casephenotypeterms-retrieveupdatedestroy",
    ),
    url(
        regex=r"^ajax/annotation-release-info/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.AnnotationReleaseInfoAjaxView.as_view(),
        name="ajax-annotationreleaseinfo-list",
    ),
    url(
        regex=r"^ajax/sv-annotation-release-info/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SvAnnotationReleaseInfoAjaxView.as_view(),
        name="ajax-svannotationreleaseinfo-list",
    ),
    url(
        regex=r"^ajax/case-gene-annotation/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseGeneAnnotationListAjaxView.as_view(),
        name="ajax-casegeneannotation-list",
    ),
    url(
        regex=r"ajax/user-permissions/(?P<project>[0-9a-f-]+)/?$",
        view=views_ajax.ProjectUserPermissionsAjaxView.as_view(),
        name="ajax-userpermissions",
    ),
    url(
        regex=r"^ajax/case-alignment-stats/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseAlignmentStatsListAjaxView.as_view(),
        name="ajax-casealignmentstats-list",
    ),
    url(
        regex=r"^ajax/case-variant-stats/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SampleVariantStatisticsListAjaxView.as_view(),
        name="ajax-casevariantstats-list",
    ),
    url(
        regex=r"^ajax/case-relatedness/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.PedigreeRelatednessListAjaxView.as_view(),
        name="ajax-caserelatedness-list",
    ),
]

api_urlpatterns = [
    url(
        regex=r"^api/case/list/(?P<project>[0-9a-f-]+)/?$",
        view=views_api.CaseListApiView.as_view(),
        name="api-case-list",
    ),
    url(
        regex=r"^api/case/retrieve-update-destroy/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.CaseRetrieveUpdateDestroyApiView.as_view(),
        name="api-case-retrieveupdatedestroy",
    ),
    url(
        regex=r"^api/case-comment/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.CaseCommentListCreateApiView.as_view(),
        name="api-casecomment-listcreate",
    ),
    url(
        regex=r"^ajax/case-comment/retrieve-update-destroy/(?P<casecomment>[0-9a-f-]+)/?$",
        view=views_api.CaseCommentRetrieveUpdateDestroyApiView.as_view(),
        name="api-casecomment-retrieveupdatedestroy",
    ),
    url(
        regex=r"^api/case-phenotype-terms/list-create/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.CasePhenotypeTermsListCreateApiView.as_view(),
        name="api-casephenotypeterms-listcreate",
    ),
    url(
        regex=r"^api/case-phenotype-terms/retrieve-update-destroy/(?P<casephenotypeterms>[0-9a-f-]+)/?$",
        view=views_api.CasePhenotypeTermsRetrieveUpdateDestroyApiView.as_view(),
        name="api-casephenotypeterms-retrieveupdatedestroy",
    ),
    url(
        regex=r"^api/annotation-release-info/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.AnnotationReleaseInfoApiView.as_view(),
        name="api-annotationreleaseinfo-list",
    ),
    url(
        regex=r"^api/sv-annotation-release-info/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_api.SvAnnotationReleaseInfoApiView.as_view(),
        name="api-svannotationreleaseinfo-list",
    ),
    url(
        regex=r"^api/case-gene-annotation/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseGeneAnnotationListAjaxView.as_view(),
        name="api-casegeneannotation-list",
    ),
    url(
        regex=r"^api/case-alignment-stats/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.CaseAlignmentStatsListAjaxView.as_view(),
        name="api-casealignmentstats-list",
    ),
    url(
        regex=r"^api/case-variant-stats/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.SampleVariantStatisticsListAjaxView.as_view(),
        name="api-casevariantstats-list",
    ),
    url(
        regex=r"^api/case-relatedness/list/(?P<case>[0-9a-f-]+)/?$",
        view=views_ajax.PedigreeRelatednessListAjaxView.as_view(),
        name="api-caserelatedness-list",
    ),
    url(
        regex=r"^api/user-and-global-settings/?$",
        view=views_api.UserAndGlobalSettingsView.as_view(),
        name="api-userandglobalsettings",
    ),
]


urlpatterns = ui_urlpatterns + ajax_urlpatterns + api_urlpatterns
