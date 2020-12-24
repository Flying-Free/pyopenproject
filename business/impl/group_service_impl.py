from business.group_service import GroupService
from business.impl.command.activity.find_by_context import FindByContext


class GroupServiceImpl(GroupService):

    def find(self, group):
        return Find(group).execute()
