from business.services.impl.command.work_package.add_attachment import AddAttachment
from business.services.impl.command.work_package.create import Create
from business.services.impl.command.work_package.create_activity import CreateActivity
from business.services.impl.command.work_package.create_form import CreateForm
from business.services.impl.command.work_package.create_relation import CreateRelation
from business.services.impl.command.work_package.create_relation_form import CreateRelationForm
from business.services.impl.command.work_package.create_watcher import CreateWatcher
from business.services.impl.command.work_package.delete import Delete
from business.services.impl.command.work_package.delete_watcher import DeleteWatcher
from business.services.impl.command.work_package.find import Find
from business.services.impl.command.work_package.find_activities import FindActivities
from business.services.impl.command.work_package.find_all import FindAll
from business.services.impl.command.work_package.find_all_schemas import FindAllSchemas
from business.services.impl.command.work_package.find_attachments import FindAttachments
from business.services.impl.command.work_package.find_available_projects import \
    FindAvailableProjects
from business.services.impl.command.work_package.find_available_watchers import \
    FindAvailableWatchers
from business.services.impl.command.work_package.find_by_context import FindByContext
from business.services.impl.command.work_package.find_relation_candidates import \
    FindRelationCandidates
from business.services.impl.command.work_package.find_relations import FindRelations
from business.services.impl.command.work_package.find_revisions import FindRevisions
from business.services.impl.command.work_package.find_schema import FindSchema
from business.services.impl.command.work_package.find_watchers import FindWatchers
from business.services.impl.command.work_package.update import Update
from business.services.impl.command.work_package.update_form import UpdateForm
from business.services.work_package_service import WorkPackageService


class WorkPackageServiceImpl(WorkPackageService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_attachments(self, work_package):
        return FindAttachments(work_package).execute()

    def add_attachment(self, work_package, attachment):
        return AddAttachment(work_package, attachment).execute()

    def find(self, work_package):
        return Find(work_package).execute()

    def update(self, work_package, notify):
        return Update(work_package, notify)

    def delete(self, work_package):
        Delete(work_package).execute()

    def find_schema(self, schema):
        return FindSchema(schema)

    def find_all_schemas(self, filters):
        return FindAllSchemas(filters)

    def update_form(self, work_package):
        return UpdateForm(work_package)

    def find_all(self, offset, pageSize, filters, sortBy, groupBy, showSums):
        return FindAll(offset, pageSize, filters, sortBy, groupBy, showSums).execute()

    def create(self, work_package, notify):
        return Create(work_package, notify)

    def create_form(self, work_package):
        return CreateForm(work_package).execute()

    def create_relation(self, work_package, relation):
        return CreateRelation(work_package, relation).execute

    def find_relations(self, work_package):
        return FindRelations(work_package).execute()

    def create_relation_form(self, work_package, relation):
        return CreateRelationForm(work_package, relation).execute()

    def find_watchers(self, work_package):
        return FindWatchers(work_package).execute()

    def create_watcher(self, work_package, watcher):
        return CreateWatcher(work_package, watcher).execute()

    def delete_watcher(self, work_package, watcher):
        DeleteWatcher(work_package, watcher).execute()

    def find_relation_candidates(self, work_package, filters, query, type, pageSize):
        return FindRelationCandidates(work_package, filters, query, type, pageSize).execute()

    def find_available_watchers(self, work_package):
        return FindAvailableWatchers(work_package).execute()

    def find_available_projects(self, work_package):
        return FindAvailableProjects(work_package).execute()

    def find_revisions(self, work_package):
        return FindRevisions(work_package).execute()

    def find_activities(self, work_package):
        return FindActivities(work_package).execute()

    def create_activity(self, work_package, activity, notify):
        return CreateActivity(work_package,activity, notify).execute()