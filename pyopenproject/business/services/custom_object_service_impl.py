from pyopenproject.business.custom_object_service import CustomObjectService
from pyopenproject.business.services.command.custom_object.find import Find


class CustomObjectServiceImpl(CustomObjectService):
    def __init__(self, connection):
        super().__init__(connection)

    def find(self, custom_object):
        return Find(self.connection, custom_object).execute()
