from business.configuration_service import ConfigurationService
from business.impl.command.activity.find import Find


class ConfigurationServiceImpl(ConfigurationService):

    def find(self):
        return Find().execute()
