from pyopenproject.business.root_service import RootService
from pyopenproject.business.services.command.root.find import Find


class RootServiceImpl(RootService):

    def __init__(self, connection):
        """Constructor for class RootServiceImpl, from RootService

        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self):
        return Find(self.connection).execute()
