from pyopenproject.business.configuration_service import ConfigurationService
from pyopenproject.business.services.command.configuration.find import Find


class ConfigurationServiceImpl(ConfigurationService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self):
        return Find(self.connection).execute()
