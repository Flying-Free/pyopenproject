from business.custom_action_service import CustomActionService
from business.impl.command.activity.find_by_context import FindByContext


class CustomActionServiceImpl(CustomActionService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
