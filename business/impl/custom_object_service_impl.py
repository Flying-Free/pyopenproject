from abc import ABC

from business.custom_object_service import CustomObjectService
from business.impl.command.custom_object.find import Find


class CustomObjectServiceImpl(CustomObjectService, ABC):

    def find(self, custom_object):
        return Find(custom_object).execute()
