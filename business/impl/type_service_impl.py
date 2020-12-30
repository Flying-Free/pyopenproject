from business.impl.command.work_package.find_all import FindAll
from business.impl.command.work_package.find_by_id import FindById
from business.type_service import TypeService


class TypeServiceImpl(TypeService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()


