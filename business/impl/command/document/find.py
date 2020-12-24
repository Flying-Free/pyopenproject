from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.document.document_command import DocumentCommand
from model.document import Document


class Find(DocumentCommand):

    def __init__(self, document):
        self.document = document

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.document.id}")
            return Document(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding document by id: {self.document.id}") from re
