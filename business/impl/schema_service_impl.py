from business.impl.work_package.find_all import FindAll
from business.impl.work_package.find_by_context import FindByContext
from business.impl.work_package.find_by_id import FindById
from business.schema_service import SchemaService


class SchemaServiceImpl(SchemaService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new schema
    def new_schema(self): raise NotImplementedError
