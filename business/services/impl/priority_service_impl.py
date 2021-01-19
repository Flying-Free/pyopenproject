from business.services.impl.command.priority.find import Find
from business.services.impl.command.priority.find_all import FindAll
from business.services.priority_service import PriorityService


class PriorityServiceImpl(PriorityService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, priority):
        return Find(self.connection, priority).execute()

    def find_all(self, offset, page_size, filters, sort_by):
        return FindAll(self.connection, offset, page_size, filters, sort_by).execute()
