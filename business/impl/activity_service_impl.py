from business.activity_service import ActivityService
from business.impl.activity.find_by_context import FindByContext


class ActivityServiceImpl(ActivityService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
