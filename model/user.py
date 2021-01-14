import business.service_factory as service_factory


class User:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def lock(self):
        if self._link.lock.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .lock_user(self.id)
        return None

    def unlock(self):
        if self._link.lock.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .unlock_user(self.id)
        return None

    # TODO:
    #         "showUser": {
    #             "href": "/users/21",
    #             "type": "text/html"
    #         },
    #         "updateImmediately": {
    #             "href": "/api/v3/users/21",
    #             "title": "Update roleopr@dxc.com",
    #             "method": "patch"
    #         },

    def delete(self):
        service_factory.ServiceFactory.get_user_service()\
            .delete(self.id)
