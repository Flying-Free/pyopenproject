from pyopenproject.business.services.command.version.create import Create
from pyopenproject.business.services.command.version.create_form import CreateForm
from pyopenproject.business.services.command.version.delete import Delete
from pyopenproject.business.services.command.version.find import Find
from pyopenproject.business.services.command.version.find_all import FindAll
from pyopenproject.business.services.command.version.find_by_context import FindByContext
from pyopenproject.business.services.command.version.find_projects import FindProjects
from pyopenproject.business.services.command.version.find_schema import FindSchema
from pyopenproject.business.services.command.version.update import Update
from pyopenproject.business.services.command.version.update_form import UpdateForm
from pyopenproject.business.version_service import VersionService


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
        Delete(self.connection, version).execute()

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
