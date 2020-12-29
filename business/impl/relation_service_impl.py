from business.impl.command.relation.delete import Delete
from business.impl.command.relation.find import Find
from business.impl.command.relation.find_all import FindAll
from business.impl.command.relation.find_by_context import FindByContext
from business.impl.command.relation.find_schema import FindSchema
from business.impl.command.relation.update import Update
from business.impl.command.relation.update_form import UpdateForm
from business.relation_service import RelationService

class RelationServiceImpl(RelationService):

    def find(self, relation):
        return Find(relation).execute()

    def update(self, relation):
        return Update(relation).execute()

    def delete(self, relation):
        return Delete(relation).execute()

    def find_schema(self):
        return FindSchema().execute()

    def find_all(self, filters, sortBy):
        return FindAll(filters, sortBy).execute()

    def update_form(self, relation):
        return UpdateForm(relation).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()
