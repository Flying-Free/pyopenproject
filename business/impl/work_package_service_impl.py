from business.impl.command.work_package.add_attachment import AddAttachment
from business.impl.command.work_package.find_by_context import FindByContext
from business.impl.command.work_package.list_attachments import ListAttachments
from business.impl.command.work_package.find import Find
from business.impl.command.work_package.update import Update
from business.impl.command.work_package.delete import Delete
from business.impl.command.work_package.find_schema import FindSchema
from business.impl.command.work_package.find_all_schemas import FindAllSchemas
from business.impl.command.work_package.update_form import UpdateForm
from business.impl.command.work_package.find_all import FindAll
from business.impl.command.work_package.create import Create
from business.impl.command.work_package.create_form import CreateForm
from business.impl.command.work_package.create_relation import CreateRelation
from business.impl.command.work_package.find_relations_by_work_package import FindRelationsByWorkPackage
from business.impl.command.work_package.create_relation_form import CreateRelationForm
from business.work_package_service import WorkPackageService



class WorkPackageServiceImpl(WorkPackageService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def list_attachments(self, work_package):
        return ListAttachments(work_package).execute()

    def add_attachment(self, work_package, attachment):
        return AddAttachment(work_package, attachment).execute()

    def find(self, work_package, notify):
        return Find(work_package, notify).execute()

    def update_work_package(self, work_package, notify):
        return Update(work_package, notify)

    def delete_work_package(self, work_package, notify):
        Delete(work_package, notify).execute()

    def find_schema(self, schema):
        return FindSchema(schema)

    def find_all_schemas(self, filters):
        return FindAllSchemas(filters)

    def update_work_package_form(self, work_package):
        return UpdateForm(work_package)

    def find_all(self, notify, offset, pageSize, filters, sortBy, groupBy, showSums):
        return FindAll(notify, offset, pageSize, filters, sortBy, groupBy, showSums).execute()

    def new_work_package(self, work_package, notify):
        return Create(work_package, notify)

    def new_work_package_form(self, work_package):
        return CreateForm(work_package).execute()

    def new_relation(self, work_package, relation):
        return CreateRelation(work_package, relation).execute

    def find_relations_by_work_package(self, work_package):
        return FindRelationsByWorkPackage(work_package).execute()

    def new_relation_form(self, work_package, relation):
        return CreateRelationForm(work_package, relation).execute()

    def find_watchers_by_work_package(self): raise NotImplementedError


    def new_watcher(self, work_package, watcher): raise NotImplementedError


    def delete_watcher(self, work_package, watcher): raise NotImplementedError


    def find_relation_candidates_by_work_package(self, work_package, filters, query, type, pageSize): raise NotImplementedError


    def find_available_watchers_by_work_package(self, work_package): raise NotImplementedError


    def find_available_projects_by_work_package(self, work_package): raise NotImplementedError


    def find_revisions_by_work_package(self, work_package): raise NotImplementedError


    def find_activities_by_work_package(self, work_package, notify): raise NotImplementedError


    def new_activity(self, work_package, activity, notify): raise NotImplementedError