from business.services.impl.command.root.find import Find
from business.services.root_service import RootService


class RootServiceImpl(RootService):

    def __init__(self, connection):
        """ Constructor for class RootServiceImpl, from RootService

        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self):
        return Find(self.connection).execute()
