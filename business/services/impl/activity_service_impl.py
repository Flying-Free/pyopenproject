from business.services.activity_service import ActivityService
from business.services.impl.command.activity.find import Find
from business.services.impl.command.activity.find_by_context import FindByContext
from business.services.impl.command.activity.update import Update


class ActivityServiceImpl(ActivityService):

    def __init__(self):
        super

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def find(self, activity):
        return Find(self.connection, activity).execute()

    def update(self, activity):
        return Update(self.connection, activity).execute()
