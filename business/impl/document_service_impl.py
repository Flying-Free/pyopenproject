from business.activity_service import ActivityService
from business.document_service import DocumentService
from business.impl.command.activity.find import Find
from business.impl.command.activity.find_by_context import FindByContext


class DocumentServiceImpl(DocumentService):

    def find(self, document):
        return Find(document).execute()

    def find_all(self, offset, pageSize, sortBy):
        return FindAll(offset, pageSize, sortBy).execute()
