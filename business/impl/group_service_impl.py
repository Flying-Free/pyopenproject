from business.group_service import GroupService


class GroupServiceImpl(GroupService):

    def find(self, group):
        return Find(group).execute()
