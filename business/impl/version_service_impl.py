from business.impl.command.version.find import Find
from business.impl.command.version.find_all import FindAll
from business.impl.command.version.find_by_context import FindByContext
from business.impl.command.version.find_projects import FindProjects
from business.impl.command.version.find_schema import FindSchema
from business.impl.command.version.update import Update
from business.impl.command.version.delete import Delete
from business.impl.command.version.create import Create
from business.impl.command.version.create_form import CreateForm
from business.impl.command.version.update_form import UpdateForm

from business.version_service import VersionService


class VersionServiceImpl(VersionService):

    def find(self, version):
        return Find(version).execute()

    def update_version(self, version):
        return Update(version).execute()

    def delete_version(self, version):
        Delete.execute(version).execute()

    def find_all(self, filters):
        return FindAll(filters).execute()

    def new_version(self, version):
        return Create(version).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_schema(self):
        return FindSchema.execute()

    def new_version_form(self, version):
        return CreateForm(version).execute

    def update_version_form(self, version):
        return UpdateForm(version).execute()

    def find_projects(self):
        return FindProjects().execute()