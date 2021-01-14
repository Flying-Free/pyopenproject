from business.services.impl.command.activity.find_by_context import FindByContext
from business.services.impl.command.role.find import Find
from business.services.impl.command.role.find_all import FindAll
from business.services.role_service import RoleService


class RoleServiceImpl(RoleService):

    def find_all(self, filters):
        return FindAll(filters).execute()

    def find(self, role):
        return Find(role).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()
