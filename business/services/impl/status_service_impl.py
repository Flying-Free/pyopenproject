from business.services.impl.command.status.find import Find
from business.services.impl.command.status.find_all import FindAll
from business.services.impl.command.status.find_by_context import FindByContext
from business.services.status_service import StatusService


class StatusServiceImpl(StatusService):

    def find_all(self):
        return FindAll().execute()

    def find_by_context(self):
        return FindByContext().execute()

    def find(self, status):
        return Find(status).execute()
