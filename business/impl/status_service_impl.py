from src.extract.business.impl.activity.find_by_context import FindByContext
from src.extract.business.impl.status.find_by_id import FindById
from src.extract.business.status_service import StatusService


class StatusServiceImpl(StatusService):

    def find_all(self):
        return FindAll().execute

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_by_id(self, identifier):
        return FindById(identifier).execute()
