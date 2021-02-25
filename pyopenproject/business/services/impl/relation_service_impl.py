from pyopenproject.business.services.impl.command import Delete
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindByContext
from pyopenproject.business.services.impl.command import FindSchema
from pyopenproject.business.services.impl.command import FindSchemaByType
from pyopenproject.business.services.impl.command import Update
from pyopenproject.business.services.impl.command import UpdateForm
from pyopenproject.business.services.relation_service import RelationService


class RelationServiceImpl(RelationService):

    def __init__(self, connection):
        """Constructor for class RelationServiceImpl, from RelationService
        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self, relation):
        return Find(self.connection, relation).execute()

    def update(self, relation):
        return Update(self.connection, relation).execute()

    def delete(self, relation):
        return Delete(self.connection, relation).execute()

    def find_schema(self):
        return FindSchema(self.connection).execute()

    def find_schema_by_type(self, relation_type):
        return FindSchemaByType(self.connection, relation_type).execute()

    def find_all(self, filters=None, sort_by=None):
        return list(FindAll(self.connection, filters, sort_by).execute())

    def update_form(self, relation, form):
        return UpdateForm(self.connection, relation, form=form).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()
