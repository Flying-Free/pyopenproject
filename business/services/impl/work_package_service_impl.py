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

    def __init__(self, connection):
        super().__init__(connection)

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def find_attachments(self, work_package):
        return FindAttachments(self.connection, work_package).execute()

    def add_attachment(self, work_package, attachment):
        return AddAttachment(self.connection, work_package, attachment).execute()

    def find(self, work_package):
        return Find(self.connection, work_package).execute()

    def update(self, work_package, notify=None):
        return Update(self.connection, work_package, notify).execute()

    def delete(self, work_package):
        return Delete(self.connection, work_package).execute()

    def find_schema(self, schema):
        return FindSchema(self.connection, schema).execute()

    def find_all_schemas(self, filters):
        return FindAllSchemas(self.connection, filters).execute()

    def update_form(self, work_package):
        return UpdateForm(self.connection)

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None, group_by=None, show_sums=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by, group_by, show_sums).execute())

    def create(self, work_package, notify=None):
        return Create(self.connection, work_package, notify).execute()

    def create_form(self):
        return CreateForm(self.connection).execute()

    def create_relation(self, type, work_package_from, work_package_to, description):
        return CreateRelation(self.connection, type, work_package_from, work_package_to, description).execute()

    def find_relations(self, work_package):
        return list(FindRelations(self.connection, work_package).execute())

    def create_relation_form(self, work_package, relation):
        return CreateRelationForm(self.connection, work_package, relation).execute()

    def find_watchers(self, work_package):
        return list(FindWatchers(self.connection, work_package).execute())

    def create_watcher(self, work_package, watcher):
        return CreateWatcher(self.connection, work_package, watcher).execute()

    def delete_watcher(self, work_package, watcher):
        DeleteWatcher(self.connection, work_package, watcher).execute()

    def find_relation_candidates(self, work_package, filters=None, query=None, type=None, page_size=None):
        return list(FindRelationCandidates(self.connection, work_package, filters, query, type, page_size).execute())

    def find_available_watchers(self, work_package):
        return list(FindAvailableWatchers(self.connection, work_package).execute())

    def find_available_projects(self, work_package=None):
        return list(FindAvailableProjects(self.connection, work_package).execute())

    def find_revisions(self, work_package):
        return list(FindRevisions(self.connection, work_package).execute())

    def find_activities(self, work_package):
        return list(FindActivities(self.connection, work_package).execute())

    def create_activity(self, work_package, activity, notify=None):
        return CreateActivity(self.connection, work_package, activity, notify).execute()
