from business.service_factory import ServiceFactory


class Membership:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_schema(self):
        if self._links.schema.href is not None:
            return ServiceFactory.get_schema_service().find_by_context(self._links.schema.href)
        return None

    def get_project(self):
        if self._links.project.href is not None:
            return ServiceFactory.get_priority_service().find_by_context(self._link.project.href)
        return None

    def get_principal(self):
        if self._links.user.href is not None:
            return ServiceFactory.get_membership_service().find_member_by_context(self._link.principal.href)
        return None

    def get_roles(self):
        if not self._links.roles:
            return None
        else:
            for role in self._link.roles:
                yield ServiceFactory.get_role_service().find_by_context(role.href)

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
