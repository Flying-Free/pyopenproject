from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.document.document_command import DocumentCommand
from model.document import Document


class FindAll(DocumentCommand):

    def __init__(self, offset, pageSize, sortBy):
        self.offset = offset
        self.pageSize = pageSize
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.sortBy}")
            for document in json_obj._embedded.elements:
                yield Document(document)
        except RequestError as re:
            raise BusinessError(f"Error finding all documents") from re
