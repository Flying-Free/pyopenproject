from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.type_service import TypeService


class TypeServiceImpl(TypeService):

    def __init__(self, connection):
        """Constructor for class TypeServiceImpl, from TypeService
        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self, work_package_type):
        return Find(self.connection, work_package_type).execute()

    def find_all(self):
        return list(FindAll(self.connection).execute())
