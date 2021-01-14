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

    def find(self, project):
        return Find(project).execute()

    def update(self, project):
        return Update(project).execute()

    def delete(self, project):
        return Delete(project).execute()

    def find_all(self, filters, sortBy):
        return FindAll().execute()

    def create(self, project):
        return Create(project).execute()

    def find_schema(self):
        return FindSchema().execute()

    def create_form(self, form):
        return CreateForm(form).execute()

    def update_form(self, project):
        return UpdateForm(project).execute()

    def find_parents(self, filters, of, sortBy):
        return FindParents(filters, of, sortBy).execute()

    def find_versions(self, project):
        return FindVersions(project).execute()

    def find_types(self, project):
        return FindTypes(project).execute()

    def find_budgets(self, project):
        return FindBudgets(project).execute()

    def find_work_packages(self, project, offset, pageSize, filters, sortBy, groupBy, showSums, notify):
        return FindWorkPackages(project, offset, pageSize, filters, sortBy, groupBy, showSums, notify).execute()

    def create_work_package(self, project, notify, workPackage):
        return CreateWorkPackage(project, notify, workPackage).execute()

    def create_work_package_form(self, project, notify, form):
        return CreateWorkPackageForm(project, notify, form).execute()

    def find_available_assignees(self, project):
        return FindAvailableAssignees(project).execute()

    def find_available_responsibles(self, project):
        return FindAvailableResponsibles(project).execute()
