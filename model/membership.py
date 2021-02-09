import json

import business.service_factory as service_factory


class Membership:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_schema(self):
        if self._links.work_package.href is not None:
            return service_factory.ServiceFactory.get_schema_service() \
                .find_by_context(self._links.work_package.href)
        return None

    def get_project(self):
        if self._links.project.href is not None:
            return service_factory.ServiceFactory.get_priority_service()\
                .find_by_context(self._link.project.href)
        return None

    def get_principal(self):
        if self._links.user.href is not None:
            return service_factory.ServiceFactory.get_membership_service()\
                .find_member_by_context(self._link.principal.href)
        return None

    def get_roles(self):
        if not self._links.roles:
            return None
        else:
            for role in self._link.roles:
                yield service_factory.ServiceFactory.get_role_service()\
                    .find_by_context(role.href)

    # TODO
    #     "update": {
    #         "href": "/api/v3/memberships/11/form",
    #         "method": "post"
    #     },
    #     "updateImmediately": {
    #         "href": "/api/v3/memberships/11",
    #         "method": "patch"
    #     },
    #  },

    def __str__(self):
        return json.dumps(self.__dict__)
