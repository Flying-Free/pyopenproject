from pyopenproject.business.project_service import ProjectService
from pyopenproject.business.services.command.project.create import Create
from pyopenproject.business.services.command.project.create_form import CreateForm
from pyopenproject.business.services.command.project.create_work_package import CreateWorkPackage
from pyopenproject.business.services.command.project.create_work_package_form import CreateWorkPackageForm
from pyopenproject.business.services.command.project.delete import Delete
from pyopenproject.business.services.command.project.find import Find
from pyopenproject.business.services.command.project.find_all import FindAll
from pyopenproject.business.services.command.project.find_available_assignees import FindAvailableAssignees
from pyopenproject.business.services.command.project.find_available_responsibles import FindAvailableResponsibles
from pyopenproject.business.services.command.project.find_budgets import FindBudgets
from pyopenproject.business.services.command.project.find_parents import FindParents
from pyopenproject.business.services.command.project.find_schema import FindSchema
from pyopenproject.business.services.command.project.find_types import FindTypes
from pyopenproject.business.services.command.project.find_versions import FindVersions
from pyopenproject.business.services.command.project.find_work_packages import FindWorkPackages
from pyopenproject.business.services.command.project.update import Update
from pyopenproject.business.services.command.project.update_form import UpdateForm


class ProjectServiceImpl(ProjectService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, project):
        return Find(self.connection, project).execute()

    def update(self, project):
        return Update(self.connection, project).execute()

    def delete(self, project):
        return Delete(self.connection, project).execute()

    def find_all(self, filters=None, sort_by=None):
        return list(FindAll(self.connection, filters, sort_by).execute())

    def create(self, project):
        return Create(self.connection, project).execute()

    def find_schema(self):
        return FindSchema(self.connection).execute()

    def create_form(self, form):
        return CreateForm(self.connection, form).execute()

    def update_form(self, form):
        return UpdateForm(self.connection, form).execute()

    def find_parents(self, filters=None, of=None, sort_by=None):
        return list(FindParents(self.connection, filters, of, sort_by).execute())

    def find_versions(self, project):
        return FindVersions(self.connection, project).execute()

    def find_types(self, project):
        return list(FindTypes(self.connection, project).execute())

    def find_budgets(self, project):
        return list(FindBudgets(self.connection, project).execute())

    def find_work_packages(self, project, offset=None, page_size=None, filters=None, group_by=None, sort_by=None,
                           show_sums=None):
        return list(FindWorkPackages(self.connection, project, offset, page_size, filters, group_by, sort_by, show_sums)
                    .execute())

    def create_work_package(self, project, work_package, notify=None):
        return CreateWorkPackage(self.connection, project, work_package, notify).execute()

    def create_work_package_form(self, project, form):
        return CreateWorkPackageForm(self.connection, project, form).execute()

    def find_available_assignees(self, project):
        return list(FindAvailableAssignees(self.connection, project).execute())

    def find_available_responsibles(self, project):
        return list(FindAvailableResponsibles(self.connection, project).execute())
