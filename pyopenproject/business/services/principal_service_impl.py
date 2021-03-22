from pyopenproject.business.principal_service import PrincipalService
from pyopenproject.business.services.command.principal.find_all import FindAll


class PrincipalServiceImpl(PrincipalService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())
