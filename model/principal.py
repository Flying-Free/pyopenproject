import json

import business.service_factory as service_factory


class Principal:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_user(self):
        if self._links.user.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .find_by_context(self._links.user.href)
        return None

    def __str__(self):
        return json.dumps(self.__dict__)
