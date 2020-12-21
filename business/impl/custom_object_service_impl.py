from business.custom_object_service import CustomObjectService
from business.impl.activity.find_by_context import FindByContext


class CustomObjectServiceImpl(CustomObjectService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
