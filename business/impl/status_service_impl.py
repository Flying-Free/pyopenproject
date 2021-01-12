from business.impl.command.status.find import Find
from business.impl.command.status.find_all import FindAll
from business.impl.command.status.find_by_context import FindByContext
from business.status_service import StatusService


class StatusServiceImpl(StatusService):

    def find_all(self):
        return FindAll().execute()

    def find_by_context(self):
        return FindByContext().execute()

    def find(self, status):
        return Find(status).execute()
