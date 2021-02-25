from pyopenproject.business import PriorityService
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll


class PriorityServiceImpl(PriorityService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, priority):
        return Find(self.connection, priority).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())
