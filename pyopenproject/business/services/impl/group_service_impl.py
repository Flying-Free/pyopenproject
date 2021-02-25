from pyopenproject.business import GroupService
from pyopenproject.business.services.impl.command import Find


class GroupServiceImpl(GroupService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, group):
        return Find(self.connection, group).execute()
