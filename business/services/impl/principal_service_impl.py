from business.services.impl.command.document.find_all import FindAll
from business.services.principal_service import PrincipalService


class PrincipalServiceImpl(PrincipalService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_all(self, filters):
        return FindAll(self.connection, filters).execute()
