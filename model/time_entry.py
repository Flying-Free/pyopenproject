import json

import business.service_factory as service_factory


class TimeEntry:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_schema(self):
        if self._links.schema.href is not None:
            return service_factory.ServiceFactory.get_schema_service()\
                .find_by_context(self._links.schema.href)
        return None

    def get_project(self):
        if self._links.project.href is not None:
            return service_factory.ServiceFactory.get_project_service()\
                .find_by_context(self._link.project.href)
        return None

    def get_work_package(self):
        if self._links.workPackage.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._link.workPackage.href)
        return None

    def get_user(self):
        if self._links.user.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .find_by_context(self._link.user.href)
        return None

    def get_activity(self):
        if self._links.activity.href is not None:
            return service_factory.ServiceFactory.get_activity_service()\
                .find_by_context(self._link.activity.href)
        return None

    # TODO: Study how to perform this actions associated to the project
    #         "updateImmediately": {
    #             "href": "/api/v3/time_entries/18",
    #             "method": "patch"
    #         },
    #         "update": {
    #             "href": "/api/v3/time_entries/18/form",
    #             "method": "post"
    #         }

    def delete(self):
        service_factory.ServiceFactory.get_time_entry_service()\
            .delete(self.id)

    def __str__(self):
        return json.dumps(self.__dict__)
