from src.extract.business.service_factory import ServiceFactory


class Category:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_project(self):
        if self._links.project.href is not None:
            return ServiceFactory.get_project_service().find_by_context(self._link.project.href)
        return None

    def get_default_assignee(self):
        if self._links.defaultAssignee.href is not None:
            return ServiceFactory.get_user_service().find_by_context(self._link.defaultAssignee.href)
        return None
