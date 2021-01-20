import json

import business.service_factory as service_factory


class Relation:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_from(self):
        work_package_from = self._links.__getattribute__("from").href
        if work_package_from.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(work_package_from)
        return None

    def get_to(self):
        if self._links.to.href is not None:
            return service_factory.ServiceFactory.get_work_package_service()\
                .find_by_context(self._links.to.href)
        return None

    def delete(self):
        service_factory.ServiceFactory.get_relation_service()\
            .delete(self.id)

    # TODO:
    #         "update": {
    #             "href": "/api/v3/relations/1/form",
    #             "method": "POST"
    #         },
    #         "updateImmediately": {
    #             "href": "/api/v3/relations/1",
    #             "method": "PATCH"
    #         }

    def __str__(self):
        return json.dumps(self.__dict__)
