from openproject.business.group_service import GroupService
from openproject.business.services.command.group.find import Find


class GroupServiceImpl(GroupService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, group):
        return Find(self.connection, group).execute()
