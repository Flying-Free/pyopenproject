from business.services.impl.command.relation.delete import Delete
from business.services.impl.command.relation.find import Find
from business.services.impl.command.relation.find_all import FindAll
from business.services.impl.command.relation.find_by_context import FindByContext
from business.services.impl.command.relation.find_schema import FindSchema
from business.services.impl.command.relation.find_schema_by_type import FindSchemaByType
from business.services.impl.command.relation.update import Update
from business.services.impl.command.relation.update_form import UpdateForm
from business.services.relation_service import RelationService


class RelationServiceImpl(RelationService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, relation):
        return Find(self.connection, relation).execute()

    def update(self, relation):
        return Update(self.connection, relation).execute()

    def delete(self, relation):
        return Delete(self.connection, relation).execute()

    def find_schema(self):
        return FindSchema(self.connection).execute()

    def find_schema_by_type(self, type):
        return FindSchemaByType(self.connection, type).execute()

    def find_all(self, filters, sort_by):
        return FindAll(self.connection, filters, sort_by).execute()

    def update_form(self, relation, form):
        return UpdateForm(self.connection, relation, form=form).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()
