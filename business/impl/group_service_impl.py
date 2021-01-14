from business.group_service import GroupService
from business.impl.command.group.find import Find


class GroupServiceImpl(GroupService):

    def find(self, group):
        return Find(group).execute()
