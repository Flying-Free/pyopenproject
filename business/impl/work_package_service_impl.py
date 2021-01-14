from business.impl.command.work_package.add_attachment import AddAttachment
from business.impl.command.work_package.create import Create
from business.impl.command.work_package.create_activity import CreateActivity
from business.impl.command.work_package.create_form import CreateForm
from business.impl.command.work_package.create_relation import CreateRelation
from business.impl.command.work_package.create_relation_form import CreateRelationForm
from business.impl.command.work_package.create_watcher import CreateWatcher
from business.impl.command.work_package.delete import Delete
from business.impl.command.work_package.delete_watcher import DeleteWatcher
from business.impl.command.work_package.find import Find
from business.impl.command.work_package.find_activities_by_work_package import FindActivitiesByWorkPackage
from business.impl.command.work_package.find_all import FindAll
from business.impl.command.work_package.find_all_schemas import FindAllSchemas
from business.impl.command.work_package.find_attachments import FindAttachments
from business.impl.command.work_package.find_available_projects_by_work_package import \
    FindAvailableProjectsByWorkPackage
from business.impl.command.work_package.find_available_watchers_by_work_package import \
    FindAvailableWatchersByWorkPackage
from business.impl.command.work_package.find_by_context import FindByContext
from business.impl.command.work_package.find_relation_candidates_by_work_package import \
    FindRelationCandidatesByWorkPackage
from business.impl.command.work_package.find_relations_by_work_package import FindRelationsByWorkPackage
from business.impl.command.work_package.find_revisions_by_work_package import FindRevisionsByWorkPackage
from business.impl.command.work_package.find_schema import FindSchema
from business.impl.command.work_package.find_watchers_by_work_package import FindWatchersByWorkPackage
from business.impl.command.work_package.update import Update
from business.impl.command.work_package.update_form import UpdateForm
from business.work_package_service import WorkPackageService


class WorkPackageServiceImpl(WorkPackageService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_attachments(self, work_package):
        return FindAttachments(work_package).execute()

    def add_attachment(self, work_package, attachment):
        return AddAttachment(work_package, attachment).execute()

    def find(self, work_package, notify):
        return Find(work_package, notify).execute()

    def update(self, work_package, notify):
        return Update(work_package, notify)

    def delete_work_package(self, work_package, notify):
        Delete(work_package, notify).execute()

    def find_schema(self, schema):
        return FindSchema(schema)

    def find_all_schemas(self, filters):
        return FindAllSchemas(filters)

    def update_form(self, work_package):
        return UpdateForm(work_package)

    def find_all(self, notify, offset, pageSize, filters, sortBy, groupBy, showSums):
        return FindAll(notify, offset, pageSize, filters, sortBy, groupBy, showSums).execute()

    def create(self, work_package, notify):
        return Create(work_package, notify)

    def create_form(self, work_package):
        return CreateForm(work_package).execute()

    def create_relation(self, work_package, relation):
        return CreateRelation(work_package, relation).execute

    def find_relations_by_work_package(self, work_package):
        return FindRelationsByWorkPackage(work_package).execute()

    def create_relation_form(self, work_package, relation):
        return CreateRelationForm(work_package, relation).execute()

    def find_watchers_by_work_package(self, work_package):
        return FindWatchersByWorkPackage(work_package).execute()

    def create_watcher(self, work_package, watcher):
        return CreateWatcher(work_package, watcher).execute()

    def delete_watcher(self, work_package, watcher):
        DeleteWatcher(work_package, watcher).execute()

    def find_relation_candidates_by_work_package(self, work_package, filters, query, type, pageSize):
        return FindRelationCandidatesByWorkPackage(work_package, filters, query, type, pageSize).execute()

    def find_available_watchers_by_work_package(self, work_package):
        return FindAvailableWatchersByWorkPackage(work_package).execute()

    def find_available_projects_by_work_package(self, work_package):
        return FindAvailableProjectsByWorkPackage(work_package).execute()

    def find_revisions_by_work_package(self, work_package):
        return FindRevisionsByWorkPackage(work_package).execute()

    def find_activities_by_work_package(self, work_package, notify):
        return FindActivitiesByWorkPackage(work_package, notify).execute()

    def create_activity(self, work_package, activity, notify):
        return CreateActivity(work_package,activity, notify).execute()