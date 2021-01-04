from business.impl.command.work_package.add_attachment import AddAttachment
from business.impl.command.work_package.find_by_context import FindByContext
from business.impl.command.work_package.list_attachments import ListAttachments
from business.work_package_service import WorkPackageService


class WorkPackageServiceImpl(WorkPackageService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def list_attachments(self, work_package):
        return ListAttachments(work_package).execute()

    def add_attachment(self, work_package, attachment):
        return AddAttachment(work_package, attachment).execute()


    def find(self, notify): raise NotImplementedError


    def update_work_package(self, work_package, notify): raise NotImplementedError


    def delete_work_package(self, work_package, notify): raise NotImplementedError


    def find_schema(self, identifier): raise NotImplementedError


    def find_all_schemas(self, filters): raise NotImplementedError


    def update_work_package_form(self, work_package): raise NotImplementedError


    def find_all(self, notify, offset, pageSize,filters, sortBy, groupBy, showSums): raise NotImplementedError


    def new_work_package(self, work_package, notify): raise NotImplementedError


    def new_work_package_form(self): raise NotImplementedError


    def new_relation(self, work_package, relation): raise NotImplementedError


    def find_relations_by_work_package(self, work_package): raise NotImplementedError


    def new_relation_form(self, relation): raise NotImplementedError


    def find_watchers_by_work_package(self): raise NotImplementedError


    def new_watcher(self, work_package, watcher): raise NotImplementedError


    def delete_watcher(self, work_package, watcher): raise NotImplementedError


    def find_relation_candidates_by_work_package(self, work_package, filters, query, type, pageSize): raise NotImplementedError


    def find_available_watchers_by_work_package(self, work_package): raise NotImplementedError


    def find_available_projects_by_work_package(self, work_package): raise NotImplementedError


    def find_revisions_by_work_package(self, work_package): raise NotImplementedError


    def find_activities_by_work_package(self, work_package, notify): raise NotImplementedError


    def new_activity(self, work_package, activity, notify): raise NotImplementedError