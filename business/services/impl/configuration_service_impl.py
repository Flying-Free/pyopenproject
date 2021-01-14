from business.services.configuration_service import ConfigurationService
from business.services.impl.command.configuration.find import Find


class ConfigurationServiceImpl(ConfigurationService):

    def find(self):
        return Find().execute()
