from pyopenproject.business.activity_service import ActivityService
from pyopenproject.business.services.command.activity.find import Find
from pyopenproject.business.services.command.activity.find_by_context import FindByContext
from pyopenproject.business.services.command.activity.update import Update


class ActivityServiceImpl(ActivityService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def find(self, activity):
        return Find(self.connection, activity).execute()

    def update(self, activity):
        return Update(self.connection, activity).execute()
