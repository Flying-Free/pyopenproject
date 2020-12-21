from business.service_factory import ServiceFactory


class Project:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_work_packages(self):
        if self._links.workPackages.href is not None:
            return ServiceFactory.get_work_package_service().find_by_context(self._links.workPackages.href)
        return None

    def get_categories(self):
        if self._links.categories.href is not None:
            return ServiceFactory.get_category_service().find_by_context(self._links.categories.href)
        return None

    def get_versions(self):
        if self._links.versions.href is not None:
            return ServiceFactory.get_version_service().find_by_context(self._links.versions.href)
        return None

    def get_membership(self):
        if self._links.memberships.href is not None:
            return ServiceFactory.get_membership_service().find_by_context(self._links.memberships.href)
        return None

    def get_types(self):
        if self._links.types.href is not None:
            return ServiceFactory.get_type_service().find_by_context(self._links.types.href)
        return None

    def get_schema(self):
        if self._links.schema.href is not None:
            return ServiceFactory.get_schema_service().find_by_context(self._links.schema.href)
        return None

    def get_parent(self):
        if self._links.parent.href is not None:
            return ServiceFactory.get_project_service().find_by_context(self._links.parent.href)
        return None

    # TODO: Study how to perform this actions associated to the project
    #     "createWorkPackage": {
    #       "href": "/api/v3/projects/15/work_packages/form",
    #       "method": "post"
    #     },
    #     "createWorkPackageImmediately": {
    #       "href": "/api/v3/projects/15/work_packages",
    #       "method": "post"
    #     },
    #     "update": {
    #       "href": "/api/v3/projects/15/form",
    #       "method": "post"
    #     },
    #     "updateImmediately": {
    #       "href": "/api/v3/projects/15",
    #       "method": "patch"
    #     }

    def delete(self):
        ServiceFactory.get_project_service().delete(self.id)
