from business.services.document_service import DocumentService
from business.services.impl.command.document.find import Find
from business.services.impl.command.document.find_all import FindAll


class DocumentServiceImpl(DocumentService):

    def find(self, document):
        return Find(document).execute()

    def find_all(self, offset, pageSize, sortBy):
        return FindAll(offset, pageSize, sortBy).execute()
