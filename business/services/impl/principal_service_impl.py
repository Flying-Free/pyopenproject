from business.services.impl.command.document.find_all import FindAll
from business.services.principal_service import PrincipalService


class PrincipalServiceImpl(PrincipalService):

    def find_all(self, filters):
        return FindAll(filters).execute()
