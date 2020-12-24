from business.service_factory import ServiceFactory


class Principal:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_user(self):
        if self._links.user.href is not None:
            return ServiceFactory.get_user_service().find_by_context(self._links.user.href)
        return None
