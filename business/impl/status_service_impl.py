
from business.status_service import StatusService


class StatusServiceImpl(StatusService):

    def find_all(self):
        return FindAll().execute()

    def find_by_context(self):
        return FindByContext().execute()

    def find(self, status):
        return Find(status).execute()
