from pyopenproject.business import HelpTextsService
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll


class HelpTextsServiceImpl(HelpTextsService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, help_text):
        return Find(self.connection, help_text).execute()

    def find_all(self):
        return list(FindAll(self.connection).execute())
