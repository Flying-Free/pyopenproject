from business.priority_service import PriorityService


class PriorityServiceImpl(PriorityService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
