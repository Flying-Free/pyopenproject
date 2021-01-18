from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.document.document_command import DocumentCommand
from model.document import Document


class FindAll(DocumentCommand):

    def __init__(self, connection, offset, pageSize, sortBy):
        super().__init__(connection)
        self.offset = offset
        self.pageSize = pageSize
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.sortBy}")\
                .execute()
            for document in json_obj._embedded.elements:
                yield Document(document)
        except RequestError as re:
            raise BusinessError(f"Error finding all documents") from re
