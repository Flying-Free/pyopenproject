from pyopenproject.business import VersionService
from pyopenproject.business.services.impl.command import Create
from pyopenproject.business.services.impl.command import CreateForm
from pyopenproject.business.services.impl.command import Delete
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindByContext
from pyopenproject.business.services.impl.command import FindProjects
from pyopenproject.business.services.impl.command import FindSchema
from pyopenproject.business.services.impl.command import Update
from pyopenproject.business.services.impl.command import UpdateForm


class VersionServiceImpl(VersionService):

    def __init__(self, connection):
        """Constructor for class VersionServiceImpl, from VersionService

        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self, version):
        return Find(self.connection, version).execute()

    def update(self, version):
        return Update(self.connection, version).execute()

    def delete(self, version):
        return Delete(self.connection, version).execute()

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())

    def create(self, version):
        return Create(self.connection, version).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def find_schema(self):
        return FindSchema(self.connection).execute()

    def create_form(self, version):
        return CreateForm(self.connection, version).execute()

    def update_form(self, form):
        return UpdateForm(self.connection, form).execute()

    def find_projects(self):
        return list(FindProjects(self.connection).execute())
