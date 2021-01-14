from business.services.impl.command.version.create import Create
from business.services.impl.command.version.create_form import CreateForm
from business.services.impl.command.version.delete import Delete
from business.services.impl.command.version.find import Find
from business.services.impl.command.version.find_all import FindAll
from business.services.impl.command.version.find_by_context import FindByContext
from business.services.impl.command.version.find_projects import FindProjects
from business.services.impl.command.version.find_schema import FindSchema
from business.services.impl.command.version.update import Update
from business.services.impl.command.version.update_form import UpdateForm
from business.services.version_service import VersionService


class VersionServiceImpl(VersionService):

    def find(self, version):
        return Find(version).execute()

    def update(self, version):
        return Update(version).execute()

    def delete(self, version):
        Delete.execute(version).execute()

    def find_all(self, filters):
        return FindAll(filters).execute()

    def create(self, version):
        return Create(version).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_schema(self):
        return FindSchema.execute()

    def create_form(self, version):
        return CreateForm(version).execute

    def update_form(self, version):
        return UpdateForm(version).execute()

    def find_projects(self):
        return FindProjects().execute()