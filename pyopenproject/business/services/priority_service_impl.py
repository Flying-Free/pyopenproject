from pyopenproject.business.priority_service import PriorityService
from pyopenproject.business.services.command.priority.find import Find
from pyopenproject.business.services.command.priority.find_all import FindAll


class PriorityServiceImpl(PriorityService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, priority):
        return Find(self.connection, priority).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())
