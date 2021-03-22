from src.business.group_service import GroupService
from src.business.services.command.group.find import Find


class GroupServiceImpl(GroupService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, group):
        return Find(self.connection, group).execute()
