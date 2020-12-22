from business.custom_object_service import CustomObjectService
from business.impl.command.activity.find_by_context import FindByContext


class CustomObjectServiceImpl(CustomObjectService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
