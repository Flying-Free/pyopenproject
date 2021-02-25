from pyopenproject.business import CustomObjectService
from pyopenproject.business.services.impl.command import Find


class CustomObjectServiceImpl(CustomObjectService):
    def __init__(self, connection):
        super().__init__(connection)

    def find(self, custom_object):
        return Find(self.connection, custom_object).execute()
