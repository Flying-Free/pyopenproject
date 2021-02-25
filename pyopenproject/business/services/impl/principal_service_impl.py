from pyopenproject.business import PrincipalService
from pyopenproject.business.services.impl.command import FindAll


class PrincipalServiceImpl(PrincipalService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())
