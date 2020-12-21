from business.impl.activity.find_by_context import FindByContext


class RoleServiceImpl(RoleService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
