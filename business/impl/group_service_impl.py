from business.impl.command.activity.find_by_context import FindByContext


class GroupServiceImpl(GroupService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
