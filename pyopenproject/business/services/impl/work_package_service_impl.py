from pyopenproject.business import WorkPackageService
from pyopenproject.business.services.impl.command import AddAttachment
from pyopenproject.business.services.impl.command import Create
from pyopenproject.business.services.impl.command import CreateActivity
from pyopenproject.business.services.impl.command import CreateForm
from pyopenproject.business.services.impl.command import CreateRelation
from pyopenproject.business.services.impl.command import CreateRelationForm
from pyopenproject.business.services.impl.command import CreateWatcher
from pyopenproject.business.services.impl.command import Delete
from pyopenproject.business.services.impl.command import DeleteWatcher
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindActivities
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindAllSchemas
from pyopenproject.business.services.impl.command import FindAttachments
from pyopenproject.business.services.impl.command import \
    FindAvailableWatchers
from pyopenproject.business.services.impl.command import FindByContext
from pyopenproject.business.services.impl.command import \
    FindRelationCandidates
from pyopenproject.business.services.impl.command import FindRelations
from pyopenproject.business.services.impl.command import FindRevisions
from pyopenproject.business.services.impl.command import FindSchema
from pyopenproject.business.services.impl.command import FindWatchers
from pyopenproject.business.services.impl.command import Update
from pyopenproject.business.services.impl.command import UpdateForm
from pyopenproject.business.services.impl.command.work_package.find_available_projects import \
    FindAvailableProjects


class WorkPackageServiceImpl(WorkPackageService):

    def __init__(self, connection):
        """Constructor for class WorkPackageServiceImpl, from WorkPackageService

        :param connection: The connection data
        """
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

    def find_schema(self, work_package):
        return FindSchema(self.connection, work_package).execute()

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

    def create_relation(self, relation_type, work_package_from, work_package_to, description):
        return CreateRelation(self.connection, relation_type, work_package_from, work_package_to, description).execute()

    def find_relations(self, work_package):
        return list(FindRelations(self.connection, work_package).execute())

    def create_relation_form(self, work_package, relation):
        return CreateRelationForm(self.connection, work_package, relation).execute()

    def find_watchers(self, work_package):
        return list(FindWatchers(self.connection, work_package).execute())

    def create_watcher(self, work_package, user):
        return CreateWatcher(self.connection, work_package, user).execute()

    def delete_watcher(self, work_package, watcher):
        DeleteWatcher(self.connection, work_package, watcher).execute()

    def find_relation_candidates(self, work_package, query, filters=None, relation_type=None, page_size=None):
        return list(FindRelationCandidates(self.connection, work_package, filters, query, relation_type, page_size)
                    .execute())

    def find_available_watchers(self, work_package):
        return list(FindAvailableWatchers(self.connection, work_package).execute())

    def find_available_projects(self, work_package=None):
        return list(FindAvailableProjects(self.connection, work_package).execute())

    def find_revisions(self, work_package):
        return list(FindRevisions(self.connection, work_package).execute())

    def find_activities(self, work_package):
        return list(FindActivities(self.connection, work_package).execute())

    def create_activity(self, work_package, comment, notify=None):
        return CreateActivity(self.connection, work_package, comment, notify).execute()
