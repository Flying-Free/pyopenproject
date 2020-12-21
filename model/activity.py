from business.service_factory import ServiceFactory


class Activity:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_work_package(self):
        if self._links.workPackage.href is not None:
            return ServiceFactory.get_work_package_service().find_by_context(self._link.workPackage.href)
        return None

    def get_user(self):
        if self._links.user.href is not None:
            return ServiceFactory.get_user_service().find_by_context(self._links.user.href)
        return None
