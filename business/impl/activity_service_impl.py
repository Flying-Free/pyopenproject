from business.activity_service import ActivityService
from business.impl.command.activity.find import Find
from business.impl.command.activity.find_by_context import FindByContext


class ActivityServiceImpl(ActivityService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_by_id(self, identifier):
        return Find(identifier).execute()

    def update(self, identifier, body):
        return Find(identifier, body).execute()
