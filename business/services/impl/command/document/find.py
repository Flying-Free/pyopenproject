from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.document.document_command import DocumentCommand
from model.document import Document


class Find(DocumentCommand):

    def __init__(self, connection, document):
        """Constructor for class Find, from DocumentCommand.

        :param connection: The connection data
        :param document: The document to find
        """
        super().__init__(connection)
        self.document = document

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.document.id}").execute()
            return Document(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding document by id: {self.document.id}") from re
