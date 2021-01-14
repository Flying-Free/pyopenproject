import business.services.impl.user_service_impl as user_service_impl


class User:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def lock(self):
        if self._link.lock.href is not None:
            return user_service_impl.UserServiceImpl().lock_user(self.id)
        return None

    def unlock(self):
        if self._link.lock.href is not None:
            return user_service_impl.UserServiceImpl().unlock_user(self.id)
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
        user_service_impl.UserServiceImpl().delete(self.id)
