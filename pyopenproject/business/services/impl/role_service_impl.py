from pyopenproject.business import RoleService
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindByContext


class RoleServiceImpl(RoleService):

    def __init__(self, connection):
        """Constructor for RoleServiceImpl, from RoleService

        :param connection: The connection data
        """
        super().__init__(connection)

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())

    def find(self, role):
        return Find(self.connection, role).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()
