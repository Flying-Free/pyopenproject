from src.extract.business.impl.work_package.find_all import FindAll
from src.extract.business.impl.work_package.find_by_context import FindByContext
from src.extract.business.impl.work_package.find_by_id import FindById
from src.extract.business.type_service import TypeService


class TypeServiceImpl(TypeService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new type
    def new_type(self): raise NotImplementedError
