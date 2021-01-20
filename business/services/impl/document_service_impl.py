from business.services.document_service import DocumentService
from business.services.impl.command.document.find import Find
from business.services.impl.command.document.find_all import FindAll


class DocumentServiceImpl(DocumentService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, document):
        return Find(self.connection, document).execute()

    def find_all(self, offset, page_size, sort_by):
        return list(FindAll(self.connection, offset, page_size, sort_by).execute())
