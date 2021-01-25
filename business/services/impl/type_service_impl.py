from business.services.impl.command.type.find import Find
from business.services.impl.command.type.find_all import FindAll
from business.services.type_service import TypeService


class TypeServiceImpl(TypeService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, type):
        return Find(self.connection, type).execute()

    def find_all(self):
        return list(FindAll(self.connection).execute)
