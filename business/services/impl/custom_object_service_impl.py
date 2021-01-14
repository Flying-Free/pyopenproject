
from business.services.custom_object_service import CustomObjectService
from business.services.impl.command.custom_object.find import Find


class CustomObjectServiceImpl(CustomObjectService):

    def find(self, custom_object):
        return Find(custom_object).execute()
