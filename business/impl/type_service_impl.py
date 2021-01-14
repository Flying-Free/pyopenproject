from business.impl.command.type.find import Find
from business.impl.command.type.find_all import FindAll
from business.type_service import TypeService


class TypeServiceImpl(TypeService):

    def find(self, type):
        return Find(type).execute()

    def find_all(self):
        return FindAll().execute


