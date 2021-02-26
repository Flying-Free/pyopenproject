from pyopenproject.business.document_service import DocumentService
from pyopenproject.business.services.command.document.find import Find
from pyopenproject.business.services.command.document.find_all import FindAll


class DocumentServiceImpl(DocumentService):

    def __init__(self, connection):
        """Constructor for class DocumentServiceImpl, from DocumentService

        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self, document):
        return Find(self.connection, document).execute()

    def find_all(self, offset=None, page_size=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, sort_by).execute())
