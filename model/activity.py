import business.services.impl.user_service_impl as user_service_impl
import business.services.impl.work_package_service_impl as work_package_service_impl


class Activity:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_work_package(self):
        if self._links.workPackage.href is not None:
            return work_package_service_impl.WorkPackageServiceImpl().find_by_context(self._link.workPackage.href)
        return None

    def get_user(self):
        if self._links.user.href is not None:
            return user_service_impl.UserServiceImpl().find_by_context(self._links.user.href)
        return None
