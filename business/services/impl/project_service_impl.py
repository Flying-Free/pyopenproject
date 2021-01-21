from business.services.impl.command.project.create import Create
from business.services.impl.command.project.create_form import CreateForm
from business.services.impl.command.project.create_work_package import CreateWorkPackage
from business.services.impl.command.project.create_work_package_form import CreateWorkPackageForm
from business.services.impl.command.project.delete import Delete
from business.services.impl.command.project.find import Find
from business.services.impl.command.project.find_all import FindAll
from business.services.impl.command.project.find_available_assignees import FindAvailableAssignees
from business.services.impl.command.project.find_available_responsibles import FindAvailableResponsibles
from business.services.impl.command.project.find_budgets import FindBudgets
from business.services.impl.command.project.find_parents import FindParents
from business.services.impl.command.project.find_schema import FindSchema
from business.services.impl.command.project.find_types import FindTypes
from business.services.impl.command.project.find_versions import FindVersions
from business.services.impl.command.project.find_work_packages import FindWorkPackages
from business.services.impl.command.project.update import Update
from business.services.impl.command.project.update_form import UpdateForm
from business.services.project_service import ProjectService


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

    def update_form(self, project):
        return UpdateForm(self.connection, project).execute()

    def find_parents(self, filters, of, sort_by):
        return FindParents(self.connection, filters, of, sort_by).execute()

    def find_versions(self, project):
        return FindVersions(self.connection, project).execute()

    def find_types(self, project):
        return FindTypes(self.connection, project).execute()

    def find_budgets(self, project):
        return FindBudgets(self.connection, project).execute()

    def find_work_packages(self, project, offset, page_size, filters, sort_by, group_by, show_sums, notify):
        return FindWorkPackages(self.connection, project, offset, page_size, filters,
                                sort_by, group_by, show_sums, notify).execute()

    def create_work_package(self, project, notify, work_package):
        return CreateWorkPackage(self.connection, project, notify, work_package).execute()

    def create_work_package_form(self, project, notify, form):
        return CreateWorkPackageForm(self.connection, project, notify, form).execute()

    def find_available_assignees(self, project):
        return FindAvailableAssignees(self.connection, project).execute()

    def find_available_responsibles(self, project):
        return FindAvailableResponsibles(self.connection, project).execute()
