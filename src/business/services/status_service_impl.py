from src.business.services.command.status.find import Find
from src.business.services.command.status.find_all import FindAll
from src.business.services.command.status.find_by_context import FindByContext
from src.business.status_service import StatusService


class StatusServiceImpl(StatusService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_all(self):
        return list(FindAll(self.connection).execute())

    def find_by_context(self):
        return FindByContext(self.connection).execute()

    def find(self, status):
        return Find(self.connection, status).execute()
