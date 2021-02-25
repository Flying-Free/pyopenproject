from pyopenproject.business import StatusService
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindByContext
from pyopenproject.business.services.impl.command.status.find import Find


class StatusServiceImpl(StatusService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_all(self):
        return list(FindAll(self.connection).execute())

    def find_by_context(self):
        return FindByContext(self.connection).execute()

    def find(self, status):
        return Find(self.connection, status).execute()
