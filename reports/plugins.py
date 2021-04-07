from projectroles.plugins import ProjectAppPluginPoint

from .urls import urlpatterns


class ProjectAppPlugin(ProjectAppPluginPoint):
    """Plugin for registering app with Projectroles"""

    name = "reports"
    title = "Reports"
    urls = urlpatterns
    # ...

    icon = "file-text-o"

    entry_point_url_id = "reports:template-list"

    description = "Generate reports on word processing templates"

    #: Required permission for accessing the app
    app_permission = "reports.view_data"

    #: Enable or disable general search from project title bar
    search_enable = False

    #: List of search object types for the app
    search_types = []

    #: No settings for this app.
    app_settings = {}

    def get_object_link(self, model_str, uuid):
        """
        Return URL for referring to a object used by the app, along with a
        label to be shown to the user for linking.
        :param model_str: Object class (string)
        :param uuid: sodar_uuid of the referred object
        :return: Dict or None if not found
        """
        return None
