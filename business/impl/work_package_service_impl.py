from business.impl.command.work_package.add_attachment import AddAttachment
from business.impl.command.work_package.find_all import FindAll
from business.impl.command.work_package.find_by_context import FindByContext
from business.impl.command.work_package.find_by_id import FindById
from business.impl.command.work_package.list_attachments import ListAttachments
from business.work_package_service import WorkPackageService


class WorkPackageServiceImpl(WorkPackageService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new work package
    def new_work_package(self): raise NotImplementedError

    def list_attachments(self, work_package):
        return ListAttachments(work_package).execute()

    def add_attachment(self, work_package, attachment):
        return AddAttachment(work_package, attachment).execute()