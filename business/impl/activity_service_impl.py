from business.activity_service import ActivityService
from business.impl.activity.find_by_context import FindByContext
from business.impl.activity.find_by_id import FindById


class ActivityServiceImpl(ActivityService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_by_id(self, identifier):
        return FindById(identifier).execute()

    def update(self, identifier, body):
        return FindById(identifier, body).execute()