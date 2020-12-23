from business.activity_service import ActivityService
from business.impl.command.activity.find import Find


class ConfigurationServiceImpl(ActivityService):

    def list(self):
        return List().execute()
