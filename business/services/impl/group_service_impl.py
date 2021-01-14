from business.services.group_service import GroupService
from business.services.impl.command.group.find import Find


class GroupServiceImpl(GroupService):

    def find(self, group):
        return Find(group).execute()
