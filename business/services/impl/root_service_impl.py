from business.services.impl.command.root.find import Find
from business.services.root_service import RootService


class RootServiceImpl(RootService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self):
        return Find(self.connection).execute()
